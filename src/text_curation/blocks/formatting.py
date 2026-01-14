from text_curation.blocks.base import Block
import re

# Heuristic to detect indented blocks (e.g. code, quoted text)
_CODE_INDENT = re.compile(r"^[ \t]+")

# Patterns that must not be altered by punctuation normalization
_URL = re.compile(r"https?://\S+")
_EMAIL = re.compile(r"\b\S+@\S+\b")
_IP = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
_TIME = re.compile(r"\b\d{1,2}:\d{2}\b")
_NUMBER = re.compile(r"\b\d{1,3}(?:,\d{3})+\b")
_NUMERIC_COLON = re.compile(r"\b\d+:\d+\b")


class FormattingBlock(Block):
    """
    Reconstructs readable paragraph and line structure from
    inconsistently formatted text.

    This block merges wrapped lines into paragraphs, preserves
    indented blocks (e.g. code), and normalizes punctuation spacing
    while protecting structured tokens.
    """

    DEFAULT_POLICY = {
        "merge_wrapped_lines": True,
        "preserve_headers": False,   # reserved for future use
        "preserve_lists": False,     # reserved for future use
        "preserve_code_blocks": True,
        "normalize_punctuation": True,
    }

    def __init__(self, policy=None):
        # Merge caller policy with stable defaults
        merged = {**self.DEFAULT_POLICY, **(policy or {})}
        super().__init__(merged)

    def apply(self, document):
        """
        Normalize formatting and paragraph boundaries.

        This block mutates document.text and does not emit signals.
        """
        text = document.text

        text = self._normalize_line_endings(text)
        text = self._trim_trailing_white_spaces(text)
        text = self._collapse_blank_lines(text)
        text = self._normalize_paragraph_boundries(text)
        text = self._normalize_punctuation_spacing(text)

        document.set_text(text)
        return document

    def _normalize_line_endings(self, text):
        return text.replace("\r\n", "\n").replace("\r", "\n")
    
    def _trim_trailing_white_spaces(self, text):
        return "\n".join(line.rstrip() for line in text.split("\n"))
    
    def _collapse_blank_lines(self, text):
        return re.sub(r"\n{3,}", "\n\n", text)
    
    def _normalize_paragraph_boundries(self, text):
        lines = text.split("\n")
        out = []
        buffer = []

        for line in lines:
            if _CODE_INDENT.match(line):
                if buffer:
                    out.extend(buffer)
                    buffer = []
                out.append(line)
                continue

            if not line.strip():
                if buffer:
                    out.append(" ".join(buffer))
                    buffer = []
                out.append("")
                continue

            buffer.append(line.strip())

        if buffer:
            out.extend(buffer)

        return "\n".join(out)

    def _normalize_punctuation_spacing(self, text):
        text = re.sub(r"([!?]){2,}", r"\1", text)
        text = re.sub(r"\.{4,}", "...", text)

        placeholders = {}

        def stash(match):
            key = f"__TOK{len(placeholders)}__"
            placeholders[key] = match.group(0)
            return key

        text = _URL.sub(stash, text)
        text = _EMAIL.sub(stash, text)
        text = _IP.sub(stash, text)
        text = _NUMBER.sub(stash, text)
        text = _NUMERIC_COLON.sub(stash, text)

        text = re.sub(r"\s+([,!?;:])", r"\1", text)
        text = re.sub(r"([,!?;:])([^\s])", r"\1 \2", text)

        for k, v in placeholders.items():
            text = text.replace(k, v)

        return text