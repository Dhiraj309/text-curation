# BasicStructureBlock

The `BasicStructureBlock` emits **inspectable structural signals**
describing observable properties of the text, without mutating it.

This block is part of the **stable core**.

This block is a **low-level deterministic primitive** intended for
profile authors and library extension.
Most users should rely on profiles rather than composing blocks directly.

---

## Scope

This block performs **structure detection only**.

It observes and records properties such as line form, repetition,
and paragraph shape, but does not interpret their meaning or quality.

All emitted signals are **descriptive**, not evaluative.

---

## Behavior

The block emits deterministic, rule-based signals including:

- Line-level structural signals (e.g. headers, bullets)
- Paragraph-level repetition indicators
- Paragraph grouping signals (e.g. list blocks)

Signal emission is driven solely by local text structure.

---

## Guarantees

When this block is applied:

- Document text is never modified
- Signal emission is deterministic
- Signal names and meanings are stable
- Signals reflect observable structure only
- No downstream action is implied or triggered

This block never makes decisions.

---

## Explicit Non-Behavior

This block does **not**:

- Perform filtering or removal
- Perform deduplication
- Classify content quality
- Infer semantic meaning or intent
- Decide whether content is useful or boilerplate
- Apply thresholds or rankings

Signals are observations, not judgments.

---

## Stability

Signal definitions and their meanings are **stable as of `v1.x`**.

Any change to:

- emitted signal names
- signal semantics
- signal granularity

requires a **major version bump** and updated tests.