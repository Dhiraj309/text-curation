# ExactParagraphDeduplicationBlock

The `ExactParagraphDeduplicationBlock` removes **exact duplicate paragraphs**
within a single document.

Deduplication is **local, deterministic, order-preserving, and conservative**.

This block is part of the **stable core**.

---

## Scope

Deduplication is applied:

- **Within a single document only**
- **At paragraph granularity**
- **After normalization and formatting**

No cross-document or dataset-level deduplication is performed.

---

## Behavior

The block performs the following steps:

1. Split the document into paragraphs using blank-line boundaries
2. Generate a comparison key for each paragraph
3. Remove paragraphs whose comparison key has already been seen
4. Preserve the first occurrence of each paragraph
5. Preserve original paragraph text in output

Paragraph order is preserved.

---

## Comparison Key (Stable)

Paragraphs are compared using a **non-semantic normalization key**:

- Leading and trailing whitespace is stripped
- Internal whitespace is collapsed
- Text is lowercased
- Punctuation is preserved
- Exact string equality is used

The normalized key is used **only for comparison**.
The original paragraph content is retained.

---

## Guarantees

When this block is applied:

- Deduplication is deterministic
- Only exact duplicates are removed
- Paragraph order is preserved
- Paragraph content is not rewritten
- No semantic inference is performed

---

## Explicit Non-Behavior

This block does **not**:

- Perform fuzzy or similarity-based matching
- Use embeddings or hashing
- Deduplicate across documents
- Deduplicate across datasets
- Remove near-duplicates
- Perform semantic comparison

---

## Stability

- Behavior is stable as of `v1.x`
- Any change requires:
  - a new block, or
  - a major version bump

---

## Notes on Use

This block is intentionally conservative.

More aggressive or cross-document deduplication must be implemented as:

- a separate block
- a dataset-level utility
- or a profile-specific opt-in pipeline
