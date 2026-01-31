# RedactionBlock

The `RedactionBlock` masks **explicitly recognized sensitive tokens**
using deterministic, pattern-based matching.

Redaction is **non-destructive** and replaces matched content
with stable, explicit placeholders.

This block is part of the **stable core**.

---

## Scope

Redaction is applied:

- At the text level
- Using fixed, bounded regular expressions
- Without inspecting context, semantics, or entropy

This block is designed for **safety and predictability**, not completeness.

---

## Behavior (Stable)

The block performs the following redactions:

- Email addresses → `<EMAIL>`
- Explicit API tokens → `<TOKEN>`
- Credentials embedded in URLs → `<REDACTED>`

Redaction replaces matched substrings in-place.
All other text is preserved verbatim.

---

## Supported Token Patterns

The following token formats are recognized:

- `sk-*` (OpenAI-style API keys)
- `hf_*` (Hugging Face tokens)
- `ghp_*` (GitHub tokens)
- `api_*`, `key_*` (generic API keys)

Patterns are intentionally narrow and explicit.

---

## Guarantees

When this block is applied:

- Redaction is deterministic
- Only recognized patterns are masked
- Placeholders are stable and explicit
- No secrets are logged or exposed
- Surrounding text is preserved exactly

---

## Explicit Non-Behavior

This block does **not**:

- Detect secrets heuristically or by entropy
- Attempt to identify personal data broadly
- Hash or encrypt sensitive values
- Remove entire lines or documents
- Perform language- or domain-specific redaction
- Infer sensitivity from context

This block does **not** provide comprehensive PII removal.

---

## Placeholders as Contract

The placeholders `<EMAIL>`, `<TOKEN>`, and `<REDACTED>`
are part of the public contract.

They:

- Are stable across releases
- Are intentionally human-readable
- Are not configurable by default

Any change to placeholders requires a breaking release.

---

## Stability

- Redaction behavior is stable as of `v1.x`
- Adding new token patterns is allowed
- Changing existing patterns or placeholders is a breaking change

---

## Notes on Use

Redaction prioritizes **safety over recall**.

If broader or heuristic-based redaction is required,
it must be implemented as:

- a separate block
- a separate profile
- or external preprocessing

Silent inference is forbidden.
