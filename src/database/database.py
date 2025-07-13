from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker
    )
# from sqlalchemy import text
from sqlalchemy.orm import DeclarativeBase

# from contextlib import asynccontextmanager
import config


engine = create_async_engine(
    url=config.settings.DATABASE_URL_asyncpg,
    echo=True
)

session = async_sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    expire_on_commit=True,
    class_=AsyncSession,
)


async def get_session():
    async with session() as db_session:
        yield db_session


class Base(DeclarativeBase):
    pass


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all, checkfirst=True)
        await conn.run_sync(Base.metadata.create_all)
