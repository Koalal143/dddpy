"""Define exception for starting an in-progress todo."""


class TodoAlreadyStartedError(Exception):
    """Raise when attempting to start a todo already in progress."""

    message = 'The Todo is already started.'

    def __str__(self):
        """Return the default human-readable error message."""
        return TodoAlreadyStartedError.message
