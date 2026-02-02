# Dataset-level Filtering

Dataset-level filtering removes entire samples (rows) from a dataset
based on an explicit, user-defined predicate.

This operation is intended for **auditable, reproducible dataset
curation**, where the reason for removing samples must be recorded
and inspectable.

Filtering is applied at the **dataset level**, not within individual
documents.

---

## When to use dataset-level filtering

Use dataset-level filtering when:

- Entire samples should be removed
- Removal criteria depend on observable row properties
- You want an explicit record of *why* samples were dropped
- You want filtering to be reproducible and reviewable later

Examples:

- Drop samples shorter than a minimum length
- Remove empty or near-empty documents
- Exclude samples based on metadata fields
- Remove rows failing a custom quality check

---

## API

```python
from text_curation.datasets import filter_rows

filter_rows

filter_rows(
    dataset,
    *,
    predicate,
    description: str,
    collect_reports: bool = True
)

Parameters

dataset (datasets.Dataset)
The Hugging Face Dataset to filter.

predicate (Callable[[dict], bool])
A function that receives a dataset row and returns:

True → keep the row

False → remove the row


description (str)
A required, human-readable description explaining why rows are removed. This description is recorded in the filtering report.

collect_reports (bool, default: True)
Whether to return a dataset-level filtering report.


Returns

If collect_reports=False
→ Dataset

If collect_reports=True
→ (Dataset, filter_report: dict)



---

Example: minimum word count filter

Drop samples with fewer than 20 words:

from text_curation.datasets import filter_rows

dataset, report = filter_rows(
    dataset,
    predicate=lambda r: len(r["text"].split()) >= 20,
    description="drop samples with fewer than 20 words",
)

This removes entire rows that do not meet the criterion.


---

Filtering report

When collect_reports=True, filter_rows returns a filtering report describing the dataset-level effect of the operation.

Example report:

{
  "operation": "filter_rows",
  "scope": "dataset",
  "description": "drop samples with fewer than 20 words",
  "input": {
    "samples": 1000000
  },
  "output": {
    "samples": 820000
  },
  "removed": {
    "samples": 180000,
    "fraction": 0.18
  },
  "determinism": {
    "predicate_pure": true
  },
  "provenance": {
    "library": "text-curation",
    "operation_version": "filter_rows_v1"
  }
}

Report semantics

input.samples
Number of samples before filtering

output.samples
Number of samples after filtering

removed.samples
Total number of samples removed

removed.fraction
Fraction of samples removed (relative to input)


The report is deterministic and can be stored, serialized, or chained with other dataset-level reports.


---

Determinism and guarantees

filter_rows guarantees:

Deterministic behavior for pure predicates

Dataset order preservation

No mutation of sample contents

No implicit normalization or heuristics


All filtering behavior is driven entirely by the provided predicate.


---

Non-goals

Dataset-level filtering explicitly does not include:

Built-in thresholds (e.g. min_words)

Semantic or ML-based filtering

Language detection

Fuzzy matching

Automatic normalization


These behaviors must be expressed explicitly in the predicate or implemented as separate, versioned primitives.


---

Relationship to blocks and profiles

Blocks operate within documents and may mutate text

Profiles orchestrate blocks at the sample level

Dataset-level filtering removes entire samples


Filtering is intentionally not part of profiles, to avoid silent dataset shrinkage and preserve clear provenance.


---

Stability

filter_rows is an experimental dataset-level primitive.

Its API and report schema may evolve until explicitly marked stable.
