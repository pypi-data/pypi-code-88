
from typing import Optional


class ScanflowSecret():
    def __init__(self,
        AWS_ACCESS_KEY_ID : Optional[str] = "admin",
        AWS_SECRET_ACCESS_KEY : Optional[str] = "admin123",
        MLFLOW_S3_ENDPOINT_URL : Optional[str] = "http://minio.minio-system.svc.cluster.local:9000",
        AWS_ENDPOINT_URL : Optional[str] = "http://minio.minio-system.svc.cluster.local:9000"):

        self.AWS_ACCESS_KEY_ID = AWS_ACCESS_KEY_ID
        self.AWS_SECRET_ACCESS_KEY = AWS_SECRET_ACCESS_KEY
        self.MLFLOW_S3_ENDPOINT_URL = MLFLOW_S3_ENDPOINT_URL
        self.AWS_ENDPOINT_URL = AWS_ENDPOINT_URL


class ScanflowTrackerConfig():
    def __init__(self,
        TRACKER_STORAGE: Optional[str] = "postgresql://scanflow:scanflow123@postgresql-service.postgresql.svc.cluster.local/scanflow-default",
        TRACKER_ARTIFACT: Optional[str] = "s3://scanflow-default"):

        self.TRACKER_STORAGE = TRACKER_STORAGE
        self.TRACKER_ARTIFACT = TRACKER_ARTIFACT

class ScanflowClientConfig():
    def __init__(self,
        SCANFLOW_TRACKER_URI : Optional[str] = "http://scanflow-tracker-service.scanflow-system.svc.cluster.local",
        SCANFLOW_SERVER_URI : Optional[str] = "http://scanflow-server-service.scanflow-system.svc.cluster.local",
        SCANFLOW_TRACKER_LOCAL_URI : Optional[str] = "http://scanflow-tracker.scanflow-default.svc.cluster.local"):

        self.SCANFLOW_TRACKER_URI = SCANFLOW_TRACKER_URI
        self.SCANFLOW_SERVER_URI = SCANFLOW_SERVER_URI
        self.SCANFLOW_TRACKER_LOCAL_URI = SCANFLOW_TRACKER_LOCAL_URI


class ScanflowEnvironment():
    def __init__(self,
        namespace: Optional[str] = "scanflow-default",
        secret : Optional[ScanflowSecret] = ScanflowSecret(),
        tracker_config : Optional[ScanflowTrackerConfig] = ScanflowTrackerConfig(),
        client_config : Optional[ScanflowClientConfig] = ScanflowClientConfig()):
     
        self.namespace = namespace
        self.secret = secret
        self.tracker_config = tracker_config
        self.client_config = client_config
    
    def to_dict(self):
        tmp_dict = {}
        env_dict = self.__dict__
        for k,v in env_dict.items():
            if k == 'namespace':
                tmp_dict[k] = v
            else:
                tmp_dict[k] = v.__dict__
        return tmp_dict
