from datasets import Dataset
def filter_rows(
        dataset: Dataset,
        *,
        predicate,
        description: str,
        collect_reports: bool = True
    ):
    """
    Filter rows from a Hugging Face Dataset using an explicit predicate.

    Rows for which predicate(row) returns False are removed.

    This operation is deterministic, order-preserving, and
    does not modify sample contents.

    Args:
        dataset: Hugging Face Dataset
        predicate: Callable taking a row dict -> bool
        description: Human-readable description of the filtering intent
        collect_report: Whether to return a filtering report

    Returns:
        Filtered Dataset, and optionally a filtering report.
    """

    if not callable(predicate):
        raise TypeError("predicate must be callable")

    if not isinstance(description, str) or not description.strip():
        raise ValueError("description must be non empty string")

    total_samples = len(dataset)

    filtered = dataset.filter(predicate)

    if not collect_reports:
        return filtered

    remaining = len(filtered)
    removed = total_samples - remaining

    report = {
        "operation": "filter_rows",
        "scope": "dataset",

        "description": description,

        "input": {
            "samples": total_samples,
        },

        "output": {
            "samples": remaining,
        },

        "removed": {
            "samples": removed,
            "fraction": removed / total_samples if total_samples else 0.0,
        },

        "determinism": {
            "predicate_assumed_pure": True,
        },

        "provenance": {
            "library": "text-curation",
            "operation_version": "filter_rows_v1",
        },
    }

    return filtered, report
