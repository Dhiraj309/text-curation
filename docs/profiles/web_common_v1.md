# web_common_v1

`web_common_v1` defines a **stable, conservative text curation profile**
for heterogeneous, web-derived content.

This profile is intended to serve as a **general-purpose baseline**
for large-scale web text curation where **predictability, reproducibility,
and semantic preservation** are required.

`web_common_v1` is a **frozen behavioral contract**.

---

## Intended Use

This profile is intended for:

- Common Crawl–like datasets
- Blog posts, forums, and scraped articles
- OCR- or PDF-derived web content
- Mixed-quality, user-generated text

It is suitable for datasets that require **light structural cleanup**
and **explicit, conservative boilerplate removal**
without semantic inference.

---

## Pipeline Definition

`web_common_v1` applies the following blocks, in order:

1. `RedactionBlock`
2. `NormalizationBlock`
3. `CodeSafeFormattingBlock`
4. `ParagraphFormattingBlock`
5. `BasicStructureBlock`
6. `ExactParagraphDeduplicationBlock`

Block ordering is part of the contract.

---

## Guarantees (Stable)

When using `web_common_v1`, the following guarantees hold:

- Output is fully deterministic for a given input
- Block execution order is fixed and reproducible
- No machine learning models are used
- No semantic inference or rewriting is applied
- Explicit secret patterns are redacted
- Unicode and whitespace artifacts are normalized
- Paragraph structure is reconstructed conservatively
- Indentation-sensitive content (e.g. code) is preserved
- Structural signals are emitted without mutating text
- Deduplication is exact and paragraph-scoped only
- Content removal is rule-based and conservative

These guarantees are enforced by **golden tests**.

---

## Explicit Non-Guarantees

The following are **not guaranteed** and must not be assumed:

- Complete boilerplate removal
- Removal of all headers, footers, or navigation text
- Cross-document or dataset-level deduplication
- Language-specific or domain-specific cleanup
- Quality scoring or semantic filtering
- Exact visual layout preservation

---

## Known and Intentional Outcomes

Users should expect that:

- Some boilerplate repetition may remain
- Some low-density or marginal content may persist
- Layout is normalized rather than preserved verbatim
- Cleanup favors semantic safety over aggressiveness

These outcomes are intentional and required
to preserve reproducibility at scale.

---

## When Not to Use

This profile must **not** be used when:

- Full preservation of repetition and boilerplate is required
- Text is intended for direct LLM pretraining
- Aggressive filtering or quality heuristics are desired
- Language- or domain-specific rules are required

Such use cases require a **different, explicitly scoped profile**
(e.g. `llm_pretrain_v1`).

---

## Versioning & Stability

- `web_common_v1` is stable across all `1.x` releases
- Its behavior will not change without a major version bump
- It may be deprecated, but will never be silently modified
- Any behavioral change requires a new profile version

**Profiles evolve. Contracts do not.**
