from pydantic import BaseModel
from datetime import date


class WorkSchema(BaseModel):
    id: int
    task_id: int
    worker_id: int
    time_seconds: int
    date: int


class WorkAddSchema(BaseModel):
    task_id: int
    worker_id: int
    time_seconds: int
    date: date
