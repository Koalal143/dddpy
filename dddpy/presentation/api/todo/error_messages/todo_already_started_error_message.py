"""Expose the error schema when a todo has already started."""

from pydantic import BaseModel, Field

from dddpy.domain.todo.exceptions import TodoAlreadyStartedError


class ErrorMessageTodoAlreadyStarted(BaseModel):
    """Represent the already-started error response payload."""

    detail: str = Field(examples=[TodoAlreadyStartedError.message])
