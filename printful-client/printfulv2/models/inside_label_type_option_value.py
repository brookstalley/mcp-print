from enum import Enum


class InsideLabelTypeOptionValue(str, Enum):
    CUSTOM = "custom"
    NATIVE = "native"

    def __str__(self) -> str:
        return str(self.value)
