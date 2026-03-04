import re
from collections import Counter

from text_curation.analysis.base import AnalysisBlock


_WORD_RE = re.compile(r"\b\w+\b", re.UNICODE)


class LanguageDetectionBlock(AnalysisBlock):
    """
    Deterministic language detection signal.

    Emits:
        document.language
        document.language_confidence

    The detector attempts to use fastText if available.
    If fastText is not installed, a lightweight heuristic
    fallback is used.
    """

    def __init__(self):
        super().__init__(policy={})

        self._detector = None

        try:
            import fasttext  # type: ignore

            # Attempt to load standard language model
            self._detector = fasttext.load_model("lid.176.ftz")

        except Exception:
            self._detector = None

    def apply(self, document):

        text = document.text

        if not text.strip():
            document.add_signal("document.language", "unknown")
            document.add_signal("document.language_confidence", 0.0)
            return document

        if self._detector is not None:
            return self._fasttext_detect(document, text)

        return self._heuristic_detect(document, text)

    def _fasttext_detect(self, document, text):

        labels, scores = self._detector.predict(text.replace("\n", " "), k=1)

        lang = labels[0].replace("__label__", "")
        confidence = float(scores[0])

        document.add_signal("document.language", lang)
        document.add_signal("document.language_confidence", round(confidence, 6))

        return document

    def _heuristic_detect(self, document, text):

        words = _WORD_RE.findall(text.lower())

        if not words:
            document.add_signal("document.language", "unknown")
            document.add_signal("document.language_confidence", 0.0)
            return document

        latin = 0
        cyrillic = 0
        other = 0

        for w in words:
            for c in w:
                code = ord(c)

                if 0x0041 <= code <= 0x024F:
                    latin += 1
                elif 0x0400 <= code <= 0x04FF:
                    cyrillic += 1
                else:
                    other += 1

        counts = Counter(
            {
                "latin": latin,
                "cyrillic": cyrillic,
                "other": other,
            }
        )

        dominant = counts.most_common(1)[0]

        language = dominant[0]
        total = sum(counts.values())

        confidence = dominant[1] / total if total else 0.0

        document.add_signal("document.language", language)
        document.add_signal("document.language_confidence", round(confidence, 6))

        return document
