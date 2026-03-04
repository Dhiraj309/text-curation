from text_curation.core.document import Document
from text_curation.analysis.extended_quality import ExtendedQualityBlock


def run_block(text):
    doc = Document(text)
    block = ExtendedQualityBlock()
    block.apply(doc)
    return doc


def test_uppercase_ratio():

    doc = run_block("HELLO world")

    signals = {s.name: s.value for s in doc.signals}

    assert signals["document.uppercase_ratio"] > 0


def test_symbol_ratio():

    doc = run_block("$$$ hello")

    signals = {s.name: s.value for s in doc.signals}

    assert signals["document.symbol_ratio"] > 0


def test_punctuation_density():

    doc = run_block("Hello!!!")

    signals = {s.name: s.value for s in doc.signals}

    assert signals["document.punctuation_density"] > 0


def test_script_distribution():

    doc = run_block("Hello мир")

    signals = {s.name: s.value for s in doc.signals}

    assert "document.script_distribution" in signals


def test_entropy_emitted():

    doc = run_block("Hello world")

    signals = {s.name: s.value for s in doc.signals}

    assert "document.language_entropy" in signals
