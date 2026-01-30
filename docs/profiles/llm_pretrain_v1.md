# llm_pretrain_v1

The `llm_pretrain_v1` profile defines a **minimal, deterministic, non-destructive**
text curation pipeline designed specifically for **large-scale LLM pretraining**.

It is optimized for scenarios where **raw text fidelity, repetition, and structural signals**
must be preserved, and where **no semantic interpretation or filtering** is acceptable.

This profile is treated as a **locked behavioral contract**.

---

## Intended Use

This profile is suitable for:

* LLM pretraining corpora (e.g. FineWeb-style datasets)
* Large-scale language modeling pipelines
* Tokenization- and loss-sensitive training data
* Datasets where repetition and boilerplate carry signal
* Pretraining inputs shared across models or organizations

It is intended for **direct consumption by LLMs**, not for downstream
retrieval, ranking, or quality-filtered datasets.

---

## Pipeline Overview

At a high level, `llm_pretrain_v1` applies the following stages:

1. Redaction of sensitive tokens
2. Character-level normalization and hygiene
3. Code-safe formatting preservation

No additional filtering, restructuring, or content removal is performed.

Each stage is deterministic and independently testable.

---

## Guarantees (Stable)

When using `llm_pretrain_v1`, the following guarantees hold:

* Output is fully deterministic for a given input
* Processing order does not affect the result
* No machine learning or semantic inference is applied
* No content is removed, rewritten, or filtered
* Repetition and boilerplate are preserved
* Paragraph and document structure are preserved
* Visual layout is preserved to the extent possible
* Indentation-sensitive content (e.g. code blocks) is preserved
* No deduplication is performed
* Secrets are redacted; general PII is not removed
* Numeric formats, timestamps, and identifiers are not modified

These guarantees are enforced by **golden tests**
and are considered part of the profile’s public contract.

---

## Known Limitations (Intentional)

The following behaviors are expected and intentional:

* Boilerplate and templated text may appear repeatedly
* Low-quality or noisy text is not filtered
* Headers, footers, and navigation text are retained
* No quality, language, or domain heuristics are applied
* No semantic cleanup or paragraph reflow is performed

These trade-offs are required to ensure **training-time fidelity**
and to avoid silent data drift in pretraining corpora.

---

## When Not to Use

This profile may not be appropriate if you require:

* Web-style cleanup or content consolidation
* Boilerplate stripping or deduplication
* Quality, safety, or semantic filtering
* Language- or domain-specific heuristics
* Downstream task optimization

Such behavior should be implemented via
**separate, explicitly opt-in profiles**.

---

## Versioning & Stability

* `llm_pretrain_v1` is stable across all `1.x` releases
* Behavior will not change without a major version bump
* The profile may be deprecated in the future, but
  **will never be silently changed**
* Any behavior changes require a new profile version
  (e.g. `llm_pretrain_v2`)

This reflects the library’s core principle:

**Profiles evolve. Contracts do not.**