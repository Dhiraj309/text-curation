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
