"""Define exception for completing an already completed todo."""


class TodoAlreadyCompletedError(Exception):
    """Raise when completing a todo that is already completed."""

    message = 'The Todo is already completed.'

    def __str__(self):
        """Return the default human-readable error message."""
        return TodoAlreadyCompletedError.message
