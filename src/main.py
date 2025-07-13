import asyncio
from fastapi import FastAPI
import uvicorn
import os

from database.database import init_db
from api.routers import all_routers
import config


app = FastAPI()


for router in all_routers:
    app.include_router(router)


async def main():
    if not os.path.exists(config.settings.DATABASE_URL_asyncpg):
        await init_db()

if __name__ == "__main__":
    asyncio.run(main())
    uvicorn.run(app="main:app", reload=True)
