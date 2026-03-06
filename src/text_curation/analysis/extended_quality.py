import json
import math
import string
import unicodedata
from collections import Counter

from text_curation.analysis.base import AnalysisBlock


class ExtendedQualityBlock(AnalysisBlock):
    """
    Emit additional corpus quality signals.

    Signals emitted:

        document.uppercase_ratio
        document.symbol_ratio
        document.punctuation_density
        document.script_distribution
        document.language_entropy
    """

    def apply(self, document):

        text = document.text

        if not text:
            return document

        total = len(text)

        uppercase_count = sum(1 for c in text if c.isupper())

        punctuation_count = sum(1 for c in text if c in string.punctuation)

        symbol_count = sum(
            1 for c in text
            if unicodedata.category(c).startswith("S")
        )

        uppercase_ratio = uppercase_count / total
        punctuation_density = punctuation_count / total
        symbol_ratio = symbol_count / total

        scripts = []

        for c in text:
            if c.isalpha():
                try:
                    name = unicodedata.name(c)
                    scripts.append(name.split()[0])
                except ValueError:
                    continue

        script_counts = Counter(scripts)

        entropy = 0.0

        if script_counts:
            total_scripts = sum(script_counts.values())

            for count in script_counts.values():
                p = count / total_scripts
                entropy -= p * math.log2(p)

        document.add_signal(
            "document.uppercase_ratio",
            round(uppercase_ratio, 6),
        )

        document.add_signal(
            "document.symbol_ratio",
            round(symbol_ratio, 6),
        )

        document.add_signal(
            "document.punctuation_density",
            round(punctuation_density, 6),
        )

        # Serialize dictionary to avoid Arrow schema drift during multiprocessing
        document.add_signal(
            "document.script_distribution",
            json.dumps(dict(script_counts), sort_keys=True),
        )

        document.add_signal(
            "document.language_entropy",
            round(entropy, 6),
        )

        return document
