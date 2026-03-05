from text_curation import TextCurator


PROFILE = "web.pretrain.production_v1"


def test_code_block_preserved():

    text = """
    ```python
    def foo():
        return 1
    ```
    """
    curator = TextCurator.from_profile(PROFILE)

    result = curator({"text": [text]})

    cleaned = result["text"][0]

    assert "def foo()" in cleaned
    assert "return 1" in cleaned
