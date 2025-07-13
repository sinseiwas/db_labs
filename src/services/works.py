from schemas.works import WorkAddSchema
from utils.repository import AbstractRepository


class WorksService:
    def __init__(self, work_repo: AbstractRepository):
        self.work_repo: AbstractRepository = work_repo()

    async def add_work(self, work: WorkAddSchema):
        work_dict = work.model_dump()
        work_id = await self.work_repo.add_one(work_dict)
        return work_id
    
    async def get_works(self):
        works = await self.work_repo.find_all()
        return works
