from pydantic import BaseModel
from datetime import date
from typing import List

class picture_get(BaseModel):
    name: str
    created_on: date
    class Config:
        orm_mode = True

class pictures_in(BaseModel):
    names: List[str] =[]


