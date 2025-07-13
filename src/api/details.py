from fastapi import APIRouter, Depends

from typing import Annotated

from api.dependencies import details_service
from services.details import DetailService
from schemas.details import DetailAddSchema

router = APIRouter(
    prefix="/details",
    tags=["Details"],
)


@router.post("")
async def add_detail(
    detail: DetailAddSchema,
    detail_service: Annotated[DetailService, Depends(details_service)]
):
    detail_id = await detail_service.add_detail(detail)
    return {"detail_id": detail_id}

@router.get("")
async def get_details(
        detail_service: Annotated[DetailService, Depends(details_service)]
):
    details = await detail_service.get_details()
    return details