from text_curation.core.pipeline import Pipeline
from text_curation.blocks.base import Block
from text_curation.core.document import Document

class StatefulBlock(Block):
    def apply(self, document):
        self._stats["calls"] = self._stats.get("calls", 0) + 1
        return document
    
def test_blocks_are_not_shared_between_pipelines():
    block = StatefulBlock()

    pipeline1 = Pipeline([block])
    pipeline2 = Pipeline([block])

    doc = Document("hello")

    pipeline1.run_document("hello")
    pipeline2.run_document("hello")

    stats1 = pipeline1.blocks[0].get_stats()
    stats2 = pipeline2.blocks[0].get_stats()

    # Each pipeline must see only its iwn calls
    assert stats1["calls"] == 1
    assert stats2["calls"] == 1

def test_pipeline_runs_are_isolated():
    """
    Multiple runs of the same Pipeline instance must not
    leak block state across runs.
    """
    block = StatefulBlock()
    pipeline = Pipeline([block])

    pipeline.run("hello")
    pipeline.run("hello")

    stats = pipeline.blocks[0].get_stats()

    assert stats["calls"] == 1