from src.domain.payment_method.model import Payment_Method
from src.adapter.sqlalchemy_repository import SqlAlchemyRepository


class Payment_Method_Repository(SqlAlchemyRepository[Payment_Method]):
  pass