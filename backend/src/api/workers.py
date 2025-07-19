from fastapi import APIRouter, Depends

from typing import Annotated

from schemas.workers import WorkerAddSchema
from services.workers import WorkerService
from api.dependencies import workers_service


router = APIRouter(
    prefix="/workers",
    tags=["Workers"]
)


@router.post("/add_worker")
async def add_worker(
    worker: WorkerAddSchema,
    worker_service: Annotated[WorkerService, Depends(workers_service)]
):
    worker_id = await worker_service.add_worker(worker)
    return {"worker_id": worker_id}


@router.get("/get_all_workers")
async def get_all_workers(
    worker_service: Annotated[WorkerService, Depends(workers_service)],
):
    workers = await worker_service.get_workers()
    return workers


@router.get("/get_worker")
async def get_worker(
    id: int,
    worker_service: Annotated[WorkerService, Depends(workers_service)],
):
    worker = await worker_service.get_worker(worker_id=id)
    return worker