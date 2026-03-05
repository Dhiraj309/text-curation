import difflib
from typing import Iterable, List, Dict


def inspect_diffs(
    raw_texts: Iterable[str],
    cleaned_texts: Iterable[str],
    max_examples: int = 20,
) -> List[Dict]:
    """
    Produce human-readable diffs between raw and cleaned text.

    This tool is intended for debugging corpus preprocessing pipelines.
    It does not modify data.

    Parameters
    ----------
    raw_texts : Iterable[str]
    cleaned_texts : Iterable[str]
    max_examples : int

    Returns
    -------
    List[Dict]
        Each entry contains raw text, cleaned text, and a unified diff.
    """

    results = []

    for raw, cleaned in zip(raw_texts, cleaned_texts):

        if raw == cleaned:
            continue

        diff = "\n".join(
            difflib.unified_diff(
                raw.splitlines(),
                cleaned.splitlines(),
                fromfile="raw",
                tofile="cleaned",
                lineterm="",
            )
        )

        results.append(
            {
                "raw": raw,
                "cleaned": cleaned,
                "diff": diff,
            }
        )

        if len(results) >= max_examples:
            break

    return results
