
from minio import Minio
from settings import setting
from datetime import date

class Data_minio:
    def __init__(self):
        self.client = Minio(setting.minio_url, access_key=setting.minio_access_key, secret_key=setting.minio_secret_key, secure=False)

    def make_picture(self,name:str):
        self.client.make_bucket(name)

    def upload_picture(self,code_new,filename):
        self.client.fput_object(str(date.today()), code_new, filename)

    def delete_picture(self,bucket,file_uuid):
        self.client.remove_object(bucket, file_uuid)



Data = Data_minio()


