# Meso Notes

A meso artifact pursues explanatory completeness for a bounded knowledge system and materializes that explanation as a navigable directory tree. Include a core unit because its role or mechanism is necessary to explain how the whole system works, not merely because it is taxonomically adjacent or belongs to a broader field. Focus on why each part exists, how the parts cooperate, and how the complete capability follows from the underlying mechanisms.

## Procedure

1. Define the system's internal boundary and identify every component, stage, mechanism, and algorithm required to reconstruct how it works. Exclude peer systems and taxonomy branches that do not participate in this explanation.
2. Choose a primary structure that expresses the internal relationships, then derive a content tree from composition, causality, process, or levels of abstraction.
3. Create a root directory named after the actual system. Place its main note at the root, then create enough subdirectories and notes to make every independently explainable core unit visible. Use a subdirectory only when it groups a coherent subsystem with multiple child notes.
4. For every core part, explain its responsibility, mechanism, inputs and outputs, collaboration with other parts, and important design tradeoffs.
5. Connect the data flow, control flow, or causal chain across parts so a reader can reconstruct the whole system from the local mechanisms. Use links to express relationships that do not fit the directory hierarchy.
6. Cover important variants, capability boundaries, failure conditions, and unsettled questions. Use these to clarify the system itself, not to expand into a survey of peer systems.
7. Create a dedicated deep-dive note whenever understanding that subunit is necessary to explain the current system completely. Before writing any such note, read `micro.md` and apply its complete procedure and completion criteria. Do this without waiting for the user to name each required subunit. Leave optional extensions uncreated. Link every deep-dive note from the main note.

The directory tree is part of the explanation. Its hierarchy must reflect explanatory dependencies, internal composition, and process structure, not a complete taxonomy of neighboring topics, storage convenience, file count, or internal scale labels. Give independently explainable core units their own notes. Keep steps, parameters, formulas, and implementation details inside the note they explain unless they form a reusable knowledge object in their own right.

The root note leads the tree and must remain independently readable. Retain each subunit's responsibility, key mechanism, and role in the end-to-end system while moving detailed derivations, variants, and boundaries into dedicated notes. It must not become a bare table of contents after explanations move into child notes.

External positioning is optional. When a higher-level structure exists, retain only the ownership link. Without one, add only the minimum context required to understand the current system. Do not introduce peer systems, map the surrounding ecosystem, or repeat relationships already established by a macro note merely for completeness.

## Completion criteria

Explanatory completeness is reached when the directory tree represents every internal unit and relationship needed to reconstruct how the system works. Every directory groups a coherent subsystem, and every required independently explainable core unit has a substantive note reachable from the root. Without opening a child note, a reader can still trace the end-to-end processes or causal chains and explain the responsibility, key mechanism, collaboration, and role of every core part. Required deep dives exist and are linked. No core part is only named without substantive explanation. Taxonomic breadth and external material do not displace internal depth or repeat an existing higher-level note.
