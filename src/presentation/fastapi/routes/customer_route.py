from fastapi import APIRouter, status
from src.services.customer.customer_service import create_custumer
from src.services.customer.customer_dto import CustomerDTO
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork
from src.presentation.fastapi.schemas.customer_schema import CreateCustomerSchema

router = APIRouter()

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(schema:CreateCustomerSchema):
    
    uow = SqlAlchemyUnitOfWork()
    dto = CustomerDTO(**schema.dict())
    customer = create_custumer(custumer_dto=dto,uow=uow)
   
    return customer