from enum import Enum


class SizeTableUnit(str, Enum):
    CM = "cm"
    INCHES = "inches"

    def __str__(self) -> str:
        return str(self.value)
