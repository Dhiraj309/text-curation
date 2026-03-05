from datasets import Dataset


def filter_boilerplate_documents(
    dataset: Dataset,
    *,
    ratio_threshold: float = 0.5,
    min_boilerplate_lines: int = 2,
    collect_reports: bool = True,
):
    """
    Remove documents dominated by boilerplate content.

    Requires signals produced by BoilerplateDetectionBlock:

        document.boilerplate_lines
        document.boilerplate_ratio

    Args
    ----
    dataset : Dataset
    ratio_threshold : float
        Fraction of lines that may be boilerplate before dropping document.
    min_boilerplate_lines : int
        Minimum boilerplate lines required before filtering triggers.
    collect_reports : bool
        Whether to return filtering report.

    Returns
    -------
    Filtered Dataset (+ optional report)
    """

    required = {"document.boilerplate_lines", "document.boilerplate_ratio"}

    missing = required - set(dataset.column_names)
    if missing:
        raise ValueError(
            "Dataset missing required boilerplate signals: "
            + ", ".join(sorted(missing))
        )

    total = len(dataset)

    keep_indices = []

    for idx, row in enumerate(dataset):

        lines = row["document.boilerplate_lines"]
        ratio = row["document.boilerplate_ratio"]

        if lines >= min_boilerplate_lines and ratio >= ratio_threshold:
            continue

        keep_indices.append(idx)

    filtered = dataset.select(keep_indices)

    if not collect_reports:
        return filtered

    removed = total - len(filtered)

    report = {
        "operation": "filter_boilerplate_documents",
        "scope": "dataset",
        "policy": {
            "ratio_threshold": ratio_threshold,
            "min_boilerplate_lines": min_boilerplate_lines,
        },
        "input": {"samples": total},
        "output": {"samples": len(filtered)},
        "removed": {
            "samples": removed,
            "fraction": removed / total if total else 0.0,
        },
        "determinism": {
            "order_preserving": True,
            "no_randomness": True,
        },
    }

    return filtered, report
