from text_curation import TextCurator

INPUT = """TERMS AND CONDITIONS
TERMS AND CONDITIONS

Last updated:  12/05/2022

By accessing this WEBSITE, you agree to the following terms and conditions.
By accessing this WEBSITE, you agree to the following terms and conditions.

Contact us at: support@example.com
"""


EXPECTED = """TERMS AND CONDITIONS TERMS AND CONDITIONS

Last updated: 12/05/2022

By accessing this WEBSITE, you agree to the following terms and conditions. By accessing this WEBSITE, you agree to the following terms and conditions.

Contact us at: <EMAIL>"""

def test_web_common_v1_golden():
    curator = TextCurator.from_profile("web_common_v1")
    out = curator({"text": [INPUT]})["text"][0]
    assert out == EXPECTED