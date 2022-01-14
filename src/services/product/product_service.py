from src.domain.product.model import Product
from src.domain.product_discounts.model import ProductDiscount
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork
from src.services.product.product_dto import ProductDTO
from src.services.product_discounts.product_discounts_dto import ProductDiscountsDTO


def create_product(product_dto: ProductDTO, uow: SqlAlchemyUnitOfWork):
  with uow:
    categorie = uow.categorie_repository.get(id= product_dto.categorie_id)
    if not categorie:
      raise Exception('Categorie not found')

    supplier = uow.supplier_repository.get(id=product_dto.supplier_id)
    if not supplier:
      raise Exception('Supplier not found')
    
    product = Product(description=product_dto.description, price=product_dto.price,
                     technical_details=product_dto.technical_details, image=product_dto.image,
                      visible=product_dto.visible, categorie=categorie, supplier=supplier)

    uow.product_repository.add(product)
    uow.commit()
  

def create_discount(product_discount_dto: ProductDiscountsDTO, uow: SqlAlchemyUnitOfWork):
  with uow:
    product = uow.product_repository.get(id=product_discount_dto.product_id)
    if not product:
      raise Exception('Product not found')

    payment_method = uow.payment_method_repository.get(id=product_discount_dto.payment_method_id)
    if not payment_method:
      raise Exception('Payment method not found')

    discount = ProductDiscount(mode=product_discount_dto.mode, value=product_discount_dto.value, payment_method=payment_method)
    product.add_discount(discount)

    uow.commit()