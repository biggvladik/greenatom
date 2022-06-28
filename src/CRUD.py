from database import get_session
from fastapi import Depends
from sqlalchemy.orm import Session
from database import Inbox
import uuid


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











