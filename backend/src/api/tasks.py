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

TaskServiceDep = Annotated[TaskService, Depends(tasks_service)]


@router.post("")
async def add_task(
    task: TaskAddSchema,
    tasks_service: TaskServiceDep
):
    task_id = await tasks_service.add_task(task)
    return {"task_id": task_id}

@router.get("/get_detail_tasks")
async def get_detail_task(
    detail_id: int,
    tasks_service: TaskServiceDep
):
    detail_tasks = await tasks_service.get_detail_tasks(detail_id=detail_id)
    return detail_tasks

@router.get("/get_task")
async def get_task(
    task_id: int,
    tasks_service: TaskServiceDep
):
    task = await tasks_service.get_task(task_id=task_id)