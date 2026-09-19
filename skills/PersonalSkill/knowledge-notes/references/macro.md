# Macro Notes

A macro artifact pursues coverage completeness by materializing the complete composition of a defined domain as a navigable set of directories and notes. Include a branch because it belongs to the domain within the coverage contract, not because it is necessary to explain how another branch works. Completeness means structural coverage within an explicit scope, perspective, and relevant time or version boundary. It does not mean explaining every branch at mechanism depth.

## Establish the coverage contract

Before writing files, resolve:

- The domain and the question this note system must answer.
- What belongs inside the domain and what is explicitly excluded.
- The perspective that determines which distinctions and branches matter.
- The time period, version, or ecosystem boundary when the domain changes over time.

Use constraints the user has already supplied. If any missing decision would change the branch inventory, ask the user or offer a recommendation for the user to delegate. The coverage contract is complete only when inclusion, exclusion, perspective, and any relevant temporal boundary are explicit.

## Procedure

1. Build a candidate branch inventory from multiple authoritative sources when the domain is not already fully specified by supplied material. Treat source outlines as evidence, not as the final note structure. Normalize duplicate concepts, reconcile competing classifications, and record unresolved disagreements. Judge each candidate by whether it belongs inside the coverage contract, not by whether it participates in one end-to-end mechanism.
2. Choose a primary structure from `structure-models.md`. Let it determine the directory hierarchy, grouping, and navigation rather than forcing every domain into the same tree shape.
3. Materialize the structure with enough directories and notes to make every branch in the verified inventory visible. Give each major branch its own substantive note. Use a directory when it groups a coherent set of subbranches, not merely to add another level.
4. Give each branch note positioning-level content that explains its scope, defining question, role in the domain, reason for being a distinct branch, direct subdivisions, and significant relationships. A name alone is not a completed branch note.
5. Continue decomposing until every leaf is a bounded knowledge object that could be explained independently. Keep steps, parameters, formulas, and implementation details inside that object rather than splitting them as macro branches. Keep leaves at positioning depth by default. If the user explicitly requests an in-depth treatment of a branch in the current task, read `meso.md` and apply it to that branch.
6. Connect parent notes, branch notes, and cross-branch relationships so the entire structure is navigable. Add an overview note when it provides a useful entry point or global explanation, but do not use one overview note as a substitute for materializing the branches.

The primary structure determines directories and grouping. A secondary structure, when needed, determines cross-branch links. Create the number of files and directory levels required by the actual domain structure. Every created note must contain useful positioning content, so structural completeness does not produce empty placeholders.

## Audit coverage

Maintain an internal coverage ledger while working. For every branch in the verified inventory, check that it has:

- A concrete location in the file tree.
- A substantive note meeting the branch-content requirements.
- A reachable parent or entry-point link.
- The parent-child and cross-branch links needed to express its relationships.

The ledger is execution state, not part of the note system. Do not persist it unless the user asks for it.

When evidence is insufficient or authoritative sources disagree, preserve the verified notes but do not claim complete coverage. Put domain-level uncertainty where readers need it in the relevant overview or branch note. Report research or execution gaps only in the handoff.

When updating an existing macro artifact, audit the changed branch, its parent, affected sibling boundaries, and related links. Expand to a full-domain audit only when the change alters the coverage contract or reveals a branch the current global structure cannot represent.

## Completion criteria

Coverage completeness is reached when the file tree lets a reader inspect the domain's complete composition within the coverage contract and navigate from the whole to every verified branch. Every inventory item passes the coverage ledger, every directory has a structural purpose, and every branch note explains all six required positioning elements. The artifact is incomplete if a component exists only as an unmaterialized label, if a branch lacks evidence, or if an unresolved gap prevents the coverage claim. State the bounded claim precisely rather than describing a time-sensitive or contested domain as universally complete.
