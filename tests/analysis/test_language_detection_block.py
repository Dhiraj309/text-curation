from text_curation.core.document import Document
from text_curation.analysis.language import LanguageDetectionBlock


def run_block(text):
    doc = Document(text)
    block = LanguageDetectionBlock()
    block.apply(doc)
    return doc


def test_language_signal_emitted():

    doc = run_block("Hello world")

    signals = {s.name: s.value for s in doc.signals}

    assert "document.language" in signals


def test_language_confidence_emitted():

    doc = run_block("Hello world")

    signals = {s.name: s.value for s in doc.signals}

    assert "document.language_confidence" in signals


def test_empty_text():

    doc = run_block("")

    signals = {s.name: s.value for s in doc.signals}

    assert signals["document.language"] == "unknown"
