# BasicStructureBlock

The `BasicStructureBlock` emits **inspectable structural signals**
without mutating text.

This block is part of the **stable core**.

This block is a **low-level deterministic primitive** intended for
profile authors and library extension.
Most users should rely on profiles rather than composing blocks directly.

---

## Behavior

- Line-level structural signals
- Paragraph-level repetition signals
- Deterministic, rule-based detection

---

## Guarantees

- Text is never modified
- Signal names and meanings are stable
- No decisions are made implicitly

---

## Explicit Non-Behavior

- No filtering
- No deduplication
- No semantic classification

---

## Stability

Signal definitions are stable as of `v1.x`.
