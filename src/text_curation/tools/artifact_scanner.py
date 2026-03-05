import re
from collections import Counter


# Existing artifact detectors
SPACE_BEFORE_PUNCT = re.compile(r"\s+[,.!?;:]")
BROKEN_NUMBER = re.compile(r"\d+\s+,\s+\d+")

# Extended detectors
MERGED_QUOTE = re.compile(r'[.!?]"[A-Za-z]')
COLON_SPACING = re.compile(r"\d+:\s+\d+")
UNICODE_DASH_LOSS = re.compile(r" - ")
ELLIPSIS_OVERFLOW = re.compile(r"\.{4,}")
NEWLINE_COLLAPSE = re.compile(r'[.!?]"?\n"[A-Za-z]')


def _extract_texts(data):
    """
    Normalize supported inputs into iterable[str].
    Supports HuggingFace Dataset or iterable[str].
    """

    if hasattr(data, "column_names") and "text" in data.column_names:
        return data["text"]

    return data


def scan_artifacts(data):
    """
    Return flat artifact metrics.
    Used by internal tools and extended tests.
    """

    texts = _extract_texts(data)

    counts = Counter()

    for text in texts:

        if not isinstance(text, str):
            continue

        counts["space_before_punctuation"] += len(SPACE_BEFORE_PUNCT.findall(text))
        counts["broken_number_format"] += len(BROKEN_NUMBER.findall(text))
        counts["merged_quotes"] += len(MERGED_QUOTE.findall(text))
        counts["colon_spacing_changes"] += len(COLON_SPACING.findall(text))
        counts["unicode_dash_replacement"] += len(UNICODE_DASH_LOSS.findall(text))
        counts["ellipsis_overflow"] += len(ELLIPSIS_OVERFLOW.findall(text))
        counts["newline_quote_pattern"] += len(NEWLINE_COLLAPSE.findall(text))

    return dict(counts)


# ------------------------------------------------
# Backward compatibility API
# ------------------------------------------------

def artifact_scan(data):
    """
    Legacy API expected by existing tests.
    """

    counts = scan_artifacts(data)

    # remove zero entries
    counts = {k: v for k, v in counts.items() if v > 0}

    return {"artifact_counts": counts}
