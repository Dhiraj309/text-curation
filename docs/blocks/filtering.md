# FilteringBlock

The `FilteringBlock` removes content **only when explicitly justified**
by structure signals.

It is intentionally conservative in `web_common_v1`.

---

## What it does

- Drops empty paragraphs
- Drops repeated short boilerplate paragraphs
- Preserves header-led sections
- Operates at paragraph granularity

---

## Filtering rules (web_common_v1)

A paragraph is dropped only if:

- It is empty  
  **OR**
- It is a repeated boilerplate candidate  
  **AND**
- It is short (less than 200 characters)

---

## What it does NOT do

- ❌ No semantic quality filtering
- ❌ No list-based pruning
- ❌ No document-level rejection

---

## Design rationale

Filtering decisions must be:
- explainable
- reproducible
- conservative by default

Aggressive filtering is intentionally out of scope.
