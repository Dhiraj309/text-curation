# DeduplicationBlock

The `DeduplicationBlock` removes **exact duplicate paragraphs**
within a document.

---

## What it does

- Splits text into paragraphs
- Normalizes whitespace and casing
- Removes repeated paragraphs
- Preserves first occurrence order

---

## Normalization rules

- Collapses whitespace
- Lowercases text
- Does NOT remove punctuation
- Does NOT perform fuzzy matching

---

## What it does NOT do

- ❌ No cross-document deduplication
- ❌ No fuzzy similarity matching
- ❌ No semantic deduplication

---

## Design rationale

Deduplication is conservative and local to avoid
false positives in narrative text.

More aggressive strategies are reserved for opt-in profiles.
