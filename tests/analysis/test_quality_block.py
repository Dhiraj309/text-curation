from text_curation.analysis import QualitySignalBlock
from text_curation.core.document import Document

def test_quality_signals_emitted():
    text = "This is test. This is only a test. Visit https://example.com"

    doc = Document(text)

    block = QualitySignalBlock()
    block.apply(doc)

    names = {sig.name for sig in doc.signals}

    assert "document.char_entropy" in names
    assert "document.stopword_ratio" in names
    assert "document.url_density" in names
    assert "document.repetition_score" in names
    assert "document.avg_sentence_length" in names

def test_quality_block_does_not_modify_text():
    text = "Simple text."
    doc = Document(text)

    block = QualitySignalBlock()
    block.apply(doc)

    assert doc.text == text