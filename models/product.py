from pydantic import BaseModel, Field
from typing import Optional


class Product(BaseModel):
    
    id: Optional[int] = None
    name: str
    price: float = Field(default=0, gt=0)# indica que acepta solo valores positivos
    caracteristic: str  