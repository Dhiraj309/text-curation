# NormalizationBlock

The `NormalizationBlock` performs **low-level, non-semantic text normalization**
to remove encoding artifacts and standardize common Unicode variants.

This block exists to ensure **text hygiene**, not readability or quality.

It is part of the **stable core**.

---

## Scope

Normalization is applied:

- At the character and line level
- Uniformly across the entire document
- Without inspecting language, semantics, or structure

This block must be safe for:
- prose
- code
- logs
- configuration files

---

## Behavior (Stable)

The block performs the following operations, in order:

1. Apply Unicode normalization (`NFKC`)
2. Remove zero-width characters
3. Remove non-printable ASCII control characters
4. Normalize line endings (`\r\n`, `\r` → `\n`)
5. Normalize quotation mark variants
6. Normalize dash variants
7. Normalize ellipses (`…` → `...`)
8. Collapse runs of spaces and tabs **within lines**
9. Limit excessive consecutive newlines
10. Trim leading and trailing document whitespace

---

## Whitespace Rules (Important)

Whitespace normalization follows strict rules:

- Leading indentation on each line is preserved exactly
- Internal runs of spaces and tabs are collapsed
- Line breaks are preserved except when excessive
- Blank-line boundaries remain meaningful

These rules are enforced to avoid damaging:
- code indentation
- aligned text
- structural layout

---

## Guarantees

When this block is applied:

- Normalization is deterministic
- No content is semantically rewritten
- No characters are reordered
- Indentation-sensitive content remains valid
- Output is safe for downstream formatting and analysis

---

## Explicit Non-Behavior

This block does **not**:

- Correct spelling or grammar
- Fix OCR errors
- Normalize casing
- Apply language-specific rules
- Rewrite sentences
- Merge or split paragraphs

---

## Reversibility

While normalization is not strictly reversible,
all transformations are:

- conservative
- predictable
- limited to encoding artifacts

No information-bearing content is intentionally removed.

---

## Stability

- Behavior is stable as of `v1.x`
- Any change to normalization rules requires:
  - a new block, or
  - a major version bump

---

## Notes on Use

Normalization should run **early** in all pipelines.

It exists to make downstream processing reliable,
not to improve textual quality.
