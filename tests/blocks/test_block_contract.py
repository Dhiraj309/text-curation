import pytest
from text_curation.blocks.base import Block
from text_curation.core.document import Document

class DummyBlock(Block):
    def apply(self, document):
        self._stats["calls"] = self._stats.get("calls", 0) + 1
        return document
    
def test_block_stats_reset_between_runs():
    block = DummyBlock()
    doc = Document("hello")

    block.reset_stats()
    block.apply(doc)
    assert block.get_stats()["calls"] == 1

    block.reset_stats()
    block.apply(doc)
    assert block.get_stats()["calls"] == 1

def test_block_stats_are_read_only():
    block = DummyBlock()
    stats = block.get_stats()

    stats["evil"] = 999

    assert "evil" not in block.get_stats()