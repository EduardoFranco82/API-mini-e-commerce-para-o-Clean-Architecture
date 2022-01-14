from dataclasses import dataclass

@dataclass
class ProductDiscountsDTO:
    mode: str
    value: float
    product_id: int
    payment_method_id: int