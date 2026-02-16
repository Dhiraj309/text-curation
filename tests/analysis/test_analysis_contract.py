from text_curation.analysis import AnalysisBlock
from text_curation.core.document import Document

class DummyAnalysis(AnalysisBlock):
    def apply(slef, document):
        document.add_signal("dummy.signal", True)

        return document
    
def test_analysis_block_does_not_modify_text():
    doc = Document("original text")

    block = DummyAnalysis()
    out = block.apply(doc)

    assert out.text == "original text"
    assert len(out.signals) == 1
    assert out.signals[0].name == "dummy.signal"