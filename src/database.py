from sqlalchemy import create_engine,String,DateTime,Column,Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import  sessionmaker
from settings import setting
from datetime import datetime
from sqlalchemy_utils import database_exists, create_database


database_url = f"postgresql+psycopg2://postgres:{setting.database_password}@localhost/{setting.database_name}"
engine=create_engine(database_url)
Session = sessionmaker(engine)
Base = declarative_base()

if not database_exists(engine.url):
    create_database(engine.url)


class Inbox(Base):
    __tablename__ = 'inbox'
    code_id = Column(String(100), primary_key=True)
    name = Column(String(100), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)



class Users(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)
    hash_password = Column(String(150), nullable=False)




Base.metadata.create_all(engine)

def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()