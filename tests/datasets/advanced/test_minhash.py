from datasets import Dataset
from text_curation.datasets.advanced import minhash_deduplicate

def test_minhash_basic():
    ds = Dataset.from_dict({
        "text": [
            "this is a test",
            "this is a test",
            "completeky different text",
        ]
    })

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
    ds = Dataset.from_dict({
        "text": ["a b c d", "a b c d"]
    })

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

    assert d1["text"] == d2["text"]
    assert r1 == r2