from text_curation.core.document import Document
from text_curation.blocks.filtering.boilerplate import BoilerplateDetectionBlock


def run_block(text):
    doc = Document(text)
    block = BoilerplateDetectionBlock()
    block.apply(doc)
    return doc


def test_detects_boilerplate():

    text = """
Share this page

This is the article text.
"""

    doc = run_block(text)

    signals = {s.name: s.value for s in doc.signals}

    assert signals["document.boilerplate_paragraphs"] == 1


def test_ratio_computation():

    text = """
Share this page

Follow us on Twitter

Real article paragraph
"""

    doc = run_block(text)

    signals = {s.name: s.value for s in doc.signals}

    assert signals["document.boilerplate_ratio"] > 0


def test_no_boilerplate():

    text = """
This is a normal paragraph.

Another paragraph of real content.
"""

    doc = run_block(text)

    signals = {s.name: s.value for s in doc.signals}

    assert signals["document.boilerplate_paragraphs"] == 0
