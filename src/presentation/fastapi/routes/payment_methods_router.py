from fastapi import APIRouter, status
from src.presentation.fastapi.schemas.payment_method_schema import CreatePaymentMethodSchema
from src.services.payment_method.payment_method_dto import PaymentMethodDTO
from src.services.payment_method.payment_method_service import create_payment_method
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork

router = APIRouter()

@router.post('/', status_code= status.HTTP_201_CREATED)
def create (schema: CreatePaymentMethodSchema):

    uow = SqlAlchemyUnitOfWork()
    dto = PaymentMethodDTO(**schema.dict())
    payment_method = create_payment_method(payment_method_dto= dto, uow= uow)

    return payment_method