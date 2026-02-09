# Roadmap

⚠️ **Non-binding roadmap**

This document describes **areas of exploration** and **possible future
directions** for `text-curation`.

It is **not a commitment** to implement specific features, behaviors,
or timelines.

Inclusion here does **not** guarantee implementation.

---

## Purpose of This Roadmap

This roadmap exists to:

- Communicate design *intent* without promising behavior
- Clarify what kinds of extensions are considered compatible
- Prevent speculation about undocumented future guarantees
- Make explicit what is intentionally **out of scope**

Nothing in this document overrides:
- tests
- profile contracts
- block documentation
- design invariants

---

## Guiding Direction

The long-term direction of `text-curation` is to support
**well-defined, profile-based text curation pipelines**
for different stages of dataset preparation, including:

- raw web-scraped text
- large-scale pretraining corpora
- fine-tuning and evaluation datasets

All future work must preserve the library’s core principles:

- determinism
- conservative defaults
- explicit behavior
- long-term reproducibility
- auditable preprocessing

---

## Near-Term Exploration (1.x Series)

**Focus:** Strengthening conservative, general-purpose text curation

Work in the `1.x` series is intentionally constrained.

The following rules apply:

- Default behavior of existing blocks **must not change**
- Existing profiles **must not change**
- All new behavior must be **explicitly opt-in**
- Stability takes priority over feature velocity

Exploratory areas *may* include:

### Enhanced Deduplication (Opt-In Only)

- Paragraph-level or windowed deduplication
- Exact or near-exact matching
- Never enabled by default
- Always profile-scoped and versioned

### Non-Destructive Boilerplate Signals

- Continuous or aggregate boilerplate indicators
- Paragraph- and document-level signals
- Signals only — no implicit filtering or removal

### Expanded Built-in Profiles

- Additional web-derived profiles (e.g. wiki-style, forum-style)
- Clearly scoped guarantees and limitations
- Explicit versioning and golden tests

### Documentation Hardening

- Additional block-level behavioral specifications
- Profile contracts with before/after examples
- Dataset-oriented usage guidance

These areas represent **exploration**, not commitments.

---

## Possible 2.x Directions (Major Releases Only)

**Focus:** Richer structure awareness and extensibility

The following areas may be explored only in **major** releases.
All such behavior must remain **explicit, opt-in, and profile-scoped**.

### HTML-Aware Preprocessing

- Tag-aware text extraction
- Boilerplate-aware DOM traversal
- Explicit separation from semantic filtering

### Advanced Deduplication Strategies

- Optional fuzzy or similarity-based deduplication
- Strictly limited to specific profiles
- Never enabled implicitly

### Profile Composition and Reuse

- Shared profile components
- Explicit composition semantics
- Full auditability of derived profiles

Inclusion here does not imply prioritization or implementation.

---

## Exploratory Directions (Longer Term)

**Focus:** Clear separation of curation responsibilities by granularity

Longer-term exploration may focus on clearer boundaries between:

### Paragraph-Level Curation

- Structure detection
- Boilerplate signaling
- Local, document-scoped deduplication

### Sample-Level Curation

- Document consistency checks
- Aggregate signal thresholds
- Explicit, opt-in sample filtering

### Corpus-Level Curation

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