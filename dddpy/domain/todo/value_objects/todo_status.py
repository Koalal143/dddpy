"""Define the Todo status enumeration."""

from enum import Enum


class TodoStatus(Enum):
    """Enumerate lifecycle states for todo items."""

    NOT_STARTED = 'not_started'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'

    def __str__(self) -> str:
        """Return the underlying status string."""
        return self.value
