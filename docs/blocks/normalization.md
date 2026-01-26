# NormalizationBlock

The `NormalizationBlock` performs **low-level, non-semantic text normalization**
to remove encoding artifacts and standardize common Unicode variations.

This block is intentionally conservative.

---

## What it does

- Applies Unicode normalization (`NFKC`)
- Removes zero-width characters
- Removes control characters
- Normalizes line endings
- Normalizes quotation marks
- Normalizes dash variants
- Normalizes ellipses (`… → ...`)
- Collapses runs of spaces and tabs
- Limits excessive consecutive newlines

---

## What it does NOT do

- ❌ No spelling correction
- ❌ No OCR error correction
- ❌ No language-specific rules
- ❌ No sentence rewriting

---

## Design rationale

Normalization is limited to **encoding and formatting artifacts**
commonly found in scraped or copied text.

All transformations are deterministic and reversible in principle.

---

## Typical use cases

- Web-scraped text
- OCR / PDF-derived text
- Mixed-encoding corpora

---

## Signals

This block does **not emit signals** and only mutates text.