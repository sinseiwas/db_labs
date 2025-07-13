# from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.database import Base
from schemas.workers import WorkerSchema

#  Модель работника
class Worker(Base):
    __tablename__ = "workers"
    id: Mapped[int] = mapped_column(primary_key=True)
    surname: Mapped[str]
    name: Mapped[str]
    second_name: Mapped[str]
    address: Mapped[str]
    passport_number: Mapped[int]
    #  Специальность
    speciality: Mapped[str]
    #  Год принятия на работу
    hire_year: Mapped[int]
    rank: Mapped[int]

    works = relationship("Work", back_populates="worker")


    def to_read_model(self) -> WorkerSchema:
        return WorkerSchema(
            id=self.id,
            surname=self.surname,
            name=self.name,
            second_name=self.second_name,
            address=self.address,
            passport_number=self.passport_number,
            speciality=self.speciality,
            hire_year=self.hire_year,
            rank=self.rank,
        )
