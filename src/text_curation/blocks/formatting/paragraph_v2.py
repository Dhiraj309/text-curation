import re
from text_curation.blocks.base import Block

_CODE_INDENT = re.compile(r"^[ \t]+")
_SENTENCE_END = re.compile(r"[.!?:;]['\"]?$")

_QUOTE_START = ('"', "'", "“", "‘", "(", "[")


class ParagraphFormattingBlockV2(Block):
    """
    Safer paragraph reconstruction designed for LLM pretraining corpora.

    Philosophy:
    - Preserve natural paragraph boundaries
    - Only merge lines likely caused by PDF line wrapping
    - Avoid stylistic punctuation rewriting
    """

    DEFAULT_POLICY = {
        "repair_punctuation": True,
    }

    def __init__(self, policy=None):
        super().__init__({**self.DEFAULT_POLICY, **(policy or {})})

    def apply(self, document):
        text = document.text

        text = self._normalize_paragraph_boundaries(text)

        if self.policy["repair_punctuation"]:
            text = self._repair_punctuation(text)

        document.set_text(text)
        return document

    # ---------------------------------------------------------------------

    def _normalize_paragraph_boundaries(self, text):
        lines = text.split("\n")

        out = []
        buffer = []

        def flush():
            nonlocal buffer
            if not buffer:
                return

            if len(buffer) > 1:
                out.append(" ".join(buffer))
            else:
                out.extend(buffer)

            buffer = []

        for line in lines:

            # Preserve code indentation
            if _CODE_INDENT.match(line):
                flush()
                out.append(line)
                continue

            # Blank line = paragraph boundary
            if not line.strip():
                flush()
                out.append("")
                continue

            stripped = line.strip()

            if not buffer:
                buffer.append(stripped)
                continue

            prev = buffer[-1]

            # Conditions for safe merge (PDF-style wrapping)
            if (
                not _SENTENCE_END.search(prev)
                and stripped
                and stripped[0].islower()
                and len(prev) < 120
                and len(stripped) < 120
                and not stripped.startswith(_QUOTE_START)
            ):
                buffer.append(stripped)
                continue

            flush()
            buffer.append(stripped)

        flush()

        return "\n".join(out)

    # ---------------------------------------------------------------------

    def _repair_punctuation(self, text):
        """
        Only repair obvious corruption.
        No stylistic normalization.
        """

        # Collapse repeated punctuation
        text = re.sub(r"([!?]){2,}", r"\1", text)

        # Normalize excessive dot sequences (4+) to ellipsis
        text = re.sub(r"\.{4,}", "…", text)

        return text
