import json
import os
from ..client import Boto3Client


class S3Client(Boto3Client):
    """
    """
    
    def __init__(self):
        """
        """
        super().__init__('s3')
        
    def upload_model(self,
                     bucket: str,
                     project_name: str,
                     version_id: int,
                     model_name: str,
                     filepath: str):
        """
        """
        file_path = f"{project_name}/versions/{version_id}/models/{model_name}/model.pb"
        self.upload_file(filepath, Bucket=bucket, Key=file_path)
        
    def download_model(self,
                       bucket: str,
                       project_name: str,
                       version_id: int,
                       model_name: str,
                       filepath: str = 'model.pb') -> str:
        """
        """
        file_path = f"{project_name}/versions/{version_id}/models/{model_name}/model.pb"
        self.download_file(bucket, file_path, filepath)
        return filepath
    
    def upload_model_parameters(self,
                                bucket: str,
                                project_name: str,
                                version_id: int,
                                model_name: str,
                                parameters: dict = {}):
        """
        """
        file_path = f"{project_name}/versions/{version_id}/models/{model_name}/parameters.json"
        self.put_object(Body=json.dumps(parameters).encode(), Bucket=bucket, Key=file_path)
        
    def get_model_parameters(self,
                             bucket: str,
                             project_name: str,
                             version_id: int,
                             model_name: str) -> dict:
        """
        """
        file_path = f"{project_name}/versions/{version_id}/models/{model_name}/parameters.json"
        self.download_file(bucket, file_path, 'tmp.json')
        parameters = json.load(open('tmp.json', 'r'))
        os.remove('tmp.json')
        return parameters
    
    def create_account_bucket(self,
                              name: str,
                              region: str = 'eu-west-3') -> str:
        """
        """
        bucket_name = f'np-{name}-bucket'
        location = {'LocationConstraint': region}
        self.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
        return bucket_name

