from text_curation.blocks.base import Block
import re


# Email pattern (conservative, RFC-inspired)
_EMAIL = re.compile(
    r"\b[a-zA-Z0-9._%+-]+"
    r"@"
    r"[a-zA-Z0-9.-]+"
    r"\.[a-zA-Z]{2,}\b"
)

# Explicit token formats only (no entropy-based detection)
_API_TOKEN = re.compile(
    r"""
    \b(
        sk-[A-Za-z0-9_-]{16,} |
        hf_[A-Za-z0-9_-]{16,} |
        ghp_[A-Za-z0-9_-]{16,} |
        api_[A-Za-z0-9_-]{16,} |
        key_[A-Za-z0-9_-]{16,}
    )\b
    """,
    re.VERBOSE
)

# Credentials embedded in URLs (user:pass@host)
_URL_CREDENTIAL = re.compile(
    r"(https?://)"
    r"[^/\s@]+"
    r":"
    r"[^@\s]*"
    r"@"
)

# IPv4 address pattern
_IP_ADDRESS = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")


class RedactionBlock(Block):
    """
    Masks sensitive information using deterministic pattern matching.

    This block redacts known secret formats such as email addresses,
    API tokens, and credentials embedded in URLs.

    Behavior is controlled through explicit policy flags so profiles
    can enable additional redactions without changing legacy behavior.
    """

    DEFAULT_POLICY = {
        "redact_emails": True,
        "redact_api_tokens": True,
        "redact_url_credentials": True,
        "redact_ip_addresses": False,  # new, opt-in
    }

    def __init__(self, policy=None):
        merged_policy = {**self.DEFAULT_POLICY, **(policy or {})}
        super().__init__(merged_policy)

    def apply(self, document):
        """
        Redact sensitive content in-place.

        This block mutates document.text and does not emit signals.
        """
        text = document.text

        if self.policy["redact_url_credentials"]:
            text = self._redact_url_credentials(text)

        if self.policy["redact_emails"]:
            text = self._redact_emails(text)

        if self.policy["redact_api_tokens"]:
            text = self._redact_api_tokens(text)

        if self.policy["redact_ip_addresses"]:
            text = self._redact_ip_addresses(text)

        document.set_text(text)

        return document

    def _redact_emails(self, text):
        return _EMAIL.sub("<EMAIL>", text)

    def _redact_api_tokens(self, text):
        return _API_TOKEN.sub("<TOKEN>", text)

    def _redact_url_credentials(self, text):
        return _URL_CREDENTIAL.sub(r"\1<REDACTED>@", text)

    def _redact_ip_addresses(self, text):
        return _IP_ADDRESS.sub("<IP_ADDRESS>", text)
