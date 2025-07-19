from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.details import Detail
from models.task_types import TaskType

from database.database import Base
from schemas.tasks import TaskSchema


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str]
    detail_id: Mapped[int] = mapped_column(ForeignKey("details.id"))
    task_type_id: Mapped[int] = mapped_column(ForeignKey("taskTypes.id"))
    duration_seconds: Mapped[int]
    sequence_number: Mapped[int]

    detail = relationship("Detail", back_populates="tasks")
    task_type = relationship("TaskType", back_populates="tasks")
    works = relationship("Work", back_populates="task")

    def to_read_model(self) -> TaskSchema:
        return TaskSchema(
            id=self.id,
            description=self.description,
            detail_id=self.detail_id,
            task_type_id=self.task_type_id,
            duration_seconds=self.duration_seconds,
            sequence_number=self.sequence_number,
        )
