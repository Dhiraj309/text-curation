# llm_pretrain_v1

`llm_pretrain_v1` defines a **minimal, deterministic, non-destructive**
text curation profile for **large-scale LLM pretraining**.

This profile exists to prepare text that is **safe to train on**
without altering distributional properties of the source data.

`llm_pretrain_v1` is a **locked behavioral contract**.

---

## Intended Use

This profile is intended **exclusively** for:

- LLM pretraining corpora
- Tokenization- and loss-sensitive training data
- Shared or long-lived pretraining datasets
- Scenarios where silent data drift is unacceptable

It is designed for **direct consumption by language models**.

---

## Pipeline Definition

`llm_pretrain_v1` applies the following blocks, in order:

1. `RedactionBlock`
2. `NormalizationBlock`
3. `CodeSafeFormattingBlock`

No additional blocks are applied.

Block ordering is part of the contract.

---

## Guarantees (Strict)

When using `llm_pretrain_v1`, the following guarantees hold:

- Output is fully deterministic for a given input
- Block execution order is fixed and reproducible
- No machine learning models are used
- No semantic inference or filtering is applied
- No content is removed
- No content is rewritten
- No deduplication is performed
- Repetition and boilerplate are preserved
- Paragraph boundaries are preserved
- Line order is preserved
- Indentation-sensitive content is preserved
- Numeric formats, identifiers, and timestamps are preserved
- Only explicitly recognized secrets are redacted

These guarantees are enforced by **golden tests**
and are part of the public contract.

---

## Explicit Non-Behavior

This profile does **not**:

- Remove boilerplate, navigation, or templates
- Filter low-quality or noisy text
- Merge or reflow paragraphs
- Apply language-specific rules
- Perform quality scoring or ranking
- Infer document structure semantically
- Modify distributional properties of the data

If any of the above occurs, it is a bug.

---

## Expected Outcomes

Users should expect that:

- Repeated text remains repeated
- Boilerplate remains present
- Messy text remains messy
- Formatting reflects the source faithfully
- Only low-level encoding artifacts are normalized

These outcomes are intentional and required
for safe pretraining.

---

## When Not to Use

This profile must **not** be used when:

- Boilerplate removal is desired
- Deduplication is required
- Readability improvements are needed
- Semantic cleanup is acceptable
- The dataset is intended for downstream tasks

Such use cases require a **different profile**
(e.g. `web_common_v1`).

---

## Versioning & Stability

- `llm_pretrain_v1` is stable across all `1.x` releases
- Its behavior will not change without a major version bump
- It may be deprecated, but will never be silently modified
- Any behavioral change requires a new profile version

**Profiles evolve. Contracts do not.**
