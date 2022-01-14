from src.domain.categorie.model import Categorie
from src.adapter.sqlalchemy_repository import SqlAlchemyRepository


class CategorieRepository(SqlAlchemyRepository[Categorie]):
  pass