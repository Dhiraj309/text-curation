# web_common_v1

The `web_common_v1` profile defines a **stable, conservative curation pipeline**
for heterogeneous web-derived text.

It is designed for large-scale datasets where predictability
and semantic preservation are critical.

---

## Intended Use

This profile is suitable for:

- Common Crawl–like datasets
- Blog posts, forums, and scraped articles
- OCR- or PDF-derived web content
- Mixed-quality user-generated text

---

## Guarantees

When using `web_common_v1`, the following guarantees hold:

- Output is fully deterministic
- No machine learning or semantic inference is applied
- Sensitive tokens (emails, credentials) are masked
- Paragraph structure is preserved
- Numeric formats and timestamps are not modified
- Filtering is conservative and signal-based

---

## Known Limitations (Intentional)

The following behaviors are expected and intentional:

- Repeated boilerplate may remain
- Footers and headers are not aggressively removed
- Short comments and low-density text may persist
- Visual formatting is normalized, not preserved exactly

These trade-offs are required to avoid semantic damage
in large-scale web corpora.

---

## When Not to Use

This profile may not be appropriate if you require:

- Aggressive boilerplate stripping
- Semantic quality filtering
- Exact preservation of visual layout
- Domain-specific cleanup rules

Such behavior should be implemented via
custom or opt-in profiles.
