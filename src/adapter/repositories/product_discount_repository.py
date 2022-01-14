from src.domain.product_discounts.model import ProductDiscount
from src.adapter.sqlalchemy_repository import SqlAlchemyRepository


class Product_discount_Repository(SqlAlchemyRepository[ProductDiscount]):
  pass