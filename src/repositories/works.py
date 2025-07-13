from models.works import Work
from utils.repository import SQLAlchemyRepository


class WorkRepository(SQLAlchemyRepository):
    model = Work
