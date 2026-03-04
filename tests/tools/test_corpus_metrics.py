from datasets import Dataset

from text_curation.tools.corpus_metrics import corpus_metrics


def test_basic_metrics():

    ds = Dataset.from_dict(
        {
            "text": [
                "Hello world 😊",
                "Another paragraph.\n\nSecond paragraph."
            ]
        }
    )

    metrics = corpus_metrics(ds)

    assert metrics["documents"] == 2
    assert metrics["total_tokens"] > 0
    assert metrics["total_paragraphs"] >= 1


def test_punctuation_detected():

    ds = Dataset.from_dict(
        {"text": ["Hello!!!"]}
    )

    metrics = corpus_metrics(ds)

    assert "!" in metrics["punctuation_distribution"]
