from schemas.details import DetailAddSchema
from utils.repository import AbstractRepository


class DetailService:
    def __init__(self, detail_repo: AbstractRepository):
        self.detail_repo: AbstractRepository = detail_repo()

    async def add_detail(self, detail: DetailAddSchema):
        detail_dict = detail.model_dump()
        detail_id = await self.detail_repo.add_one(detail_dict)
        return detail_id
    
    async def get_details(self):
        details = await self.detail_repo.find_all()
        return details