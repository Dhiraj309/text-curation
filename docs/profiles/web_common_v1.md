# web_common_v1

The `web_common_v1` profile defines a **stable, conservative text curation pipeline**
for heterogeneous, web-derived content.

It is designed for large-scale datasets where **predictability,
reproducibility, and semantic preservation** are critical.

This profile is treated as a **long-term behavioral contract**.

---

## Intended Use

This profile is suitable for:

- Common Crawl–like datasets
- Blog posts, forums, and scraped articles
- OCR- or PDF-derived web content
- Mixed-quality, user-generated text

It is intended to serve as a **general-purpose baseline**
for web text curation in the Hugging Face ecosystem.

---

## Pipeline Overview

At a high level, `web_common_v1` applies the following stages:

1. Redaction of sensitive tokens
2. Unicode and whitespace normalization
3. Conservative formatting and paragraph reconstruction
4. Structural signal extraction
5. Signal-based filtering
6. Exact paragraph-level deduplication

Each stage is deterministic and independently testable.

---

## Guarantees (Stable)

When using `web_common_v1`, the following guarantees hold:

- Output is fully deterministic for a given input
- No machine learning or semantic inference is applied
- Sensitive tokens (e.g. emails, credentials) are masked
- Paragraph structure and semantics are preserved
- Indentation-sensitive content (e.g. code blocks) is preserved
- Numeric formats, timestamps, and identifiers are not modified
- Filtering decisions are conservative and signal-based
- Deduplication is exact and paragraph-local only

These guarantees are enforced by **golden tests**
and are considered part of the profile’s public contract.

---

## Known Limitations (Intentional)

The following behaviors are expected and intentional:

- Some boilerplate repetition may remain
- Headers and footers are not aggressively removed
- Short comments and low-density text may persist
- Visual layout is normalized rather than preserved exactly

These trade-offs are required to avoid semantic damage
in large-scale, heterogeneous web corpora.

---

## When Not to Use

This profile may not be appropriate if you require:

- Aggressive boilerplate stripping
- Semantic or quality-based filtering
- Language-specific or domain-specific cleanup
- Exact preservation of visual layout

Such behavior should be implemented via
custom or explicitly opt-in profiles.

---

## Versioning & Stability

- `web_common_v1` is stable across all `1.x` releases
- Behavior will not change without a major version bump
- The profile may be deprecated in the future, but
  **will never be silently changed**

For alternative behavior, create a new profile version
(e.g. `web_common:v2`) rather than modifying this one.