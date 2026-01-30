# web_common_v1

The `web_common_v1` profile defines a **stable, conservative text curation pipeline**
for heterogeneous, web-derived content.

It is designed for large-scale datasets where **predictability, reproducibility,
and semantic preservation** are critical, while still allowing **light structural cleanup**
and **conservative boilerplate removal**.

This profile is treated as a **long-term behavioral contract**.

---

## Intended Use

This profile is suitable for:

* Common Crawl–like datasets
* Blog posts, forums, and scraped articles
* OCR- or PDF-derived web content
* Mixed-quality, user-generated text

It is intended to serve as a **general-purpose baseline**
for web text curation in the Hugging Face ecosystem, balancing
safety, cleanliness, and semantic fidelity.

---

## Pipeline Overview

At a high level, `web_common_v1` applies the following stages:

1. Redaction of sensitive tokens
2. Unicode and whitespace normalization
3. Code-safe formatting preservation
4. Paragraph and line structure reconstruction
5. Structural signal extraction (headers, lists, repetition)
6. Conservative paragraph-level deduplication

Each stage is deterministic and independently testable.

---

## Guarantees (Stable)

When using `web_common_v1`, the following guarantees hold:

* Output is fully deterministic for a given input
* Processing order does not affect the result
* No machine learning models are used
* No semantic inference or rewriting is applied
* Sensitive tokens (e.g. emails, credentials) are redacted
* Paragraph-level structure is preserved
* Indentation-sensitive content (e.g. code blocks) is preserved
* Numeric formats, timestamps, and identifiers are not modified
* Structural signals are extracted without mutating text
* Content removal is conservative and rule-based
* Deduplication is exact and paragraph-scoped

These guarantees are enforced by **golden tests**
and are considered part of the profile’s public contract.

---

## Known Limitations (Intentional)

The following behaviors are expected and intentional:

* Some boilerplate repetition may remain
* Deduplication may remove short or repeated boilerplate paragraphs
* Headers and footers are not aggressively stripped
* Low-density or marginal text may persist
* Visual layout is normalized rather than preserved exactly

These trade-offs are required to avoid semantic damage
and over-filtering in large-scale, heterogeneous web corpora.

---

## When Not to Use

This profile may not be appropriate if you require:

* Pretraining-safe, non-destructive text preservation
* Full preservation of repetition and boilerplate
* Aggressive quality or semantic filtering
* Language-specific or domain-specific cleanup
* Exact visual layout preservation

Such behavior should be implemented via
**custom or explicitly opt-in profiles** (e.g. `llm_pretrain_v1`).

---

## Versioning & Stability

* `web_common_v1` is stable across all `1.x` releases
* Behavior will not change without a major version bump
* The profile may be deprecated in the future, but
  **will never be silently changed**
* Any behavioral changes require a new profile version
  (e.g. `web_common_v2`)

This reflects the library’s guiding principle:

**Profiles evolve. Contracts do not.**