# web_common_v1

The `web_common_v1` profile defines a **stable, conservative text curation pipeline**
for heterogeneous web-derived content.

It is designed for large-scale datasets where **predictability,
reproducibility, and semantic preservation** are critical.

---

## Intended Use

This profile is suitable for:

- Common Crawl–like datasets
- Blog posts, forums, and scraped articles
- OCR- or PDF-derived web content
- Mixed-quality, user-generated text

It is intended to be a **general-purpose baseline** for web text curation.

---

## Guarantees

When using `web_common_v1`, the following guarantees hold:

- Output is fully deterministic
- No machine learning or semantic inference is applied
- Sensitive tokens (e.g. emails, credentials) are masked
- Paragraph structure is preserved
- Numeric formats and timestamps are not modified
- Filtering decisions are conservative and signal-based

These guarantees are treated as part of the profile’s
**behavioral contract**.

---

## Known Limitations (Intentional)

The following behaviors are expected and intentional:

- Repeated boilerplate may remain
- Headers and footers are not aggressively removed
- Short comments and low-density text may persist
- Visual formatting is normalized, not preserved exactly

These trade-offs are required to avoid semantic damage
in large-scale, heterogeneous web corpora.

---

## When Not to Use

This profile may not be appropriate if you require:

- Aggressive boilerplate stripping
- Semantic or quality-based filtering
- Exact preservation of visual layout
- Domain-specific or language-specific cleanup rules

Such behavior should be implemented via
custom or explicitly opt-in profiles.