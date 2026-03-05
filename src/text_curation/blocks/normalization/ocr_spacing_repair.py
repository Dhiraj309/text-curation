import re
from text_curation.blocks.base import Block


# Detect OCR-style spaced letters
_OCR_PATTERN = re.compile(r"(?:\b[A-Za-z]\b\s+){3,}\b[A-Za-z]\b")

# Detect indentation (code blocks)
_INDENT = re.compile(r"^[ \t]+")


class OCRSpacingRepairBlock(Block):
    """
    Repairs OCR artifacts where words are split into characters.

    Example
    -------
    T h i s    s e n t e n c e
    → This sentence

    Safety rules
    ------------
    • Never modify indented lines (code blocks)
    • Never cross newline boundaries
    • Only repair high-confidence OCR patterns
    • Do not normalize general whitespace
    """

    def apply(self, document):

        text = document.text

        lines = text.split("\n")
        repaired_lines = []
        repaired = False

        for line in lines:

            # Preserve code indentation exactly
            if _INDENT.match(line):
                repaired_lines.append(line)
                continue

            # Only operate if OCR pattern exists
            if not _OCR_PATTERN.search(line):
                repaired_lines.append(line)
                continue

            segments = re.split(r"\s{2,}", line)
            rebuilt = []

            for seg in segments:
                tokens = seg.split()

                if len(tokens) >= 3 and all(len(t) == 1 for t in tokens):
                    rebuilt.append("".join(tokens))
                    repaired = True
                else:
                    rebuilt.append(seg)

            repaired_lines.append(" ".join(rebuilt))

        new_text = "\n".join(repaired_lines)

        document.set_text(new_text)

        if repaired:
            document.add_signal("document.ocr_spacing_repaired", True)

        return document
