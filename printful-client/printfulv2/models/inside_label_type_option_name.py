from enum import Enum


class InsideLabelTypeOptionName(str, Enum):
    INSIDE_LABEL_TYPE = "inside_label_type"

    def __str__(self) -> str:
        return str(self.value)
