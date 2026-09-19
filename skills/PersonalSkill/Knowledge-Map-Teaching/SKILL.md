---
name: knowledge-map-teaching
description: Interview the user about their learning goal and scope, then build and persist a recursively expandable knowledge map organized by concepts and relationships rather than source layouts. Use to explore the structure of a broad domain. Do not use for personal study progress, courses, or project practice.
metadata:
  short-description: Interview first, then map a domain's knowledge system
---

# Expandable Knowledge Maps

Present a broad topic as a navigable domain map, not as a course, study plan, or fully expanded encyclopedia. The map describes the structure of the concepts themselves and lets the user zoom from the whole domain into selected details.

## Establish the map brief first

For a new map, interview the user before drawing a diagram or creating files. The topic name alone is not a sufficient brief. Establish what the user wants the map to help them understand or do, which parts of the domain belong in this map, and which adjacent parts should remain outside it.

Treat the intake as a decision tree and work it in short rounds. In each round, ask the current frontier: the smallest set of independent questions whose answers can materially change the map. Number the questions and provide a recommended answer with its tradeoff. Wait for the answers before asking questions that depend on them. Do not ask the user for facts that can be discovered from the workspace, supplied material, or authoritative sources.

Resolve these decisions, using information the user already supplied instead of asking again:

- **Learning goal:** The understanding, decision, or capability the map should support.
- **Scope:** Included subdomains and explicit exclusions.
- **Perspective:** The conceptual, practical, architectural, historical, ecosystem, or other lens that should shape the hierarchy and relationships.
- **Depth:** The useful stopping point and the level of detail expected in the initial map.
- **Context:** Prior knowledge, intended application, source constraints, or version boundaries only when they would change the map's structure.

Summarize the resolved decisions as a `Map Brief` and ask the user to confirm it. If the user delegates a decision, supply a recommended choice and include it in the brief. The intake is complete only when the learning goal, inclusions, exclusions, perspective, and initial depth are explicit. Generate and persist the root map only after confirmation.

Do not repeat the full intake when expanding an existing map under its confirmed brief. Ask a focused follow-up only when the requested expansion changes the learning goal, crosses an exclusion, or makes the existing depth or perspective unsuitable.

## Derive concepts, not source structure

Treat files in the workspace and material supplied by the user as reference sources, not as a proposed map outline. Inspect only material relevant to the requested topic. Extract concepts, mechanisms, operations, and meaningful relationships from the content, then normalize duplicates and synthesize a domain structure across sources.

File names, directory names, book titles, tables of contents, chapter names, headings, and source order are retrieval cues and provenance. A source heading qualifies as a node only when it independently names a concept, mechanism, or operation that belongs in the domain map. Organize nodes by semantic containment and relationships even when that differs from how a source is packaged. Preserve source locations in citations or `sources.md`, not as structural nodes.

Follow a source's chapter or file structure only when the user explicitly asks for a source-aligned map. Reading reference material does not authorize modifying, relocating, or copying the source files.

## Start at the root

After the user confirms the map brief, show the root node's direct children with a short explanation of each role. Stop at that layer unless the confirmed initial depth or the user's subsequent request says to continue.

At each step, show only one layer of direct children under the current node, plus the cross-node relationships needed to understand that layer. Let the user choose which node to expand. The user may instead name a node, specify a depth, or ask to expand to the deepest useful level. For the latter two cases, continue along the requested branch without pausing at every layer. Keep diagram granularity independent from file granularity: several small diagrams from the same coherent module may belong in one Markdown file.

Stop decomposing when a node is the smallest structural unit useful within the current map: it represents one distinct concept, mechanism, or operation, and further decomposition would enter implementation details, term definitions, or adjacent areas outside the agreed scope. This is a boundary for the map, not a claim that the concept is theoretically indivisible.

## Represent the structure

Assign every node a stable ID. Its title may improve over time, but its ID remains unchanged so parent-child relationships and cross-node references stay stable.

Keep stable IDs as internal mechanics inside Mermaid source, provenance fields, and invisible Markdown anchors. Do not prefix human-facing headings, navigation labels, node notes, or filenames with an ID or abbreviation. Name each map page after the complete knowledge subsystem it contains, using a readable lowercase kebab-case slug. A reader should understand every visible label and filename without decoding an internal identifier.

Distinguish hierarchical containment from cross-node relationships. Use at least `prerequisite`, `recommended connection`, and `application branch` for cross-node links. Do not present every connection as a strict learning order. Each diagram shows the current node, its direct children, and the cross-node relationships needed to read and navigate that layer independently.

Treat a coherent knowledge system as the primary unit of organization. Preserve concepts that explain one another as a single subsystem even when doing so produces a longer page. Split storage only at a natural semantic boundary where the resulting subsystem remains understandable, its internal relationships remain visible, and its external relationships can be represented without losing necessary context. File size alone is not a reason to split a subsystem.

The map is an index, not a collection of concept lessons. Node descriptions should contain enough information for the user to decide whether to expand them. Provide full explanations only when separately requested. Avoid decomposing uncertain areas into large numbers of falsely precise nodes.

For version-specific facts, ecosystem conventions, or disputed structural judgments, verify against official documentation or other primary sources and cite them when useful. Do not rely on model memory as the sole basis for those claims.

## Persist the map

Persist the map by default. Unless the user explicitly requests a preview or conversation-only map, create or maintain `knowledge-map-<topic-slug>/` in the current writable workspace or in a workspace the user names. Derive the slug from the confirmed topic. Ask about the location or slug only when the current workspace is unsuitable, the topic is ambiguous, or a naming collision cannot be resolved safely. Every generated map artifact stays inside this directory.

Check for an existing directory with the same name before creating anything. Read and update a compatible map in place rather than clearing or rebuilding it. If the directory is unrecognized, belongs to another topic, or would cause user files to be overwritten, stop and ask how to proceed. Legacy `learning-map-*` or `learning_map/` content may be read and a migration may be proposed, but never rename, move, merge, or delete it automatically.

Before creating or updating files, read [Split Mermaid Knowledge Map Format](./references/mermaid-map-format.md). Write the root map after the topic and scope are confirmed. After every requested expansion, update the relevant navigation and map page before completing the turn. Mermaid represents the map, while Markdown pages package related local views. Each diagram contains only the current node and its direct children. Add an expanded node as a section in its nearest coherent subsystem page by default. Create another map page only at a natural subsystem boundary. Complexity signals may prompt a boundary review or better within-page navigation, but they never override systemic coherence. The number of files should reflect meaningful subsystems, not the number of nodes.

In the response, identify the files created or updated and summarize the visible layer. Do not duplicate every persisted diagram in the conversation unless the user asks to see it there. If persistence is unavailable, explain the limitation and provide the map in the conversation without claiming it was saved. Project code, personal progress, exercises, course materials, and study records do not belong in a knowledge map.

## Boundaries

Use `$teach` when the user needs a personal study plan, cross-session progress, or course materials. Use `$stage-proj-teaching` when the user has selected a set of capabilities and wants to integrate them through project practice. This skill only builds and navigates domain structure.
