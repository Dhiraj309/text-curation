from text_curation.core.document import Document
from text_curation.core.pipeline import Pipeline
from text_curation.blocks.base import Block

class DropBlock(Block):
    def apply(self, document):
        document.drop("test_reason")
        return document
    
class MutatingBlock(Block):
    def apply(self, document):
        return document
    

def test_document_drop_flag():
    doc = Document("hello")
    doc.drop("reason")

    assert doc.is_dropped is True
    assert doc.drop_reason == "reason"

def test_pipeline_short_circuit_on_drop():
    pipeline = Pipeline([DropBlock(), MutatingBlock()])

    doc, _ = pipeline.run_document("original", collect_report=False)

    assert doc.text == "original"
    assert doc.is_dropped is True

def test_drop_is_idempotent():
    doc = Document("text")
    doc.drop("a")
    doc.drop("b")

    assert doc.drop_reason == "a"