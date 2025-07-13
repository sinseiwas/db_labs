from sqlalchemy.orm import mapped_column, Mapped, relationship

from datetime import date
from decimal import Decimal


from database.database import Base
from schemas.details import DetailSchema


class Detail(Base):
    __tablename__ = "details"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    length: Mapped[Decimal]
    width: Mapped[Decimal]
    height: Mapped[Decimal]
    task_count: Mapped[int]
    start_date: Mapped[date]
    end_date: Mapped[date]

    tasks = relationship("Task", back_populates="detail")
    
    def to_read_model(self) -> DetailSchema:
        return DetailSchema(
            id=self.id,
            name=self.name,
            length=self.length,
            width=self.width,
            height=self.height,
            task_count=self.task_count,
            start_date=self.start_date,
            end_date=self.end_date
        )
