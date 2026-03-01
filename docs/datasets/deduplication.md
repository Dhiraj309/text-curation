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

## Deterministic Two-Phase Deduplication (Shard-Invariant)

For large-scale corpus compilation (millions to hundreds of millions of samples),
deduplication must remain invariant to shard count and execution order.

The canonical protocol consists of two explicit phases.

### Phase A — Shard-Local Dedup

Each shard independently:

1. Runs text curation (including `FingerprintBlock`)
2. Produces canonical `document_id`
3. Applies identity-based deduplication (`deduplicate_by_document_id`)

Within a shard:

- Rows are grouped by identical `document_id`
- Representative selection is canonical
- No randomness is permitted
- No reliance on dataset order is allowed

Shard-local dedup reduces memory pressure while preserving determinism.

---

### Phase B — Global Canonical Merge

After shard-local processing:

1. Collect all rows from all shards
2. Sort globally by `document_id`
3. Drop duplicate `document_id`s
4. Compute canonical dataset identity using:
   - Sorted `document_id`s
   - Deterministic `pipeline_hash`

This guarantees:

- Shard-count invariance (1 shard == 200 shards)
- Order independence
- Stable dataset identity
- Reproducible corpus compilation

---

### Canonical Representative Rule

Whenever duplicates exist:

The canonical representative is the row whose  
`document_id` is lexicographically smallest.

Index order must never determine retention.  
Iteration order must never determine retention.  
Set ordering must never determine retention.  

Only canonical identity is permitted.

---

### Determinism Requirements

To preserve dataset identity stability:

- Do not use Python's built-in `hash()`
- Do not introduce randomness
- Do not rely on iteration order
- Do not perform unordered multiprocessing merges
- Do not change representative selection without versioning

This protocol is considered part of the corpus compiler contract.

---

## Stability  

Dataset-level deduplication is currently **experimental**.  

Its API and report schema may evolve until explicitly  
marked stable in a future release.
