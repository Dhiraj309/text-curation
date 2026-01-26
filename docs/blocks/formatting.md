# Formatting Blocks

Formatting is implemented as **two distinct, ordered blocks**
to preserve structure while improving readability.

Formatting operates at the **line and paragraph level**
and is intentionally conservative.

---

## Formatting pipeline

Formatting is composed of:

1. **CodeSafeFormattingBlock**
2. **ParagraphFormattingBlock**

Both blocks are required to achieve correct behavior.

---

## CodeSafeFormattingBlock

This block performs **structural normalization only**.

### What it does

- Normalizes line endings
- Trims trailing whitespace
- Collapses excessive blank lines
- Preserves indentation-sensitive content verbatim

### Guarantees

- Leading indentation is never removed
- No lines are merged
- No semantics are altered

---

## ParagraphFormattingBlock

This block reconstructs **human-readable paragraph structure**
and normalizes punctuation.

### What it does

- Reconstructs paragraphs from wrapped text
- Preserves indented blocks (e.g. code, quoted text)
- Normalizes punctuation spacing
- Preserves URLs, emails, IPs, and numeric formats

---

## Paragraph reconstruction rules (stable)

- Paragraphs are reconstructed **only at explicit boundaries**
- Adjacent non-empty lines are **never merged implicitly**
- Blank lines flush paragraph buffers
- Indented lines are preserved exactly
- Relative indentation inside blocks is preserved

These rules are enforced by tests and considered stable.

---

## Punctuation handling

- Fixes spacing around `, ! ? : ;`
- Does **not** modify:
  - URLs
  - email addresses
  - IP addresses
  - numeric separators
  - time formats

---

## What formatting does NOT do

- ❌ No sentence splitting
- ❌ No Markdown parsing
- ❌ No HTML awareness
- ❌ No aggressive reflowing

---

## Design rationale

Formatting improves **readability and consistency**
without making assumptions about document semantics.

Preserving paragraph meaning is prioritized over visual uniformity.