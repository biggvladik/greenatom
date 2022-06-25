from sqlalchemy import create_engine,String,Date,Column
import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import  sessionmaker
from settings import setting
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID

engine=create_engine(setting.database_url)


Session = sessionmaker(engine)
Base = declarative_base()

class Inbox(Base):
    __tablename__ = 'inbox'
    code_id = Column(UUID(), primary_key=True)
    name = Column(String(100), nullable=False)
    created_on = Column(Date(), default=datetime.now)

Base.metadata.create_all(engine)

def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()