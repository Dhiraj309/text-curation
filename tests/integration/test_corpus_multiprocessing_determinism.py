
from datasets import Dataset
from text_curation import CorpusPipeline

def test_corpus_pipeline_num_proc_deterministic():
    dataset = Dataset.from_dict({
        "text": [
            "Hello world",
            "Hello world",
            "Another example",
            "More text here",
        ]
    })

    pipeline_single = CorpusPipeline(
        profile="web_pretrain_v1",
        dedup="hash",
        strict_manifest=True,
        num_proc=1,
    )

    pipeline_multi = CorpusPipeline(
        profile="web_pretrain_v1",
        dedup="hash",
        strict_manifest=True,
        num_proc=2,
    )

    _, manifest_single = pipeline_single(dataset)
    _, manifest_multi = pipeline_multi(dataset)

    assert manifest_single.dataset_hash == manifest_multi.dataset_hash
    assert manifest_single.document_count == manifest_multi.document_count
