import re
from text_curation.blocks.base import Block


# Example match:
# 25:23More → insert space
_PATTERN = re.compile(r"(\d+:\d+)([A-Za-z])")


class ColonSpacingRepairBlock(Block):
    """
    Repairs missing space after numeric colon references.

    Example
    -------
    25:23More → 25:23 More

    This commonly occurs in scripture references, timestamps,
    and OCR text where whitespace was dropped.
    """

    def apply(self, document):

        text = document.text

        repaired = _PATTERN.sub(r"\1 \2", text)

        if repaired != text:
            document.add_signal("document.colon_spacing_repair", True)

        document.set_text(repaired)

        return document
