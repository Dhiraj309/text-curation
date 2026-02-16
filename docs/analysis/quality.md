# QualitySignalBlock

`QualitySignalBlock` emits document-level quality metrics.

## Signals Emitted

- `document.char_entropy`
- `document.stopword_ratio`
- `document.url_density`
- `document.repetition_score`
- `document.avg_sentence_length`

All signals are numeric and deterministic.

## Design Characteristics

- Whitespace-based tokenization
- No external model dependencies
- No filtering logic
- No implicit thresholds
- Float rounding applied for stability

This block is intended for:

- Dataset inspection
- Profiling
- Downstream filtering (explicitly applied elsewhere)

It does not modify text and does not remove content.

## Determinism

Given identical input text and identical configuration:

- All metrics are identical across runs
- No randomness is used
- No environment-dependent state is accessed

This block is safe for reproducible corpus analysis.