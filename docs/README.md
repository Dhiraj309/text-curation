# text-curation Documentation

This directory contains **specification-level documentation**
for the `text-curation` library.

These documents define **behavioral contracts**, **design invariants**,
and **stability guarantees** for the system.

They are intentionally **not tutorials**.

---

## Purpose of This Documentation

The documentation in this directory exists to:

- Define what the system **guarantees**
- Define what the system **will not do**
- Make preprocessing behavior **auditable and reproducible**
- Prevent silent semantic or structural drift over time

If something is documented here, it is treated as part of the
library’s **public contract**.

---

## Documentation Structure

### Block Documentation (`docs/blocks/`)

Block documentation defines:

- What each block does
- What each block guarantees
- What must **never change** without a breaking release

Block docs describe **local, isolated behavior** only.
They do not define end-to-end pipelines.

---

### Profile Documentation (`docs/profiles/`)

Profile documentation defines:

- End-to-end pipeline behavior
- Ordering and interaction of blocks
- User-facing guarantees and limitations
- Intended and non-intended use cases

Profiles are treated as **versioned artifacts**.
Once released, their documented behavior must not change.

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

Reporting utilities are descriptive and **never affect curation behavior**.

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

All documented behavior is enforced by:

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
- A stability guarantee changes
- A non-goal is clarified or added

Documentation should describe **behavioral contracts**,
not implementation details or future intentions.

---

## Summary

This documentation exists to make text curation:

- explicit
- inspectable
- reproducible
- stable over time

If a behavior is not documented or tested,
it must be treated as undefined.
