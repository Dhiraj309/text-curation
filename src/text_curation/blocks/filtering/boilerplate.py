import re

from text_curation.blocks.base import Block


BOILERPLATE_PATTERNS = [
    r"share this",
    r"follow us",
    r"all rights reserved",
    r"privacy policy",
    r"cookie policy",
    r"terms of service",
    r"subscribe",
    r"sign up",
    r"newsletter",
    r"citation",
]


class BoilerplateDetectionBlock(Block):
    """
    Detect common web boilerplate paragraphs.

    This block does NOT modify text. It only emits signals.

    Signals:
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

        paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]

        if not paragraphs:
            document.add_signal("document.boilerplate_paragraphs", 0)
            document.add_signal("document.boilerplate_ratio", 0.0)
            return document

        boilerplate_count = 0

        for p in paragraphs:
            for pattern in self._compiled:
                if pattern.search(p):
                    boilerplate_count += 1
                    break

        ratio = boilerplate_count / len(paragraphs)

        document.add_signal(
            "document.boilerplate_paragraphs",
            boilerplate_count,
        )

        document.add_signal(
            "document.boilerplate_ratio",
            round(ratio, 6),
        )

        return document
