from src.domain.address.model import Address
from src.adapter.sqlalchemy_repository import SqlAlchemyRepository


class AddreesRepository(SqlAlchemyRepository[Address]):
  pass