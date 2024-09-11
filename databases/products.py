from io import StringIO
from fastapi import UploadFile,File, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd
import json


dFrame = pd.read_csv("databases/productos_heladeria.csv")

def read_products():
    Json_data = dFrame.to_json(orient="records")
    json_out = json.loads(Json_data)
    return json_out


