from src.domain.categorie.model import Categorie
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork
from src.services.categorie.categorie_dto import CategorieDTO

def create_category(categorie_dto:CategorieDTO, uow: SqlAlchemyUnitOfWork):
  with uow:
    uow.categorie_repository.add(Categorie(name=categorie_dto.name))
    uow.commit()
    