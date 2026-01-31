# BasicStructureBlock

The `BasicStructureBlock` analyzes document structure and emits
**inspectable structural signals**.

This block **never mutates text**.

It exists solely to observe and describe structure in a
deterministic and reproducible way.

This block is part of the **stable core**.

---

## Scope

Structure analysis is applied:

- At the line and paragraph level
- Using deterministic, rule-based detection
- Without semantic or linguistic interpretation

The block observes structure; it does not act on it.

---

## Behavior

The block performs the following operations:

1. Split the document into lines
2. Split the document into paragraphs using blank-line boundaries
3. Compute repetition statistics for lines and paragraphs
4. Emit structural signals for downstream consumption

All signals are **append-only** and immutable once emitted.

---

## Signals Emitted (Stable)

### Line-Level Signals

For each line `i`:

- `line[i].is_blank`  
  Whether the line contains only whitespace

- `line[i].is_header`  
  Whether the line matches a header-like pattern
  (Markdown-style or ALL CAPS)

- `line[i].is_bullet`  
  Whether the line appears to be a bullet item

- `line[i].is_numbered_item`  
  Whether the line appears to be a numbered list item

- `line[i].is_all_caps`  
  Whether the line consists primarily of uppercase characters

- `line[i].is_short`  
  Whether the line length is below the configured threshold

- `line[i].repetition_count`  
  Frequency of the normalized line within the document

---

### Paragraph-Level Signals

For each paragraph `j`:

- `paragraph[j].is_list_block`  
  Whether the paragraph consists primarily of list-like lines

- `paragraph[j].is_boilerplate_candidate`  
  Whether the paragraph is repeated within the document

- `paragraph[j].repetition_count`  
  Frequency of the paragraph within the document

---

## Detection Methods

Signal detection is based on:

- Explicit regular expressions
- Length thresholds
- Frequency counts within the document

No probabilistic or learned logic is used.

---

## Guarantees

When this block is applied:

- Text content is never modified
- Signal emission is deterministic
- Signal meanings are stable
- Signal names are stable
- No decisions are made implicitly

---

## Explicit Non-Behavior

This block does **not**:

- Modify or remove text
- Perform semantic classification
- Detect language or topic
- Score quality or usefulness
- Decide what content should be kept or removed

Any removal or transformation must be performed
by downstream blocks explicitly.

---

## Separation of Concerns

This block enforces a strict separation between:

- **Observation** (this block)
- **Decision** (filtering, deduplication, etc.)

This separation is fundamental to:

- auditability
- explainability
- reproducibility

Hidden decision logic is forbidden.

---

## Stability

- Signal definitions are stable as of `v1.x`
- Renaming or redefining signals is a breaking change
- Adding new signals is allowed but must be documented

---

## Notes on Use

Structure signals are intended to be:

- consumed explicitly by downstream blocks
- surfaced in reports
- inspected during debugging

They are **descriptive**, not prescriptive.
