#!/usr/bin/env python3
"""
Bilibili 视频 → 笔记素材提取管线（标题/简介/字幕/音频转录）

流程:
  1. 解析 BV 号（支持完整链接、share 链接、b23.tv 短链）
  2. 公开 API 获取元信息（标题、简介、UP主、时长、aid/cid）
  3. 优先取字幕（CC / AI 字幕，免语音识别）
  4. 无字幕 → 下载 dash 音频流（最低码率）→ 语音识别

设计参考 douyin_pipeline.py：标准解析 → 产物落盘 → 由 Agent 结构化整理成笔记。
B站公开接口无需登录，无需 wbi 签名（本管线仅用基础清晰度/音频流）。

用法:
  uv run python ~/.config/opencode/skills/douyin-obsidian/scripts/bilibili_pipeline.py \
    --link "<B站链接或BV号>" [--action info|extract] [--output <目录>] [--quiet]

示例:
  # 只取元信息（无需任何 Key）
  ... bilibili_pipeline.py --link "https://www.bilibili.com/video/BV1JrCsBCE8D/" --action info

  # 完整提取（有字幕直接用字幕；无字幕则下载音频并转录）
  ... bilibili_pipeline.py --link "BV1JrCsBCE8D" --output "assets/<笔记名>" --quiet

语音识别（无字幕时）按顺序选择:
  1. ASR_PROVIDER=openai      → 使用 OPENAI_API_KEY（可选 OPENAI_BASE_URL / OPENAI_MODEL / OPENAI_PROXY）
  2. ASR_PROVIDER=siliconflow → 使用 ~/.douyin-video/config.json 中的硅基流动 Key
  未显式设置时: 有 OPENAI_API_KEY 用 openai，否则有硅基流动 Key 用 siliconflow
"""
import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import requests

BASE = "https://www.bilibili.com"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
HEADERS = {"User-Agent": UA, "Referer": BASE + "/"}

VIEW_API = "https://api.bilibili.com/x/web-interface/view"
PLAYER_API = "https://api.bilibili.com/x/player/v2"
PLAYURL_API = "https://api.bilibili.com/x/player/playurl"

PREFERRED_SUBTITLE_LANGS = ["zh-Hans", "zh-CN", "ai-zh", "zh", "zh-Hant", "ai-zh-Hans"]

sys.path.insert(0, str(Path(__file__).resolve().parent))
from douyin_downloader import DouyinProcessor, load_persisted_api_key  # noqa: E402


def _log(quiet: bool, msg: str):
    if not quiet:
        print(msg, flush=True)


# --------------------------------------------------------------------------
# 解析
# --------------------------------------------------------------------------

def resolve_bvid(link: str) -> str:
    """从链接/BV号/短链中解析 bvid"""
    m = re.search(r"(BV[0-9A-Za-z]{10})", link)
    if m:
        return m.group(1)
    # b23.tv 短链或其它跳转链接
    resp = requests.get(link, headers=HEADERS, allow_redirects=True, timeout=30)
    m = re.search(r"(BV[0-9A-Za-z]{10})", resp.url)
    if m:
        return m.group(1)
    # 有时会给出 av 号
    ma = re.search(r"av(\d+)", resp.url)
    if ma:
        data = _api(VIEW_API, {"aid": ma.group(1)})
        return data["bvid"]
    raise ValueError(f"无法从链接解析出 BV 号: {link}")


def _api(url: str, params: dict) -> dict:
    r = requests.get(url, params=params, headers=HEADERS, timeout=30)
    r.raise_for_status()
    j = r.json()
    if j.get("code") != 0:
        raise ValueError(f"B站接口错误 code={j.get('code')}: {j.get('message')}")
    return j["data"]


def fetch_view(bvid: str) -> dict:
    d = _api(VIEW_API, {"bvid": bvid})
    return {
        "bvid": d.get("bvid"),
        "aid": d.get("aid"),
        "cid": d.get("cid"),
        "title": d.get("title", ""),
        "desc": d.get("desc", ""),
        "author": (d.get("owner") or {}).get("name", ""),
        "duration_s": d.get("duration", 0),
        "cover": d.get("pic", ""),
        "url": f"{BASE}/video/{d.get('bvid')}/",
    }


def fetch_subtitle(aid: int, bvid: str, cid: int, quiet: bool) -> tuple:
    """返回 (text, lang)；无字幕返回 (None, None)"""
    try:
        d = _api(PLAYER_API, {"aid": aid, "bvid": bvid, "cid": cid})
    except Exception as e:
        _log(quiet, f"  字幕接口失败: {e}")
        return None, None

    subs = (d.get("subtitle") or {}).get("subtitles") or []
    if not subs:
        return None, None

    def rank(s):
        lan = s.get("lan", "")
        return PREFERRED_SUBTITLE_LANGS.index(lan) if lan in PREFERRED_SUBTITLE_LANGS else 99

    sub = sorted(subs, key=rank)[0]
    url = sub.get("subtitle_url") or ""
    if url.startswith("//"):
        url = "https:" + url
    elif url.startswith("/"):
        url = BASE + url
    if not url:
        return None, None
    try:
        body = requests.get(url, headers=HEADERS, timeout=30).json()
    except Exception as e:
        _log(quiet, f"  字幕下载失败: {e}")
        return None, None
    lines = [item.get("content", "") for item in (body.get("body") or [])]
    text = "".join(lines).strip()
    return (text, sub.get("lan") or "") if text else (None, None)


def fetch_audio_url(bvid: str, cid: int) -> str:
    """取最低码率的 dash 音频流地址"""
    d = _api(PLAYURL_API, {"bvid": bvid, "cid": cid, "fnval": 16, "qn": 64})
    audios = (d.get("dash") or {}).get("audio") or []
    if audios:
        best = sorted(audios, key=lambda a: a.get("bandwidth", 0))[0]
        return best.get("baseUrl") or (best.get("backupUrl") or [""])[0]
    # 兼容老的 durl 格式
    durl = d.get("durl") or []
    if durl:
        return durl[0].get("url", "")
    raise ValueError("未获取到音频流地址")


def download_audio(url: str, dest: Path, show_progress: bool = True) -> Path:
    dest.parent.mkdir(parents=True, exist_ok=True)
    with requests.get(url, headers=HEADERS, stream=True, timeout=120) as r:
        r.raise_for_status()
        total = int(r.headers.get("Content-Length") or 0)
        done = 0
        with open(dest, "wb") as f:
            for chunk in r.iter_content(65536):
                if chunk:
                    f.write(chunk)
                    done += len(chunk)
                    if show_progress and total:
                        print(f"\r音频下载 {done * 100 // total}%", end="", flush=True)
    if show_progress:
        print()
    return dest


# --------------------------------------------------------------------------
# 语音识别
# --------------------------------------------------------------------------

def _pick_provider() -> str:
    p = os.getenv("ASR_PROVIDER")
    if p:
        return p.lower()
    if os.getenv("OPENAI_API_KEY"):
        return "openai"
    if load_persisted_api_key():
        return "siliconflow"
    return ""


def transcribe_audio(audio_path: Path, provider: str, quiet: bool) -> str:
    if provider == "openai":
        return _transcribe_openai(audio_path)
    if provider == "siliconflow":
        key = load_persisted_api_key()
        if not key:
            raise ValueError("硅基流动 Key 未配置（~/.douyin-video/config.json）")
        proc = DouyinProcessor(api_key=key)
        return proc.extract_text_from_audio(audio_path, show_progress=not quiet)
    raise ValueError(
        "未配置语音识别服务：请设置 ASR_PROVIDER=openai 并提供 OPENAI_API_KEY，"
        "或配置硅基流动 Key（~/.douyin-video/config.json）"
    )


def _transcribe_openai(audio_path: Path) -> str:
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        raise ValueError("OPENAI_API_KEY 未设置")
    base = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/")
    model = os.getenv("OPENAI_MODEL", "whisper-1")
    proxy = os.getenv("OPENAI_PROXY")
    proxies = {"http": proxy, "https": proxy} if proxy else None

    ext = audio_path.suffix.lower()
    mime = {".mp3": "audio/mpeg", ".m4a": "audio/mp4", ".m4s": "audio/mp4",
            ".wav": "audio/wav", ".mp4": "video/mp4", ".flac": "audio/flac"}.get(ext, "audio/mpeg")

    with open(audio_path, "rb") as f:
        files = {"file": (audio_path.name, f, mime)}
        data = {"model": model, "response_format": "text", "language": "zh"}
        r = requests.post(f"{base}/audio/transcriptions",
                          headers={"Authorization": f"Bearer {key}"},
                          files=files, data=data, proxies=proxies, timeout=1800)
    r.raise_for_status()
    return r.text


# --------------------------------------------------------------------------
# 产物落盘
# --------------------------------------------------------------------------

def _video_transcript_md(info: dict, text: str, source: str) -> str:
    asr_row = f"| 来源 | {source} |\n" if source else ""
    return (
        f"# {info['title']}\n\n"
        f"| 属性 | 值 |\n"
        f"|------|----|\n"
        f"| 平台 | Bilibili |\n"
        f"| BV号 | `{info['bvid']}` |\n"
        f"| 作者 | {info.get('author', '')} |\n"
        f"| 时长 | {info.get('duration_s', 0)}s |\n"
        f"{asr_row}"
        f"| 链接 | {info.get('url', '')} |\n\n"
        f"---\n\n"
        f"## 逐字稿\n\n{text}\n"
    )


def _save_meta(info: dict, link: str, out_dir: Path, source: str):
    meta = dict(info)
    meta.update({"url_input": link, "type": "video", "transcript_source": source})
    (out_dir / "video_info.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")


def process(info: dict, link: str, out_dir: Path, quiet: bool, asr_provider: str) -> str:
    out_dir.mkdir(parents=True, exist_ok=True)

    _log(quiet, "获取字幕...")
    sub_text, sub_lang = fetch_subtitle(info["aid"], info["bvid"], info["cid"], quiet)

    if sub_text:
        text, source = sub_text, f"B站字幕（{sub_lang}）"
        _log(quiet, f"✅ 命中字幕（{sub_lang}），跳过语音识别")
    else:
        if not asr_provider:
            raise ValueError(
                "该视频无字幕，需要语音识别，但未配置 ASR：\n"
                "  - 设置 ASR_PROVIDER=openai + OPENAI_API_KEY，或\n"
                "  - 配置硅基流动 Key（~/.douyin-video/config.json）"
            )
        _log(quiet, f"无字幕，下载音频并用 {asr_provider} 识别...")
        url = fetch_audio_url(info["bvid"], info["cid"])
        with tempfile.TemporaryDirectory() as td:
            audio_path = download_audio(url, Path(td) / f"{info['bvid']}.m4a", show_progress=not quiet)
            text = transcribe_audio(audio_path, asr_provider, quiet)
        source = f"语音识别（{asr_provider}）"

    (out_dir / "transcript_raw.txt").write_text(text, encoding="utf-8")
    (out_dir / "transcript.md").write_text(
        _video_transcript_md(info, text, source), encoding="utf-8")
    _save_meta(info, link, out_dir, source)
    return text


def main():
    parser = argparse.ArgumentParser(description="Bilibili 视频素材提取管线")
    parser.add_argument("--link", required=True, help="B站链接 / BV号 / b23.tv 短链")
    parser.add_argument("--action", choices=["info", "extract"], default="extract")
    parser.add_argument("--output", "-o", default=".", help="产物输出目录")
    parser.add_argument("--quiet", action="store_true")
    parser.add_argument("--asr", default="", help="语音识别服务: openai | siliconflow（默认自动选择）")
    args = parser.parse_args()

    bvid = resolve_bvid(args.link)
    _log(args.quiet, f"BV号: {bvid}")
    info = fetch_view(bvid)
    _log(args.quiet, f"标题: {info['title']}  |  UP: {info['author']}  |  时长: {info['duration_s']}s")

    if args.action == "info":
        print(json.dumps(info, ensure_ascii=False, indent=2))
        return

    out_dir = Path(args.output)
    provider = args.asr or _pick_provider()
    text = process(info, args.link, out_dir, args.quiet, provider)
    _log(args.quiet, f"✅ 完成，文案 {len(text)} 字，产物在 {out_dir}")


if __name__ == "__main__":
    main()
