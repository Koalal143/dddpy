"""Define the Todo description value object."""

from dataclasses import dataclass


@dataclass(frozen=True)
class TodoDescription:
    """Represent the optional description for a todo item."""

    value: str

    def __post_init__(self):
        """Validate the description length constraints.

        Raises:
            ValueError: If the description exceeds 1000 characters.
        """
        if len(self.value) > 1000:
            raise ValueError('Description must be 1000 characters or less')

    def __str__(self) -> str:
        """Return the wrapped description string."""
        return self.value
