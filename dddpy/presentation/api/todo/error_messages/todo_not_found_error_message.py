"""Expose the error schema returned when a todo is missing."""

from pydantic import BaseModel, Field

from dddpy.domain.todo.exceptions import TodoNotFoundError


class ErrorMessageTodoNotFound(BaseModel):
    """Represent the not-found error response payload."""

    detail: str = Field(examples=[TodoNotFoundError.message])
