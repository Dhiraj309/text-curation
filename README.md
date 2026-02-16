<!--
Copyright 2026 The text-curation Authors.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
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
  <i>Deterministic corpus compilation for reproducible NLP datasets</i>
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

# Overview

**text-curation** is a Python library for building **profile-driven, deterministic corpus compilation pipelines**
for large-scale NLP datasets, with first-class integration into the
**Hugging Face Datasets** ecosystem.

As of **v1.6.0**, text-curation is no longer just a text cleaning library.

It is a **deterministic corpus compilation foundation**.

It treats preprocessing as a:

- versioned artifact  
- inspectable transformation graph  
- reproducible build step  
- dataset-level identity boundary  

All transformations and analysis are **explicit, deterministic, and conservative by default**.

---

# What 1.6.0 Introduces

Version 1.6.0 extends document-level cleaning into corpus-level infrastructure:

- Signal-only analysis namespace
- Deterministic document fingerprinting (SHA-256)
- Deterministic dataset-level hash deduplication
- Deterministic reference MinHash deduplication
- Exact n-gram decontamination (signal-only)
- Dataset lineage manifests
- Pipeline configuration hashing
- Pretraining-oriented profile (`web_pretrain_v1`)
- Deterministic replay enforcement

All changes are additive.  
No public API was removed or renamed.

---

# Why text-curation exists

Text preprocessing is one of the least reproducible stages of modern ML pipelines.

In practice it is often implemented as:

- evolving regex scripts  
- undocumented heuristics  
- silent cleanup steps  

Small changes alter dataset distributions yet go untracked.

text-curation enforces the same rigor on preprocessing that modern ML systems apply to:

- model checkpoints  
- tokenizer versions  
- dataset artifacts  

Preprocessing becomes:

- explicit  
- inspectable  
- versioned  
- reproducible  

---

# Canonical workflow

1. **Select a curation profile**  
   A versioned, immutable description of behavior.

2. **Apply it to a dataset**  
   Using Hugging Face Datasets.

3. **Inspect emitted signals and reports**  
   Signals never mutate behavior.

4. **Freeze dataset identity**  
   With profile version + pipeline hash + dataset hash.

> Profiles are the unit of behavior.  
> Blocks are implementation details and not part of the public stability contract.

---

# Deterministic Corpus Compilation Model

text-curation now separates:

### 1. Transformation (blocks/)
Mutate or structure text deterministically.

### 2. Observation (analysis/)
Emit signals only.
Never mutate text.
Never filter implicitly.

### 3. Dataset Operations
Explicit, order-preserving, deterministic dataset-level utilities.

### 4. Identity & Lineage
Pipeline hash + document fingerprints + dataset hash + manifest.

This separation prevents silent data drift.

---

# Analysis Namespace (Signal-Only)

`src/text_curation/analysis/`

Analysis blocks:

- Subclass `AnalysisBlock`
- Must not modify text
- Must not mutate annotations
- Must emit deterministic signals

Included in 1.6.0:

### QualitySignalBlock
Emits:
- `char_entropy`
- `stopword_ratio`
- `url_density`
- `repetition_score`
- `avg_sentence_length`

Whitespace tokenization.  
Float rounding for stability.  
No ML. No external dependencies.

### TokenStatsBlock
Emits:
- `token_count`
- `unique_token_count`
- `rare_token_ratio`
- `max_token_length`

Whitespace tokenization.  
Rare token = frequency == 1 within document.  
No tokenizer dependency.

### FingerprintBlock
Emits:
- `sha256` (UTF-8, deterministic)

Provides stable document identity.

---

# Dataset-Level Operations (Advanced)

Located under:

`src/text_curation/datasets/advanced/`

All operations:

- Preserve order
- Are deterministic
- Require explicit configuration
- Avoid Python’s built-in `hash()`

### SHA-256 Deduplication

`deduplicate_by_hash()`

- Groups identical hashes
- Keeps first or last (explicit)
- Emits deterministic report
- Order preserved

### Exact n-gram Decontamination (Signal-Only)

`decontaminate()`

- Accepts precomputed benchmark n-grams
- Explicit ngram_size
- Whitespace tokenization
- Emits overlap_score
- Does not filter by default

Detection is separated from filtering.

### Deterministic Reference MinHash

`minhash_deduplicate()`

- Seed-controlled
- Explicit num_hashes
- Explicit ngram_size
- Explicit threshold
- SHA1-based stable hashing
- Canonical representative = lowest index
- O(n²) reference semantics

Semantics are frozen before scaling.

---

# Dataset Lineage & Reproducibility

## DatasetManifest

Captures:

- profile_ids
- library_version
- block_order
- dataset_hash
- total_token_count
- explicit timestamp
- metadata

Immutable dataclass.  
No implicit timestamps.  
No environment reads.

## Pipeline Configuration Hash

`compute_pipeline_hash(profile)`

Hashes:

- profile.id
- block order
- block class names
- block policy dictionaries (sorted)

Excludes:

- runtime stats
- dataset content
- emitted signals

Purpose: detect semantic drift in configuration.

---

# Deterministic Replay Guarantee

Given:

- Same input
- Same profile
- Same settings
- Same library version

text-curation guarantees:

- Byte-identical output text
- Identical emitted signals
- Identical reports
- Identical pipeline hash
- Identical dataset hash (same ordering)

Deterministic replay is treated as sacred.

---

# Profiles

Profiles define ordered deterministic behavior.

They are:

- Explicitly versioned
- Immutable once released
- Resolved via global registry

New in 1.6.0:

`web_pretrain_v1`

Includes:

- Redaction
- Normalization
- Code-safe formatting
- Paragraph formatting
- Basic structure emission
- Quality signals
- Token statistics
- Fingerprinting

It does not:

- Perform dataset-level deduplication
- Perform filtering by default
- Use ML models
- Introduce nondeterminism

Profiles are behavioral contracts.

---

# Stability & Scope

### Stable

- `TextCurator` public API
- Released profiles and their semantics
- Deterministic replay invariant
- Pipeline hash semantics
- Dataset manifest structure

### Experimental

- New blocks
- Advanced dataset utilities
- New profiles until marked stable

Breaking behavior requires a major version bump.

---

# Non-Goals

text-curation intentionally does not:

- Use machine learning
- Perform semantic classification
- Infer document intent
- Apply aggressive irreversible cleanup
- Introduce probabilistic scoring
- Manage model artifacts

ML scoring, perplexity, language detection, and distributed deduplication
are intentionally out of scope for 1.x.

---

# Installation

Python ≥ 3.9 required.

```bash
pip install text-curation
````

Development:

```bash
git clone https://github.com/Dhiraj309/text-curation.git
cd text-curation
pip install -e .
```

---

# Quickstart

```python
from datasets import load_dataset
from text_curation import TextCurator

dataset = load_dataset(
    "HuggingFaceFW/fineweb-edu",
    split="train",
)

curator = TextCurator.from_profile(
    "web_pretrain_v1",
    collect_reports=True,
)

dataset = dataset.map(
    curator,
    batched=True,
    num_proc=4,
)
```

---

# Reporting

Reports describe what changed and what was observed.

```python
from text_curation.reports import summary
summary(dataset)
```

Reports enable:

* Auditing preprocessing behavior
* Detecting dataset drift
* Comparing profiles
* Inspecting quality signals

Reports never affect behavior.

---

# When not to use text-curation

* One-off regex cleanup
* Already fully curated datasets
* ML-based content scoring
* Distributed approximate deduplication at massive scale

---

# Versioning

Semantic Versioning is followed.

1.x guarantees:

* Deterministic replay stability
* Profile semantic stability
* Public API stability

Profiles are versioned independently.

---

# Contributing

Expectations:

* Deterministic behavior
* Conservative defaults
* Tests as specifications
* No silent semantic changes
* No nondeterminism

Reproducibility is a first-class constraint.

---

# License

Apache 2.0. See LICENSE.

---

# Acknowledgements

Inspired by large-scale dataset curation practices in the Hugging Face ecosystem.