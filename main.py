from fastapi import FastAPI#, Query, Path
#from models.product import Product
from routers.product import router as product_router


app = FastAPI()
app.include_router(product_router)



@app.get("/")
def index():
    return "hola heladeria"


    