from fastapi import APIRouter, status
from src.presentation.fastapi.schemas.product_schema import CreateProductSchema
from src.presentation.fastapi.schemas.product_discount_schema import CreateProductDiscountSchema
from src.services.product.product_dto import ProductDTO
from src.services.product_discounts.product_discounts_dto import ProductDiscountsDTO
from src.services.product.product_service import create_product , create_discount
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(schema: CreateProductSchema):
  
  uow = SqlAlchemyUnitOfWork()
  dto = ProductDTO(**schema.dict())
  product = create_product(product_dto= dto, uow=uow)
  
  return product

@router.post('/create discount', status_code= status.HTTP_201_CREATED)
def create_product_discount(schema:CreateProductDiscountSchema):
      
  uow = SqlAlchemyUnitOfWork()
  dto = ProductDiscountsDTO(**schema.dict())
  product_discount = create_discount(product_discount_dto=dto, uow= uow)
      
  return product_discount    

