import asyncio

from models.details import Detail
from models.task_types import TaskType
from models.workers import Worker
from models.tasks import Task
from models.works import Work

from database.database import init_db


async def main():
    await init_db()


if __name__ == "__main__":
    asyncio.run(main())
