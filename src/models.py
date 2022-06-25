from pydantic import BaseModel
from datetime import date


class picture_get(BaseModel):
    name: str
    created_on: date
    class Config:
        orm_mode = True

