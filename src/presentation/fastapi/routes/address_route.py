from audioop import add
from fastapi import APIRouter, status
from src.services.customer.customer_service import create_address
from src.presentation.fastapi.schemas.address_schema import CreateAddressSchema
from src.services.address.address_dto import AddressDTO
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork

router = APIRouter()

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(schema:CreateAddressSchema):
    uow = SqlAlchemyUnitOfWork()
    dto = AddressDTO(**schema.dict())

    address =create_address(dto,uow)
    return address