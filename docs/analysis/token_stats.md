# TokenStatsBlock

`TokenStatsBlock` emits token-level statistics based on whitespace tokenization.

## Signals Emitted

- `document.token_count`
- `document.unique_token_count`
- `document.rare_token_ratio`
- `document.max_token_length`

## Token Definition

Tokens are defined as whitespace-separated units.

This block does not use external tokenizers.

## Rare Token Definition

A rare token is defined as appearing exactly once within the document.

This definition is local to the document and deterministic.

## Design Rationale

Tokenizer-dependent statistics introduce version drift risk.

This block intentionally avoids:

- External tokenizers
- Model-specific vocabulary
- Subword segmentation

It provides lightweight, deterministic statistics suitable for:

- Corpus inspection
- Distribution analysis
- Reproducibility tracking

## Determinism

All outputs are deterministic and environment-independent.