from enum import Enum


class KnitwearTrimColorOptionName(str, Enum):
    TRIM_COLOR = "trim_color"

    def __str__(self) -> str:
        return str(self.value)
