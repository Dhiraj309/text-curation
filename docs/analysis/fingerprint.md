# FingerprintBlock

`FingerprintBlock` computes a deterministic SHA-256 fingerprint of document text.

## Signal Emitted

- `document.sha256`

## Hashing Method

- UTF-8 encoding
- SHA-256 digest
- Hexadecimal representation

## Normalization

Optional normalization may be applied prior to hashing.
Normalization behavior must be explicit in the block policy.

The fingerprint reflects the exact post-normalization document text.

## Purpose

Document fingerprints support:

- Dataset deduplication
- Lineage tracking
- Reproducibility auditing

## Determinism

- No randomness
- No dependency on Python's built-in `hash()`
- Stable across machines and interpreter restarts