# Design Invariants

`text-curation` is a **deterministic, structure-aware text curation system**
designed for large-scale dataset preprocessing.

This document defines the **non-negotiable invariants** that govern
the behavior, evolution, and contribution rules of the system.

These invariants are treated as architectural law.
Violations are considered bugs or breaking changes.

---

## Guarantees vs Behavioral Descriptions

text-curation distinguishes between **hard guarantees** and
**behavioral descriptions**.

**Guarantees** are mechanically enforced by the execution model
(e.g. determinism, explicit block order, absence of hidden state).

**Behavioral descriptions** document intended effects of profiles
and blocks, but may vary depending on input data.

Only guarantees are relied upon for reproducibility claims.

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
