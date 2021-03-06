import shutil
import os
from fastapi.security import OAuth2PasswordRequestForm
from CRUD import Crud
from minio_data import Data
from fastapi import FastAPI,Depends,UploadFile,HTTPException
from typing import List
from datetime import datetime,date
from schemas import pictures_in,UserIn,picture_get,User
from passlib.hash import bcrypt
import jwt
from auth import get_current_user
from settings import setting



app= FastAPI()





@app.get("/frames/{file_uuid}", response_model=picture_get)
async def get_picture(file_uuid:str,service: Crud = Depends(Crud)):
    pictures = service.get_pictures(file_uuid)
    if not pictures:
        raise HTTPException(status_code=404, detail="Item not found")
    return pictures



@app.post("/frames/")
async def save_file(files: List[UploadFile],service: Crud = Depends(Crud),user:User = Depends(get_current_user)):
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



@app.delete("/frames/{file_uuid}")
async def delete_pictures(file_uuid:str,service: Crud = Depends(Crud)):

    bucket = service.get_bucket(file_uuid)
    service.delete_picture(file_uuid)
    Data.delete_picture(bucket,file_uuid)

    return {}



@app.post('/token')
def generate_token(form_data:OAuth2PasswordRequestForm =Depends(),service: Crud = Depends(Crud)):
    user = service.authenticate_user(form_data.username,form_data.password)

    if not user:
        return {'error':'invalid credentials'}

    token = jwt.encode(user.dict(),setting.JWT_SECRET)

    return {
        'access_token': token,
        'token_type': 'bearer'
    }

@app.post('/users', response_model = User)
async def create_user(user:UserIn,service:Crud = Depends(Crud)):
    user_obj = User(username = user.username,
                    hash_password = bcrypt.hash(user.password) )
    service.insert_users(user_obj.username,user_obj.hash_password)

    return user_obj



