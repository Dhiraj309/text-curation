# Design Invariants

`text-curation` is a **deterministic, structure-aware text curation system**
designed for large-scale dataset preprocessing.

This document defines the **non-negotiable invariants** that govern
the behavior, evolution, and contribution rules of the system.

These invariants are treated as architectural law.
Violations are considered bugs or breaking changes.

---

## 1. Determinism Is Mandatory

All behavior in `text-curation` **must be deterministic**.

Given:
- the same input text
- the same profile identifier

The output **must be identical** across:
- runs
- machines
- environments

The system **must not** introduce:

- randomness
- probabilistic thresholds
- data-dependent drift
- time-dependent behavior

Determinism is a **hard requirement**, not an optimization.

---

## 2. No Machine Learning in the Core

The core system **must not** depend on machine learning.

This includes (but is not limited to):

- classifiers
- learned heuristics
- embedding-based similarity
- probabilistic scoring
- model-dependent behavior

All decisions must be:

- rule-based
- explicit
- inspectable
- reproducible

ML-based analysis may exist **outside** the core,
but must never affect default or profile-defined behavior.

---

## 3. Profiles Are Behavioral Contracts

A profile defines a **complete behavioral contract**.

A profile specifies:

- the exact blocks applied
- the exact order of execution
- the default policies of each block
- the guarantees exposed to users

Once released, a profile’s behavior **must not change**.

If a profile is named `web_common_v1`:

- its behavior is frozen
- its output is stable across all `1.x` releases
- any change requires a new profile version

Profiles may be deprecated.
Profiles may never be silently modified.

Golden tests enforce this contract.

---

## 4. Blocks Are Semantic Primitives

Each block represents a **single, well-defined responsibility**.

Blocks must:

- be stateless
- operate deterministically
- avoid semantic inference
- avoid hidden coupling with other blocks

Blocks may:
- mutate text
- emit signals
- do both

Blocks must **not**:

- depend on execution context
- inspect downstream behavior
- implicitly coordinate with other blocks

If new behavior is required, it must be introduced as:
- a new block
- or a new profile

---

## 5. Conservative Defaults Are Required

The system prioritizes:

- semantic preservation over cleanliness
- false negatives over false positives
- stability over aggressiveness

Text that appears “messy” after processing is often left that way
**intentionally**.

Aggressive cleanup is always opt-in and profile-scoped.

This is required to prevent:
- silent meaning changes
- irreproducible datasets
- downstream data drift

---

## 6. Observation Is Separate From Decision

Structural analysis and content modification are **strictly separated**.

Blocks that observe structure must:
- emit signals
- never mutate text

Blocks that mutate text must:
- act only on explicit rules
- avoid implicit interpretation of signals

This separation ensures:
- auditability
- explainability
- composability

Hidden logic is forbidden.

---

## 7. Explicit Non-Goals

By design, `text-curation` does **not** attempt to:

- infer document quality or usefulness
- classify text semantically or topically
- perform language detection or language-specific rules
- aggressively remove repetition or boilerplate by default
- preserve exact visual layout of source documents
- integrate with tokenizers or models

These constraints are intentional and permanent.

---

## 8. Extension Rules

New functionality must follow these rules:

- New behavior must be opt-in
- Default behavior must not change
- Profiles evolve; existing contracts do not
- Breaking changes require a major version bump
- Tests define and lock behavior

If a change cannot be expressed as:
- a new block
- a new profile
- or an explicitly versioned contract

It does not belong in the core system.

---

## 9. Authority Order

When sources disagree, authority is resolved as follows:

1. **Tests** (final authority)
2. **Profile documentation**
3. **Block documentation**
4. **Design invariants (this document)**

Implementation details are not authoritative.

---

## Summary

`text-curation` is intentionally boring.

Predictability, reproducibility, and auditability
are valued over flexibility or cleverness.

The system exists to make dataset preprocessing:

- explicit
- inspectable
- stable over time

Anything that compromises these goals
is out of scope.
