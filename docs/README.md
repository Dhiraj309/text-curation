# text-curation Documentation

This directory contains **specification-level documentation**
for the `text-curation` library.

These documents define **behavioral contracts**, **design invariants**,
and **documented behavior** for the system.

They are intentionally **not tutorials**.

---

## Purpose of This Documentation

The documentation in this directory exists to:

- Define what the system **guarantees**
- Define what the system **will not do**
- Make preprocessing behavior **auditable and reproducible**
- Prevent silent semantic or structural drift over time

**Hard guarantees are explicitly identified and mechanically enforced.**  
All other documented behavior describes **intended outcomes**, not enforceable guarantees.

If something is documented here, it is treated as part of the
library’s **public contract** within those constraints.

---

## Documentation Structure

### Block Documentation (`docs/blocks/`)

Block documentation defines:

- What each block does
- Which behaviors are **guaranteed**
- Which behaviors are **explicitly not performed**
- What must **never change** without a breaking release

Block docs describe **local, isolated behavior** only.
They do not define end-to-end pipelines.

Blocks are **low-level deterministic primitives** intended for
profile authors and library extension.
Most users should rely on **profiles**, not compose blocks directly.

---

### Profile Documentation (`docs/profiles/`)

Profile documentation defines:

- End-to-end pipeline behavior
- Ordering and interaction of blocks
- **Hard guarantees** (enforced)
- **Intended behavior** (not guaranteed)
- Explicit limitations and non-goals
- Intended and non-intended use cases

Profiles are treated as **versioned artifacts**.
Once released, their documented behavior **must not change**.

---

### Design Documentation (`design.md`)

Design documentation defines:

- System-wide invariants
- Architectural constraints
- Explicit non-goals
- Extension rules

These invariants apply to **all blocks, profiles, and utilities**.

---

### Roadmap (`roadmap.md`)

The roadmap documents:

- Areas of exploration
- Possible future directions
- Explicitly deferred or out-of-scope behavior

The roadmap is **non-binding** and does not constitute a commitment.

---

### Reports Documentation (`docs/reports/`)

Reporting documentation defines:

- Dataset-level observability utilities
- Aggregation semantics
- Stability guarantees for reporting outputs

Reporting utilities are **descriptive only** and
**never affect curation behavior**.

---

## Documentation Authority

When multiple sources appear to conflict, authority is resolved in
the following order:

1. **Tests** (final authority)
2. **Profile documentation**
3. **Block documentation**
4. **Design invariants**
5. **Roadmap**

Implementation details are not authoritative.

---

## Relationship to Tests

All **hard guarantees** are enforced by:

- Block-level unit tests
- Profile-level golden tests

Documentation describes **what must hold**.
Tests enforce **what actually holds**.

If documentation and tests ever disagree,
**tests are authoritative**.

---

## Relationship to the Main README

For installation instructions, examples, and high-level usage,
see the project README:

👉 [../README.md](../README.md)

The main README explains *how to use* the library.
This documentation explains *what the library guarantees*.

---

## Contributing to Documentation

Documentation updates are required when:

- A new block is added
- A new profile or profile version is introduced
- A hard guarantee changes
- A non-goal is clarified or added

Documentation must describe **behavioral contracts** and **intentional limits**,
not implementation details or future intentions.

---

## Summary

This documentation exists to make text curation:

- explicit
- inspectable
- reproducible
- stable over time

If a behavior is not documented **or not enforced by tests**,
it must be treated as **undefined**.
