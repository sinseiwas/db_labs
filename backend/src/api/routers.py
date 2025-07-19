from api.details import router as details_router
from api.works import router as works_router
from api.tasks import router as tasks_router
from api.workers import router as workers_router

all_routers = [
    details_router,
    works_router,
    tasks_router,
    workers_router
]
