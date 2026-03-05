from text_curation.blocks.normalization.ocr_digit_repair import OCRDigitRepairBlock
from text_curation.core.document import Document


def test_ocr_digit_repair():

    text = "Th1s t3xt c0ntains OCR nois3."

    block = OCRDigitRepairBlock()

    doc = Document(text)

    result = block.apply(doc)

    assert "This text contains OCR noise" in result.text
