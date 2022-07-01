from database import get_session
from fastapi import Depends
from sqlalchemy.orm import Session
from database import Inbox,Users
import uuid
from schemas import UserBD
import passlib.hash


class Crud:
    def __init__(self,session:Session = Depends(get_session)):
        self.session = session

    def get_pictures(self,file_uuid):
        pictures = (
                self.session
                .query(Inbox.name, Inbox.created_on)
                .filter(Inbox.code_id == file_uuid)
                .first()
        )
        return pictures

    def insert_pictures(self,filename,created_on):
        x = Inbox(
            name=filename,
            created_on=created_on,
            code_id=str(uuid.uuid4())
        )
        self.session.add(x)
        self.session.commit()

    def take_uuid(self,filename):
        code = dict((
                self.session
                .query(Inbox.code_id)
                .filter(Inbox.name == filename)
                .first()
        ))

        return code['code_id']

    def get_bucket(self,file_uuid):
        date = dict((
                self.session
                .query(Inbox.created_on)
                .filter(Inbox.code_id == file_uuid)
                .first()

        ))
        date = date['created_on']
        return str(date)[:10]


    def delete_picture(self,file_uuid):
        i = self.session.query(Inbox).filter(Inbox.code_id == file_uuid).one()
        self.session.delete(i)
        self.session.commit()


    def take_random_uuid(self):
        code = dict((
                self.session
                .query(Inbox.code_id)
                .first()
        ))

        return code['code_id']


    def insert_users(self, username, hash_password):
        user = Users(
            username=username,
            hash_password=hash_password
        )
        self.session.add(user)
        self.session.commit()



    def authenticate_user(self,username: str, password: str):
        user = (
            self.session
            .query(Users)
            .filter(Users.username == username)
            .first() )

        q = UserBD.from_orm(user)

        if not user:
            return 'False'

        if not passlib.hash.bcrypt.verify(password,user.hash_password):
            return False

        return q









