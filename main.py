from fastapi import FastAPI# type: ignore #, Query, Path

from routers.product import router as product_router


app = FastAPI()

@app.get("/")
def index():
    return "hola heladeria"


app.include_router(product_router)



    