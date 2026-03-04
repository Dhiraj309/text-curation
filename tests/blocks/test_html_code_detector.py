from text_curation.core.document import Document
from text_curation.blocks.structure.html_code_detector import HtmlCodeDetector


def run_block(text):
    doc = Document(text)
    block = HtmlCodeDetector()
    block.apply(doc)
    return doc


def test_detects_pre_block():

    text = """
Here is code:

<pre>
def foo():
    return 1
</pre>

End.
"""

    doc = run_block(text)

    assert "html_code_regions" in doc.annotations
    assert len(doc.annotations["html_code_regions"]) == 1


def test_detects_code_tag():

    text = "<code>print('hello')</code>"

    doc = run_block(text)

    assert len(doc.annotations["html_code_regions"]) == 1


def test_detects_script_tag():

    text = "<script>console.log('hello')</script>"

    doc = run_block(text)

    assert len(doc.annotations["html_code_regions"]) == 1


def test_no_false_positive():

    text = "<p>Hello world</p>"

    doc = run_block(text)

    assert doc.annotations["html_code_regions"] == []


def test_signal_emitted():

    text = "<pre>code</pre>"

    doc = run_block(text)

    signals = {s.name: s.value for s in doc.signals}

    assert signals["document.html_code_blocks"] == 1
