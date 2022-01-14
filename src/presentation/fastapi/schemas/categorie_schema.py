from pydantic import BaseModel

class CreateCategorieSchema(BaseModel):
    name:str
