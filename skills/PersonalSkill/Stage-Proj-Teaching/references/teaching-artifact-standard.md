# Teaching Artifact Standard

Use this standard when generating or reviewing a staged teaching project. Adapt headings to the project, but preserve the learning functions below.

## Root learning guide

The root `README.md` is the learner's entry point. It must provide:

- The learning target, scope contract, final outcome, prerequisites, and environment setup.
- A progression table showing what each stage can do, what limitation it removes, the main concepts introduced, and how to verify it.
- A recommended learning sequence with links to every stage and to the final-project guide when present.
- The relationship between the reconstructed stages and the final endpoint, including where teaching simplifications stop matching the endpoint exactly.
- Commands that have been checked in the generated workspace, not generic placeholders.

Keep source provenance and detailed historical evidence in `Source-Notes.md`; link to it instead of duplicating it.

## Stage README

Every intermediate stage has a `README.md` that allows a learner to study that directory without relying on chat history. It must cover:

1. **Learning objective:** The capability and mental model the learner should gain.
2. **Starting context:** Required knowledge and the previous stage's limitation.
3. **System view:** A compact architecture or data-flow explanation naming the important components and their relationships.
4. **Guided code tour:** An ordered reading path from entry point through the core mechanism to boundaries and tests. Name concrete files and symbols.
5. **Run and verify:** Exact commands, expected observable behavior, and a fast check for success.
6. **What changed:** The structural change from the preceding stage and why it was necessary. Describe concepts rather than dumping a file diff.
7. **Experiments:** A small set of safe modifications or observations that expose the stage's central mechanism.
8. **Checkpoints:** Questions or predictions that let the learner test understanding before continuing.
9. **Next limitation:** The unresolved problem that motivates the following stage.
10. **Source correspondence:** For open-source endpoints, identify which endpoint files, symbols, behaviors, or evidence this stage reconstructs and which parts are teaching adaptations.

Omit only an item that genuinely does not apply, and make the reason evident from the stage. Keep the guide focused on decisions and relationships that are not obvious from opening the files.

## Teaching annotations in code

Comments are navigation aids at the points where a learner would otherwise need to reverse-engineer intent. Add them near:

- The capability newly introduced in the current stage.
- Non-obvious control flow, data flow, state transitions, concurrency, or error handling.
- Invariants and constraints that would be easy to violate during an experiment.
- Module boundaries and interfaces whose purpose is architectural rather than mechanical.
- Deliberate simplifications, temporary limitations, and tradeoffs that motivate a later stage.

Use comments to explain intent, collaboration, and consequence. Let clear code explain syntax and routine operations. Prefer one useful comment at a decision boundary over comments on every statement. Remove or update a comment whenever it no longer describes the code.

## Curated-source final project

A curated-source `Final-Project/` preserves the selected project's core implementation and architecture while removing material that does not serve the agreed learning scope. Inventory and classify the source tree before pruning it.

Retain:

- Source, configuration, assets, generated inputs, and tests required to build, run, or verify the selected capabilities.
- Files that explain architecture, domain terminology, important decisions, or non-obvious operation.
- License, copyright, attribution, notice, and third-party-license files required by the project's licenses.

Repository operations such as CI workflows, issue templates, funding configuration, release automation, unrelated examples, and out-of-scope documentation are candidates for removal only after confirming that the retained project does not reference or require them. A file's unfamiliarity or lack of runtime code is not evidence that it is disposable.

Add `Final-Project/LEARNING-GUIDE.md` as the entry point for the curated source. Add further descriptive files only when they provide a distinct learning function, such as an architectural overview that would overload the guide. Teaching comments may be added at learning-critical decision boundaries, but preserve the source project's structure and behavior. Record every removed, added, and materially edited path with its reason in `Source-Notes.md`.

Re-run the retained build, run, and test paths after curation. If removing a file breaks behavior, navigation, attribution, or license compliance, restore it or repair the curated package before proceeding.

## Exact-source final project

Do not insert teaching comments or replace documentation inside an exact-source `Final-Project/`. Create `Final-Project-Guide.md` beside the root `README.md` instead. It must provide:

- Verified build, run, and test entry points for the pinned source revision.
- A reading path through the upstream project using concrete files and symbols.
- A mapping from each reconstructed stage to the corresponding mechanisms in the final source.
- The architectural gap between the last intermediate stage and the complete endpoint.
- Important upstream terminology, documentation links, and assumptions needed to navigate the project.

For a teaching adaptation or original reference project, place teaching annotations in its code and provide equivalent final-stage guidance without claiming it is unmodified upstream source.

## Completion check

Before finishing, follow each documented reading path against the actual files, run every documented verification command that the environment permits, and repair stale names, missing files, incorrect commands, or unexplained learning-critical mechanisms. Documentation that does not match the runnable snapshot fails the stage even when the code itself works.
