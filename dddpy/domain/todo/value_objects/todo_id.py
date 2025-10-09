"""Define the Todo identifier value object."""

from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass(frozen=True)
class TodoId:
    """Represent the unique identifier for a todo item."""

    value: UUID

    @staticmethod
    def generate() -> 'TodoId':
        """Generate a new identifier for a todo entity.

        Returns:
            TodoId: Newly generated identifier.
        """
        return TodoId(uuid4())

    def __str__(self) -> str:
        """Return the string representation of the UUID."""
        return str(self.value)
