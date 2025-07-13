from pydantic import BaseModel

class TaskTypeSchema(BaseModel):
    id: int
    name: str
    required_rank: int


class TaskTypeAddSchema(BaseModel):
    name: str
    required_rank: int
