import re
from datasets import Dataset


_PIPE_SPLIT = re.compile(r"\s*\|\s*")


def _is_pipe_navigation(line: str) -> bool:
    """
    Detect navigation menus like:

    Home | About | Contact | Privacy Policy
    """

    if "|" not in line:
        return False

    segments = _PIPE_SPLIT.split(line.strip())

    if len(segments) < 3:
        return False

    # each segment should be short
    for seg in segments:
        if len(seg.split()) > 4:
            return False

    return True


def boilerplate_filter(
    dataset: Dataset,
    *,
    column: str,
    collect_reports: bool = True,
):
    """
    Remove common web boilerplate lines.

    Currently handles:
    - pipe navigation menus

    This is intentionally conservative.
    """

    if column not in dataset.column_names:
        raise ValueError(f"Column '{column}' not found in dataset")

    texts = dataset[column]

    total_samples = len(texts)

    keep_indices = []

    removed = 0

    for idx, text in enumerate(texts):

        if not isinstance(text, str):
            raise TypeError("boilerplate_filter expects string values")

        lines = text.split("\n")

        cleaned_lines = []

        for line in lines:

            if _is_pipe_navigation(line):
                removed += 1
                continue

            cleaned_lines.append(line)

        cleaned = "\n".join(cleaned_lines)

        if cleaned.strip():
            keep_indices.append(idx)

    filtered = dataset.select(keep_indices)

    if not collect_reports:
        return filtered

    report = {
        "operation": "boilerplate_filter",
        "input_samples": total_samples,
        "output_samples": len(keep_indices),
        "lines_removed": removed,
        "patterns": ["pipe_navigation"],
        "determinism": {
            "order_preserving": True,
            "no_randomness": True,
        },
    }

    return filtered, report
