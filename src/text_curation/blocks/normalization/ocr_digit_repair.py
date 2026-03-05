
import re
from text_curation.blocks.base import Block


_OCR_MAP = {
    "0": "o",
    "1": "i",
    "3": "e",
    "4": "a",
    "5": "s",
    "7": "t",
}


_TOKEN = re.compile(r"\b[A-Za-z0-9]+\b")


class OCRDigitRepairBlock(Block):
    """
    Repairs OCR digit-to-letter substitutions such as:

    Th1s -> This
    t3xt -> text

    Only applied to tokens that contain both letters and digits,
    avoiding modification of real numbers.
    """

    def apply(self, document):

        text = document.text

        repaired_tokens = 0

        def repair(match):

            token = match.group(0)

            # Only repair tokens that begin with a letter and contain digits
            if not (token[0].isalpha() and any(c.isdigit() for c in token)):
                return token

            new = token

            for d, l in _OCR_MAP.items():
                new = new.replace(d, l)

            nonlocal repaired_tokens
            if new != token:
                repaired_tokens += 1

            return new

        repaired_text = _TOKEN.sub(repair, text)

        if repaired_tokens:
            document.add_signal("document.ocr_digit_repairs", repaired_tokens)

        document.set_text(repaired_text)

        return document
