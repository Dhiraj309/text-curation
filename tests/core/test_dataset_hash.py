import pytest

from text_curation.core.dataset_hash import compute_dataset_hash


def test_dataset_hash_order_invariant():
    document_ids_a = ["c", "a", "b"]
    document_ids_b = ["b", "c", "a"]

    pipeline_hash = "pipeline123"

    hash_a = compute_dataset_hash(document_ids_a, pipeline_hash)
    hash_b = compute_dataset_hash(document_ids_b, pipeline_hash)

    assert hash_a == hash_b


def test_dataset_hash_changes_with_pipeline_hash():
    document_ids = ["a", "b", "c"]

    hash1 = compute_dataset_hash(document_ids, "pipelineA")
    hash2 = compute_dataset_hash(document_ids, "pipelineB")

    assert hash1 != hash2


def test_dataset_hash_empty_documents():
    document_ids = []

    hash1 = compute_dataset_hash(document_ids, "pipelineX")
    hash2 = compute_dataset_hash(document_ids, "pipelineX")

    assert hash1 == hash2


def test_dataset_hash_invalid_document_ids_type():
    with pytest.raises(TypeError):
        compute_dataset_hash("not-a-list", "pipeline")


def test_dataset_hash_invalid_document_ids_contents():
    with pytest.raises(TypeError):
        compute_dataset_hash(["a", 123], "pipeline")


def test_dataset_hash_invalid_pipeline_hash():
    with pytest.raises(TypeError):
        compute_dataset_hash(["a", "b"], "")
