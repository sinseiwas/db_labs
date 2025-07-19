from models.workers import Worker
from utils.repository import SQLAlchemyRepository


class WorkerRepository(SQLAlchemyRepository):
    model = Worker
