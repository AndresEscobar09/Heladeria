from fastapi import FastAPI, APIRouter, Query, Path
from fastapi.responses import JSONResponse
from models.product import Product
from databases.products import upload_csv



router = APIRouter()
products =[
    {
        "id": 1,
        "name":"Cono 1",
        "price": 2000,
        "stock":81
    

    },
    {
        "id": 2,
        "name":"Cono 2",
        "price": 3800,
        "stock":100
        
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
            products[index]["stock"] = product.stock
    return products

# para borrar un producto

@router.delete("/products/{id}")
def delete_product(id: int):
    for item in products:
         if item['id'] == id:
            products.remove(item)

    return products

#@router.post("/products_csv/")
#def upload_products():
 #  return upload_csv()

# para leer el archibo csv

@router.get("/products/all/")
def products_all():
    return(upload_csv())


# para añadir productos al archivo csv

@router.put("/products/add/")
def product_add(product: Product):
    








