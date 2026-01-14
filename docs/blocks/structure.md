# StructureBlock

The `StructureBlock` analyzes text structure and emits
**inspectable signals** without mutating the text.

---

## Signals emitted

### Line-level signals

- `is_blank`
- `is_header`
- `is_bullet`
- `is_numbered_item`
- `is_all_caps`
- `is_short`
- `repetition_count`

### Paragraph-level signals

- `is_list_block`
- `is_boilerplate_candidate`
- `repetition_count`

---

## Detection methods

- Regex-based pattern matching
- Frequency-based repetition analysis
- Conservative structural heuristics

---

## What it does NOT do

- ❌ No text modification
- ❌ No semantic classification
- ❌ No language detection

---

## Design rationale

Structure signals intentionally separate **observation from decision**.

They allow downstream blocks to make explicit,
auditable choices without hidden logic.

This block is central to the library’s inspectability.