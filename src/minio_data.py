import datetime

from minio import Minio
from settings import setting
from datetime import date


class Data_minio:
    def __init__(self):
        self.client = Minio(setting.minio_url, access_key=setting.minio_access_key, secret_key=setting.minio_secret_key, secure=False)

    def make(self,name:str):
        self.client.make_bucket(name)


Data = Data_minio()

Data.client.fput_object(str(date.today()), "qwerty", 'models.py')
