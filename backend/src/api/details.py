from fastapi import APIRouter, Depends

from typing import Annotated

from api.dependencies import details_service
from services.details import DetailService
from schemas.details import DetailAddSchema

router = APIRouter(
    prefix="/details",
    tags=["Details"],
)

DetailServiceDep = Annotated[DetailService, Depends(details_service)]


@router.post("")
async def add_detail(
    detail: DetailAddSchema,
    detail_service: DetailServiceDep
):
    detail_id = await detail_service.add_detail(detail)
    return {"detail_id": detail_id}


@router.get("/get_details")
async def get_details(
    detail_service: DetailServiceDep
):
    details = await detail_service.get_details()
    return details


@router.get("/get_detail")
async def get_detail(
    detail_id: int,
    detail_service: DetailServiceDep
):
    detail = detail_service.get_detail(detail_id=detail_id)
    return detail