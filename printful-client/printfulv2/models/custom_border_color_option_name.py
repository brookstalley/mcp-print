from enum import Enum


class CustomBorderColorOptionName(str, Enum):
    CUSTOM_BORDER_COLOR = "custom_border_color"

    def __str__(self) -> str:
        return str(self.value)
