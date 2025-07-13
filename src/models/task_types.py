from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.database import Base
from schemas.task_types import TaskTypeSchema

class TaskType(Base):
    __tablename__ = "taskTypes"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    required_rank: Mapped[int]

    tasks = relationship("Task", back_populates="task_type")

    def to_read_model(self) -> TaskTypeSchema:
        return TaskTypeSchema(
            id=self.id,
            name=self.name,
            required_rank=self.required_rank,
        )