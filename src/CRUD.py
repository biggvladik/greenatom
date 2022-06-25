from database import get_session
from fastapi import Depends
from sqlalchemy.orm import Session
from database import Inbox
class Crud:
    def __init__(self,session:Session = Depends(get_session)):
        self.session = session

    def get_pictures(self,file_uuid):
        query = self.session.query(Inbox)
        pictures = (
                self.session
                .query(Inbox.name, Inbox.created_on)
                .filter(Inbox.code_id == file_uuid)
                .first()
        )
        return pictures
