from pydantic import BaseSettings


class Settings(BaseSettings):
    database_password:str = "vladzuev201555"
    database_name:str = "greenatom"
    minio_url:str = '127.0.0.1:9000'
    minio_access_key = 'minioadmin'
    minio_secret_key = 'minioadmin'
    JWT_SECRET = 'SECRET'


setting = Settings()
