from enum import Enum


class KnitwearYarnColorsOptionName(str, Enum):
    YARN_COLORS = "yarn_colors"

    def __str__(self) -> str:
        return str(self.value)
