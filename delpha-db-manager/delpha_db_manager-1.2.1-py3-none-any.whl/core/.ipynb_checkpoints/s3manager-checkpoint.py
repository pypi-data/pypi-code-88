from delpha_db_manager.utils.aws import start_s3
import boto3
import json
import uuid
import io
import os
import string


class S3Manager:
    """
    Delpha AWS Salesforce data Handler - S3
    :param key: String AWS key
    :param secret: String AWS secret
    :param region: String AWS region 
    """
    def __init__(self, key, secret, region):
        self.handler = start_s3(key, secret, region)
        self.buckets = self.list_buckets()
    
    def list_buckets(self):
        try:
            return self.handler.list_buckets()['Buckets']
        except:
            return list()
        
    def create_bucket(self, bucket_name, region):
        return self.handler.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': region,
            },
        )
        
    def list_files(self, bucket_name, prefix=None):
        """
        List all files available within a bucket, regarding a certain prefix
        :param bucket_name: String Bucket name to retrieve files from
        :param prefix: String possible prefix path to use for file retrieval
        """
        list_obj = []
        kwargs = {'Bucket': bucket_name}
        if isinstance(prefix, str):
                kwargs['Prefix'] = prefix
        while True:
                resp = self.handler.list_objects_v2(**kwargs)
                for obj in resp['Contents']:
                    key = obj['Key']
                    if key.startswith(prefix):
                        list_obj.append(key)
                try:
                    kwargs['ContinuationToken'] = resp['NextContinuationToken']
                except KeyError:
                    break
        return list_obj
