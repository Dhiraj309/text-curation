# Analysis Namespace

The `analysis/` namespace contains signal-only blocks that observe document
properties without mutating text.

## Design Principle

Analysis blocks:

- MUST NOT modify `document.text`
- MUST NOT mutate `document.annotations`
- MAY emit signals via `document.add_signal`
- MUST be deterministic
- MUST not rely on hidden global state

This namespace separates detection from transformation.

- `blocks/` mutate or structure text.
- `analysis/` computes inspectable metrics and fingerprints.

Filtering decisions must be explicit and occur outside analysis blocks.

## Why This Exists

As `text-curation` evolved toward corpus compilation, it became necessary to:

- Compute quality metrics
- Compute fingerprints
- Compute token statistics
- Emit structural signals

without coupling those observations to filtering behavior.

This separation preserves:

- Auditability
- Reproducibility
- Explicit policy control

## Determinism Requirements

All analysis blocks must:

- Use explicit configuration
- Avoid randomness unless seed is required and explicit
- Avoid model downloads
- Avoid hardware-dependent behavior
- Produce byte-identical output for identical input

Analysis blocks are pure observation layers.