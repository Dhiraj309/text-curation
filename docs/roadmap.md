# Roadmap

⚠️ **Non-binding roadmap**

This document describes areas of exploration and possible future
directions for `text-curation`.  
It is **not a commitment** to implement specific features or timelines.

Inclusion here does **not** guarantee implementation.

---

This document outlines **exploratory and potential areas of future work**
for `text-curation`.

The guiding direction of the project is to support **well-defined,
profile-based text curation pipelines** suitable for different stages
of large-scale dataset preparation, including:

- raw web-scraped text
- pretraining corpora
- fine-tuning and evaluation datasets

All future work must preserve the library’s core principles:

- determinism
- conservative defaults
- explicit behavior
- long-term reproducibility

---

## Near-Term (1.x series)

**Focus:** Strengthening general-purpose, conservative text curation

Work in the `1.x` series is intentionally constrained.

The following rules apply:

- Default behavior of existing blocks **must not change**
- Existing profiles **must not change**
- All new behavior must be **opt-in**
- Stability takes priority over feature velocity

Exploratory areas may include:

- **Enhanced deduplication (opt-in only)**
  - Paragraph-level or windowed deduplication
  - Exact or near-exact matching
  - Never enabled by default
  - Always profile-scoped

- **Non-destructive boilerplate signals**
  - Continuous boilerplate likelihood indicators
  - Paragraph- and document-level aggregation
  - Signals only; no implicit filtering

- **Expanded built-in profiles**
  - Additional web-derived profiles (e.g. wiki-style, forum-style)
  - Clearly scoped behavior and guarantees
  - Explicit versioning and golden tests

- **Documentation hardening**
  - Block-level behavioral specifications
  - Profile contracts with before/after examples
  - Dataset-oriented usage guidance

---

## Possible 2.x Directions

**Focus:** Richer structure awareness and extensibility

The following areas may be explored in future **major** releases.
All such behavior must remain **explicit, opt-in, and profile-scoped**.

- **HTML-aware preprocessing**
  - Tag-aware text extraction
  - Boilerplate-aware DOM traversal
  - Explicit separation from semantic filtering

- **Advanced deduplication strategies**
  - Optional fuzzy or similarity-based deduplication
  - Strictly limited to specific profiles
  - Never enabled implicitly

- **Profile composition and reuse**
  - Shared profile components
  - Explicit composition semantics
  - Full auditability of derived profiles

---

## Exploratory Directions (Longer Term)

**Focus:** Clear separation of curation responsibilities by granularity

Longer-term exploration may focus on clearer boundaries between:

- **Paragraph-level curation**
  - Structure detection
  - Boilerplate signaling
  - Local deduplication

- **Sample-level curation**
  - Document consistency checks
  - Aggregate signal thresholds
  - Explicit, opt-in sample filtering

- **Corpus-level curation**
  - Template and repetition detection
  - Dataset-wide deduplication utilities
  - Metadata-aware hooks

These directions are intended to support different dataset needs, such as:

- large-scale pretraining corpora
- domain-adapted fine-tuning datasets
- evaluation and benchmark preparation

---

## Explicitly Out of Scope

The following are intentionally **not planned**:

- ML-based quality scoring or ranking
- Automatic semantic classification
- Language-specific default rules
- Aggressive or opaque content pruning
- Model- or tokenizer-dependent preprocessing

Such behavior is better handled by downstream systems
or explicitly opt-in tooling.

---

## Stability Commitment

All future changes must adhere to the following rules:

- Existing profile behavior is preserved
- Default block behavior is stable
- Silent behavior changes are forbidden

Breaking changes require:

- a major version bump
- explicit documentation
- updated golden tests
