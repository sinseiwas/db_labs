from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date

from database.database import Base
from schemas.works import WorkSchema

class Work(Base):
    __tablename__ = "works"

    id: Mapped[int] = mapped_column(primary_key=True)
    task_id: Mapped[int] = mapped_column(ForeignKey("tasks.id"))
    worker_id: Mapped[int] = mapped_column(ForeignKey("workers.id"))
    time_seconds: Mapped[int]
    date: Mapped[date]

    task = relationship("Task", back_populates="works")
    worker = relationship("Worker", back_populates="works")

    def to_read_model(self) -> WorkSchema:
        return WorkSchema(
            id=self.id,
            task_id=self.task_id,
            worker_id=self.worker_id,
            time_seconds=self.time_seconds,
            date=self.date
        )
