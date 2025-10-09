"""Define exception for operations requiring a started todo."""


class TodoNotStartedError(Exception):
    """Raise when acting on a todo that has not been started."""

    message = 'The Todo is not started.'

    def __str__(self):
        """Return the default human-readable error message."""
        return TodoNotStartedError.message
