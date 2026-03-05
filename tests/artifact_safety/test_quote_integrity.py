from text_curation import TextCurator


PROFILE = "web.pretrain.production_v1"


def test_quotes_preserved():

    text = '"Hello world," she said.'

    curator = TextCurator.from_profile(PROFILE)

    result = curator({"text": [text]})

    cleaned = result["text"][0]

    assert '"Hello world,"' in cleaned
