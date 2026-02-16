# Exact N-gram Decontamination (Signal-Only)

`decontaminate()` computes overlap between dataset samples
and a provided benchmark n-gram set.

## Inputs

- `benchmark_ngrams: Set[str]`
- `ngram_size: int`

## Output

Adds:

- `overlap_score` column

No rows are removed by default.

## Design Philosophy

Detection is separate from filtering.

This function:

- Computes deterministic overlap scores
- Does not filter samples implicitly

Filtering decisions must be applied explicitly by the user.

## Determinism

- No randomness
- Whitespace tokenization
- Explicit n-gram size
- Stable across runs