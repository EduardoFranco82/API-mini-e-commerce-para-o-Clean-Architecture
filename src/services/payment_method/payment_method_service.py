from src.domain.payment_method.model  import Payment_Method
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork
from src.services.payment_method.payment_method_dto import PaymentMethodDTO

def create_payment_method(payment_method_dto: PaymentMethodDTO, uow: SqlAlchemyUnitOfWork):
  with uow:
    uow.payment_method_repository.add(Payment_Method(name=payment_method_dto.name,
                                                      enabled= payment_method_dto.enabled))
    uow.commit()
    