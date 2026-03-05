from text_curation.blocks.normalization.ocr_digit_repair import OCRDigitRepairBlock
from text_curation.core.document import Document


def run_block(text):
    block = OCRDigitRepairBlock()
    doc = Document(text)
    return block.apply(doc)


def test_ocr_repair_basic():

    doc = run_block("Th1s t3xt c0ntains OCR nois3.")

    assert "This text contains OCR noise." in doc.text


def test_does_not_modify_numbers():

    doc = run_block("Population reached 1,234,567 in 2023.")

    assert "1,234,567" in doc.text
    assert "2023" in doc.text


def test_does_not_modify_urls():

    text = "Docs at https://docs.example.org/v1/api/index.html"

    doc = run_block(text)

    assert "v1/api" in doc.text


def test_does_not_modify_mentions():

    text = "@user123 This is amazing"

    doc = run_block(text)

    assert "@user123" in doc.text


def test_does_not_modify_hashtags():

    text = "#AI #ml2023"

    doc = run_block(text)

    assert "#ml2023" in doc.text


def test_signal_emitted():

    doc = run_block("Th1s t3xt")

    signals = {s.name: s.value for s in doc.signals}

    assert signals["document.ocr_digit_repairs"] == 2
