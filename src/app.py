import shutil
import os
from CRUD import Crud
from minio_data import Data
from fastapi import FastAPI,Depends,UploadFile
from typing import List
from schemas import picture_get
from datetime import datetime,date
from schemas import pictures_in
app= FastAPI()


@app.get("/frames/{file_uuid}", response_model=picture_get)
def get_picture(file_uuid:str,service: Crud = Depends(Crud)):
    pictures = service.get_pictures(file_uuid)
    return pictures



@app.post("/frames")
def save_file(files: List[UploadFile],service: Crud = Depends(Crud)):
    filesname= pictures_in()
    if Data.client.bucket_exists(str(date.today())):
        pass
    else:
        Data.make_picture(str(date.today()))
    for file in files:
        with open(file.filename,'wb') as buffer:
            shutil.copyfileobj(file.file,buffer)

        service.insert_pictures(file.filename,datetime.now())

        code_new = service.take_uuid(file.filename)
        Data.upload_picture(code_new,file.filename)

        os.remove(file.filename)
        filesname.names.append(file.filename)

    return filesname



@app.delete("/frames{file_uuid}")
def delete_pictures(file_uuid:str,service: Crud = Depends(Crud)):

    bucket = service.get_bucket(file_uuid)
    service.delete_picture(file_uuid)
    Data.delete_picture(bucket,file_uuid)
