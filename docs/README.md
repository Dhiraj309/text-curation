# text-curation Documentation

This directory contains **design- and behavior-level documentation**
for the `text-curation` library.

These documents describe:

- The design philosophy and architectural invariants of the system
- The responsibilities, guarantees, and non-goals of each block
- The behavioral contracts of built-in profiles
- Planned future work and explicitly deferred features

The documentation here is intentionally **specification-oriented**,
not tutorial-oriented.

---

## How to Use These Docs

- **Block docs (`docs/blocks/`)**  
  Define *what each block guarantees* and *what must never change*
  without a breaking release.

- **Profile docs (`docs/profiles/`)**  
  Define end-to-end pipeline behavior and stability guarantees
  for specific use cases.

- **Design docs (`design.md`, `roadmap.md`)**  
  Capture architectural intent and future direction.

Together, these documents act as **human-readable contracts**
that complement the test suite.

---

## Relationship to Tests

Behavior described in these documents is enforced by:

- Block-level unit tests
- Profile-level golden tests

If documentation and tests ever disagree,
**tests are authoritative**.

---

## Relationship to the Main README

For installation instructions, examples, and high-level usage,
see the main project README:

👉 [../README.md](../README.md)

---

## Contributing to Docs

Documentation updates are encouraged when:

- Block semantics change
- A profile is added or versioned
- Stability guarantees are clarified
- New non-goals are introduced

Documentation should describe **behavioral contracts**, not
implementation details.