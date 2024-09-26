from fastapi import APIRouter, Query, Path # type: ignore
from models.product import Product
import pandas as pd
from databases.products import read_products
from databases.products import product_add

dFrame = pd.read_csv("databases/productos_heladeria.csv")

router = APIRouter()
products =[
    {
        "id": 1,
        "name":"Cono 1",
        "price": 2000,
        "description": "helado de 1 bolita"
    

    },
    {
        "id": 2,
        "name":"Cono 2",
        "price": 3800,
        "description":"helado de 2 bolitas"
        
    }
]

@router.get("/products")
def all_products():
    return products


@router.get("/products/{id}")
def get_products(id: int = Path(gt=0)): # se hace una validacion solo se permite numeros positivos.
    return list(filter(lambda item: item["id"] == id, products))

# ejemplo de parametro query

@router.get("/products/")
def get_products_by_stock(stock: int=Query(gt=0)):
    return list(filter(lambda item: item["stock"] == stock, products))

#  para crear un producto

@router.post("/products")
def create_product(product: Product):
    products.append(product)
    return products

# para modificar un producto

@router.put("/products/{id}")
def update_product(id: int, product: Product):
    for index, item in enumerate(products):
        if item['id'] == id:
            products[index]["name"] = product.name
            products[index]["price"] = product.price
            products[index]["description"] = product.description
    return products

# para borrar un producto

@router.delete("/products/{id}")
def delete_product(id: int):
    for item in products:
         if item['id'] == id:
            products.remove(item)

    return products


@router.get("/products/all/")
def products_all():
    products = read_products()

    return products

@router.post("/product/add")    
def add_product(product: Product):
    product_add(product)
    #print(type(product))
    return 'el producto fue creado exitosamente'

@router.put("/product/{id}")
def edit_product(id: int, product: Product):
    product_edit(id,product)
    return("el producto fue modificado exitosamente")




