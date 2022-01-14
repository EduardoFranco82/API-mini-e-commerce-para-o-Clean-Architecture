from pydantic import BaseModel

class CreateProductSchema(BaseModel):
  description: str
  price: float
  technical_details: str
  image: str
  visible: bool
  categorie_id: int
  supplier_id: int