from src.domain.payment_method.model import Payment_Method


class ProductDiscount:
  def __init__(self, mode: str, value: float, payment_method: Payment_Method):
      self.mode = mode
      self.value = value
      self.payment_method = payment_method