import pytest
from datasets import Dataset

from text_curation.datasets.advanced.minhash import minhash_deduplicate


def _make_dataset(texts, document_ids):
    return Dataset.from_dict({
        "text": texts,
        "document_id": document_ids,
    })


def test_minhash_keeps_lowest_document_id():
    dataset = _make_dataset(
        texts=[
            "alpha beta gamma",
            "alpha beta gamma",
        ],
        document_ids=[
            "b_id",
            "a_id",  # lexicographically smaller
        ],
    )

    deduped, _ = minhash_deduplicate(
        dataset,
        column="text",
        ngram_size=1,
        num_hashes=8,
        threshold=1.0,
        seed=42,
    )

    assert len(deduped) == 1
    assert deduped["document_id"][0] == "a_id"


def test_minhash_order_invariant():
    dataset_a = _make_dataset(
        texts=[
            "repeat me",
            "repeat me",
        ],
        document_ids=[
            "z_id",
            "a_id",
        ],
    )

    dataset_b = _make_dataset(
        texts=[
            "repeat me",
            "repeat me",
        ],
        document_ids=[
            "a_id",
            "z_id",
        ],
    )

    deduped_a, _ = minhash_deduplicate(
        dataset_a,
        column="text",
        ngram_size=1,
        num_hashes=8,
        threshold=1.0,
        seed=123,
    )

    deduped_b, _ = minhash_deduplicate(
        dataset_b,
        column="text",
        ngram_size=1,
        num_hashes=8,
        threshold=1.0,
        seed=123,
    )

    # Canonical representative must be identical
    assert deduped_a["document_id"] == deduped_b["document_id"]


def test_minhash_requires_document_id():
    dataset = Dataset.from_dict({
        "text": ["a", "a"]
    })

    with pytest.raises(ValueError):
        minhash_deduplicate(
            dataset,
            column="text",
            ngram_size=1,
            num_hashes=8,
            threshold=1.0,
            seed=0,
        )
