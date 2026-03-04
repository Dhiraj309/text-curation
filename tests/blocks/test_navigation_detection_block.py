from text_curation.core.document import Document
from text_curation.blocks.filtering.navigation import NavigationDetectionBlock


def run_block(text):
    doc = Document(text)
    block = NavigationDetectionBlock()
    block.apply(doc)
    return doc


def test_detects_navigation_cluster():

    text = "Home | About | Contact | Privacy"

    doc = run_block(text)

    signals = {s.name: s.value for s in doc.signals}

    assert signals["document.navigation_lines"] == 1


def test_detects_navigation_word():

    text = "Login"

    doc = run_block(text)

    signals = {s.name: s.value for s in doc.signals}

    assert signals["document.navigation_lines"] == 1


def test_ratio_computation():

    text = """
Home | About | Contact

Real article paragraph here.
"""

    doc = run_block(text)

    signals = {s.name: s.value for s in doc.signals}

    assert signals["document.navigation_ratio"] > 0


def test_no_navigation():

    text = """
This is a real paragraph.

Another paragraph of text.
"""

    doc = run_block(text)

    signals = {s.name: s.value for s in doc.signals}

    assert signals["document.navigation_lines"] == 0
