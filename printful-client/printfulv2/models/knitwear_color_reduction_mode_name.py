from enum import Enum


class KnitwearColorReductionModeName(str, Enum):
    COLOR_REDUCTION_MODE = "color_reduction_mode"

    def __str__(self) -> str:
        return str(self.value)
