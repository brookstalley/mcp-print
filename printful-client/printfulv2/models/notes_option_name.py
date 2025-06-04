from enum import Enum


class NotesOptionName(str, Enum):
    NOTES = "notes"

    def __str__(self) -> str:
        return str(self.value)
