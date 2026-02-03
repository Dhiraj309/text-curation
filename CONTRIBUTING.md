# Contributing to text-curation

Thank you for considering contributing to text-curation 🙌

This project exists to provide deterministic, structure-aware, production-grade text curation for large-scale NLP datasets. The goal is not clever cleaning — it is reproducible, auditable data preprocessing.

Contributions are welcome across code, tests, documentation, performance improvements, and new profiles.


---

🧭 Project Philosophy

This library is built around a few non-negotiable principles:

Conservative by default
Avoid destructive transformations unless they are explicit, versioned, and intentional.

Deterministic behavior
Given the same input text and the same profile, the output must be stable and reproducible.

Structure-aware processing
Text is not just strings. Paragraphs, lists, headers, repetition, and boilerplate matter.

Pipeline-first design
Each block does one thing, remains composable, and has a clearly defined responsibility.

Real-world robustness
Code should handle OCR artifacts, web boilerplate, emails, scanned text, forums, and scraped content without semantic assumptions.

Tests as executable specifications
Tests define and lock in behavior. They are part of the public contract.



---

🔒 Stability Contract (Read This Carefully)

As of v1.x, text-curation provides stable default behavior.

Contributors must assume:

Default block behavior is part of the public API

Changing output for existing inputs is a breaking change

Breaking changes require discussion and a major version bump


If a proposal changes behavior, it should usually be introduced as:

a new block

a new profile

an explicit opt-in policy (disabled by default)


Profiles may be deprecated, but must never be silently modified.

If you are unsure whether a change is breaking — assume that it is.


---

🧪 Stable vs Experimental Contributions

To preserve trust and reproducibility, contributions fall into two categories:

✅ Stable (preferred)

Bug fixes that do not change outputs

Performance improvements

New blocks with conservative defaults

New profiles with explicit versioning

Documentation improvements

New tests and regression coverage


⚠️ Experimental (allowed, but labeled)

New heuristics

Aggressive cleanup strategies

New profiles with evolving behavior

Dataset-level utilities under active iteration


Experimental features must be:

clearly documented as experimental

opt-in only

isolated from existing stable profiles



---

📦 Project Structure

src/text_curation/
├── blocks/
│   ├── base.py
│   ├── normalization.py
│   ├── redaction.py
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
│   ├── report.py
│   └── signals.py
├── profiles/
│   ├── base.py
│   ├── web_common_v1.py
│   └── llm_pretrain_v1.py
├── curator.py
├── registry.py
└── __init__.py

tests/
├── blocks/
├── profiles/
└── test_curation_report.py

Documentation lives under docs/ and mirrors this structure.


---

🚀 Getting Started

1️⃣ Clone the repository

git clone https://github.com/Dhiraj309/text-curation.git
cd text-curation

2️⃣ Create a virtual environment

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

3️⃣ Install dependencies

pip install -e .[dev]


---

🧪 Running Tests

We use pytest.

python -m pytest

Before submitting a PR:

✅ All tests must pass

✅ New behavior must include tests

✅ Existing tests must not change unless behavior is intentionally revised


Golden tests are used to lock in profile-level behavior.


---

🧩 Adding a New Block

To add a new block:

1. Create a file under src/text_curation/blocks/


2. Subclass Block from blocks.base


3. Implement apply(self, document)


4. Add tests under tests/blocks/


5. Optionally include it in a new profile



Block guidelines

Blocks must not silently change semantics

Prefer signals over deletions

Avoid semantic inference or probabilistic heuristics

Keep logic explainable and inspectable

Do not rely on global state


If a block grows complex, split it — do not add modes.


---

🧩 Formatting Blocks (High-Risk Area)

Formatting is intentionally split into separate responsibilities:

CodeSafeFormattingBlock
Structural normalization only (line endings, blank lines, trailing whitespace).

ParagraphFormattingBlock
Paragraph reconstruction and punctuation normalization.


When touching formatting:

Preserve existing semantics

Never merge lines implicitly

Add regression tests for every edge case


Formatting regressions are considered high risk and reviewed carefully.


---

🧩 Adding or Updating a Profile

Profiles define ordered block pipelines and are treated as behavioral contracts.

To add a profile:

1. Create a file in src/text_curation/profiles/


2. Construct a Profile instance


3. Register it explicitly


4. Add golden tests under tests/profiles/



Profiles must be explicitly versioned (e.g. web_common:v1) to ensure long-term reproducibility.


---

📐 Coding Style

Python ≥ 3.9

Type hints encouraged

Avoid unbounded or catastrophic regexes

Prefer clarity over cleverness

Keep functions small and testable



---

🔒 Redaction & Safety

When working on redaction logic:

Always err on the side of over-redaction

Never log or print raw secrets

Ensure regexes are bounded, deterministic, and safe

Use explicit placeholders rather than deletions



---

🧠 Tests You Should Add

When contributing, consider tests for:

Unicode edge cases

OCR artifacts

Repeated boilerplate

Mixed-language text

Emails, URLs, tokens, and IDs

Paragraph and list detection

Deduplication behavior

Regression cases for known bugs


Golden tests are preferred for profiles.


---

📄 Commit Messages

Use a simple, scoped format:

<area>: short description

Examples:

normalization: improve unicode dash handling

reports: add word-level statistics

profiles: add llm_pretrain_v2



---

🔖 Versioning Policy

This project follows Semantic Versioning:

1.x — bug fixes, performance improvements, new opt-in features

2.0 — breaking changes to default behavior


Profiles are versioned independently (e.g. web_common:v1) to preserve reproducibility across releases.


---

🤝 Pull Request Process

1. Fork the repository


2. Create a feature branch


3. Add or update tests


4. Ensure all tests pass


5. Open a PR with:

clear description

rationale for changes

before/after examples if applicable





---

📬 Questions & Design Discussions

If you are unsure about an approach:

Open an issue

Start a discussion


Design discussions are encouraged, especially for changes that may affect default behavior or profile semantics.


---

🙏 Thank You

Text data is messy.
Thoughtful, conservative contributions make it usable.

Thanks for helping improve text-curation ❤️
