# Dataset-level Filtering

Dataset-level filtering removes **entire samples (rows)**
from a dataset based on an explicit, user-defined predicate.

This utility is designed for **auditable, reproducible dataset curation**,
where both behavior and rationale must remain inspectable over time.

Filtering is applied strictly at the **dataset level**.
No document-level processing is performed.

---

## When to Use Dataset-level Filtering

Use dataset-level filtering when:

- Entire samples should be removed
- Removal criteria depend on observable row properties
- You require an explicit record of *why* samples were dropped
- Filtering must be reproducible and reviewable later

Common use cases include:

- Dropping empty or near-empty samples
- Enforcing minimum length requirements
- Filtering by metadata fields
- Removing rows failing a custom validation rule

---

## API

```python
from text_curation.datasets import filter_rows

filter_rows(
    dataset,
    *,
    predicate,
    description: str,
    collect_reports: bool = True,
)
```





#docs/profiles/llm_pretrain_v1.md
# llm_pretrain_v1

`llm_pretrain_v1` defines a **minimal, deterministic, non-destructive**
text curation profile intended for **large-scale LLM pretraining**.

This profile is a **locked behavioral contract**.

---

## Pipeline Definition

1. `RedactionBlock`
2. `NormalizationBlock`
3. `CodeSafeFormattingBlock`

Block order is fixed and enforced.

---

## Hard Guarantees (Enforced)

When this profile is applied:

- Execution is deterministic
- Block order is fixed and explicit
- The profile ID fully specifies behavior
- No hidden global or cross-document state is used
- All transformations are document-local

---

## Intended Behavior (Not Guaranteed)

Depending on input content:

- Explicitly recognized secrets may be redacted
- Unicode and encoding artifacts may be normalized
- Whitespace may be conservatively normalized
- Structural layout is generally preserved

These outcomes are descriptive and not enforced guarantees.

---

## Explicit Non-Behavior

This profile does **not**:

- Perform deduplication
- Perform filtering or content removal
- Emit or consume structural signals
- Perform semantic inference or classification
- Apply dataset-level operations

---

## Stability

The behavior of `llm_pretrain_v1` is stable across all `1.x` releases.

Any behavioral change requires a new profile version or a major release.