from abc import ABC, abstractmethod
from sqlalchemy import insert, select
from database.database import session as async_session


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self, data: dict):
        raise NotImplementedError
    
    @abstractmethod
    async def find_all(self):
        raise NotImplementedError

    @abstractmethod
    async def find_one(self, data: dict):
        raise NotImplementedError

class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def add_one(self, data: dict) -> int:
        async with async_session() as session:
            stmt = insert(self.model).values(**data).returning(self.model.id)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()
        
    async def find_all(self, **filter_by):
        async with async_session() as session:
            stmt = select(self.model).filter_by(**filter_by)
            res = await session.execute(stmt)
            objects = res.scalars().all()
            return [obj.to_read_model() for obj in objects]

    async def find_one(self, **filter_by):
        async with async_session() as session:
            stmt = select(self.model).filter_by(**filter_by)
            res = await session.execute(stmt)
            res = res.scalar_one_or_none()
            return res