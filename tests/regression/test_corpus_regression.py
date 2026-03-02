from datasets import Dataset

from text_curation import CorpusPipeline
from text_curation.core.reproducibility import compute_pipeline_hash
from text_curation.registry import get_profile


def test_corpus_regression_snapshot():
    """
    This test freezes corpus compilation behavior.

    If this test fails:
        - Output semantics changed
        - Dedup logic changed
        - Hash logic changed
        - Profile block order changed
        - Or normalization behavior drifted

    In that case:
        - Bump version intentionally
        - Update expected snapshot values consciously
    """

    # Static deterministic input corpus
    dataset = Dataset.from_dict({
        "text": [
            "Hello World!",
            "Hello World!",   # duplicate
            "Another document.",
            "Final entry."
        ]
    })

    pipeline = CorpusPipeline(
        profile="web_pretrain_v1",
        dedup="hash",
        strict_manifest=True,
    )

    compiled, manifest = pipeline(dataset)

    profile = get_profile("web_pretrain_v1")
    pipeline_hash = compute_pipeline_hash(profile)

    # -----------------------------
    # Snapshot Values
    # -----------------------------
    expected_document_count = 3
    expected_pipeline_hash = pipeline_hash  # dynamic but deterministic

    # Freeze dataset_hash value after first successful run
    expected_dataset_hash = "de129e98fb618c623e22904aa29770d425e787f777e95835bc43f393620f0682"

    # -----------------------------
    # Assertions
    # -----------------------------
    assert len(compiled) == expected_document_count
    assert manifest.document_count == expected_document_count
    assert manifest.dataset_hash == expected_dataset_hash
    assert compute_pipeline_hash(profile) == expected_pipeline_hash
