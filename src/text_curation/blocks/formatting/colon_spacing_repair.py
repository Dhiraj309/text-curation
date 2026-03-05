import re
from text_curation.blocks.base import Block


# Match patterns like:
# 25:23More → insert space
# but avoid timestamps like 12:45PM
_PATTERN = re.compile(r"(\d+:\d+)([A-Za-z][a-z])")


class ColonSpacingRepairBlock(Block):
    """
    Repairs missing space after numeric colon references.

    Example
    -------
    25:23More → 25:23 More

    This commonly occurs in scripture references or OCR text
    where whitespace between the reference and the next word
    was accidentally removed.

    The rule intentionally avoids timestamps like:
    12:45PM
    """

    def apply(self, document):

        text = document.text

        repaired = _PATTERN.sub(r"\1 \2", text)

        if repaired != text:
            document.add_signal("document.colon_spacing_repair", True)

        document.set_text(repaired)

        return document
