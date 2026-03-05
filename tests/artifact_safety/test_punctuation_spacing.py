from text_curation import TextCurator


PROFILE = "web.pretrain.production_v1"


def test_no_space_before_punctuation():

    text = "Hello, world."

    curator = TextCurator.from_profile(PROFILE)

    result = curator({"text": [text]})

    cleaned = result["text"][0]

    assert " ," not in cleaned
    assert " ." not in cleaned
