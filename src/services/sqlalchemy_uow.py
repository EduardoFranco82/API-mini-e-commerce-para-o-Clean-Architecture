from src.adapter.repositories.categorie_repository import CategorieRepository
from src.adapter.repositories.payment_method_repository import Payment_Method_Repository
from src.adapter.repositories.supplier_repository import SupplierRepository
from src.adapter.repositories.product_repository import ProductRepository
from src.adapter.repositories.coupon_repository import CouponRepository
from src.adapter.repositories.address_repository import AddreesRepository
from src.adapter.repositories.customer_repository import CustomerRepository
from src.adapter.repositories.product_discount_repository import Product_discount_Repository
from src.domain.categorie.model import Categorie
from src.domain.supplier.model import Supplier
from src.domain.payment_method.model import Payment_Method
from src.domain.product.model import Product
from src.domain.coupon.model import Coupon
from src.domain.address.model import Address
from src.domain.customer.model import Customer
from src.domain.product_discounts.model import ProductDiscount
from src.adapter.database import Session


class SqlAlchemyUnitOfWork:
  def __init__(self):
      self.session = Session()


  def __enter__(self):
    self.payment_method_repository = Payment_Method_Repository(self.session, Payment_Method)
    self.categorie_repository = CategorieRepository(self.session, Categorie)
    self.supplier_repository = SupplierRepository(self.session, Supplier)
    self.product_repository = ProductRepository(self.session, Product)
    self.coupon_repository = CouponRepository(self.session, Coupon)
    self.address_repository = AddreesRepository(self.session, Address)
    self.customer_repository = CustomerRepository(self.session, Customer)
    self.product_discount_repository = Product_discount_Repository(self.session, ProductDiscount)
    

  def __exit__(self, *args):
    self.session.rollback()
    self.session.close()

  def commit(self):
    self.session.commit()