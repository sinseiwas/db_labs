from pydantic import BaseModel


class TaskSchema(BaseModel):
    id: int
    description: str
    detail_id: int
    task_type_id: int
    duration_seconds: int
    sequence_number: int


class TaskAddSchema(BaseModel):
    description: str
    detail_id: int
    task_type_id: int
    duration_seconds: int
    sequence_number: int