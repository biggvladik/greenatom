from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
import jwt
from schemas import UserBD
from database import database_url
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from database import Users
from settings import setting



oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


def get_current_user( token: str = Depends(oauth2_scheme)):
    payload = jwt.decode(token, setting.JWT_SECRET,algorithms=['HS256'])
    session = Session(bind=create_engine(database_url))

    user = (
        session
            .query(Users)
            .filter(Users.id == payload.get('id'))
            .first())
    return UserBD.from_orm(user)