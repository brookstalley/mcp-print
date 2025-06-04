from enum import Enum


class UnlimitedColorOptionName(str, Enum):
    UNLIMITED_COLOR = "unlimited_color"

    def __str__(self) -> str:
        return str(self.value)
