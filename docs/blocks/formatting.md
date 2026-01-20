# FormattingBlock

The `FormattingBlock` reconstructs **human-readable structure**
from text that is hard-wrapped, inconsistently spaced,
or poorly formatted.

It operates at the **paragraph and line level**.

---

## What it does

- Normalizes line endings
- Trims trailing whitespace
- Collapses excessive blank lines
- Reconstructs paragraphs from wrapped lines
- Preserves indented blocks (e.g. code, quoted text)
- Normalizes punctuation spacing
- Preserves URLs, emails, IPs, and numeric formats

---

## Paragraph reconstruction rules

- Lines are merged only when separated by blank lines
- Indented lines are preserved exactly
- Relative indentation inside blocks is preserved
- Absolute indentation is normalized

This ensures code and quoted blocks remain readable
without assuming language or syntax.

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

## What it does NOT do

- ❌ No sentence splitting
- ❌ No Markdown parsing
- ❌ No HTML awareness
- ❌ No aggressive reflowing

---

## Design rationale

Formatting improves **readability and consistency**
without making assumptions about document semantics.
