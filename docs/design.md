# Design Invariants

`text-curation` is a **deterministic, structure-aware corpus compiler**
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
(e.g. determinism, canonical identity, explicit block order, schema completeness).

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
- the same execution topology

The output **must be identical** across:
- runs
- machines
- environments
- CPU counts

The system **must not** introduce:

- randomness
- probabilistic thresholds
- data-dependent drift
- time-dependent behavior
- hidden global state
- topology-dependent behavior

Determinism is a **hard requirement**, not an optimization.

---

## 2. Explicit Ordering Is Required

All execution order must be **explicit and declared**.

This applies to:

- block execution within a pipeline
- profile-defined block sequences
- profile discovery and registration
- dataset-level canonicalization steps

Implicit ordering based on:

- filesystem layout
- import order side effects
- dictionary iteration
- hash ordering
- multiprocessing chunk boundaries

is **forbidden**.

Canonical ordering must be explicitly defined and enforced.

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

## 5. Documents Have Canonical Identity

Every processed document must have a **canonical, immutable identity**.

Rules:

- `document_id` is derived deterministically (e.g., SHA-256)
- `document_id` is immutable once set
- Identity must not depend on execution order
- Identity must not depend on sharding topology
- Identity must not depend on CPU count

Document identity is the foundation of:

- dataset deduplication
- shard invariance
- canonical dataset hashing

Without canonical identity, reproducibility is impossible.

---

## 6. Dataset Identity Must Be Canonical

A dataset has a canonical identity defined by:

- sorted `document_id` values
- the canonical `pipeline_hash`

Rules:

- Dataset identity must be independent of input order
- Dataset identity must be independent of shard count
- Dataset identity must be independent of multiprocessing
- Dataset identity must be reproducible across machines

If:
- 1 shard
- 32 shards
- 128 shards

produce different dataset hashes, the system is incorrect.

Dataset identity must be topology-invariant.

---

## 7. Pipelines Must Be Isolated

Pipeline execution must be isolated:

- Blocks are not shared across pipelines
- Block state must not leak across runs
- Multiple runs of the same pipeline must not accumulate state

Pipeline behavior must depend **only** on:
- input text
- profile configuration

Parallel execution must not alter semantic behavior.

---

## 8. Explicit Parallel Execution Model

`CorpusPipeline` may parallelize **document-level transforms only**.

Rules:

- Parallelism must be explicit (`num_proc`)
- No automatic CPU detection
- No implicit sharding
- No topology-dependent logic

Canonical stages must remain single-threaded:

- global deduplication
- document_id sorting
- dataset_hash computation
- manifest generation

Parallelism is an optimization layer.
Canonical identity is a correctness layer.

They must remain separate.

---

## 9. Documents Are the Only Mutable State

The `Document` object is the **only mutable state** passed through blocks.

Rules:

- Text mutation must be explicit
- Signals are append-only
- Signals are never reinterpreted or deleted
- `document_id` is immutable once set
- No block may mutate another block’s state

This ensures inspectability and auditability.

---

## 10. Reporting Is Descriptive, Not Causal

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

## 11. Schemas Must Be Total and Stable

Public schemas (profiles, reports, dataset utilities, manifests) must be:

- structurally complete
- explicit about optionality
- stable within a major version

Optional data is represented as **empty structures**, not missing fields.

Schema drift without versioning is forbidden.

---

## 12. No Implicit Dataset Shrinkage

`text-curation` must never silently remove dataset samples.

Rules:

- Blocks operate within documents
- Profiles operate per-sample
- Dataset utilities remove samples **only explicitly**
- Deduplication must be declared
- Filtering must be declared

Any operation that removes samples must be:
- opt-in
- explicit
- auditable
- reportable

---

## 13. Strict Manifest Enforcement

In strict mode:

- `profile_id` must be present
- `pipeline_hash` must be present
- `dataset_hash` must be present
- `document_count` must be present

Compilation without reproducibility metadata is considered invalid.

Training without a manifest is considered non-reproducible.

---

## Summary

These invariants ensure that `text-curation` remains:

- deterministic
- topology-invariant
- shard-invariant
- multiprocessing-safe
- auditable
- extensible
- trustworthy
- boring in the best possible way

`text-curation` is not a cleaning script.

It is a corpus compiler.

Any change that violates these invariants
**must not be merged without explicit versioning and documentation**.
