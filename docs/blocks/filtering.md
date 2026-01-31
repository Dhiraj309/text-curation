# SignalBasedBoilerplateFilteringBlock

The `SignalBasedBoilerplateFilteringBlock` removes paragraphs
**only when explicitly justified by structure-derived signals**.

Filtering is **deterministic, conservative, and rule-based**.

This block is part of the **stable core**.

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

The block performs no probabilistic scoring and no ranking.

---

## Removal Conditions (Stable)

A paragraph is removed if:

1. The paragraph is empty  
   **OR**

2. All of the following are true:
   - The paragraph is marked as a boilerplate candidate
   - The paragraph repetition count meets or exceeds the threshold
   - The paragraph length is below the maximum length threshold
   - The paragraph is not explicitly marked as a header

All conditions must be satisfied exactly.
No partial or heuristic removal is performed.

---

## Signal Dependencies

This block consumes signals emitted by upstream structure analysis,
including (but not limited to):

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
- Remove paragraphs based on language or topic
- Rank or score paragraphs
- Remove list blocks by default
- Remove entire documents
- Apply document-level thresholds

---

## Stability

- Behavior is stable as of `v1.x`
- Changes to removal rules require:
  - a new block, or
  - a new profile version, or
  - a major version bump

---

## Notes on Use

This block is intentionally conservative.

More aggressive filtering strategies must be implemented as:

- a separate block
- a profile-specific pipeline
- or an explicit opt-in mechanism

Filtering decisions must always remain
explainable and auditable.
