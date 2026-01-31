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

1. `CodeSafeFormattingBlock`
2. `ParagraphFormattingBlock`

This ordering is **required**.

---

## CodeSafeFormattingBlock

Performs structural whitespace hygiene only.

### Guarantees

- Leading indentation preserved
- No line merging or splitting
- Safe for code and config files

---

## ParagraphFormattingBlock

Reconstructs readable paragraph structure conservatively.

### Guarantees

- Paragraph semantics preserved
- Indentation-sensitive content preserved
- No semantic rewriting

---

## Stability

Formatting behavior is stable as of `v1.x`.
Any behavioral change requires a major version bump.
