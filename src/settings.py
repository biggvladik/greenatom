from pydantic import BaseSettings


class Settings(BaseSettings):
    database_password:str = "password"
    database_name:str = "greenatom"
    minio_url:str = '127.0.0.1:9000'
    minio_access_key = 'minioadmin'
    minio_secret_key = 'minioadmin'


setting = Settings()
