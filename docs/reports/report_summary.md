# report.summary

`report.summary()` is a **deterministic, dataset-level auditing utility**
for text curation pipelines.

It provides a consolidated, human-readable view of how a curation
profile transformed a corpus, without affecting curation behavior.

This utility is part of the **stable reporting surface**.

---

## Purpose

`report.summary()` exists to make preprocessing **observable**.

It answers questions such as:

- How much text changed after curation?
- What structural content was removed or preserved at scale?
- Did a preprocessing run materially alter dataset structure?
- Are two curation runs behaviorally equivalent?

The summary is **descriptive only**.
It never modifies data and never influences curation decisions.

---

## Intended Use

`report.summary()` is intended for:

- Auditing preprocessing runs
- Validating profile behavior at dataset scale
- Comparing datasets before and after curation
- Detecting unintended structural drift
- Producing reproducible preprocessing logs

It complements **profile guarantees** and **golden tests**
with corpus-level visibility.

---

## Enabling Reports During Curation

To generate summaries, per-sample reports must be collected
during curation.

```python
from text_curation import TextCurator

curator = TextCurator.from_profile(
    "web_common_v1",
    collect_reports=True,
)

cleaned = dataset.map(curator, batched=True)
```

This adds a curation_report column to the dataset.

No reports are generated unless explicitly enabled.


---

Generating a Summary
```python
from text_curation.reports import summary

summary(cleaned)
```

The summary aggregates all per-sample reports into a single corpus-level view.


---

Example Output
```text

Curation Summary
===========================
Samples Processed: 60

┌─────────────┬────────┬────────┬────────────┬───────────┐
│ Metric │ Input │ Output │ Δ (Change) │ % Change │
├─────────────┼────────┼────────┼────────────┼───────────┤
│ Chars │ 6,910 │ 4,820 │ -2,090 │ -30.2% │
│ Lines │ 460 │ 200 │ -260 │ -56.5% │
│ Paragraphs │ 120 │ 100 │ -20 │ -16.7% │
└─────────────┴────────┴────────┴────────────┴───────────┘

```
---

Metrics Reported

The summary aggregates structural text statistics only.

Metric Description

chars Total number of characters
words Total number of whitespace-delimited words
lines Total number of newline-delimited lines
paragraphs Paragraphs separated by blank lines


Metrics reflect the actual post-curation document state.


---

Guarantees

When using report.summary():

Aggregation is fully deterministic

Results are independent of dataset ordering

No additional transformations are applied

All report fields are structurally present

Output format is stable and machine-inspectable


These guarantees are part of the public reporting contract.


---

Block-Level Statistics

If blocks emit per-block statistics, they are aggregated and included in the summary.

If no blocks emit statistics, block-level sections appear as empty structures.

No inference is performed at the reporting layer.


---

What report.summary() Does Not Do

By design, report.summary() does not:

Perform semantic or quality scoring

Rank, filter, or drop samples

Modify dataset contents

Infer document usefulness

Apply heuristics beyond existing block behavior


It is an observability tool, not a decision engine.


---

Relationship to Profiles

report.summary() is profile-agnostic.

It reports the net effect of whatever profile was applied, including:

web_common_v1

llm_pretrain_v1

Custom user-defined profiles


The summary does not interpret whether an outcome is “good” or “bad”. It reports what happened.


---

Known Limitations (Intentional)

The following limitations are expected:

Only aggregate statistics are shown

Per-sample details are not expanded

Semantic meaning is not evaluated

Block-level stats depend on block emission


For deeper inspection, individual curation_report entries should be examined directly.


---

Versioning & Stability

report.summary() is stable in the 1.x series.

The output schema and presentation format are part of the public API.

Any change requires an explicit version bump.


---

Summary

report.summary() provides visibility without interference.

It allows preprocessing to be:

inspectable

auditable

reproducible


without compromising the conservative, deterministic design of text-curation.