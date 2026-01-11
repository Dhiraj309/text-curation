import re

class DeduplicationBlock:
    """
    Removes exact duplicate paragraphs within a document.

    Deduplication is local, order-preserving, and based on
    conservative normalization rules.
    """
        
    def apply(self, document):
        """
        Deduplicate repeated paragraphs in-place.

        This block mutates document.text and does not emit signals.
        """
        text = document.text

        if not text.strip():
            return document
        
        paragraphs = text.split("\n\n")

        seen = set()
        kept = []

        for para in paragraphs:
            key = self._normalize_key(para)

            if not key:
                continue
            if key in seen:
                continue

            seen.add(key)
            kept.append(para)

        document.set_text("\n\n".join(kept))
        return document

    def _normalize_key(self, paragraph: str) -> str:
        return re.sub(r"\s+", " ", paragraph.strip()).lower()