from io import StringIO
from fastapi import UploadFile,File, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd


dFrame = pd.read_csv("databases/productos_heladeria.csv", encoding="utf-8")

#print(dFrame)
def upload_csv():
    Json_data = dFrame.to_json(orient = "records",)

    #print(JSONResponse(content=dFrame.to_dict(orient="records")))

    #return JSONResponse(content=dFrame.to_dict(orient="records"))
    return Json_data

print(upload_csv())