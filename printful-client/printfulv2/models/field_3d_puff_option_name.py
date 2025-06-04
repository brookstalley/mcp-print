from enum import Enum


class Field3DPuffOptionName(str, Enum):
    VALUE_0 = "3d_puff"

    def __str__(self) -> str:
        return str(self.value)
