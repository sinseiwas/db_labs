from pydantic import BaseModel

class WorkerSchema(BaseModel):
    id: int
    surname: str
    name: str
    second_name: str
    address: str
    passport_number: int
    #  Специальность
    speciality: str
    #  Год принятия на работу
    hire_year: int
    rank: int


class WorkerAddSchema(BaseModel):
    surname: str
    name: str
    second_name: str
    address: str
    passport_number: int
    speciality: str
    hire_year: int
    rank: int