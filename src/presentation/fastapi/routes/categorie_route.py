from fastapi import APIRouter,status
from src.services.categorie.categorie_dto import CategorieDTO
from src.services.categorie.categorie_service import create_category
from src.presentation.fastapi.schemas.categorie_schema import CreateCategorieSchema
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED)
def create (schema: CreateCategorieSchema):
    
    uow = SqlAlchemyUnitOfWork()
    dto = CategorieDTO(**schema.dict())
    categorie = create_category(categorie_dto= dto, uow= uow)

    return categorie