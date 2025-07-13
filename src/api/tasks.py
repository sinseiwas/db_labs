from fastapi import APIRouter, Depends
from typing import Annotated

from schemas.tasks import TaskAddSchema, TaskSchema

from api.dependencies import tasks_service
from services.tasks import TaskService
from schemas.tasks import TaskAddSchema, TaskSchema


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.post("")
async def add_task(
    task: TaskAddSchema,
    tasks_service: Annotated[TaskService, Depends(tasks_service)]
):
    task_id = await tasks_service.add_task(task)
    return {"task_id": task_id}

# @router.get("")
# async def