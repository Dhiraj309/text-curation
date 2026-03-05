import re
from text_curation.blocks.base import Block


class PunctuationQuoteRepairBlock(Block):
    """
    Repair spacing artifacts introduced by punctuation normalization.

    Example:
        "Hello world, " → "Hello world,"

    This block is intentionally minimal and deterministic.
    """

    def apply(self, document):

        text = document.text

        # remove space between punctuation and closing quotes
        text = re.sub(r'([.,!?])\s+"', r'\1"', text)

        text = re.sub(r"([.,!?])\s+'", r"\1'", text)

        document.set_text(text)

        return document
