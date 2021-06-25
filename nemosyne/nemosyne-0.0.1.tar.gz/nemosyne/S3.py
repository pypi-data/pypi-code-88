import boto3
from dotenv import load_dotenv
import os
import typer


app = typer.Typer()

class Storage():
    def __init__(self):
        load_dotenv()
        access_key =os.getenv("access_key")
        secret_key = os.getenv('secret_key')
        endpoint = os.getenv('endpoint')
        self.bucket_name = os.getenv("bucket_name")
        session = boto3.session.Session()
        self.s3_client = session.client(
            service_name='s3',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            endpoint_url=endpoint,
            )
        self.s3_resource = boto3.resource(
        's3',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        endpoint_url=endpoint
    )
    def downloader(self):
        pass
    def uploader(self,file_name,bucket_name= None, object_name=None, ExtraArgs=None):
        
        if bucket_name is None:
            bucket_name = self.bucket_name
        if object_name is None:
            object_name=file_name
        self.s3_client.upload_file(file_name, bucket_name, object_name, ExtraArgs)
        return("https://{}.s3.ir-thr-at1.arvanstorage.com/{}".format(bucket_name,object_name))
        
    def unsignedDownloader(self):
        pass
    def unsignedUploader(self):
        pass
