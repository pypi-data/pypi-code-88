from delpha_db_manager.utils.aws import start_appflow, start_s3
import boto3
import json
import uuid
import io
import os
import string


class AppFlowManager:
    """
    Delpha AWS Salesforce data Handler
    :param key: String AWS key
    :param secret: String AWS secret
    :param flow_type: String Flow type to handle ['contact', 'account']
    :param bucket_name: String to use specific bucket
    :param region: String AWS region 
    """
    def __init__(self, key, secret, flow_type, bucket_name, region='eu-west-1'):
        self.CURRENT_BUCKET = bucket_name
        self.s3_handler = start_s3(key, secret, region)
        self.flow_handler = start_appflow(key, secret, region)
        self.buckets = None
        self.settings = {}
        self.current_settings = {}
        self._load_settings(flow_type)
        
    def _load_settings(self, flow_type):
        """
        Load buckets name from AWS
        """
        buckets = self.s3_handler.list_buckets()
        self.buckets = [bucket["Name"] for bucket in buckets["Buckets"]]
        self.settings = json.loads(self.s3_handler.get_object(Bucket=self.CURRENT_BUCKET, Key = "config/flow_settings.json")["Body"].read().decode('utf-8'))
        self.current_settings = self.settings[flow_type]
        self.current_settings["bucket_name"] = self.CURRENT_BUCKET
        
    def set_flow_settings(self, flow_type, bucket):
        """
        Set flow configuration
        :param flow_type: String Flow type to be used ['contact', 'account']
        """
        self.current_settings = self.settings[flow_type]
        self.current_settings["bucket_name"] = bucket
        
    def list_objects(self, bucket_name=None):
        """
        List all AWS object in S3 bucket
        :param bucket_name: String Bucket name to retrieve object from
        """
        if not isinstance(bucket_name, str):
            bucket_name = self.current_settings["bucket_name"]
        all_objects = self.s3_handler.list_objects(Bucket = bucket_name, Prefix = "Salesforce/Objects/", Delimiter = '/')
        all_objects = [prefix["Prefix"] for prefix in all_objects["CommonPrefixes"]]
        return all_objects
    
    def list_files(self, bucket_name=None, prefix=None):
        """
        List all files available within a bucket, regarding a certain prefix
        :param bucket_name: String Bucket name to retrieve files from
        :param prefix: String prefix path to use for file retrieval
        """
        if not isinstance(bucket_name, str):
            bucket_name = self.current_settings["bucket_name"]
        if not isinstance(prefix, str):
            prefix = self.current_settings["prefix"]
        list_obj = []
        kwargs = {'Bucket': bucket_name}
        if isinstance(prefix, str):
                kwargs['Prefix'] = prefix
        while True:
                resp = self.s3_handler.list_objects_v2(**kwargs)
                for obj in resp['Contents']:
                    key = obj['Key']
                    if key.startswith(prefix):
                        list_obj.append(key)
                try:
                    kwargs['ContinuationToken'] = resp['NextContinuationToken']
                except KeyError:
                    break
        return list_obj
    
    def get_flow_parquet_data(self, bucket_name=None, prefix=None, flow_name=None):
        """
        Load Flow data in a pd.DataFrame object
        :param bucket_name: String Bucket name to retrieve data from
        :param prefix: String prefix path to use for data retrieval
        :param flow_name: String Flow name to use
        """
        if not isinstance(bucket_name, str):
            bucket_name = self.current_settings["bucket_name"]
        if not isinstance(prefix, str):
            prefix = self.current_settings["prefix"]
        if not isinstance(flow_name, str):
            flow_name = self.current_settings["flow_name"]
        last_flow = self.get_last_flow_id(flow_name)
        file_folder = prefix+last_flow
        file_keys = handler.list_files(prefix=file_folder)
        def pd_read_s3_parquet(key, **args):
            print(key)
            obj = self.s3_handler.get_object(Bucket=self.current_settings["bucket_name"], Key=key)
            return pd.read_parquet(io.BytesIO(obj['Body'].read()), **args)
        dfs = [pd_read_s3_parquet(key=key) 
           for key in file_keys]
        
        return pd.concat(dfs, ignore_index=True)
    
    def start_flow(self, flow_name):
        """
        Start a Flow Process
        :param flow_name: String Name of the flow to trigger
        """
        flow_start_response = self.flow_handler.start_flow(flowName=flow_name)
        flow_status = flow_start_response["ResponseMetadata"]["HTTPStatusCode"]
        flow_last_execution_record = flow_start_response['executionId']
        return flow_status, flow_last_execution_record
    
    def ensure_spark_format(self, flow_name, suffix=".parquet"):
        """
        Function to be called on Spark loading to make sure data is in good format
        :param flow_name: String AppFlow name to be checked
        """
        prefix = self.current_settings["prefix"]
        last_flow = self.get_last_flow_id(flow_name)
        file_folder = prefix+last_flow
        file_keys = self.list_files(prefix=file_folder)
        if any(suffix in s for s in file_keys):
            return True
        else:
            for key in file_keys:
                self.s3_handler.copy_object(Bucket=self.current_settings['bucket_name'], CopySource="/"+self.current_settings['bucket_name']+"/"+key, Key=file_folder+"/"+str(uuid.uuid4())+suffix)
                self.s3_handler.delete_object(Bucket=self.current_settings['bucket_name'], Key=key)
        return True
    
    def get_last_flow_id(self, flow_name):
        """
        Get last folder ID for the requested flow
        :param flow_name: String AppFlow name to be checked
        """
        return self.flow_handler.describe_flow_execution_records(flowName=flow_name)["flowExecutions"].pop(0)["executionId"]
