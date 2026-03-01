import pytest
from datasets import Dataset

from text_curation.datasets.advanced.hash_dedup_streaming import (
    deduplicate_by_document_id,
)


def _make_dataset(texts, document_ids):
    return Dataset.from_dict({
        "text": texts,
        "document_id": document_ids,
    })


def test_deduplicate_by_document_id_basic():
    dataset = _make_dataset(
        texts=["a", "b", "c", "dup1", "dup2"],
        document_ids=["1", "2", "3", "X", "X"],
    )

    deduped, report = deduplicate_by_document_id(dataset)

    assert len(deduped) == 4
    assert report["duplicates"]["groups"] == 1
    assert report["removed"]["samples"] == 1


def test_deduplicate_by_document_id_order_invariant():
    dataset_a = _make_dataset(
        texts=["a", "b", "dup1", "dup2"],
        document_ids=["1", "2", "X", "X"],
    )

    dataset_b = _make_dataset(
        texts=["dup2", "a", "dup1", "b"],
        document_ids=["X", "1", "X", "2"],
    )

    deduped_a, _ = deduplicate_by_document_id(dataset_a)
    deduped_b, _ = deduplicate_by_document_id(dataset_b)

    # Compare document_id sets
    assert set(deduped_a["document_id"]) == set(deduped_b["document_id"])


def test_deduplicate_by_document_id_keeps_lowest_index_per_id():
    dataset = _make_dataset(
        texts=["first", "second"],
        document_ids=["X", "X"],
    )

    deduped, _ = deduplicate_by_document_id(dataset)

    # Representative should be first occurrence
    assert deduped["text"][0] == "first"
    assert len(deduped) == 1


def test_deduplicate_by_document_id_missing_column():
    dataset = Dataset.from_dict({"text": ["a", "b"]})

    with pytest.raises(ValueError):
        deduplicate_by_document_id(dataset)


def test_deduplicate_by_document_id_invalid_type():
    dataset = Dataset.from_dict({
        "text": ["a", "b"],
        "document_id": [1, 2],
    })

    with pytest.raises(TypeError):
        deduplicate_by_document_id(dataset)
