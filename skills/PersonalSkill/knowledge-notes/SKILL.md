---
name: knowledge-notes
description: Turn knowledge topics into maintainable Markdown note systems. Use when the user wants to create knowledge notes, organize a knowledge base, design a note structure, or capture a domain, technical system, algorithm, or mechanism as connected notes. Do not use for personal study plans, course design, or questions that only need an explanation.
metadata:
  short-description: Organize knowledge into structured, connected Markdown notes
---

# Knowledge Notes

Organize knowledge in a spatial structure that matches its relationships, then express it as a maintainable, navigable set of standard Markdown notes. Structure should make relationships visible rather than decorate the content.

## Establish the task boundary

First inspect the user's source material, existing note directories, and naming conventions. Preserve the location, naming, and linking conventions of an existing system, and modify only what the request requires. When no system exists, default to one `.md` file per knowledge object and use standard relative links.

Determine the current question, intended reader, desired depth, and output location. Ask only when missing information would materially change the structure or create an overwrite risk. Otherwise, make the smallest reasonable assumption and state it.

Use authoritative primary sources when the task requires current facts, version-specific details, or disputed structural judgments. Distinguish sourced facts, structural inferences, and explanatory examples.

## Choose the scale

Classify the scale from the scope of the user's current request, not from the topic's absolute position in an academic taxonomy:

- **Macro, coverage completeness:** A broad domain whose full branch inventory within a defined boundary must be represented as a navigable hierarchy of directories and notes. Include a node because it belongs to the domain's composition. Read [Macro Notes](references/macro.md).
- **Meso, explanatory completeness:** A bounded system made of multiple independently explainable core units whose collaboration must be expressed through a navigable directory-and-note hierarchy. Include a node because the system cannot be explained without its role or mechanism. Read [Meso Notes](references/meso.md).
- **Micro:** One independently reusable algorithm, mechanism, or focused technique whose remaining parts are steps, parameters, or implementation details rather than cooperating knowledge units. Read [Micro Notes](references/micro.md).

When macro and meso both appear plausible, use the inclusion test. If the task asks which branches belong to a domain, pursue coverage completeness. If it asks which internal units and interactions are necessary to explain how a bounded system works, pursue explanatory completeness. Use micro when the object is one reusable unit and further decomposition only exposes its steps, parameters, or implementation details. File count, directory shape, and academic taxonomy do not determine scale. If the working scale proves wrong during execution, switch scales.

Scale labels are internal planning concepts. Never place `macro`, `meso`, `micro`, or equivalent scale labels in generated directory names, filenames, note titles, or note prose unless the user explicitly asks for an explanation of the method. Name every artifact after its actual domain, system, mechanism, or knowledge object.

## Descend only when required

Load the reference for the starting scale, then descend under these rules:

- Macro work materializes every branch at positioning depth and stops there by default. Load `references/meso.md` for a branch only when the user explicitly asks this task to explain that branch in depth.
- Meso work must remain independently readable. When a dedicated deep-dive note is necessary to explain the system completely, read `references/micro.md` and apply its full standard to that note. Create required deep dives automatically, but leave optional extensions uncreated.
- Micro work is terminal. Explain internal steps, parameters, and implementation details inside the same note instead of creating another scale of knowledge artifact.

Apply descent per branch. A task may keep most of a domain at positioning depth while deepening only the branches requested or required by these rules.

## Backfill upward

Deeper work can invalidate a parent note. When a child note changes what the parent must explain, rewrite the parent's own content and structure. Do not add a summary section, a progress note, or a status annotation, and do not move child content wholesale into the parent.

Backfill is complete when the parent again satisfies the completion criteria for its own reference. For a coverage parent, restore the affected branch's placement, scope, subdivisions, and relationships without importing mechanism detail. For an explanatory parent, restore the end-to-end account and each core part's role and key mechanism without requiring child notes. The parent's structure carries the synthesis; where an explicit cue is genuinely useful, keep it short and content-bearing.

Add or reshape a macro-level branch only when a genuinely new branch appears that the existing composition cannot name. Otherwise, treat the parent's gaps as gaps in its own content and close them there.

## Choose the structure

After selecting the scale, read [Structure Models](references/structure-models.md) and choose one primary structure for the current question. Add one secondary structure only when the primary structure would lose an important relationship, and state what each structure is responsible for.

Structure follows the question. The same topic may need a different structure for a different question. Rebuild the structure when concepts repeat without adding relational information, layer relationships cannot be named, or the core cannot be separated from the boundary.

## Write and connect

Check the target location for notes with the same name or compatible content before writing. Update compatible notes in place. Stop for confirmation when ownership is unclear or a user file may be overwritten. Create files with substantive content, not empty placeholders used only to complete a structure.

Use standard Markdown by default, including headings, lists, tables, and relative links. Use editor-specific syntax only when the user's existing system already relies on it or the user explicitly requests it.

When no convention exists:

- Give each file a clear, stable knowledge-object name.
- Link to a parent note at the beginning when ownership needs to be explicit.
- Add a "Related Notes" section at the end when cross-topic navigation is useful.
- If a link target does not exist, list its name and mark it as pending instead of inventing a valid link.

## Completion criteria

Before finishing, verify that:

- The content satisfies every requirement for each scale reference loaded during the task.
- The primary structure matches the knowledge relationships, and any secondary structure is necessary.
- Every new or modified link resolves or is explicitly marked as pending.
- New notes are reachable from an existing entry point, with no orphaned placeholder files.
- The files render correctly in a standard Markdown reader.

In the handoff, list the files created or modified, summarize the organizing structure in domain terms, and identify anything that still needs content or verification. Keep internal scale labels out of the handoff unless the user asks about the method.

## Boundaries

This skill independently handles the complete knowledge-note workflow, including discovering domain boundaries, enumerating major branches, designing the global structure, writing detailed content, and connecting notes. If the user only needs an explanation and no note artifact, answer directly without creating files. Personal study plans, progress tracking, course design, and project practice are outside the knowledge-note artifact.
