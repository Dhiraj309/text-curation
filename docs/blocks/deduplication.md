# DeduplicationBlock

The `DeduplicationBlock` removes **exact duplicate paragraphs**
within a single document.

Deduplication is **local, deterministic, and conservative** by design.

---

## What it does

- Splits text into paragraphs
- Normalizes paragraphs for comparison only
- Removes repeated paragraphs
- Preserves first-occurrence order

Deduplication is performed **after normalization and formatting**
to ensure stable comparisons.

---

## Normalization rules (comparison only)

For deduplication keys:

- Collapses whitespace
- Lowercases text
- Preserves punctuation
- Uses exact string equality

The **original paragraph text is preserved** in output.

---

## What it does NOT do

- ❌ No cross-document deduplication
- ❌ No fuzzy or similarity-based matching
- ❌ No semantic or embedding-based comparison

---

## Design rationale

Deduplication is intentionally limited to **exact, local repetition**
to avoid false positives in narrative, legal, or technical text.

More aggressive deduplication strategies must be introduced
via explicit, opt-in profiles.