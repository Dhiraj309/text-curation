from datasets import Dataset
from typing import Set, List, Tuple

def _extract_ngrams(text: str, n: int) -> List[str]:
    """
    Deterministically extract whitespace-tokenized n-grams
    """
    tokens = text.split()
    if len(tokens) < n:
        return []
    
    return [
        " ".join(tokens[i:i+n])
        for i in range(len(tokens) - n + 1)
    ]

def decontaminate(
        dataset: Dataset,
        *,
        column: str,
        benchmark_ngrams: Set[str],
        ngram_size: int,
        collect_reports: bool = True,
) -> Tuple[Dataset, dict]:
    """
    Deterministic n-gram overlap computation against a benchmark set.

    This function does NOT filter rows.
    It only computes and attaches an overlap_score column.

    Args:
        dataset: Hugging Face Dataset
        column: Text column name
        benchmark_ngrams: Precomputed benchmark n-gram set
        ngram_size: Size of n-grams
        collect_reports: Whether to return report

    Returns:
    Augmented dataset, optionally with report
    """

    if column not in dataset.column_names:
        raise TypeError(f"Column '{column}' not found in dataset")
    
    if not isinstance(benchmark_ngrams, set):
        raise TypeError("benchmark_ngrams must be a set")
    
    if not isinstance(ngram_size, int) or ngram_size <= 0:
        raise ValueError("ngram_size must be positive integer")
    
    total_samples = len(dataset)

    overlap_scores = []

    for value in dataset[column]:
        if not isinstance(value, str):
            raise TypeError(
                f"decontaminae expects strinf values in column '{column}'"
            )
        
        doc_ngrams = _extract_ngrams(value, ngram_size)

        if not doc_ngrams:
            overlap_scores.append(0.0)
            continue

        overlap_count = sum(
            1 for ng  in doc_ngrams if ng in benchmark_ngrams
        )

        score = overlap_count /len(doc_ngrams)
        overlap_scores.append(score)

    augmented = dataset.add_column("overlap_score", overlap_scores)

    if not collect_reports:
        return augmented
    
    report = {
        "operation": "decontaminate",
        "score": "dataset",
        "column": column,
        "ngram_size": ngram_size,
        "benchmark_size": len(benchmark_ngrams),
        "input": {
            "samples": total_samples
        },
        "determinism": {
            "order_preserving": True,
            "no_randomness": True,
        }
    }

    return augmented, report