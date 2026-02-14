import hashlib

from text_curation.analysis import AnalysisBlock

class FingerprintBlock(AnalysisBlock):
    """
    Deterministic document fingerprinting using SHA-256.

    Emits:
        document.sha256

    Fingerprinting behavior may optionally normalize text according
    to explicit policy parameters
    """

    DEFAULT_POLICY = {
        "normalize_whitespace": False,
        "strip": False,
    }

    def __init__(self, policy = None):
        merged = {**self.DEFAULT_POLICY, **(policy or {})}
        super().__init__(merged)

    def apply(self, document):
        text = document.text

        if self.policy.get("strip"):
            text = text.strip()

        if self.policy.get("normalize_whitespace"):
            text = " ".join(text.split())

        digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
        document.add_signal("document.sha256", digest)

        return document