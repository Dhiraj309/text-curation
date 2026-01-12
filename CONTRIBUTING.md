# Contributing to text-curation

First off, thank you for considering contributing to **text-curation** 🙌  
This project aims to provide **deterministic, structure-aware, production-grade text curation**
for real-world, messy text data.

Contributions of all kinds are welcome — bug fixes, new blocks, tests, documentation,
performance improvements, and new profiles.

---

## 🧭 Project Philosophy

This library is built with the following principles in mind:

* **Conservative by default**  
  Avoid destructive transformations unless explicitly requested.

* **Deterministic behavior**  
  Given the same input and profile, output must be stable and reproducible.

* **Structure-aware**  
  Text is not just strings — paragraphs, lists, headers, repetition, and boilerplate matter.

* **Pipeline-first design**  
  Each block should do one thing well and remain composable.

* **Real-world robustness**  
  Code should handle OCR junk, web boilerplate, emails, scanned text, forums,
  and scraped content without semantic assumptions.

* **Test-driven evolution**  
  Every new behavior must be covered by tests.

---

## 🔒 Stability Contract (Important)

As of **v1.0.0**, `text-curation` provides **stable default behavior**.

Contributors must assume that:

* Default block behavior is **part of the public contract**
* Changing outputs for existing inputs is a **breaking change**
* Breaking changes require explicit discussion and a major version bump

If a proposed change alters behavior, it should usually be introduced as:
- a new block
- a new profile
- an opt-in flag (not default)

---

## 📦 Project Structure

```

src/text_curation/
├── _blocks/
│   ├── normalization.py
│   ├── formatting.py
│   ├── redaction.py
│   ├── structure.py
│   ├── filtering.py
│   └── dedupe.py
├── _core/
│   ├── document.py
│   └── pipeline.py
├── profiles/
│   └── web_common_v1.py
└── curator.py

tests/
├── blocks/
├── test_datasets_map.py

````

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

---

## 🧩 Adding a New Block

To add a new block:

1. Create a file in `src/text_curation/_blocks/`
2. Implement an `apply(self, document)` method
3. Add tests under `tests/blocks/`
4. Optionally add it to a profile

### Block guidelines

* Blocks **must not mutate text silently**
* Prefer **signals over hard deletions**
* Avoid semantic inference or heuristics
* Keep transformations explainable and inspectable

---

## 📐 Coding Style

* Python ≥ 3.9
* Type hints encouraged
* Avoid unbounded or overly complex regexes
* Prefer readability over cleverness
* Keep functions small and testable

---

## 🔒 Redaction & Safety

When working on redaction:

* Always err on the side of **over-redacting**
* Never log or print raw secrets
* Ensure regexes are safe, bounded, and deterministic

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

---

## 📄 Commit Messages

Follow a simple convention:

```
block: short description
```

Examples:

* `normalization: improve unicode dash handling`
* `filtering: refine boilerplate threshold`
* `dedupe: add paragraph-level exact deduplication`

---

## 🔖 Versioning Policy

This project follows **Semantic Versioning**:

* **1.x** — bug fixes, performance improvements, new opt-in behavior
* **2.0** — breaking changes to default behavior
* Profiles are versioned explicitly (e.g. `web_common_v1`)
  to preserve reproducibility

---

## 🤝 Pull Request Process

1. Fork the repository
2. Create a feature branch
3. Add tests
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
affect default behavior.

---

## 🙏 Thank You

Text data is messy — thoughtful contributions help make it usable.

Thanks for helping improve **text-curation** ❤️
