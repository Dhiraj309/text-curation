from text_curation import TextCurator

INPUT = """TERMS AND CONDITIONS
TERMS AND CONDITIONS

Last updated:  30/01/2026

This is a paragraph
that was wrapped
incorrectly by the scraper.

def example(x,y):
    return x+y

Contact us at: support@example.com
"""


EXPECTED = """TERMS AND CONDITIONS
TERMS AND CONDITIONS

Last updated: 30/01/2026

This is a paragraph
that was wrapped
incorrectly by the scraper.

def example(x,y):
    return x+y

Contact us at: <EMAIL>"""


def test_llm_pretrain_v1_golden():
    curator = TextCurator.from_profile("llm_pretrain_v1")
    out = curator({"text": [INPUT]})["text"][0]
    assert out == EXPECTED
