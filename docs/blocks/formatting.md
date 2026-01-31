# Formatting Blocks

Formatting in `text-curation` is implemented as a **two-stage pipeline**
with strict ordering and stability guarantees.

Formatting is **structural**, not semantic.

These blocks are part of the **stable core**.

---

## Formatting Pipeline (Mandatory Order)

Formatting consists of the following blocks, applied **in order**:

1. `CodeSafeFormattingBlock`
2. `ParagraphFormattingBlock`

This ordering is **required**.

Reordering or omitting blocks may result in undefined behavior
and is not supported by any built-in profile.

---

## CodeSafeFormattingBlock

The `CodeSafeFormattingBlock` performs **structural hygiene only**.

It exists to normalize low-risk whitespace artifacts
without altering content meaning or structure.

---

### Behavior

This block performs the following operations:

- Normalize line endings to `\n`
- Trim trailing whitespace on each line
- Collapse runs of more than two blank lines

---

### Guarantees

When this block is applied:

- Leading indentation is preserved exactly
- Relative indentation is preserved
- No lines are merged
- No lines are split
- No content is rewritten

This block is safe for indentation-sensitive content,
including code blocks and configuration files.

---

### Explicit Non-Behavior

This block does **not**:

- Normalize indentation width
- Align indentation
- Reflow text
- Modify punctuation
- Interpret language or syntax

---

## ParagraphFormattingBlock

The `ParagraphFormattingBlock` reconstructs **human-readable paragraph structure**
from wrapped or line-broken prose.

It operates only at **explicit structural boundaries**.

---

### Behavior

This block performs the following operations:

- Reconstruct paragraphs from wrapped prose
- Preserve indented lines verbatim
- Respect explicit blank-line boundaries
- Normalize punctuation spacing (when enabled)

Paragraph reconstruction is applied **only** when paragraph intent
can be determined conservatively.

---

### Paragraph Reconstruction Rules (Stable)

Paragraph reconstruction follows these rules exactly:

- Blank lines always terminate a paragraph buffer
- Indented lines are never merged with surrounding text
- Adjacent lines are merged **only** when:
  - The paragraph is identified as prose
  - The previous line does not terminate a sentence
- Non-prose blocks flush the buffer immediately
- Original line order is preserved

These rules are enforced by tests and are considered stable.

---

### Punctuation Normalization

When enabled, punctuation normalization:

- Fixes spacing around `, ! ? : ;`
- Reduces excessive punctuation runs (e.g. `!!!!` → `!`)
- Preserves:
  - URLs
  - email addresses
  - IP addresses
  - numeric formats
  - timestamps

---

### Guarantees

When this block is applied:

- Paragraph semantics are preserved
- Indentation-sensitive content is preserved
- No implicit sentence splitting occurs
- No semantic rewriting occurs

---

### Explicit Non-Behavior

This block does **not**:

- Perform sentence tokenization
- Parse Markdown or HTML
- Infer document structure semantically
- Merge unrelated lines
- Normalize stylistic formatting

---

## Stability

- Formatting behavior is stable as of `v1.x`
- Formatting regressions are considered **high-risk**
- Any behavioral change requires:
  - new tests
  - a new block, or
  - a major version bump

---

## Notes on Use

Formatting exists to improve **readability and consistency**
without sacrificing semantic integrity.

When in doubt, formatting **does less**, not more.
