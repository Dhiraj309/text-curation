from collections import defaultdict
from datasets import Dataset


def deduplicate_exact(
        dataset: Dataset,
        *,
        column: str,
        keep: str = "first",
        collect_reports: bool = True,
    ):
    """
    Remove exact duplicate samples from a Hugging Face Dataset.

    Deduplication is performed at the dataset level using exact
    string matching on the specified column.

    The operation is deterministic, order-independent, and does
    not perform normalization or semantic matching.

    Args:
        dataset: Hugging Face Dataset
        column: Column name to deduplicate on (must contain strings)
        keep: Which duplicate to retain ("first" or "last")
        collect_reports: Whether to return a deduplication report

    Returns:
        Deduplicated Dataset, and optionally a deduplication report.
    """

    if keep not in {"first", "last"}:
        raise ValueError("keep must be either 'first' or 'last'")

    if column not in dataset.column_names:
        raise ValueError(f"Column '{column}' not found in dataset")

    texts = dataset[column]
    total_samples = len(texts)

    grouped = defaultdict(list)

    for idx, value in enumerate(texts):
        if not isinstance(value, str):
            raise TypeError(
                f"deduplicate_exact expects string values in column '{column}'"
            )
        grouped[value].append(idx)

    keep_indices = []
    duplicate_groups = 0
    max_group_size = 1

    for indices in grouped.values():
        if len(indices) > 1:
            duplicate_groups += 1
            max_group_size = max(max_group_size, len(indices))

        keep_idx = indices[0] if keep == "first" else indices[-1]
        keep_indices.append(keep_idx)

    keep_indices.sort()

    dedupe_dataset = dataset.select(keep_indices)

    if not collect_reports:
        return dedupe_dataset

    removed_samples = total_samples - len(dedupe_dataset)

    report = {
        "operation": "deduplicate_exact",
        "scope": "dataset",

        "column": column,

        "strategy": {
            "type": "exact",
            "normalization": None,
        },

        "policy": {
            "keep": keep,
        },

        "input": {
            "samples": total_samples,
        },

        "output": {
            "samples": len(keep_indices),
        },

        "removed": {
            "samples": removed_samples,
            "fraction": removed_samples / total_samples if total_samples else 0.0,
        },

        "duplicates": {
            "groups": duplicate_groups,
            "max_group_size": max_group_size,
        },

        "determinism": {
            "order_independent": False,
            "selection_strategy": keep,
        },
    }

    return dedupe_dataset, report
