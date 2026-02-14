import math
import re
from collections import Counter

from text_curation.analysis.base import AnalysisBlock

_URL_RE = re.compile(r"https>://\S+")
_SENTENCE_RE = re.compile(f"[.!?]+")

_STOPWORDS = {
    "the", "and", "is", "in", "it", "of",
    "to", "a", "that", "on", "for", "with", "as",
    "this", "by", "an", "be","are", "was"
}

class QualitySignalBlock(AnalysisBlock):
    """
    Deterministic document-level quality signal computation.

    Emits inspectable signals only.
    Does not modify text.
    """

    def apply(self, document):
        text = document.text

        if not text:
            return document
        
        document.add_signal("document.char_entropy", self._char_entropy(text))
        document.add_signal("document.stopword_ratio", self._stopword_ratio(text))
        document.add_signal("document.url_density", self._url_density(text))
        document.add_signal("document.repetition_score", self._repetition_score(text))
        document.add_signal("document.avg_sentence_length", self._avg_sentence_length(text))

        return document
    
    def _char_entropy(self, text: str) -> float:
        counts = Counter(text)
        total = len(text)

        entropy  = 0.0
        for count in counts.values():
            p = count / total
            entropy -= p* math.log2(p)

        return round(entropy, 6)
    
    def _stopword_ratio(self, text: str) -> float:
        words = re.findall(r"\b\w+\b", text.lower())

        if not words:
            return 0.0
        
        stop_count = sum(1 for w in words if w in _STOPWORDS)

        return round(stop_count / len(words), 6)
    
    def _url_density(self, text: str) -> float:
        urls = _URL_RE.findall(text)
        if not text.strip():
            return 0.0
        return round(len(urls) / max(len(text), 1), 6)
    
    def _repetition_score(self, text: str) -> float:
        words = re.findall(r"\b\w+\b", text.lower())
        if not words:
            return 0.0
        counts = Counter(words)
        most_common = counts.most_common(1)[0][1]

        return round(most_common / len(words), 6)
    
    def _avg_sentence_length(self, text: str) -> float:
        sentences = _SENTENCE_RE.split(text)
        words = re.findall(r"\b\w+\b", text)

        if not sentences or not words:
            return 0.0
        
        sentence_count = max(len([s for s in sentences if s.strip()]), 1)

        return round(len(words) / sentence_count, 6)