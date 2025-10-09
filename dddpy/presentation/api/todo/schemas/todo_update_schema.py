"""Define request schema for updating todos."""

from pydantic import BaseModel, Field


class TodoUpdateSchema(BaseModel):
    """Validate the payload for updating a todo."""

    title: str = Field(min_length=1, max_length=100, examples=['Complete the project'])
    description: str | None = Field(
        default=None,
        max_length=1000,
        examples=['Finish implementing the DDD architecture'],
    )
