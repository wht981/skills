# Micro Notes

A micro note explains one independently reusable algorithm, mechanism, or focused technique in depth and places it at a specific point in its parent structure. Its internal parts may be complex, but they remain steps, parameters, or implementation details that do not need independent knowledge artifacts.

## Procedure

Choose the structure from `structure-models.md` that best explains the subject itself. Common choices include a flow for operational steps, an onion for the core mechanism and replaceable parts, or a matrix for variants and parameters. Reclassify the subject as a system when it contains multiple independently explainable core units and explaining their collaboration is necessary to explain the whole. Do not reclassify it because the note is long or its implementation has many steps.

This is the terminal scale. Keep further decomposition inside the current note as sections, steps, parameters, formulas, or implementation details. Do not create another layer of knowledge artifacts from those details.

The note must cover:

1. **Mechanism:** The internal process step by step, not a black-box description.
2. **Design decisions:** The problem solved, the tradeoffs made, and important alternatives.
3. **Variants and parameters:** The available variants and the meaning and effect of important values.
4. **Applications:** Where and how it is used, including common combinations.
5. **Limits and misuse:** Boundary conditions, failure cases, and common incorrect uses.
6. **Operational interfaces:** The inputs, outputs, dependencies, and interactions required for the mechanism to work. Broader ecosystem placement and relationships to peer topics are optional.

These six items are a coverage checklist, not a fixed section template. Let the chosen structure determine section order and emphasis.

## Completion criteria

All six areas contain substantive information, the mechanism is not treated as a black box, and its required operational interfaces are clear. Further decomposition would produce only steps, parameters, or implementation details without independent reuse value. The explanation does not expand into adjacent systems merely to appear globally complete.
