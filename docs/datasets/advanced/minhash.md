# Deterministic Reference MinHash Deduplication

`minhash_deduplicate()` performs approximate duplicate detection
using seeded MinHash signatures.

This implementation is deterministic and reference-oriented.

## Configuration

- `ngram_size` (explicit)
- `num_hashes` (explicit)
- `threshold` (explicit)
- `seed` (required)

No randomness is allowed without an explicit seed.

## Hashing Method

- SHA-1 based hashing
- Explicit seed integration
- No reliance on Python's built-in `hash()`

## Cluster Representative Rule

For each cluster of near-duplicates:

- The canonical representative is the sample with the lowest index.

This ensures:

- Deterministic selection
- Order preservation

## Performance

This is a reference implementation:

- O(n²) comparison
- Single-process
- Not optimized for distributed scale

It prioritizes semantic stability over performance.

## Determinism

Given identical dataset ordering and identical configuration:

- Clusters are identical
- Representatives are identical
- Output ordering is identical