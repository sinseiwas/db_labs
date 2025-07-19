from models.details import Detail
from utils.repository import SQLAlchemyRepository


class DetailsRepository(SQLAlchemyRepository):
    model = Detail
