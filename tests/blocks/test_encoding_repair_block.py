from text_curation.core.document import Document
from text_curation.blocks.normalization.encoding_repair import EncodingRepairBlock


def run_block(text):
    doc = Document(text)
    block = EncodingRepairBlock()
    block.apply(doc)
    return doc


def test_mojibake_repair():
    doc = run_block("FranÃ§ais")

    assert "Français" in doc.text


def test_no_change_for_clean_text():
    doc = run_block("Hello world")

    assert doc.text == "Hello world"


def test_signal_emitted():
    doc = run_block("cafÃ©")

    signals = {s.name: s.value for s in doc.signals}

    assert "document.encoding_repair_count" in signals


def test_unicode_preserved():
    doc = run_block("Hello 😊")

    assert "😊" in doc.text
