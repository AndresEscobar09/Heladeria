from fastapi import FastAPI 
from Models.product import product

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


@app.post("/products")
def create_product(product: Product):
    products.append(product)
    return products