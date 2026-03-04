import re
import re
from collections import Counter

from datasets import Dataset


# Common formatting artifacts introduced by cleaning systems
ARTIFACT_PATTERNS = {
    "space_before_punctuation": re.compile(r"\s+[.,!?;:]"),
    "space_inside_quotes": re.compile(r"\"\s+|\s+\""),
    "broken_number_format": re.compile(r"\d+\s+,\s+\d+"),
    "double_space": re.compile(r" {2,}"),
    "space_before_closing_paren": re.compile(r"\s+\)"),
}


def artifact_scan(dataset: Dataset, *, column: str = "text"):
    """
    Scan dataset for common formatting artifacts.

    This tool detects artifacts typically introduced by
    preprocessing pipelines.

    Examples detected:

        "Hello , world"
        "word ."
        "10 , 000"
        "space )"

    The function returns counts of each artifact type.
    """

    if column not in dataset.column_names:
        raise ValueError(f"Column '{column}' not found in dataset")

    texts = dataset[column]

    artifact_counts = Counter()
    total_documents = 0

    for text in texts:

        if not isinstance(text, str):
            raise TypeError("Dataset must contain string text")

        total_documents += 1

        for name, pattern in ARTIFACT_PATTERNS.items():
            matches = pattern.findall(text)

            if matches:
                artifact_counts[name] += len(matches)

    return {
        "documents_scanned": total_documents,
        "artifact_counts": dict(artifact_counts),
    }
