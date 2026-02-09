# Formatting Blocks

Formatting in `text-curation` is implemented as a **two-stage pipeline**
with strict ordering and stability guarantees.

Formatting is **structural**, not semantic.

These blocks are part of the **stable core**.

These blocks are **low-level deterministic primitives** intended for
profile authors and library extension.
Most users should rely on profiles rather than composing blocks directly.

---

## Formatting Pipeline (Mandatory Order)

Formatting **must** be applied in the following order:

1. `CodeSafeFormattingBlock`
2. `ParagraphFormattingBlock`

This ordering is **required and non-negotiable**.

Reordering these blocks is a **breaking change**.

---

## CodeSafeFormattingBlock

Performs **structural whitespace hygiene only**.

This block exists to normalize text in a way that is
**safe for code, configuration files, logs, and mixed content**.

### Guarantees

When this block is applied:

- Leading indentation is preserved
- Trailing whitespace may be normalized
- Line endings are normalized deterministically
- No lines are merged
- No lines are split
- No content is reflowed

This block is safe to apply to:

- source code
- configuration files
- logs
- stack traces
- mixed prose/code documents

---

## ParagraphFormattingBlock

Reconstructs readable paragraph structure **conservatively**.

This block operates only after `CodeSafeFormattingBlock`
and assumes line endings and indentation are already normalized.

### Guarantees

When this block is applied:

- Paragraph boundaries are inferred conservatively
- Paragraph order is preserved
- Paragraph semantics are preserved
- Indentation-sensitive content is preserved
- No semantic rewriting is performed
- No content is reordered

---

## Explicit Non-Behavior

Formatting blocks do **not**:

- Merge lines based on semantic meaning
- Rewrap or reflow prose
- Normalize casing
- Modify punctuation beyond canonical Unicode normalization
- Interpret Markdown, HTML, or other markup
- Apply language-specific formatting rules
- Perform any content deletion

---

## Stability

Formatting behavior is **stable as of `v1.x`**.

Formatting changes are considered **high-risk**.

Any behavioral change requires:

- a **major version bump**, and
- updated golden tests, and
- explicit documentation of before/after behavior