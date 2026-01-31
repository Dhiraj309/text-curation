# NormalizationBlock

The `NormalizationBlock` performs **low-level, non-semantic normalization**
to remove encoding artifacts and standardize Unicode variants.

This block is part of the **stable core**.

This block is a **low-level deterministic primitive** intended for
profile authors and library extension.
Most users should rely on profiles rather than composing blocks directly.

---

## Behavior (Stable)

Normalization includes:

- Unicode normalization (NFKC)
- Removal of zero-width and control characters
- Canonicalization of quotes, dashes, ellipses
- Conservative whitespace normalization

---

## Guarantees

- Deterministic behavior
- No semantic rewriting
- Indentation preserved
- Safe for code and logs

---

## Explicit Non-Behavior

- No casing normalization
- No spelling or grammar fixes
- No paragraph restructuring

---

## Stability

Stable as of `v1.x`.
Changes require a major version bump.
