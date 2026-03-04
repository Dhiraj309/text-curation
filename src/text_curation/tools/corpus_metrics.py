import string
import unicodedata
from collections import Counter

from datasets import Dataset


def _tokenize(text):
    return text.split()


def _paragraphs(text):
    return [p for p in text.split("\n\n") if p.strip()]


def _emoji_count(text):
    count = 0
    for c in text:
        if "EMOJI" in unicodedata.name(c, ""):
            count += 1
    return count


def corpus_metrics(dataset: Dataset, *, column: str = "text"):
    """
    Compute corpus-level structural metrics for observability.

    This tool is designed to detect distribution shifts introduced
    by cleaning pipelines.

    Metrics include:

    - emoji frequency
    - punctuation distribution
    - token length distribution
    - paragraph length distribution
    - unicode script distribution
    """

    if column not in dataset.column_names:
        raise ValueError(f"Column '{column}' not found in dataset")

    texts = dataset[column]

    total_chars = 0
    total_tokens = 0
    total_paragraphs = 0
    total_emoji = 0

    punctuation_counter = Counter()
    token_length_counter = Counter()
    paragraph_length_counter = Counter()
    script_counter = Counter()

    for text in texts:

        if not isinstance(text, str):
            raise TypeError("Dataset must contain string text")

        total_chars += len(text)

        tokens = _tokenize(text)
        total_tokens += len(tokens)

        for tok in tokens:
            token_length_counter[len(tok)] += 1

        paragraphs = _paragraphs(text)
        total_paragraphs += len(paragraphs)

        for p in paragraphs:
            paragraph_length_counter[len(_tokenize(p))] += 1

        total_emoji += _emoji_count(text)

        for c in text:

            if c in string.punctuation:
                punctuation_counter[c] += 1

            if c.isalpha():
                try:
                    script = unicodedata.name(c).split()[0]
                    script_counter[script] += 1
                except ValueError:
                    continue

    metrics = {
        "documents": len(texts),
        "total_chars": total_chars,
        "total_tokens": total_tokens,
        "total_paragraphs": total_paragraphs,
        "emoji_count": total_emoji,
        "punctuation_distribution": dict(punctuation_counter),
        "token_length_distribution": dict(token_length_counter),
        "paragraph_length_distribution": dict(paragraph_length_counter),
        "script_distribution": dict(script_counter),
    }

    return metrics
