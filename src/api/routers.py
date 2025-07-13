from api.details import router as detail_router
from api.works import router as works_router
from api.tasks import router as task_router

all_routers = [
    detail_router,
    works_router,
    task_router
]
