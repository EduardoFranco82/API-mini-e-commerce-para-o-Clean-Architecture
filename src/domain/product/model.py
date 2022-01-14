from typing import List
from src.domain.categorie.model import Categorie
from src.domain.supplier.model import Supplier
from src.domain.product_discounts.model import ProductDiscount


class Product:
    def __init__(self, description: str, price: float,
     technical_details: str, image: str, visible: bool,
      categorie: Categorie, supplier: Supplier):
        self.description = description
        self.price = price
        self.technical_details = technical_details
        self.image = image
        self.visible = visible
        self.categorie = categorie
        self.supplier = supplier
        self.discounts : List[ProductDiscount] = []

    def add_discount(self, discount: ProductDiscount):
        if not discount.payment_method.enabled:
            raise Exception('Este método de pagamento não está disponível')
        
        has_discount = len(list(filter(lambda d: d.payment_method.id == discount.payment_method.id, self.discounts))) > 0
        if has_discount:
            raise Exception(f'Já existe um desconto para este método de pagammento: {discount.payment_method.name}')

        self.discounts.append(discount)