from text_curation.tools.chunking import chunk_text


def test_basic_chunking():

    text = "Sentence one. Sentence two. Sentence three."

    chunks = chunk_text(text, max_tokens=3)

    assert len(chunks) >= 1


def test_respects_sentence_boundary():

    text = "Hello world. This is a test."

    chunks = chunk_text(text, max_tokens=10)

    assert "Hello world." in chunks[0]


def test_long_sentence_split():

    text = " ".join(["word"] * 100)

    chunks = chunk_text(text, max_tokens=20)

    assert len(chunks) >= 5


def test_invalid_input():

    try:
        chunk_text(123)
        assert False
    except TypeError:
        assert True
