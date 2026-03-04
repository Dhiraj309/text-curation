import re


_SENTENCE_BOUNDARY_RE = re.compile(r"(?<=[.!?])\s+")


def _paragraphs(text):
    return [p for p in text.split("\n\n") if p.strip()]


def _sentences(paragraph):
    return _SENTENCE_BOUNDARY_RE.split(paragraph)


def chunk_text(
    text: str,
    *,
    max_tokens: int = 512,
):
    """
    Structure-aware chunking utility.

    Rules:
    - Prefer paragraph boundaries
    - Avoid sentence splits where possible
    - Never split inside tokens
    - Never split empty regions
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if max_tokens <= 0:
        raise ValueError("max_tokens must be positive")

    chunks = []

    paragraphs = _paragraphs(text)

    current_chunk = []
    current_len = 0

    for para in paragraphs:

        sentences = _sentences(para)

        for sent in sentences:

            tokens = sent.split()
            token_len = len(tokens)

            if token_len == 0:
                continue

            if current_len + token_len > max_tokens:

                if current_chunk:
                    chunks.append(" ".join(current_chunk))
                    current_chunk = []
                    current_len = 0

                # handle extremely long sentence
                if token_len > max_tokens:

                    start = 0
                    while start < token_len:
                        part = tokens[start:start + max_tokens]
                        chunks.append(" ".join(part))
                        start += max_tokens

                    continue

            current_chunk.append(sent.strip())
            current_len += token_len

        current_chunk.append("\n\n")
        current_len += 1

    if current_chunk:
        chunks.append(" ".join(current_chunk).strip())

    return chunks
