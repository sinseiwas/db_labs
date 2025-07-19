from utils.repository import AbstractRepository

from schemas.tasks import TaskAddSchema, TaskSchema

class TaskService:
    def __init__(self, tasks_repo: AbstractRepository):
        self.tasks_repo: AbstractRepository = tasks_repo()

    async def add_task(self, task: TaskAddSchema):
        tasks_dict = task.model_dump()
        task_id = await self.tasks_repo.add_one(tasks_dict)
        return task_id
    
    async def get_detail_tasks(self, detail_id: int):
        tasks = await self.tasks_repo.find_all(detail_id=detail_id)
        return tasks
    
    async def get_task(self, task_id: int):
        task = await self.tasks_repo.find_one(id=task_id)
        return task