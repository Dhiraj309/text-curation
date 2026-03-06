import json

from text_curation import TextCurator
from text_curation.registry import get_profile


PROFILE_ID = "web.pretrain.production_v1"


def run_pipeline(text):
    curator = TextCurator.from_profile(
        PROFILE_ID,
        collect_reports=True,
    )

    result = curator({"text": [text]})
    return result["text"][0], json.loads(result["curation_report"][0])


# -----------------------------------------------------
# ZWS behavior
# -----------------------------------------------------

def test_zero_width_space_repair():
    raw = "hello\u200bworld"

    cleaned, report = run_pipeline(raw)

    # Should not fuse tokens
    assert "helloworld" not in cleaned


# -----------------------------------------------------
# Ellipsis normalization
# -----------------------------------------------------

def test_ellipsis_normalization():
    raw = "Wait..... what?"

    cleaned, report = run_pipeline(raw)

    # ensure ellipsis preserved or normalized
    assert "..." in cleaned or "…" in cleaned


# -----------------------------------------------------
# OCR corruption guard
# -----------------------------------------------------

def test_ocr_does_not_corrupt_clean_identifiers():
    raw = "The GS1 standard defines barcode formats."

    cleaned, report = run_pipeline(raw)

    assert "GSi" not in cleaned


# -----------------------------------------------------
# Code block preservation
# -----------------------------------------------------

def test_code_block_integrity():
    raw = """Example:

```python
print("hello")
```"""

    cleaned, report = run_pipeline(raw)

    assert "```python" in cleaned
    assert "print(\"hello\")" in cleaned


# -----------------------------------------------------
# SEO pipe spam detection (baseline)
# -----------------------------------------------------

def test_pipe_spam_detection():
    raw = (
        "Essay Writing Help|Research Paper Help|Cheap Essays|Order Essay"
    )

    cleaned, report = run_pipeline(raw)

    # baseline pipeline may not remove yet,
    # but we verify pipeline does not crash
    assert isinstance(cleaned, str)
