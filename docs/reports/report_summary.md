# report.summary

The `report.summary()` utility provides a **deterministic, dataset-level overview**
of how a text curation pipeline transformed a corpus.

It aggregates **per-sample curation reports** into a single,
human-readable summary describing **structural changes** across the dataset.

---

## Overview

`report.summary()` is designed to answer questions such as:

* How much text was removed or normalized?
* How did corpus size change after curation?
* What was the net effect of a profile at scale?

The summary is **purely observational** and does **not**
affect curation behavior.

---

## Intended Use

`report.summary()` is suitable for:

* Auditing preprocessing runs
* Comparing corpus size before and after curation
* Monitoring large-scale dataset cleanup
* Debugging and validating profile behavior
* Producing reproducible preprocessing logs

It is intended to be used **after** applying a curator
with report collection enabled.

---

## Usage

### Enabling reports during curation

```python
from text_curation import TextCurator
from datasets import Dataset

curator = TextCurator.from_profile(
    "web_common_v1",
    collect_reports=True,
)

cleaned = dataset.map(curator, batched=True)
```

This adds a `curation_report` column to the dataset.

---

### Generating a summary

```python
from text_curation.reports import summary

summary(cleaned)
```

---

## Example Output

```
Curation Summary
===========================
Samples Processed: 60

┌─────────────┬────────┬────────┬────────────┬───────────┐
│ Metric      │ Input  │ Output │ Δ (Change) │ % Change  │
├─────────────┼────────┼────────┼────────────┼───────────┤
│ Chars       │  6,910 │  4,820 │   -2,090   │  -30.2%   │
│ Lines       │    460 │    200 │     -260   │  -56.5%   │
│ Paragraphs  │    120 │    100 │      -20   │  -16.7%   │
└─────────────┴────────┴────────┴────────────┴───────────┘
```

---

## What the Summary Measures

The summary aggregates **structural text statistics** only:

| Metric       | Description                             |
| ------------ | --------------------------------------- |
| `chars`      | Total number of characters              |
| `lines`      | Total number of newline-delimited lines |
| `paragraphs` | Paragraphs separated by blank lines     |

For each metric, the summary shows:

* **Input**: Total before any blocks run
* **Output**: Total after all blocks complete
* **Δ (Change)**: Net difference (`output − input`)
* **% Change**: Relative change compared to input

---

## Guarantees

When using `report.summary()`, the following guarantees hold:

* Aggregation is fully deterministic
* No additional transformations are applied
* Results are reproducible across runs
* Statistics reflect actual document state
* Output is independent of dataset ordering

These guarantees are treated as part of the
**reporting contract**.

---

## What report.summary() Does *Not* Do

By design, `report.summary()` does **not**:

* Perform semantic or quality scoring
* Rank or filter samples
* Modify dataset contents
* Infer document usefulness
* Apply heuristics beyond existing blocks

The summary is **descriptive, not prescriptive**.

---

## Relationship to Profiles

`report.summary()` is **profile-agnostic**.

It works with any profile that emits curation reports, including:

* `web_common_v1`
* Custom user-defined profiles
* Future opt-in profiles

The summary reflects the **net effect of whatever profile was used**.

---

## Known Limitations (Intentional)

The following limitations are expected:

* Only aggregate statistics are shown
* Per-sample detail is not displayed
* Semantic meaning is not evaluated
* Block-level stats are shown only if blocks emit them

For detailed inspection, individual `curation_report`
entries should be examined directly.

---

## When Not to Use

`report.summary()` may not be appropriate if you require:

* Sample-level inspection
* Semantic quality evaluation
* ML-based scoring or ranking
* Real-time streaming metrics

Such use cases should be handled by
custom analysis pipelines.

---

## Versioning & Stability

* `report.summary()` is **stable as of v1.1.0**
* Output format is considered part of the public API
* Breaking changes require a minor or major version bump

---

## Summary

`report.summary()` provides **visibility without interference**.

It makes preprocessing runs:

* Inspectable
* Auditable
* Reproducible

— while preserving the conservative, deterministic
design principles of `text-curation`.