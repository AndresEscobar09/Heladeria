from io import StringIO
from fastapi import UploadFile,File, HTTPException
import pandas as pd


data = {
    "Item": ["cono 1","cono 2","canasta 2"],
    "Precio": [2000,3800,3800],
    "Description": ["una bola de helado servida en un cono de galleta, decorado con una galleta de corazon salsa y chispitas","dos bolas de helado servidas en un cono de galleta, decorado con una galleta de corazon salsa y chispitas","dos bolas de helado servidas en una canasta de galleta, decorado con una galleta de corazon salsa y chispitas",] 
}





dframe = {}

async def upload_csv(file: UploadFile = File("databases/productos_heladeria.csv")):
    
    try:
        # se lee el archivo csv en un dataframe de pandas
        content = await file.read()
        df = pd.read_csv(StringIO(content.decode('utf-8')))
        
        # se guarda el dataframe en el diccionario usando como "key" el nombre del archivo
        dframe[file.productos_heladeria] = df
        
      #  return "el archivo se ha subido con exito"
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

#dframe.to_csv('databases/productos_heladeria.csv',index=False)

