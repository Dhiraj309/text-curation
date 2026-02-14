import hashlib
from collections import defaultdict
from datasets import Dataset

def _sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def deduplicate_by_hash(
        dataset: Dataset,
        *,
        column: str,
        keep: str = "first",
        collect_reports: bool = True,
        ):
    """
    Deterministic dataset-level deduplication using SHA-256 hasing.

    Args:
        dataset: Hugging Face Dataset
        column: Column containing string text
        keep: "first" or "last"
        collect_reports: Whether to return report

    Returns:
        Deduplicated dataset, optionally with report.
    """

    if keep not in {"first", "last"}:
        raise ValueError("keep mus be eihter 'first' or 'last'")
    
    if column not in dataset.column_names:
        raise ValueError(f"Column '{column}' not found in dataset")
    
    texts = dataset[column]
    total_samples = len(texts)

    grouped = defaultdict(list)

    for idx, value in enumerate(texts):
        if not isinstance(value, str):
            raise TypeError(
                f"deduplicated_by_hash expects string values in column '{column}"
            )
        
        digest = _sha256(value)
        grouped[digest].append(idx)

    keep_indices = []
    deduplicate_groups = 0
    max_group_size = 1

    for indices in grouped.values():
        if len(indices) > 1:
            duplicate_groups += 1
            max_group_size = max(max_group_size, len(indices))

        keep_idx = indices[0] if keep == "first" else indices[-1]
        keep_indices.append(keep_idx)

    keep_indices.sort()

    dedup_dataset = dataset.select(keep_indices)

    if not collect_reports:
        return dedup_dataset
    
    removed_samples = total_samples - len(dedup_dataset)

    report = {
        "operation": "deduplicate_by_hash",
        "scope": "dataset",
        "column": column,
        "strategy": {
            "type": "sha256",
            "normalization": None,
        },
        "policy": {
            "keep": keep,
        },
        "input": {
            "samples": total_samples,
        },
        "outputs": {
            "samples": len(keep_indices),
        },
        "removed": {
            "samples": removed_samples,
            "fration": removed_samples / total_samples if total_samples else 0.0,
        },
        "duplicate": {
            "groups": duplicate_groups,
            "max_group_size": max_group_size,
        },
        "determinism": {
            "order_independent_grouping": True,
            "selection_order_dependent": True,
        },
    }

    return dedup_dataset, report