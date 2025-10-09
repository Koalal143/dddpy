"""Expose the error schema when a todo has not been started."""

from pydantic import BaseModel, Field

from dddpy.domain.todo.exceptions import TodoNotStartedError


class ErrorMessageTodoNotStarted(BaseModel):
    """Represent the not-started error response payload."""

    detail: str = Field(examples=[TodoNotStartedError.message])
