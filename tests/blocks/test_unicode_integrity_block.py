from text_curation.core.document import Document
from text_curation.blocks.normalization.unicode_integrity import UnicodeIntegrityBlock


def run_block(text):
    doc = Document(text)
    block = UnicodeIntegrityBlock()
    block.apply(doc)
    return doc


def test_unicode_normalization_runs():
    doc = run_block("Café")
    assert doc.text == "Café"


def test_emoji_preserved():
    doc = run_block("Hello 😊🔥")
    assert "😊" in doc.text
    assert "🔥" in doc.text


def test_replacement_character_detection():
    text = "Hello \uFFFD world"
    doc = run_block(text)

    signals = {s.name: s.value for s in doc.signals}

    assert signals["document.unicode_replacement_characters"] == 1


def test_script_distribution_emitted():
    doc = run_block("Hello мир مرحبا")

    signals = {s.name: s.value for s in doc.signals}

    assert "document.unicode_script_distribution" in signals


def test_unicode_repair_signal_present():
    doc = run_block("Cafe\u0301")  # decomposed accent form

    signals = {s.name: s.value for s in doc.signals}

    assert "document.unicode_repair_count" in signals
