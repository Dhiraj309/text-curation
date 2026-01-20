# DeduplicationBlock

The `DeduplicationBlock` removes **exact duplicate paragraphs**
within a single document.

Deduplication is **local, deterministic, and conservative**.

---

## What it does

- Splits text into paragraphs
- Normalizes paragraphs for comparison
- Removes repeated paragraphs
- Preserves first-occurrence order

---

## Normalization rules

For comparison only:

- Collapses whitespace
- Lowercases text
- Does **not** remove punctuation
- Does **not** perform fuzzy matching

The original paragraph text is preserved for output.

---

## What it does NOT do

- ❌ No cross-document deduplication
- ❌ No fuzzy or similarity-based matching
- ❌ No semantic deduplication

---

## Design rationale

Deduplication is intentionally limited to **exact, local repetition**
to avoid false positives in narrative or technical text.

More aggressive deduplication strategies are reserved for
explicit opt-in profiles.
