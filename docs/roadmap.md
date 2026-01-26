# Roadmap

This document outlines **planned and potential areas of future work**
for `text-curation`.

The guiding direction of the project is to explore **well-defined,
profile-based text curation pipelines** suitable for different stages
of large-scale dataset preparation, including:

- raw web-scraped text
- pretraining corpora
- fine-tuning and evaluation datasets

All future work is expected to preserve the library’s
**deterministic, conservative, and reproducible** design principles.

---

## Near-Term (1.x series)

**Focus:** Strengthening general-purpose web text curation

Work in the `1.x` series is limited to:

- improving signal quality
- expanding profile coverage
- refining documentation and tests

Default behavior of existing blocks and profiles
**must not change**.

Potential areas include:

- **Enhanced deduplication (opt-in only)**
  - Paragraph-level and sliding-window deduplication
  - Conservative exact or near-exact matching
  - Never enabled by default

- **Boilerplate scoring (non-destructive)**
  - Continuous boilerplate likelihood signals
  - Paragraph- and document-level aggregation
  - Filtering decisions remain explicit and opt-in

- **Expanded built-in profiles**
  - Additional web-derived profiles (e.g. wiki-style, forum-style)
  - Clearly scoped profile contracts and guarantees

- **Improved documentation**
  - Block-level behavioral specifications
  - Profile contracts with before/after examples
  - Dataset-oriented usage guidance

---

## Medium-Term (2.x candidates)

**Focus:** Richer structure awareness and extensibility

The following areas may be explored in future major releases.
All such behavior must remain **opt-in or profile-specific**.

- **HTML-aware preprocessing**
  - Tag-aware text extraction
  - Boilerplate-aware DOM traversal
  - Explicit separation from semantic filtering

- **Advanced deduplication strategies**
  - Optional fuzzy or similarity-based deduplication
  - Strictly scoped to specific profiles or use cases
  - Never enabled implicitly

- **Profile composition and reuse**
  - Shared profile components
  - Explicit composition or inheritance semantics
  - Improved auditability of profile changes

---

## Long-Term Direction

**Focus:** Dataset preparation across multiple levels of granularity

Longer-term exploration may focus on clearer separation of
responsibilities across different levels of text curation:

- **Paragraph-level curation**
  - Structure detection
  - Boilerplate scoring
  - Local deduplication

- **Sample-level curation**
  - Document consistency checks
  - Aggregate signal thresholds
  - Conservative sample filtering

- **Document-level curation**
  - Repetition and template detection
  - Metadata-aware filtering hooks
  - Profile-specific cleanup strategies

These directions are intended to support different dataset needs, such as:

- large-scale pretraining corpora
- domain-adapted fine-tuning datasets
- evaluation and benchmark preparation

---

## Explicitly Out of Scope

The following are **intentionally not planned**:

- ML-based quality scoring or ranking
- Automatic semantic classification
- Language-specific default rules
- Aggressive or opaque content pruning
- Model-dependent preprocessing logic

Such behavior is better handled by downstream systems
or explicitly opt-in tooling.

---

## Stability Commitment

Future changes are expected to be introduced in a way that:

- preserves existing profile behavior
- maintains reproducibility guarantees
- avoids silent changes to defaults

Breaking changes will require a major version bump
and explicit communication.