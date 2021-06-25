import boto3
import os
from config import access_key,endpoint, secret_key , bucket_name

session = boto3.session.Session()

s3_client = session.client(
    service_name='s3',
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    endpoint_url=endpoint,
    )

# file_name = "carpet_staticData.tar.gz"
object_name = "sourceList"


def uploader(file_name,bucket_name, object_name=None, ExtraArgs=None):
    if object_name is None:
        object_name=file_name
    s3_client.upload_file(file_name, bucket_name, object_name, ExtraArgs)

    return("https://{}.s3.ir-thr-at1.arvanstorage.com/{}".format(bucket_name,object_name))


# url = uploader(file_name, bucket_name, object_name, ExtraArgs={'ACL':'public-read'})

# print(url)
s3_resource = boto3.resource(
        's3',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        endpoint_url=endpoint
    )
bucket = s3_resource.Bucket('git')
download_path = "inja/"+object_name
print(download_path)
bucket.download_file(
            object_name,
            download_path
        )