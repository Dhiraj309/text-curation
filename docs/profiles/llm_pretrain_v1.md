# llm_pretrain_v1

`llm_pretrain_v1` defines a **minimal, deterministic, non-destructive**
text curation profile intended for **large-scale LLM pretraining**.

This profile is a **locked behavioral contract**.

---

## Pipeline Definition

1. `RedactionBlock`
2. `NormalizationBlock`
3. `CodeSafeFormattingBlock`

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
- Unicode and encoding artifacts may be normalized
- Whitespace may be conservatively normalized
- Structural layout is generally preserved

These outcomes are descriptive and not enforced guarantees.

---

## Explicit Non-Behavior

This profile does **not**:

- Perform deduplication
- Perform filtering or content removal
- Emit or consume structural signals
- Perform semantic inference or classification
- Apply dataset-level operations

---

## Stability

The behavior of `llm_pretrain_v1` is stable across all `1.x` releases.

Any behavioral change requires a new profile version or a major release.