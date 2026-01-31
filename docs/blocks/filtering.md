# SignalBasedBoilerplateFilteringBlock

The `SignalBasedBoilerplateFilteringBlock` removes paragraphs
**only when explicitly justified by structure-derived signals**.

Filtering is **deterministic, conservative, and rule-based**.

This block is part of the **stable core**.

This block is a **low-level deterministic primitive** intended for
profile authors and library extension.
Most users should rely on profiles rather than composing blocks directly.

---

## Scope

Filtering is applied:

- **At paragraph granularity**
- **Within a single document**
- **Based exclusively on emitted structural signals**

This block does not inspect document-level context
or external information.

---

## Behavior

For each paragraph, the block evaluates a fixed set of conditions.
A paragraph is removed **if and only if** all required conditions
are satisfied.

No probabilistic scoring or ranking is performed.

---

## Removal Conditions (Stable)

A paragraph is removed if:

1. The paragraph is empty  
   **OR**

2. All of the following are true:
   - Marked as a boilerplate candidate
   - Repetition count meets or exceeds the threshold
   - Paragraph length is below the maximum threshold
   - Paragraph is not explicitly marked as a header

All conditions must be satisfied exactly.

---

## Signal Dependencies

This block consumes signals emitted by upstream structure analysis,
including:

- `paragraph[*].is_boilerplate_candidate`
- `paragraph[*].repetition_count`
- `paragraph[*].starts_with_header` (if present)

Signals are treated as **inputs**, not interpretations.

---

## Guarantees

When this block is applied:

- Filtering decisions are deterministic
- Only explicitly signaled paragraphs are removed
- Paragraph order is preserved
- No paragraph content is rewritten
- No semantic inference is performed

---

## Explicit Non-Behavior

This block does **not**:

- Perform semantic quality filtering
- Rank or score paragraphs
- Remove list blocks by default
- Remove entire documents
- Apply document-level thresholds

---

## Stability

- Behavior is stable as of `v1.x`
- Changes require:
  - a new block, or
  - a new profile version, or
  - a major version bump
