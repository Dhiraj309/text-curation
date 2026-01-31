<!--Copyright 2026 The text-curation Authors.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0
-->

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)"
            srcset="https://dummyimage.com/720x140/0d1117/ffffff&text=text-curation">
    <source media="(prefers-color-scheme: light)"
            srcset="https://dummyimage.com/720x140/ffffff/000000&text=text-curation">
    <img alt="text-curation logo"
         src="https://dummyimage.com/720x140/ffffff/000000&text=text-curation"
         width="360"
         style="max-width: 100%">
  </picture>
  <br/>
  <br/>
</p>

<p align="center">
  <i>Reproducible, auditable text preprocessing as a first-class artifact</i>
</p>

<p align="center">
  <a href="https://pypi.org/project/text-curation/">
    <img alt="PyPI version" src="https://img.shields.io/pypi/v/text-curation.svg">
  </a>
  <a href="https://pypi.org/project/text-curation/">
    <img alt="PyPI downloads" src="https://img.shields.io/pypi/dm/text-curation">
  </a>
  <a href="https://github.com/Dhiraj309/text-curation/releases">
    <img alt="GitHub release" src="https://img.shields.io/github/release/Dhiraj309/text-curation.svg">
  </a>
  <a href="https://pypi.org/project/text-curation/">
    <img alt="Python versions" src="https://img.shields.io/pypi/pyversions/text-curation.svg">
  </a>
  <a href="https://github.com/Dhiraj309/text-curation/blob/main/LICENSE">
    <img alt="License" src="https://img.shields.io/github/license/Dhiraj309/text-curation.svg">
  </a>
</p>

---

**Documentation**: https://github.com/Dhiraj309/text-curation  
**Source Code**: https://github.com/Dhiraj309/text-curation

---

## Overview

**text-curation** is a Python library for building **profile-driven, deterministic text curation pipelines**
for **large-scale NLP datasets**, with first-class integration into the
**Hugging Face Datasets** ecosystem.

It treats text preprocessing as a **versioned, inspectable artifact** rather than
an ad-hoc collection of cleanup scripts.

All transformations are **explicit, deterministic, and conservative by default**,
making dataset preparation **reproducible, auditable, and stable over time**.

---

## Why text-curation exists

Text preprocessing is one of the least reproducible stages of modern ML pipelines.

In practice, it is often implemented as:
- evolving regex scripts
- undocumented heuristics
- silent cleanup steps

Small changes can significantly alter data distributions, yet are rarely tracked,
audited, or reproducible.

**text-curation** enforces the same rigor on data preprocessing that modern ML
systems apply to models, tokenizers, and datasets.

---

## Canonical workflow

The intended workflow is explicit and intentional:

1. **Select a curation profile**  
   A versioned, immutable description of preprocessing behavior.

2. **Apply it to a dataset**  
   Using Hugging Face Datasets at scale.

3. **Inspect what changed**  
   Via structured, dataset-level curation reports.

4. **Freeze and publish the artifact**  
   With the profile version as part of the dataset identity.

This workflow is designed to prevent silent data drift and make preprocessing
decisions inspectable.

> **Profiles are the unit of behavior in text-curation.**  
> Blocks are implementation details and are not part of the stability or
> compatibility contract.

---

## Design principles

- **Profile-driven pipelines**  
  Reusable, declarative profiles define *what* happens, not hidden heuristics.

- **Deterministic and conservative**  
  Given the same input and profile, output is identical across runs.

- **Structure-aware processing**  
  Text is treated as structured content (paragraphs, lists, headers), not raw strings.

- **Dataset-scale friendly**  
  Designed for efficient use with large Hugging Face Datasets.

- **Explicit over clever**  
  No probabilistic inference, no semantic guessing, no silent behavior.

---

## Stability & scope

Only features **explicitly documented as stable** are guaranteed not to change
across minor releases.

### Stable
- Built-in profiles and their behavior
- `TextCurator` public API
- Curation report formats

### Experimental
- New blocks
- Dataset-level utilities
- New profiles until documented as stable

Profiles are treated as **behavioral contracts**.
Once released, their semantics do not change.

---

## Profiles

Profiles define **what preprocessing behavior is applied and in what order**.

They are:
- Explicitly versioned
- Registered at import time
- Resolved via a global registry

Conceptually, a profile defines an ordered sequence of deterministic transformations.
The specific block composition is an implementation detail and not part of the
public contract.

Profiles may be deprecated, but are never silently modified.

---

## Implementation primitives (advanced)

Blocks are low-level, deterministic primitives intended for profile authors and
library extension.

End users should consume behavior exclusively via profiles.

Stable primitives include:

- **Normalization** — Unicode, typography, whitespace normalization
- **Formatting** — Paragraph reconstruction and code-safe formatting
- **Redaction** — Deterministic masking of emails and explicit tokens
- **Structure** — Emission of inspectable structural signals
- **Filtering** — Conservative, signal-based removal
- **Deduplication** — Exact, normalization-safe paragraph deduplication

More aggressive or semantic behavior is intentionally out of scope by default.

---

## Non-goals

text-curation intentionally does not:

- Perform semantic or topical classification
- Use machine learning or probabilistic heuristics
- Infer document quality or intent
- Apply aggressive, irreversible cleanup by default

These constraints are critical to reproducibility.

---

## Installation

Python ≥ 3.9 is required.

```bash
pip install text-curation

For development:

git clone https://github.com/Dhiraj309/text-curation.git
cd text-curation
pip install -e .


Quickstart
from datasets import load_dataset
from text_curation import TextCurator

dataset = load_dataset(
    "HuggingFaceFW/fineweb-edu",
    split="train",
)

curator = TextCurator.from_profile(
    "web_common_v1",
    collect_reports=True,
)

dataset = dataset.map(
    curator,
    batched=True,
    num_proc=4,
)


Reporting
Curation reports describe what changed, not just what was produced.

from text_curation.reports import summary
summary(dataset)

Reports enable:


auditing preprocessing behavior
detecting dataset drift
comparing profiles

They never affect curation behavior.


When not to use text-curation

One-off regex cleanup
Already-curated datasets
ML-based content scoring or classification


Versioning
This project follows Semantic Versioning.


1.x guarantees stable default behavior
Breaking changes require a major version bump
Profiles are versioned independently of library releases


Contributing
Contributions are welcome.

Please read CONTRIBUTING.md before submitting changes.

Key expectations:


Deterministic behavior
Conservative defaults
Tests as specifications
No silent behavior changes


License
Apache 2.0. See LICENSE.


Acknowledgements
Inspired by large-scale dataset curation practices in the Hugging Face ecosystem.
