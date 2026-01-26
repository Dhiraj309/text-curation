# RedactionBlock

The `RedactionBlock` masks **sensitive information**
using deterministic, pattern-based matching.

All redaction is performed via **non-destructive masking**.

---

## What it does

- Redacts email addresses → `<EMAIL>`
- Redacts API tokens → `<TOKEN>`
- Redacts credentials embedded in URLs → `<REDACTED>`

---

## Supported token patterns

- `sk-*` (OpenAI-style keys)
- `hf_*` (Hugging Face tokens)
- `ghp_*` (GitHub tokens)
- `api_*`, `key_*`

---

## What it does NOT do

- ❌ No entropy-based secret detection
- ❌ No hashing or encryption
- ❌ No logging of secrets
- ❌ No redaction of generic IDs or checksums

---

## Design rationale

Redaction prioritizes **safety and predictability**.

Only well-defined patterns are masked to avoid accidental
removal of non-sensitive identifiers.

---

## Signals

This block does **not emit signals**.