# llm_pretrain_v1

`llm_pretrain_v1` defines a **minimal, deterministic, non-destructive**
text curation profile for **large-scale LLM pretraining**.

This profile is a **locked behavioral contract**.

---

## Pipeline Definition

1. `RedactionBlock`
2. `NormalizationBlock`
3. `CodeSafeFormattingBlock`

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

- Secrets are redacted
- Structure preserved
- Layout preserved
- Repetition preserved

---

## Explicit Non-Behavior

- No deduplication
- No filtering
- No semantic inference
- No content removal

---

## Stability

Stable across all `1.x` releases.
