from enum import Enum


class FileRole(str, Enum):
    LABEL = "label"
    PREVIEW = "preview"
    PRINTFILE = "printfile"

    def __str__(self) -> str:
        return str(self.value)
