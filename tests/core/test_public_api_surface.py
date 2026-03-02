import text_curation

def test_public_api_is_explicit_and_minimal():
    public = set(text_curation.__all__)

    assert public == {
        "TextCurator",
        "CorpusPipeline",
        "__version__"
    }

def test_no_internal_symbols_leak():
    forbidden = {
        "Pipeline",
        "Document",
        "Block",
        "register",
        "get_profile"
    }

    leaked = forbidden.intersection(dir(text_curation))
    assert not leaked
