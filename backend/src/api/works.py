from fastapi import APIRouter, Depends

from typing import Annotated

from api.dependencies import works_service
from services.works import WorksService
from schemas.works import WorkAddSchema

router = APIRouter(
    prefix="/works",
    tags=["Works"],
)



@router.post("")
async def add_work(
    work: WorkAddSchema,
    works_service: Annotated[WorksService, Depends(works_service)]
):
    work_id = await works_service.add_work(work)
    return {"work_id": work_id}


@router.get("")
async def get_works(
    works_service: Annotated[WorksService, Depends(works_service)]
):
    works = await works_service.get_works()
    return works
