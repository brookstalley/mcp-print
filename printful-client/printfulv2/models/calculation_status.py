from enum import Enum


class CalculationStatus(str, Enum):
    CALCULATING = "calculating"
    DONE = "done"
    FAILED = "failed"

    def __str__(self) -> str:
        return str(self.value)
