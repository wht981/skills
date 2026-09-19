---
name: stage-proj-teaching
description: Turn a user-selected learning scope into runnable project stages that grow from minimal to complete. For broad topics, select capabilities through a knowledge map first, then derive the staged path from an open-source project or a complete reference project. Do not use for concept-only explanations or one-off coding questions.
metadata:
  short-description: Learn complex topics through staged project directories
---

# Staged Project Teaching

Organize one complete project as a sequence of runnable directory snapshots. The learner starts with a minimal `Stage-One/`. Each later directory shows how the same project gains another real capability until `Final-Project/` becomes the complete implementation.

A stage is a project snapshot stored in a directory, not a Git commit or a patch containing only differences. Every stage opens, runs, and can be checked independently. Each later stage grows from the previous design instead of switching to an unrelated example.

## Scope the learning target first

First decide whether the request already defines a projectable target or still names a broad domain that needs decomposition. Proceed directly to endpoint design when the user has specified a reference project, described a concrete final product with its core capabilities, or selected nodes from a knowledge map. Otherwise, complete scope selection first.

Call `$knowledge-map-teaching` when the topic contains several independently useful branches, does not naturally converge on one coherent project, or would lose teaching focus if a single implementation tried to cover the whole domain. Have it present the root map, then let the user select, exclude, or further expand nodes. If the user already has a knowledge map, select from it instead of creating another one. Follow that skill's default persistence contract, and keep its knowledge-map directory separate from the staged project root.

Turn the selected nodes into a scope contract. Preserve the learning-target name confirmed by the user, and record the selected nodes, prerequisites needed to implement them, capabilities the project must demonstrate, and adjacent material explicitly excluded. Map nodes select the scope but do not become project stages directly. Translate them into capabilities that a project can demonstrate and verify, then design how those capabilities grow. Mark nodes that cannot be verified through the project as background knowledge or exclusions rather than inventing stages for them.

Scope selection is complete only when one complete project can demonstrate the chosen capabilities coherently, the endpoint can be stated in one sentence, and the exclusions are clear. If the selected nodes require unrelated project forms, recommend narrowing the scope or splitting it into independent staged project paths. When the user explicitly delegates scope selection, state the recommended scope and its tradeoffs before continuing. Otherwise, wait for the user to confirm the scope before producing a stage outline or files.

## Choose the complete endpoint

Prefer an open-source project selected by the user as the complete endpoint. Otherwise, recommend an open-source project whose history, architecture, and license suit a teaching reconstruction. Study its code, history, documentation, and release material to identify real capability growth and tradeoffs.

Distinguish these endpoint modes before acquiring or generating project files:

- **Curated-source endpoint:** Use this by default when the user selects an open-source project as the final project for learning. `Final-Project/` remains that project's implementation and architecture at a recorded revision, while repository material unrelated to the learning scope may be removed and teaching annotations may be added. It is a curated copy of the selected project, not a new implementation based on it.
- **Exact-source endpoint:** Use this when the user explicitly wants the selected revision unchanged. `Final-Project/` contains the unmodified source tree, and all teaching material stays outside it.
- **Teaching adaptation:** Use this only when the user explicitly wants the core implementation reduced, modified, or reimplemented. State what differs from the source project and why, and do not present the adaptation as the selected project itself.
- **Original reference project:** Use this when no suitable open-source project exists or the user explicitly requests an original endpoint.

If the user selects a repository as the final project without requesting exact preservation, use the curated-source endpoint and state that choice before changing files. Ask only when the requested cleanup would remove learning-relevant functionality, alter core behavior, or create uncertainty about license obligations. Selecting a repository for study does not authorize changing its role from final project to external reference or reimplementing its core.

If no suitable open-source project exists, or if the user explicitly prefers an original endpoint, first build a complete and credible reference project and then decompose it backward into stages. Record the chosen mode in `Source-Notes.md` as `curated-source endpoint`, `exact-source endpoint`, `teaching adaptation`, or `original reference project`. Keep original design distinct from open-source history, and describe curation and teaching adaptations rather than presenting them as the project's literal past.

When using an open-source project, verify its license, attribution, and redistribution requirements before pruning or modifying it. Preserve required license, copyright, attribution, notice, and third-party-license material even when it is not part of the learning path. Intermediate stages may use minimal teaching implementations that express the source structure. A curated endpoint documents every removal and addition, an exact-source endpoint remains unchanged, and a teaching adaptation documents every material implementation difference.

## Design the staged path

Work backward from the complete endpoint to identify the minimum capabilities that make it possible, then arrange them into one continuous growth path. `Stage-One/` contains the smallest runnable version that exposes the core problem. Each later stage adds only the capabilities needed to overcome the previous stage's limitation, such as state, data modeling, module boundaries, persistence, testing, performance, deployment, or concurrency.

Derive stages from capability growth rather than file counts, feature-list chunks, or the number of commits in the source repository. Side features may be omitted, small changes may be combined, and implementations may be simplified when the causal relationship between stages remains clear. For open-source sources, distinguish verifiable project facts, teaching adaptations, and unknown motivations.

Every stage states:

- What the current project can do, and how to run and verify it.
- The previous stage's limitation, or the core problem addressed by the first stage.
- What this stage adds or changes.
- Why the new capability requires this structure or tradeoff.
- The limitation that motivates the next stage.
- For open-source sources, evidence links or locations and an explanation of teaching adaptations.

## Make every stage teachable

Treat learning material as part of the project, not as optional commentary after the code works. Before generating stage files, read [Teaching Artifact Standard](./references/teaching-artifact-standard.md). Apply it to the root guide, every intermediate stage, and the final-project guide.

Write intermediate-stage code for a learner to inspect. Add concise comments around the mechanism introduced by that stage, non-obvious control or data flow, invariants, architectural boundaries, intentional limitations, and tradeoffs. Prefer expressive names and clear structure for ordinary code. Comments explain why the design exists and how its important parts cooperate rather than translating syntax line by line.

A stage is complete only when it runs independently, its verification instructions have been checked, its learning-critical code is intelligible with the supplied comments, and its README gives the learner an ordered path through the stage. Working code without the corresponding learning guide is incomplete.

## Directory structure

Create the standalone teaching project below after the user confirms the output location, scope contract, endpoint mode, and stage outline. Normalize the user-confirmed learning-target name into a short filesystem-safe form, then combine it with `Stage-Proj-Teaching` as one root directory name. Preserve the confirmed learning target instead of substituting the reference project name, final product name, or an unconfirmed inferred topic. Keep all persistent artifacts for this teaching project inside this single root directory, including acquired open-source source trees. Do not leave a persistent source checkout beside the teaching-project directory.

```text
Stage-Proj-Teaching-<learning-target>/
├── README.md
├── Source-Notes.md             # Source, revision, and endpoint mode
├── Final-Project-Guide.md      # Exact-source mode learning guide
├── Stage-One/
│   ├── README.md
│   └── <runnable minimal project files>
├── Stage-Two/
│   ├── README.md
│   └── <complete snapshot grown from Stage One>
├── Stage-Three/
│   └── ...
└── Final-Project/
    ├── README.md
    ├── LEARNING-GUIDE.md      # Curated-source mode guide
    └── <complete project files>
```

The combined directory name directly represents the confirmed learning target and remains short and stable. Selected knowledge-map nodes define the capability scope but are not concatenated into the directory name. The open-source project or original reference project determines stage content and the final implementation, while its name and provenance belong in `Source-Notes.md`. The root `README.md` records the scope contract, stage navigation, prerequisites, and the value of each stage. Keep stage numbers or names stable and ordered. `Final-Project/` is the complete runnable endpoint.

For a curated-source or exact-source endpoint, resolve the teaching-project root before acquiring the repository. Materialize the selected revision directly as `Final-Project/`, without wrapping it in another directory and without creating a separate derivative final implementation. Avoid embedding a nested Git repository when the teaching-project root is itself version-controlled. Prefer a release archive or export a temporary checkout at the pinned revision, and record the repository URL and exact revision in `Source-Notes.md`. Temporary acquisition data is not part of the teaching workspace and must not become a persistent sibling directory.

In curated-source mode, audit the source tree before removing anything. Keep files required for the selected capabilities, build, runtime, tests, comprehension, provenance, and legal compliance. Remove repository operations or out-of-scope material only after checking that retained files do not depend on it. Add teaching comments and guides without obscuring the original architecture, and record the curation in `Source-Notes.md`. In exact-source mode, leave `Final-Project/` unchanged and put teaching commentary in `Final-Project-Guide.md`.

Intermediate stage directories are teaching reconstructions and may simplify the implementation while preserving the causal path toward the endpoint. Each stage runs without importing code from another stage directory or from `Final-Project/`. Run or otherwise validate every stage after creation so a working final project cannot hide broken intermediate stages.

## Guide the learner

Start with `Stage-One/` and advance one stage at a time. Have the user run the current directory and understand its capability and limitation before comparing the additions that overcome that limitation in the next directory. Keep the intermediate stages visible instead of jumping directly to the final architecture.

The user may pause at, modify, or extend a stage. Keep that exploration within the stage or in an explicitly named branch directory rather than mixing it into later teaching snapshots. If the user asks to inspect the complete project, treat `Final-Project/` as the reference endpoint rather than the starting point.

## Boundaries

This skill produces a progressive project path. The knowledge map selects a scope within a broad domain but does not replace stage design. Stop after the knowledge map when the user only needs domain structure. When the user only wants to inspect an open-source repository's commit history, perform historical analysis instead of generating a staged project.
