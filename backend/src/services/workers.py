from utils.repository import AbstractRepository
from schemas.workers import WorkerAddSchema


class WorkerService:
    def __init__(self, workers_repo: AbstractRepository):
        self.workers_repo: AbstractRepository = workers_repo()

    async def add_worker(self, worker: WorkerAddSchema):
        workers_dict = worker.model_dump()
        worker_id = await self.workers_repo.add_one(workers_dict)
        return worker_id
    
    async def get_worker(self, worker_id):
        worker = await self.workers_repo.find_one(id=worker_id)
        return worker
    
    async def get_workers(self):
        workers = await self.workers_repo.find_all()
        return workers
