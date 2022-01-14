from src.domain.coupon.model import Coupon
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork
from src.services.coupon.coupon_dto import CouponDTO

def create_coupon(coupon_dto: CouponDTO, uow: SqlAlchemyUnitOfWork):
  with uow:

    if uow.coupon_repository.get(code =coupon_dto.code):
          raise Exception ('coupon already exists') 
    
    uow.coupon_repository.add(Coupon(code=coupon_dto.code,
                                     limit = coupon_dto.limit,
                                     expire_at= coupon_dto.expire_at,
                                    type=coupon_dto.type,
                                     value=coupon_dto.value))

    
    uow.commit()
    
