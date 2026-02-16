from datasets import Dataset
from text_curation.datasets.advanced import decontaminate

def test_decontamination_overlap():
    ds = Dataset.from_dict({
        "text": ["this is a test", "completely different"]
    })

    benchmark = {"is a", "a test"}

    augmented, report = decontaminate(
        ds,
        column="text",
        benchmark_ngrams=benchmark,
        ngram_size=2,
    )

    scores = augmented["overlap_score"]

    assert scores[0] > 0.0
    assert scores[1] == 0.0
    assert report["operation"] == "decontaminate"


def test_decontamination_deterministic():
    ds = Dataset.from_dict({
        "text": ["a b c d"]
    })

    benchmark = {"b c"}

    a1, r1 = decontaminate(
        ds,
        column="text",
        benchmark_ngrams=benchmark,
        ngram_size=2,
    )

    a2, r2 = decontaminate(
        ds,
        column="text",
        benchmark_ngrams=benchmark,
        ngram_size=2,
    )

    assert a1["overlap_score"] == a2["overlap_score"]
    assert r1 == r2