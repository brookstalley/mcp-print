from enum import Enum


class KnitwearColorReductionModeValue(str, Enum):
    PIXELATED = "pixelated"
    SOLID = "solid"

    def __str__(self) -> str:
        return str(self.value)
