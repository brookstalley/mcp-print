from enum import Enum


class StitchColorOptionName(str, Enum):
    STITCH_COLOR = "stitch_color"

    def __str__(self) -> str:
        return str(self.value)
