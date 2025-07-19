from pydantic import BaseModel, Field


class TaskSchema(BaseModel):
    id: int
    description: str
    detail_id: int = Field(ge=1)
    task_type_id: int = Field(ge=1)
    duration_seconds: int
    sequence_number: int


class TaskAddSchema(BaseModel):
    description: str
    detail_id: int = Field(ge=1)
    task_type_id: int = Field(ge=1)
    duration_seconds: int = Field(ge=1)
    sequence_number: int