# RedactionBlock

The `RedactionBlock` masks **explicitly recognized sensitive tokens**
using deterministic, rule-based pattern matching.

This block is part of the **stable core**.

This block is a **low-level deterministic primitive** intended for
profile authors and library extension.
Most users should rely on profiles rather than composing blocks directly.

---

## Scope

Redaction operates at the **token and substring level only**.

It is intended to remove **clearly identifiable, high-risk secrets**
without interpreting intent, meaning, or context.

Redaction is applied conservatively and only to patterns that are
explicitly defined and documented.

---

## Behavior (Stable)

The following redactions are performed:

- Email addresses → `<EMAIL>`
- Explicit API tokens → `<TOKEN>`
- URL credentials → `<REDACTED>`

Patterns are applied deterministically and globally.

Only the matched substring is replaced.
All surrounding text is preserved exactly.

---

## Guarantees

When this block is applied:

- Redaction behavior is fully deterministic
- Only explicitly defined patterns are redacted
- No surrounding text is modified
- Redaction placeholders are stable and predictable
- Behavior is safe for logs, documents, and code-like text

---

## Explicit Non-Behavior

This block does **not**:

- Perform heuristic or probabilistic PII detection
- Perform entropy-based secret discovery
- Infer sensitive information from context
- Redact names, phone numbers, or identifiers
- Perform semantic or language-aware analysis
- Attempt “best effort” coverage of sensitive data

If a pattern is not explicitly defined, it is not redacted.

---

## Stability

Redaction behavior is **stable as of `v1.x`**.

The following are considered part of the public contract:

- Supported redaction patterns
- Replacement placeholders
- Deterministic matching behavior

Any change requires:

- a **major version bump**, and
- updated unit tests locking the new behavior, and
- explicit documentation of the change