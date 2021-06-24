import logging as logger
from src.aws import create_client
from botocore.exceptions import ClientError

s3_client = create_client('s3')


def create_bucket(bucket_name, region=None):
    try:
        if region is None:
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
    except ClientError as e:
        logger.error(e)
        return False
    return True


def list_all_bucket():
    response = s3_client.list_buckets()
    for bucket in response['Buckets']:
        print("{}".format(bucket["Name"]))


def delte_bucket():
    pass


if __name__ == '__main__':
    print("1- Create bucket")
    create_bucket("test-bucket-py-massi")
    list_all_bucket()
