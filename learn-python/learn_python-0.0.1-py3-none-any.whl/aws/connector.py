import boto3

ACCESS_KEY = ""
SECRET_KEY = ""
REGION = 'eu-west-3'


def create_client(resource, region=REGION):
    client = boto3.client(
        resource,
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
        region_name=region
    )
    return client


def session():
    return boto3.Session(
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
        region_name=REGION
    )
