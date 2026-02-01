# Changelog

All notable changes to **text-curation** are documented here.

This project follows **Semantic Versioning** (`MAJOR.MINOR.PATCH`).
Only features explicitly documented as **stable** are guaranteed across minor releases.

---

## Unreleased

### Added
- Dataset-level exact deduplication (`deduplicate_exact`)
- Deterministic corpus-level deduplication reports
- `dedupe_summary` helper for inspecting deduplication effects
- `text_curation.datasets` namespace for dataset-scale operations

---

## 1.4.0 — `llm_pretrain_v1`

### Added
- New profile: **`llm_pretrain_v1`**
  - Deterministic, non-destructive curation for LLM pretraining
  - Preserves structure, repetition, and boilerplate
  - Character-level hygiene only (no semantic filtering or deduplication)
- Golden test locking profile behavior

### Changed
- Dataset summaries now report percentage deltas with four-decimal precision

### Stability
- No breaking changes
- Existing profiles unchanged
- New behavior is opt-in

---

## 1.3.x — Core & Profile Stabilization

- Locked formatting and normalization semantics
- Finalized `web_common_v1` as a stable behavioral contract
- Fixed whitespace, paragraph reconstruction, and code/prose edge cases
- Expanded golden test coverage

---

## 1.2.0 — Dataset-Level Reporting

- Introduced per-sample `curation_report` (opt-in)
- Added dataset-level summary utilities
- Reporting is strictly observational and deterministic

---

## 1.1.0 — Structured Core Refactor

- Clean separation of blocks, core, and profiles
- Explicit profile registration and resolution
- Documentation elevated to behavioral specification

---

## 1.0.0 — Initial Release

- Profile-based deterministic text curation
- Core normalization, formatting, redaction, structure, filtering, and deduplication blocks
- Hugging Face `datasets.Dataset.map` integration
