# Design Invariants

`text-curation` is a **deterministic, structure-aware text curation system**
designed for large-scale dataset preprocessing.

This document defines the **non-negotiable invariants** that govern
the behavior, evolution, and contribution rules of the system.

These invariants are treated as **architectural law**.
Violations are considered **bugs or breaking changes**.

---

## Guarantees vs Behavioral Descriptions

`text-curation` distinguishes strictly between **hard guarantees** and
**behavioral descriptions**.

**Guarantees** are mechanically enforced by the execution model and tests
(e.g. determinism, explicit block order, schema completeness).

**Behavioral descriptions** document intended effects of profiles
and blocks, but may vary depending on input data.

Only **guarantees** may be relied upon for reproducibility,
auditing, or scientific claims.

---

## 1. Determinism Is Mandatory

All behavior in `text-curation` **must be deterministic**.

Given:
- the same input text
- the same profile identifier
- the same library version

The output **must be identical** across:
- runs
- machines
- environments

The system **must not** introduce:

- randomness
- probabilistic thresholds
- data-dependent drift
- time-dependent behavior
- hidden global state

Determinism is a **hard requirement**, not an optimization.

---

## 2. Explicit Ordering Is Required

All execution order must be **explicit and declared**.

This applies to:

- block execution within a pipeline
- profile-defined block sequences
- profile discovery and registration

Implicit ordering based on:

- filesystem layout
- import order side effects
- dictionary iteration
- hash ordering

is **forbidden**.

---

## 3. Profiles Are Immutable Contracts

Profiles define **behavioral contracts**.

Once a profile version is released:

- its block sequence must not change
- its guarantees must not change
- its intended non-behavior must not change

Profile identity (`name + version`) is:

- globally unique
- immutable
- non-overridable

Breaking a released profile requires:
- a new profile version, or
- a major library version bump

---

## 4. Blocks Are Local, Deterministic Primitives

Blocks are **local transformation primitives**.

They must:

- operate only on the provided `Document`
- be deterministic
- avoid global or shared state
- make all mutations explicit

Blocks must **not**:

- inspect external context
- depend on dataset-level information
- perform implicit filtering
- introduce semantic inference

---

## 5. Pipelines Must Be Isolated

Pipeline execution must be isolated:

- Blocks are not shared across pipelines
- Block state must not leak across runs
- Multiple runs of the same pipeline must not accumulate state

Pipeline behavior must depend **only** on:
- input text
- profile configuration

---

## 6. Documents Are the Only Mutable State

The `Document` object is the **only mutable state** passed through blocks.

Rules:

- Text mutation must be explicit
- Signals are append-only
- Signals are never reinterpreted or deleted
- No block may mutate another block’s state

This ensures inspectability and auditability.

---

## 7. Reporting Is Descriptive, Not Causal

Reports are **observational artifacts**.

They:

- describe what happened
- never affect execution
- never influence block behavior
- never trigger filtering or mutation

Reporting must be:

- deterministic
- structurally total (no missing keys)
- safe for aggregation and serialization

---

## 8. Schemas Must Be Total and Stable

Public schemas (profiles, reports, dataset utilities) must be:

- structurally complete
- explicit about optionality
- stable within a major version

Optional data is represented as **empty structures**, not missing fields.

Schema drift without versioning is forbidden.

---

## 9. No Implicit Dataset Shrinkage

`text-curation` must never silently remove dataset samples.

Rules:

- Blocks operate within documents
- Profiles operate per-sample
- Dataset utilities remove samples **only explicitly**

Any operation that removes samples must be:
- opt-in
- explicit
- auditable
- reportable

---

## 10. Safety Over Convenience

When design tradeoffs exist, the system always prefers:

- safety over convenience
- explicitness over magic
- reproducibility over heuristics
- boring behavior over clever behavior

This is intentional.

---

## Summary

These invariants exist to ensure that `text-curation` remains:

- deterministic
- auditable
- extensible
- trustworthy
- boring in the best possible way

Any change that violates these invariants
**must not be merged without explicit versioning and documentation**.