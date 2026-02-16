from text_curation.analysis import TokenStatsBlock
from text_curation.core.document import Document

def test_token_stats_basic():
    text = "a b c a"
    doc = Document(text)

    block = TokenStatsBlock()
    block.apply(doc)

    values = {sig.name: sig.value for sig in doc.signals}

    assert values["document.token_count"] == 4
    assert values["document.unique_token_count"] == 3
    assert values["document.rare_token_ratio"] == 0.5
    assert values["document.max_token_length"] == 1

def test_token_stats_empty():
    doc = Document("")
    block = TokenStatsBlock()
    block.apply(doc)

    values = {sig.name: sig.value for sig in doc.signals}

    assert values["document.token_count"] == 0
    assert values["document.unique_token_count"] == 0
    assert values["document.rare_token_ratio"] == 0
    assert values["document.max_token_length"] == 0

def test_token_stats_does_not_modify_text():
    text = "keep intact"
    doc = Document(text)

    block = TokenStatsBlock()
    block.apply(doc)

    assert doc.text == text