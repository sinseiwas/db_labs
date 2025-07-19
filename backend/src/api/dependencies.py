from repositories.details import DetailsRepository
from repositories.works import WorkRepository
from repositories.tasks import TaskRepository
from repositories.workers import WorkerRepository

from services.details import DetailService
from services.works import WorksService
from services.tasks import TaskService
from services.workers import WorkerService

def details_service() -> DetailService:
    return DetailService(DetailsRepository)

def works_service():
    return WorksService(WorkRepository)

def tasks_service():
    return TaskService(TaskRepository)

def workers_service():
    return WorkerService(WorkerRepository)
