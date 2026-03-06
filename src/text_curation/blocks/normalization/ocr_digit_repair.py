
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

# Protected token classes
_URL = re.compile(r"https?://\S+")
_EMAIL = re.compile(r"\b\S+@\S+\b")
_MENTION = re.compile(r"@\w+")
_HASHTAG = re.compile(r"#\w+")


# ---------------------------------------------------------
# OCR corruption detector
# ---------------------------------------------------------

def _ocr_candidate_count(text: str) -> int:
    """
    Count likely OCR digit substitutions.

    We look for digits embedded inside alphabetic tokens,
    which is a common OCR corruption pattern.

    Example:
        Th1s, t3xt, m1stake

    Isolated identifiers like GS1 or ISO9001 should not
    trigger the repair rule unless multiple occurrences
    appear in the same document.
    """

    count = 0

    for i, c in enumerate(text):

        if c not in _OCR_MAP:
            continue

        left = text[i - 1] if i > 0 else ""
        right = text[i + 1] if i + 1 < len(text) else ""

        if left.isalpha() or right.isalpha():
            count += 1

    return count


class OCRDigitRepairBlock(Block):
    """
    Repairs OCR digit-to-letter substitutions such as:

        Th1s -> This
        t3xt -> text

    Safety rules:
    - Only repair tokens starting with letters
    - Token must contain both letters and digits
    - Do NOT modify URLs, emails, mentions, or hashtags
    - Repair only if document shows OCR corruption density
    """

    # Minimum OCR artifacts required before repair activates
    _OCR_ACTIVATION_THRESHOLD = 3

    def apply(self, document):

        text = document.text

        # -------------------------------------------------
        # Corruption density gate
        # -------------------------------------------------

        candidate_count = _ocr_candidate_count(text)

        # If corruption density is low, skip repair entirely
        if candidate_count < self._OCR_ACTIVATION_THRESHOLD:
            return document

        # -------------------------------------------------
        # Protected spans
        # -------------------------------------------------

        protected_spans = []

        for pattern in (_URL, _EMAIL, _MENTION, _HASHTAG):
            for m in pattern.finditer(text):
                protected_spans.append((m.start(), m.end()))

        def is_protected(idx):
            for s, e in protected_spans:
                if s <= idx < e:
                    return True
            return False

        repaired_tokens = 0

        def repair(match):

            nonlocal repaired_tokens

            token = match.group(0)

            # Skip tokens inside protected spans
            if is_protected(match.start()):
                return token

            # Only repair tokens that start with a letter and contain digits
            if not (token[0].isalpha() and any(c.isdigit() for c in token)):
                return token

            new = token

            for d, l in _OCR_MAP.items():
                new = new.replace(d, l)

            if new != token:
                repaired_tokens += 1

            return new

        repaired_text = _TOKEN.sub(repair, text)

        if repaired_tokens:
            document.add_signal("document.ocr_digit_repairs", repaired_tokens)

        document.set_text(repaired_text)

        return document
