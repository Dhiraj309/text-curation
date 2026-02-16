# SHA-256 Hash Deduplication

`deduplicate_by_hash()` removes exact duplicate samples
based on SHA-256 fingerprint comparison.

## Behavior

- Computes SHA-256 for each sample
- Groups identical hashes
- Keeps either "first" or "last" (explicit)
- Preserves dataset order

## Determinism

- No use of Python built-in `hash()`
- Stable hash function (SHA-256)
- Explicit `keep` policy
- Order preserved

## Guarantees

Given identical dataset content and ordering:

- Output dataset is identical
- Report is identical

This operation performs exact deduplication only.
No normalization or semantic similarity is applied.
