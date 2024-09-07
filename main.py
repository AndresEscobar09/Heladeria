from fastapi import FastAPI 
from models.product import Product

app = FastAPI()

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


@app.get("/")
def index():
    return "hola heladeria"

@app.get("/products")
def all_products():
    return products


@app.get("/products/{id}")
def get_products(id: int):
    return list(filter(lambda item: item["id"] == id, products))

# ejemplo de parametro query

@app.get("/products/")
def get_products_by_stock(stock: int):
    return list(filter(lambda item: item["stock"] == stock, products))

#  para crear un producto

@app.post("/products")
def create_product(product: Product):
    products.append(product)
    return products

# para modificar un producto

@app.put("/products/{id}")
def update_product(id: int, product: Product):
    for index, item in enumerate(products):
        if item['id'] == id:
            products[index]["name"] = product.name
            products[index]["price"] = product.price
            products[index]["stock"] = product.stock
    return products

# para borrar un producto

@app.delete("/products/{id}")
def delete_product(id: int):
    for item in products:
         if item['id'] == id:
            products.remove(item)

    return products
    