from pydantic import BaseModel, Field

from decimal import Decimal
from datetime import date


class DetailSchema(BaseModel):
    id: int
    name: str
    length: Decimal
    width: Decimal
    height: Decimal
    task_count: int = Field(ge=1)
    start_date: date
    end_date: date


class DetailAddSchema(BaseModel):
    name: str
    length: Decimal
    width: Decimal
    height: Decimal
    task_count: int = Field(ge=1)
    start_date: date
    end_date: date