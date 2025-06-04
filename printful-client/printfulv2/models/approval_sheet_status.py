from enum import Enum


class ApprovalSheetStatus(str, Enum):
    APPROVAL_PENDING = "approval_pending"
    APPROVED = "approved"
    CHANGES_REQUESTED = "changes_requested"
    FILES_CHANGED = "files_changed"
    WAITING_FOR_ACTION = "waiting_for_action"

    def __str__(self) -> str:
        return str(self.value)
