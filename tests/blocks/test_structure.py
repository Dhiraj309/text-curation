"""
Tests for structure and repetition signal emission.

StructureBlock emits signals only — it never mutates text.
"""

from text_curation.core.document import Document
from text_curation.blocks.structure.basic import BasicStructureBlock

def get_signal(doc, name):
    return [s.value for s in doc.signals if s.name == name]

def analyze(text):
    doc = Document(text)
    BasicStructureBlock().apply(doc)
    return doc

def test_header_detection():
    doc = analyze('### Title ###')
    assert True in get_signal(doc, "line[0].is_header")

def test_bullet_detection():
    doc = analyze("- a\n- b")
    assert True in get_signal(doc, "line[0].is_bullet")
    assert True in get_signal(doc, "line[1].is_bullet")

def test_repetition_detection():
    doc = analyze("A\nA\nA")
    assert 3 in get_signal(doc, "line[0].repetition_count")

def test_list_block_detection():
    doc = analyze("- a\n- b\n -c")
    assert True in get_signal(doc, "paragraph[0].is_list_block")

def test_boilerplate_candidate():
    doc = analyze("FOOTER\n\nFOOTER")
    assert True in get_signal(doc, "paragraph[0].is_boilerplate_candidate")