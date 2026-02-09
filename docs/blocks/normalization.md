# NormalizationBlock

The `NormalizationBlock` performs **low-level, non-semantic normalization**
to remove encoding artifacts and standardize Unicode variants.

This block is part of the **stable core**.

This block is a **low-level deterministic primitive** intended for
profile authors and library extension.
Most users should rely on profiles rather than composing blocks directly.

---

## Scope

Normalization operates at the **character and token boundary level only**.

It is intended to make text **mechanically comparable and processable**
without changing meaning, structure, or intent.

---

## Behavior (Stable)

Normalization includes the following deterministic transformations:

- Unicode normalization using **NFKC**
- Removal of zero-width characters
- Removal of non-printable control characters
- Canonicalization of:
  - quotation marks
  - dashes
  - ellipses
- Conservative whitespace normalization that does **not** alter structure

All transformations are applied uniformly and without context.

---

## Guarantees

When this block is applied:

- Behavior is fully deterministic
- No semantic rewriting is performed
- No structural rewriting is performed
- Indentation is preserved
- Line boundaries are preserved
- Safe for:
  - source code
  - logs
  - configuration files
  - mixed prose/code documents

---

## Explicit Non-Behavior

This block does **not**:

- Normalize casing
- Perform spelling correction
- Perform grammar correction
- Rewrite words or tokens
- Reflow or merge lines
- Reconstruct paragraphs
- Interpret language, markup, or syntax
- Perform locale- or language-specific normalization

---

## Stability

Normalization behavior is **stable as of `v1.x`**.

Normalization changes are considered **high-risk**.

Any behavioral change requires:

- a **major version bump**, and
- updated unit tests locking the new behavior, and
- explicit documentation of the change