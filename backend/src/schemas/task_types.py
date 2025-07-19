from pydantic import BaseModel, Field

class TaskTypeSchema(BaseModel):
    id: int
    name: str
    required_rank: int = Field(ge=1)


class TaskTypeAddSchema(BaseModel):
    name: str
    required_rank: int = Field(ge=1)
