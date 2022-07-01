from pydantic import BaseModel
from datetime import datetime
from typing import List

class picture_get(BaseModel):
    name: str
    created_on: datetime

    class Config:
        orm_mode = True

class pictures_in(BaseModel):
    names: List[str] =[]


class test_picture(picture_get):
    code_id: str

    class Config:
        orm_mode = True


class User(BaseModel):
    username: str
    hash_password: str

    class Config:
        orm_mode = True

class UserIn(BaseModel):
    username: str
    password : str



class UserBD(BaseModel):
    id: int
    username: str
    hash_password: str

    class Config:
        orm_mode = True