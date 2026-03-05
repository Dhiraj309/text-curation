from text_curation.curator import TextCurator
from text_curation.registry import get_profile


PROFILE = "web.pretrain.production_v1"


def test_markdown_code_fence_preserved():

    text = """Here is code:
    ```python
    print("hello")
    ```"""

    curator = TextCurator.from_profile(PROFILE)

    result = curator({"text": [text]})
    cleaned = result["text"][0]

    assert "```python" in cleaned
    assert "```" in cleaned
