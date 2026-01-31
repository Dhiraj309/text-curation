# web_common_v1

`web_common_v1` defines a **conservative, deterministic**
text curation profile for heterogeneous web-derived content.

This profile is a **frozen behavioral contract**.

---

## Pipeline Definition

1. `RedactionBlock`
2. `NormalizationBlock`
3. `CodeSafeFormattingBlock`
4. `ParagraphFormattingBlock`
5. `BasicStructureBlock`
6. `ExactParagraphDeduplicationBlock`

Block order is fixed.

---

## Hard Guarantees (Enforced)

- Deterministic execution
- Explicit block order
- Profile ID fully specifies behavior
- No hidden global state
- Document-local transforms only

---

## Intended Behavior (Not Guaranteed)

- Secrets redacted
- Structure preserved
- Layout normalized
- Conservative content removal
- Exact paragraph deduplication

---

## Explicit Non-Guarantees

- Full boilerplate removal
- Dataset-level deduplication
- Semantic filtering
- Layout preservation

---

## Stability

Stable across all `1.x` releases.
