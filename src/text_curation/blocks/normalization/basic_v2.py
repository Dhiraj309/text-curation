import re
import unicodedata
from text_curation.blocks.base import Block

_ZERO_WIDTH = re.compile(r"[\u200B\u200C\u200D\uFEFF]")
_CONTROL_CHARS = re.compile(r"[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]")

_QUOTES = {
    "“": '"', "”": '"',
    "‘": "'", "’": "'",
    "«": '"', "»": '"',
    "‚": "'",
    "`": "'",
}


class NormalizationBlockV2(Block):
    """
    Safer normalization for large-scale LLM pretraining corpora.

    Philosophy:
    - Preserve Unicode punctuation (— – − …)
    - Repair encoding corruption only
    - Remove invisible/control characters
    - Avoid stylistic rewriting
    """

    def __init__(self, policy=None):
        super().__init__(policy)

    def apply(self, document):

        text = document.text

        text = self._normalize_unicode(text)
        text = self._remove_zero_width(text)
        text = self._remove_control_char(text)
        text = self._normalize_line_endings(text)
        text = self._normalize_quotes(text)

        # NOTE:
        # No dash normalization
        # No ellipsis normalization

        text = self._collapse_whitespace(text)
        text = self._normalize_newlines(text)

        document.set_text(text.strip())

        return document

    def _normalize_unicode(self, text):
        return unicodedata.normalize("NFKC", text)

    def _remove_zero_width(self, text):
        return _ZERO_WIDTH.sub("", text)

    def _remove_control_char(self, text):
        return _CONTROL_CHARS.sub("", text)

    def _normalize_line_endings(self, text):
        return text.replace("\r\n", "\n").replace("\r", "\n")

    def _normalize_quotes(self, text):
        for k, v in _QUOTES.items():
            text = text.replace(k, v)
        return text

    def _collapse_whitespace(self, text):
        lines = text.split("\n")
        out = []

        for line in lines:

            prefix = len(line) - len(line.lstrip(" \t"))
            indent = line[:prefix]
            rest = line[prefix:]

            rest = re.sub(r"[ \t]+", " ", rest)

            out.append(indent + rest)

        return "\n".join(out)

    def _normalize_newlines(self, text):
        return re.sub(r"\n{3,}", "\n\n", text)
