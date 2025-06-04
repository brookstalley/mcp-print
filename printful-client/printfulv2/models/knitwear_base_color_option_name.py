from enum import Enum


class KnitwearBaseColorOptionName(str, Enum):
    BASE_COLOR = "base_color"

    def __str__(self) -> str:
        return str(self.value)
