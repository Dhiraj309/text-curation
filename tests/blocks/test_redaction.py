from text_curation._blocks.redaction import RedactionBlock
from text_curation._core.document import Document

def redact(text):
    doc = Document(text)
    RedactionBlock().apply(doc)

    return doc.text

def test_email_redaction():
    assert redact("Contact me at test@example.com") == "Contact me at <EMAIL>"

def test_multiple_emails():
    assert redact("a@b.com c@d.org") == "<EMAIL> <EMAIL>"

def test_api_token_redaction():
    text = "My key is sk-abcdefghijklmnopqrstuvwwxy"
    assert redact(text) == "My key is <TOKEN>"

def test_url_credentials():
    text = "Go to page https://user:pass@example.com/page"
    assert redact(text) == "Go to page https://<REDACTED>@example.com/page"

def test_no_false_positives():
    text = "This is a normal sentece with numbers 12345"
    assert redact(text) == text