from collections import Counter
from text_curation.analysis import AnalysisBlock

class TokenStatsBlock(AnalysisBlock):
    """
    Deterministic token-level statistics using whitespace tokenization.

    Emits:
        document.token_count
        document.unique_token_count
        document.rare_token_ratio
        document.max_token_length
    """

    def apply(self, document):
        text = document.text

        tokens = text.split()

        token_count = len(tokens)
        unique_count = len(set(tokens))

        if token_count == 0:
            document.add_signal("document.token_count", 0)
            document.add_signal("document.unique_token_count", 0)
            document.add_signal("document.rare_token_ratio", 0.0)
            document.add_signal("document.max_token_length", 0)

            return document
        
        counts = Counter(tokens)

        rare_count = sum(1 for t in tokens if counts[t] == 1)
        rare_ratio = round(rare_count / token_count, 6)
        max_len = max(len(t) for t in tokens)

        document.add_signal("document.token_count", token_count)
        document.add_signal("document.unique_token_count", unique_count)
        document.add_signal("document.rare_token_ratio", rare_ratio)
        document.add_signal("document.max_token_length", max_len)

        return document
