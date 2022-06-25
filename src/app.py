import shutil
import uuid
import os
from minio_data import Data
from fastapi import FastAPI,Depends,UploadFile
from database import Inbox,get_session
from typing import List
from sqlalchemy.orm import  Session
from models import picture_get
from datetime import datetime,date
from models import pictures_in
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
def save_file(files: List[UploadFile],session: Session = Depends(get_session)):
    filesname= pictures_in()
    if Data.client.bucket_exists(str(date.today())):
        pass
    else:
        Data.make(str(date.today()))
    for file in files:
        with open(file.filename,'wb') as buffer:
            shutil.copyfileobj(file.file,buffer)

        x= Inbox(
            name = file.filename,
            created_on = datetime.now(),
            code_id = str(uuid.uuid4())
        )
        session.add(x)
        session.commit()

        code = dict((
            session
                .query(Inbox.code_id)
                .filter(Inbox.name == file.filename)
                .first()

        ))
        code_new = code['code_id']
        Data.client.fput_object(str(date.today()),code_new,file.filename)
        os.remove(file.filename)
        filesname.names.append(file.filename)
    return filesname

