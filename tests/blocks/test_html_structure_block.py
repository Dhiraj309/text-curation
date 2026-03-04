from text_curation.core.document import Document
from text_curation.blocks.formatting.html_structure import HTMLStructureBlock


def run_block(text):
    doc = Document(text)
    block = HTMLStructureBlock()
    block.apply(doc)
    return doc


def test_removes_script_tag():

    text = "<p>Hello</p><script>alert(1)</script>"

    doc = run_block(text)

    assert "<script>" not in doc.text


def test_removes_nav():

    text = "<nav>Home | About | Contact</nav><p>Article text</p>"

    doc = run_block(text)

    assert "<nav>" not in doc.text
    assert "Article text" in doc.text


def test_preserves_pre():

    text = "<pre>def foo(): pass</pre>"

    doc = run_block(text)

    assert "<pre>" in doc.text


def test_signal_emitted():

    text = "<script>test</script>"

    doc = run_block(text)

    signals = {s.name: s.value for s in doc.signals}

    assert signals["document.html_tags_removed"] == 1
