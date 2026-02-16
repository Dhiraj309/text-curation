# web_pretrain_v1

`web_pretrain_v1` is a deterministic, signal-rich profile
designed for heterogeneous web-derived corpora.

## Block Order

1. RedactionBlock
2. NormalizationBlock
3. CodeSafeFormattingBlock
4. ParagraphFormattingBlock
5. BasicStructureBlock
6. QualitySignalBlock
7. TokenStatsBlock
8. FingerprintBlock

## Behavior

- Redacts secrets
- Normalizes Unicode artifacts
- Preserves code indentation
- Reconstructs paragraphs
- Emits structural signals
- Emits quality metrics
- Emits token statistics
- Emits document fingerprint

## Non-Goals

This profile does not:

- Perform dataset-level deduplication
- Filter content
- Apply ML-based scoring
- Introduce randomness

## Guarantees

- Deterministic
- Explicit block order
- No hidden global state
- Profile ID fully specifies behavior

Golden tests enforce stability.