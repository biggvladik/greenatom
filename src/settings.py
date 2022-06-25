from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url:str = "postgresql+psycopg2://postgres:vladzuev201555@localhost/appi"
    minio_url:str = '127.0.0.1:9000'
    minio_access_key = 'minioadmin'
    minio_secret_key = 'minioadmin'


setting = Settings()
