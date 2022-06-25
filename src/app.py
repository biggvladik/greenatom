import shutil
import io
from minio_data import Data
from fastapi import FastAPI,Depends, File,UploadFile
from database import Inbox,get_session
from typing import List
from sqlalchemy.orm import  Session
from models import picture_get
from datetime import date
app= FastAPI()
@app.get("/frames/{file_uuid}", response_model=picture_get)
def get_picture(file_uuid,session: Session = Depends(get_session)):
    pictures = (
        session
            .query(Inbox.name, Inbox.created_on)
            .filter(Inbox.code_id == file_uuid)
            .first()
    )

    return picture_get.from_orm(pictures)

@app.post("/frames")
def save_file(file: UploadFile = File()):
    if Data.client.bucket_exists(str(date.today())):
        pass
    else:
        Data.make(str(date.today()))
    content = file.read()
    with open(file.filename,'wb') as buffer:
        shutil.copyfileobj(file.file,buffer)

    Data.client.fput_object(str(date.today()),file.filename,file.filename)
    shutil.rmtree()






