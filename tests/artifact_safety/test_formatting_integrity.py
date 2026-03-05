from text_curation.curator import TextCurator
from text_curation.registry import get_profile


PROFILE = "web.pretrain.production_v1"


def run(text):
    curator = TextCurator.from_profile(PROFILE)
    result = curator({"text": [text]})
    return result["text"][0]


def test_colon_spacing_preserved():
    text = "Matthew 25:23More text follows."
    cleaned = run(text)

    assert "25:23More" in cleaned


def test_paragraph_boundary_preserved():
    text = "Sentence ends here.\n\n\"Quote begins new paragraph.\""
    cleaned = run(text)

    parts = cleaned.split("\n\n")
    assert len(parts) == 2
    assert parts[1].startswith('"')


def test_unicode_dash_preserved():
    text = "— Defense Secretary"
    cleaned = run(text)

    assert "—" in cleaned


def test_ellipsis_repair():
    text = "Wait..... what happened?"
    cleaned = run(text)

    assert "…" in cleaned


def test_markdown_fence_preserved():
    text = """Here is code:

```python
print("hello")
```"""
    cleaned = run(text)

    assert "```python" in cleaned
    assert "```" in cleaned
