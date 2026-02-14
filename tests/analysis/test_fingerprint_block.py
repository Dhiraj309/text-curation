from text_curation.analysis import FingerprintBlock
from text_curation.core.document import Document

def text_fingerprint_is_deterministic():
    text = "Example text"
    doc1 = Document(text)
    doc2 = Document(text)

    block = FingerprintBlock()

    block.apply(doc1)
    block.apply(doc2)

    sig1 = doc1.signals[0].value
    sig2 = doc2.signals[0].value

    assert sig1 == sig2

def test_fingrprint_respects_policy():
    text = "  Hello world  "
    doc = Document(text)

    block = FingerprintBlock(policy={"strip": True, "normalize_whitespace": True})
    block.apply(doc)

    digest = doc.signals[0].value

    normalized = "Hello world"
    import hashlib
    expected = hashlib.sha256(normalized.encode("utf-8")).hexdigest()

    assert digest == expected

def test_fingerprint_does_not_modify_text():
    text = "Keep me intact"
    doc = Document(text)

    block = FingerprintBlock()
    block.apply(doc)

    assert doc.text == text