# Contributing to text-curation

First off, thank you for considering contributing to **text-curation** 🙌  
This project exists to provide **deterministic, structure-aware, production-grade text curation**
for real-world, messy text data at dataset scale.

Contributions of all kinds are welcome — bug fixes, new blocks, tests, documentation,
performance improvements, and new profiles.

---

## 🧭 Project Philosophy

This library is built with the following principles in mind:

- **Conservative by default**  
  Avoid destructive transformations unless explicitly requested.

- **Deterministic behavior**  
  Given the same input and profile, output must be stable and reproducible.

- **Structure-aware processing**  
  Text is not just strings — paragraphs, lists, headers, repetition, and boilerplate matter.

- **Pipeline-first design**  
  Each block should do one thing well and remain composable.

- **Real-world robustness**  
  Code should handle OCR artifacts, web boilerplate, emails, scanned text, forums,
  and scraped content without semantic assumptions.

- **Tests as specifications**  
  Tests define and lock in behavior; they are not optional.

---

## 🔒 Stability Contract (Important)

As of **v1.3.0**, `text-curation` provides **stable default behavior**.

Contributors must assume that:

- Default block behavior is **part of the public API**
- Changing outputs for existing inputs is a **breaking change**
- Breaking changes require explicit discussion and a major version bump

If a proposed change alters behavior, it should usually be introduced as:

- a new block
- a new profile
- an opt-in policy flag (disabled by default)

Profiles may be deprecated, but must never be silently changed.

---

## 📦 Project Structure

```

src/text_curation/
├── blocks/
│   ├── base.py
│   ├── normalization.py
│   ├── redaction.py
│   ├── temp.py
│   ├── deduplication/
│   ├── filtering/
│   ├── formatting/
│   │   ├── code_safe.py
│   │   └── paragraph.py
│   └── structure/
├── core/
│   ├── annotations.py
│   ├── document.py
│   ├── pipeline.py
│   └── signals.py
├── profiles/
│   ├── base.py
│   └── web_common_v1.py
├── curator.py
├── registry.py
└── **init**.py

tests/
├── blocks/
│   ├── test_normalization.py
│   ├── test_formatting.py
│   ├── test_redaction.py
│   ├── test_structure.py
│   ├── test_filtering.py
│   └── test_deduplication.py
└── profiles/
└── test_web_common_v1_golden.py

````

Documentation lives under `docs/` and mirrors this structure.

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Dhiraj309/text-curation.git
cd text-curation
````

### 2️⃣ Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -e .[dev]
```

---

## 🧪 Running Tests

We use **pytest** for all tests.

```bash
python -m pytest
```

Before submitting a PR:

* ✅ All tests must pass
* ✅ New behavior must include tests
* ✅ Existing tests must not change unless behavior is intentionally revised

Golden tests are used to lock in profile-level behavior.

---

## 🧩 Adding a New Block

To add a new block:

1. Create a file under `src/text_curation/blocks/`
2. Subclass `Block` from `blocks.base`
3. Implement `apply(self, document)`
4. Add tests under `tests/blocks/`
5. Optionally include the block in a new or existing profile

### Block guidelines

* Blocks **must not silently change semantics**
* Prefer **signals over hard deletions**
* Avoid semantic inference or probabilistic heuristics
* Keep transformations explainable and inspectable
* Do not rely on global state

---

## 🧩 Formatting Blocks (Special Note)

Formatting is intentionally split into multiple blocks:

* `CodeSafeFormattingBlock`
  Handles structural normalization without altering semantics
  (indentation, blank lines, trailing whitespace).

* `ParagraphFormattingBlock`
  Reconstructs paragraph structure and normalizes punctuation
  without merging unrelated lines.

When modifying formatting behavior:

* Preserve existing paragraph semantics
* Never merge lines implicitly
* Add regression tests for every edge case

Formatting regressions are considered **high risk**.

---

## 🧩 Adding or Updating a Profile

Profiles define **ordered block pipelines** and are registered at import time.

To add a profile:

1. Create a file in `src/text_curation/profiles/`
2. Construct a `Profile` instance
3. Register it explicitly
4. Add golden tests under `tests/profiles/`

Profiles **must be versioned explicitly** (e.g. `web_common:v1`)
to ensure long-term reproducibility.

---

## 📐 Coding Style

* Python ≥ 3.9
* Type hints encouraged
* Avoid unbounded or catastrophic regexes
* Prefer clarity over cleverness
* Keep functions small and testable

---

## 🔒 Redaction & Safety

When working on redaction logic:

* Always err on the side of **over-redacting**
* Never log or print raw secrets
* Ensure regexes are bounded, deterministic, and safe
* Use explicit placeholders rather than deletions

---

## 🧠 Tests You Should Add

When contributing, consider adding tests for:

* Unicode edge cases
* OCR artifacts
* Repeated boilerplate
* Mixed-language text
* Emails, URLs, tokens, and IDs
* Paragraph and list detection
* Deduplication behavior
* Regression cases for known bugs

Golden tests are preferred for profile-level validation.

---

## 📄 Commit Messages

Follow a simple convention:

```
<area>: short description
```

Examples:

* `normalization: improve unicode dash handling`
* `filtering: refine boilerplate threshold`
* `profiles: add web_common_v2 profile`

---

## 🔖 Versioning Policy

This project follows **Semantic Versioning**:

* **1.x** — bug fixes, performance improvements, new opt-in behavior
* **2.0** — breaking changes to default behavior
* Profiles are versioned independently (e.g. `web_common:v1`)
  to preserve reproducibility across releases

---

## 🤝 Pull Request Process

1. Fork the repository
2. Create a feature branch
3. Add or update tests
4. Ensure all tests pass
5. Open a PR with:

   * Clear description
   * Rationale for changes
   * Before/after examples if applicable

---

## 📬 Questions & Design Discussions

If you are unsure about an approach:

* Open an **issue**
* Start a **discussion**

Design discussions are encouraged — especially for changes that may
affect default behavior or profile semantics.

---

## 🙏 Thank You

Text data is messy — thoughtful, conservative contributions help make it usable.

Thanks for helping improve **text-curation** ❤️