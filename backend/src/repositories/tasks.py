from models.tasks import Task
from utils.repository import SQLAlchemyRepository


class TaskRepository(SQLAlchemyRepository):
    model = Task
