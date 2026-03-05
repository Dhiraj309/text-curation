import re

from text_curation.blocks.base import Block


# Phrase-level boilerplate patterns
BOILERPLATE_PATTERNS = [
    r"\bshare this\b",
    r"\bfollow us\b",
    r"\ball rights reserved\b",
    r"\bcopyright\b",
    r"\bprivacy policy\b",
    r"\bcookie policy\b",
    r"\bterms of service\b",
    r"\bsubscribe\b",
    r"\bsign up\b",
    r"\bnewsletter\b",
    r"\bcitation\b",
]


# Navigation patterns
_NAV_SEPARATOR = re.compile(r"\s*\|\s*")
_BREADCRUMB_SEPARATOR = re.compile(r"\s*>\s*")


class BoilerplateDetectionBlock(Block):
    """
    Detect common web boilerplate content.

    This block **does not modify text**. It only emits signals.

    Signals emitted:
        document.boilerplate_paragraphs
        document.boilerplate_ratio
    """

    DEFAULT_POLICY = {}

    def __init__(self, policy=None):
        super().__init__(policy or {})

        self._compiled = [
            re.compile(pattern, re.IGNORECASE)
            for pattern in BOILERPLATE_PATTERNS
        ]

    def apply(self, document):

        text = document.text
        lines = [line.strip() for line in text.split("\n")]

        if not lines:
            document.add_signal("document.boilerplate_paragraphs", 0)
            document.add_signal("document.boilerplate_ratio", 0.0)
            return document

        boilerplate_count = 0

        for line in lines:

            if not line:
                continue

            # Phrase-based detection
            for pattern in self._compiled:
                if pattern.search(line):
                    boilerplate_count += 1
                    break

            # Navigation menus
            if _NAV_SEPARATOR.search(line) and line.count("|") >= 2:
                boilerplate_count += 1
                continue

            # Breadcrumb navigation
            if _BREADCRUMB_SEPARATOR.search(line) and line.count(">") >= 2:
                boilerplate_count += 1
                continue

        total_lines = max(len(lines), 1)
        ratio = boilerplate_count / total_lines

        document.add_signal(
            "document.boilerplate_paragraphs",
            boilerplate_count,
        )

        document.add_signal(
            "document.boilerplate_ratio",
            round(ratio, 6),
        )

        return document
