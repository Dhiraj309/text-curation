# Contributing to text-curation

First off, thank you for considering contributing to **text-curation** 🙌
This project aims to provide **production-grade text cleaning, normalization, redaction, structure detection, filtering, and deduplication** for real-world, messy text data.

Contributions of all kinds are welcome — bug fixes, new blocks, tests, documentation, or performance improvements.

---

## 🧭 Project Philosophy

This library is built with the following principles in mind:

* **Conservative by default**
  Avoid destructive transformations unless explicitly requested.

* **Structure-aware**
  Text is not just strings — paragraphs, lists, headers, and boilerplate matter.

* **Pipeline-first design**
  Each block should do one thing well and be composable.

* **Real-world robustness**
  Code should handle OCR junk, web boilerplate, emails, scanned text, forums, and scraped content.

* **Test-driven evolution**
  Every new behavior should be covered by tests.

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
```

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Dhiraj309/text-curation.git
cd text-curation
```

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
* ✅ New functionality must include tests

---

## 🧩 Adding a New Block

To add a new block:

1. Create a file in `src/text_curation/_blocks/`
2. Implement an `apply(self, document)` method
3. Add tests under `tests/blocks/`
4. (Optional) Add it to a pipeline profile

### Block guidelines

* Blocks **must not mutate text silently**
* Prefer **signals over hard deletions**
* Keep transformations explainable and reversible where possible

---

## 📐 Coding Style

* Python ≥ 3.9
* Type hints encouraged
* Avoid unnecessary regex complexity
* Prefer readability over cleverness
* Keep functions small and testable

---

## 🔒 Redaction & Safety

When working on redaction:

* Always err on the side of **over-redacting**
* Never log or print raw secrets
* Ensure regexes are safe and bounded

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

---

## 📄 Commit Messages

Follow a simple convention:

```
block: short description
```

Examples:

* `normalization: improve unicode dash handling`
* `filtering: drop repeated boilerplate paragraphs`
* `dedupe: add paragraph-level exact deduplication`

---

## 🔖 Versioning

This project follows **Semantic Versioning**:

* `0.1.x` — bug fixes, conservative improvements
* `0.2.x` — new blocks or opt-in behavior
* `1.0.0` — stable API guarantees

---

## 🤝 Pull Request Process

1. Fork the repo
2. Create a feature branch
3. Add tests
4. Ensure all tests pass
5. Open a PR with:

   * Clear description
   * Before/after examples if applicable

---

## 📬 Questions & Ideas

If you’re unsure about an approach:

* Open an **issue**
* Or start a **discussion**

Thoughtful questions and design discussions are welcome.

---

## 🙏 Thank You

Text data is messy — your contribution helps make it usable.

Thanks for helping improve **text-curation** ❤️