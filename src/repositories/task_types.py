from models.task_types import TaskType
from utils.repository import SQLAlchemyRepository


class TaskTypeRepository(SQLAlchemyRepository):
    model = TaskType
