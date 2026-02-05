from text_curation.core.document import Document
from text_curation.core.signals import Signal

def test_document_summarize_signals():
    doc = Document("hello")

    doc.signals.append(Signal("line[0].is_header", True))
    doc.signals.append(Signal("line[1].is_header", True))
    doc.signals.append(Signal("paragraph[0].is_list_block", True))

    summary = doc.summarize_signals()

    assert summary["is_header"] == 2
    assert summary["is_list_block"] == 1