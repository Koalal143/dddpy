"""Expose the error schema when a todo is already completed."""

from pydantic import BaseModel, Field

from dddpy.domain.todo.exceptions import TodoAlreadyCompletedError


class ErrorMessageTodoAlreadyCompleted(BaseModel):
    """Represent the already-completed error response payload."""

    detail: str = Field(examples=[TodoAlreadyCompletedError.message])
