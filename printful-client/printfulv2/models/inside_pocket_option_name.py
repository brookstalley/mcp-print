from enum import Enum


class InsidePocketOptionName(str, Enum):
    INSIDE_POCKET = "inside_pocket"

    def __str__(self) -> str:
        return str(self.value)
