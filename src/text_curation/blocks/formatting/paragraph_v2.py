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
    - Never modify fenced code blocks
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

        in_fence = False

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

            stripped = line.strip()

            # --------------------------------------------------
            # Markdown code fence detection
            # --------------------------------------------------
            if stripped.startswith("```") or stripped.startswith("~~~"):
                flush()
                out.append(line)
                in_fence = not in_fence
                continue

            # --------------------------------------------------
            # Preserve lines inside fenced code blocks exactly
            # --------------------------------------------------
            if in_fence:
                flush()
                out.append(line)
                continue

            # Preserve indented code blocks
            if _CODE_INDENT.match(line):
                flush()
                out.append(line)
                continue

            # Blank line = paragraph boundary
            if not stripped:
                flush()
                out.append("")
                continue

            stripped_line = stripped

            if not buffer:
                buffer.append(stripped_line)
                continue

            prev = buffer[-1]

            # Conditions for safe merge (PDF-style wrapping)
            if (
                not _SENTENCE_END.search(prev)
                and stripped_line
                and stripped_line[0].islower()
                and len(prev) < 120
                and len(stripped_line) < 120
                and not stripped_line.startswith(_QUOTE_START)
            ):
                buffer.append(stripped_line)
                continue

            flush()
            buffer.append(stripped_line)

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
