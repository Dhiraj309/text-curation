## Dataset-level Deduplication

Dataset-level deduplication operates on the dataset **exactly as provided**
at the time the operation is invoked.

This utility performs **exact, representation-level deduplication**
and produces an **auditable report** describing what was removed.

---

## Semantics and Scope

Deduplication:

- Operates on the dataset **as-is**
- Uses the exact column representation supplied
- Is **not aware of profiles or blocks**
- Is **not reapplied automatically**

The deduplication report reflects the precise dataset state
at the moment the operation is executed.

If samples are later transformed (for example, via a curation profile),
the deduplication report **does not change** and does not attempt
to reflect post-transformation content.

---

## Guarantees

When dataset-level deduplication is applied:

- Behavior is deterministic
- Order of retained samples is stable
- Only exact duplicates are removed
- No normalization or semantic matching is performed
- The report accurately reflects the operation performed

---

## Explicit Non-Behavior

Dataset-level deduplication does **not**:

- Perform semantic or fuzzy matching
- Deduplicate across transformed representations
- Re-run automatically after later processing
- Enforce uniqueness guarantees on downstream operations
- Integrate implicitly with profiles or blocks

---

## Relationship to Profiles and Blocks

Dataset-level deduplication is intentionally **decoupled**
from document-level curation.

- Profiles operate on individual samples
- Blocks operate within documents
- Dataset utilities operate across rows

This separation prevents silent behavior coupling
and preserves clear provenance.

---

## Stability

Dataset-level deduplication is currently **experimental**.

Its API and report schema may evolve until explicitly
marked stable in a future release.