# Design Philosophy

`text-curation` is designed as a **deterministic text curation system**
for large-scale dataset preprocessing.

This document explains the core design decisions and constraints
that shape the library’s behavior.

---

## Determinism First

All transformations in `text-curation` are **rule-based and deterministic**.

Given the same input text and the same profile:
- Output is guaranteed to be identical across runs
- No randomness or probabilistic behavior is introduced

This is essential for dataset reproducibility and auditability.

---

## Why No Machine Learning

Machine learning introduces:
- Non-deterministic behavior
- Opaque failure modes
- Dataset-dependent drift

For dataset curation, these properties are unacceptable.

`text-curation` therefore avoids:
- classifiers
- learned heuristics
- scoring models

Semantic decisions must remain **explicit and inspectable**.

---

## Profiles as Behavioral Contracts

A profile defines:
- which blocks are applied
- in what order
- with what default behavior

Profiles are **versioned** and treated as **contracts**, not suggestions.

If a profile is named `web_common_v1`, its behavior is guaranteed
not to change within the `1.x` series.

---

## Conservative Defaults

The library prioritizes:
- semantic preservation over cleanliness
- false negatives over false positives
- stability over aggressiveness

Text that looks “messy” after processing is often left that way
intentionally.

---

## Explicit Non-Goals

By design, `text-curation` does not attempt to:

- Infer document quality or intent
- Aggressively remove all boilerplate
- Preserve exact visual formatting
- Perform language-specific transformations
- Apply semantic filtering

These constraints are essential to maintaining predictable behavior.
Understood 👍
Below is a **clean, minimal improvement** of your **Design Philosophy** document:

* **No new concepts added**
* **No scope expansion**
* Only **clarity, consistency, and tightening of language**
* Aligned implicitly with **v1.1.x**, without adding version noise

You can **copy–paste this directly** as `docs/design.md`.

---

```md
# Design Philosophy

`text-curation` is designed as a **deterministic text curation system**
for large-scale dataset preprocessing.

This document describes the core design decisions and constraints
that intentionally shape the library’s behavior.

---

## Determinism First

All transformations in `text-curation` are **rule-based and deterministic**.

Given the same input text and the same profile:

- Output is guaranteed to be identical across runs
- No randomness or probabilistic behavior is introduced

This property is essential for:
- dataset reproducibility
- long-running preprocessing pipelines
- auditing and debugging data decisions

---

## Why No Machine Learning

Machine learning introduces:

- Non-deterministic behavior
- Opaque or hard-to-debug failure modes
- Dataset-dependent drift over time

For dataset curation, these properties are unacceptable.

Accordingly, `text-curation` deliberately avoids:

- classifiers
- learned heuristics
- scoring or ranking models

All semantic decisions must remain **explicit, inspectable, and stable**.

---

## Profiles as Behavioral Contracts

A profile defines:

- which blocks are applied
- in what order
- with which default policies

Profiles are **versioned** and treated as **behavioral contracts**, not suggestions.

If a profile is named `web_common:v1`, its behavior is guaranteed
not to change within the `1.x` series.

Any behavior change requires:
- a new profile version, or
- a major library version bump

---

## Conservative Defaults

The library consistently prioritizes:

- semantic preservation over cleanliness
- false negatives over false positives
- stability over aggressiveness

Text that appears “messy” after processing is often left that way
intentionally.

This conservatism ensures that:
- meaning is not silently altered
- downstream consumers retain control
- preprocessing decisions remain reversible and auditable

---

## Explicit Non-Goals

By design, `text-curation` does **not** attempt to:

- infer document quality or author intent
- aggressively remove all boilerplate or repetition
- preserve exact visual formatting
- perform language-specific transformations
- apply semantic or topical filtering

These constraints are essential to maintaining predictable,
reproducible behavior at dataset scale.