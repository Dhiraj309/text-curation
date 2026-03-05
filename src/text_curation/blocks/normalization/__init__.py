from .basic import NormalizationBlock
from .basic_v2 import NormalizationBlockV2
from .encoding_repair import EncodingRepairBlock
from .unicode_integrity import UnicodeIntegrityBlock
from .ocr_spacing_repair import OCRSpacingRepairBlock
__all__ = [
    "NormalizationBlock",
    "EncodingRepairBlock",
    "UnicodeIntegrityBlock",
    "NormalizationBlockV2",
    "OCRSpacingRepairBlock",
    ]
