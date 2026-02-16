# DatasetManifest

`DatasetManifest` captures dataset lineage and reproducibility metadata.

## Fields

- `profile_ids`
- `library_version`
- `block_order`
- `dataset_hash`
- `total_token_count`
- `timestamp`
- `metadata`

## Dataset Hash

Computed as:

- SHA-256 over ordered text column
- UTF-8 encoding
- Order-sensitive

Identical datasets with identical ordering produce identical hashes.

## Timestamp

Must be provided explicitly by the caller.

No implicit system time is read.

## Purpose

The manifest enables:

- Lineage tracking
- Experiment reproducibility
- Configuration auditing

It does not enforce policy automatically.
It is an explicit artifact.

## Determinism

Manifest contents are deterministic
except for explicitly provided timestamp.