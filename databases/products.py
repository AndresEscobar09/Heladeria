from io import StringIO
from pydantic import BaseModel, Field # type: ignore
from typing import Optional
import pandas as pd # type: ignore
import json
import csv



class Product(BaseModel):
    
    id: int
    name: str
    price: float = Field(default=0, gt=0)# indica que acepta solo valores positivos
    description: str  


products_csv = "databases/productos_heladeria.csv"


def read_products():
    dFrame = pd.read_csv(products_csv)
    Json_data = dFrame.to_json(orient="records")
    json_out = json.loads(Json_data)
    return json_out


campos = ['id','name','price','description']



def product_add(product: Product):
    with open(products_csv,mode='a', newline='') as archivo:
        new_product =vars(product)
        write_product = csv.DictWriter(archivo, fieldnames=campos)
        write_product.writerow(new_product)
        