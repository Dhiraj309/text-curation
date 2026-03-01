from datasets import Dataset
from text_curation.datasets.advanced import minhash_deduplicate


def _make_dataset(texts):
    """
    Helper to attach deterministic document_id column.
    Using stable string IDs avoids index-based ambiguity.
    """
    return Dataset.from_dict({
        "text": texts,
        "document_id": [str(i) for i in range(len(texts))],
    })


def test_minhash_basic():
    ds = _make_dataset([
        "this is a test",
        "this is a test",
        "completeky different text",
    ])

    deduped, report = minhash_deduplicate(
        ds,
        column="text",
        ngram_size=2,
        num_hashes=10,
        threshold=0.8,
        seed=42,
    )

    assert len(deduped) == 2
    assert report["clusters"]["count"] == 1


def test_mismatch_deterministic():
    ds = _make_dataset([
        "a b c d",
        "a b c d",
    ])

    d1, r1 = minhash_deduplicate(
        ds,
        column="text",
        ngram_size=2,
        num_hashes=5,
        threshold=0.9,
        seed=123,
    )

    d2, r2 = minhash_deduplicate(
        ds,
        column="text",
        ngram_size=2,
        num_hashes=5,
        threshold=0.9,
        seed=123,
    )

    # Representative should be canonical (lowest document_id)
    assert d1["document_id"] == d2["document_id"]
    assert d1["text"] == d2["text"]
    assert r1 == r2
