from enum import Enum


class TechniqueEnum(str, Enum):
    CUT_SEW = "cut-sew"
    DIGITAL = "digital"
    DTFILM = "dtfilm"
    DTG = "dtg"
    EMBROIDERY = "embroidery"
    SUBLIMATION = "sublimation"
    UV = "uv"

    def __str__(self) -> str:
        return str(self.value)
