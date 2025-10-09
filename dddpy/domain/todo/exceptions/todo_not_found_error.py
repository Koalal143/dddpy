"""Define exception for missing todo entities."""


class TodoNotFoundError(Exception):
    """Raise when a requested todo entity cannot be located."""

    message = 'The Todo you specified does not exist.'

    def __str__(self):
        """Return the default human-readable error message."""
        return TodoNotFoundError.message
