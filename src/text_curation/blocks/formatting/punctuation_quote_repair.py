import re
from text_curation.blocks.base import Block


_QUOTE_REPAIR = re.compile(r'([.!?])(["“”])([A-Za-z])')


class PunctuationQuoteRepairBlock(Block):
    """
    Repairs cases where punctuation and opening quotes collapse
    without whitespace:

        Sentence."Quote

    ->

        Sentence. "Quote

    Safety guarantees:

    - Never modifies text across newline boundaries
    - Never merges paragraphs
    - Deterministic and local
    """

    def apply(self, document):
        text = document.text

        lines = text.split("\n")
        repaired_lines = []

        for line in lines:
            repaired = _QUOTE_REPAIR.sub(r"\1 \2\3", line)
            repaired_lines.append(repaired)

        document.set_text("\n".join(repaired_lines))

        return document
