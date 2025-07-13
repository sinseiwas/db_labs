from pydantic import BaseModel

from decimal import Decimal
from datetime import date


class DetailSchema(BaseModel):
    id: int
    name: str
    length: Decimal
    width: Decimal
    height: Decimal
    task_count: int
    start_date: date
    end_date: date


class DetailAddSchema(BaseModel):
    name: str
    length: Decimal
    width: Decimal
    height: Decimal
    task_count: int
    start_date: date
    end_date: date