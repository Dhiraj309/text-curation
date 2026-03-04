from text_curation.core.document import Document
from text_curation.blocks.structure.code_fence_detector import CodeFenceDetector


def run_block(text):
    doc = Document(text)
    block = CodeFenceDetector()
    block.apply(doc)
    return doc


def test_detects_code_fence():

    text = """
    Here is some code:

    ```python
    def foo():
        return 1
    ```

    End. """

    doc = run_block(text)

    assert "code_regions" in doc.annotations
    assert len(doc.annotations["code_regions"]) == 1

def test_no_false_positive():

    text = "This is normal text."

    doc = run_block(text)

    assert doc.annotations["code_regions"] == []

def test_signal_emitted():

    text = """
~~~python
print("hello")
~~~
"""

    doc = run_block(text)

    signals = {s.name: s.value for s in doc.signals}

    assert signals["document.code_fence_blocks"] == 1
