from sqlalchemy import create_engine,String,DateTime,Column
import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import  sessionmaker
from settings import setting
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
database_url = f"postgresql+psycopg2://postgres:{setting.database_password}@localhost/{setting.database_name}"
engine=create_engine(database_url)
Session = sessionmaker(engine)
Base = declarative_base()

class Inbox(Base):
    __tablename__ = 'inbox'
    code_id = Column(String(100), primary_key=True)
    name = Column(String(100), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)

Base.metadata.create_all(engine)

def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()