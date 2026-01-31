# RedactionBlock

The `RedactionBlock` masks **explicitly recognized sensitive tokens**
using deterministic pattern matching.

This block is part of the **stable core**.

This block is a **low-level deterministic primitive** intended for
profile authors and library extension.
Most users should rely on profiles rather than composing blocks directly.

---

## Behavior (Stable)

- Email addresses → `<EMAIL>`
- Explicit API tokens → `<TOKEN>`
- URL credentials → `<REDACTED>`

---

## Guarantees

- Deterministic redaction
- Narrow, explicit patterns only
- Surrounding text preserved exactly

---

## Explicit Non-Behavior

- No heuristic PII detection
- No entropy-based matching
- No semantic inference

---

## Stability

Placeholders and patterns are stable as of `v1.x`.
