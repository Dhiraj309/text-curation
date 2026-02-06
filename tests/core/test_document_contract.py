import pytest
from text_curation.core.document import Document

def test_document_text_is_read_only():
    doc = Document("hello")

    with pytest.raises(AttributeError):
        doc.text = "illegal"

def test_document_text_mutation_must_use_set_text():
    doc = Document("hello")
    doc.set_text("world")

    assert doc.text == "world"

def test_document_signals_are_append_only():
    doc = Document("hello")

    doc.add_signal("test.signal", True)
    doc.add_signal("test.signal", False)

    assert len(doc.signals) == 2
    assert doc.signals[0].value is True
    assert doc.signals[1].value is False