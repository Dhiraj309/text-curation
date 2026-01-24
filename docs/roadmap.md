# Roadmap

This document outlines **planned and potential areas of future work**
for `text-curation`.

The guiding direction of the project is to explore **well-defined,
profile-based text curation pipelines** suitable for different stages
of large-scale dataset preparation, including:

- raw web-scraped text
- pretraining corpora
- fine-tuning and evaluation datasets

All future work is expected to preserve the library’s **deterministic,
conservative, and reproducible** design principles.

---

## Near-Term (1.x)

**Focus:** Strengthening general-purpose web text curation

Work in the `1.x` series is intended to improve signal quality,
profile coverage, and documentation **without changing default behavior**.

Potential areas include:

- **Enhanced deduplication (opt-in)**
  - Paragraph-level and sliding-window deduplication
  - Conservative, exact or near-exact matching
  - No fuzzy or semantic deduplication by default

- **Boilerplate scoring (non-destructive)**
  - Continuous boilerplate likelihood signals
  - Paragraph- and document-level aggregation
  - Filtering decisions remain explicit and opt-in

- **Expanded built-in profiles**
  - Additional web-derived profiles (e.g. wiki- or forum-style text)
  - Clearly defined profile contracts and scope

- **Improved documentation**
  - Block-level behavior references
  - Profile contracts with before/after examples
  - Dataset-oriented usage guidance

---

## Medium-Term (2.x candidates)

**Focus:** Richer structure awareness and extensibility

The following areas may be explored in future major releases.
All such behavior is expected to remain **opt-in or profile-specific**.

- **HTML-aware preprocessing**
  - Tag-aware text extraction
  - Boilerplate-aware DOM traversal
  - Explicit separation from semantic filtering

- **Advanced deduplication strategies**
  - Optional fuzzy or similarity-based deduplication
  - Clearly scoped to specific profiles or use cases
  - Never enabled implicitly

- **Profile composition and reuse**
  - Shared profile components
  - Clear composition or inheritance semantics
  - Improved auditability of profile changes

---

## Long-Term Direction

**Focus:** Dataset preparation across multiple granularity levels

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

- Preserves existing profile behavior
- Maintains reproducibility guarantees
- Avoids silent changes to defaults

Breaking changes will require a major version bump
and explicit communication.
