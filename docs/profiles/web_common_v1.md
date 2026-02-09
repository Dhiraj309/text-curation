# web_common_v1

`web_common_v1` defines a **conservative, deterministic**
text curation profile for heterogeneous, web-derived content.

This profile is a **frozen behavioral contract**.

---

## Pipeline Definition

1. `RedactionBlock`
2. `NormalizationBlock`
3. `CodeSafeFormattingBlock`
4. `ParagraphFormattingBlock`
5. `BasicStructureBlock`
6. `ExactParagraphDeduplicationBlock`

Block order is fixed and enforced.

---

## Hard Guarantees (Enforced)

When this profile is applied:

- Execution is deterministic
- Block order is fixed and explicit
- The profile ID fully specifies behavior
- No hidden global or cross-document state is used
- All transformations are document-local

---

## Intended Behavior (Not Guaranteed)

Depending on input content:

- Explicitly recognized secrets may be redacted
- Unicode and formatting artifacts may be normalized
- Paragraph structure may be reconstructed conservatively
- Exact duplicate paragraphs may be removed
- Structural signals may be emitted for inspection

These outcomes are descriptive and not enforced guarantees.

---

## Explicit Non-Guarantees

This profile does **not** guarantee:

- Complete boilerplate removal
- Removal of near-duplicate or similar paragraphs
- Dataset-level or cross-document deduplication
- Semantic filtering or quality scoring
- Preservation of original layout in all cases

---

## Stability

The behavior of `web_common_v1` is stable across all `1.x` releases.

Any behavioral change requires a new profile version or a major release.