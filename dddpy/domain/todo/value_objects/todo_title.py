"""Define the Todo title value object."""

from dataclasses import dataclass


@dataclass(frozen=True)
class TodoTitle:
    """Represent the title for a todo item."""

    value: str

    def __post_init__(self):
        """Validate the provided title string.

        Raises:
            ValueError: If the title is empty or longer than 100 characters.
        """
        if not self.value:
            raise ValueError('Title is required')
        if len(self.value) > 100:
            raise ValueError('Title must be 100 characters or less')

    def __str__(self) -> str:
        """Return the wrapped title string."""
        return self.value
