import os

from ml_platform_client.constants import MODE_CLUSTER


class ClientConfig:
    def __init__(self):
        self.minio_host = os.environ.get('MINIO_HOST', '172.17.0.1:9000')
        self.minio_access_key = os.environ.get('MINIO_ACCESS_KEY', '24WTCKX23M0MRI6BA72Y')
        self.minio_secret_key = os.environ.get('MINIO_SECRET_KEY', '6mxoQMf1Lha2q1H3fp3fjNHEZRJJ7LvbC5k3+CQX')
        self.minio_secure = os.environ.get('MINIO_SECURE', 'false') in ['true', 'True']
        self.db_host = os.environ.get('DB_HOST', '172.17.0.1')
        self.db_port = int(os.environ.get('DB_PORT', 3306))
        self.db_user = os.environ.get('DB_USER', 'root')
        self.db_password = os.environ.get('DB_PASS', 'password')
        self.num_worker = int(os.environ.get('MLP_CLIENT_WORKER', 5))
        self.num_thread = int(os.environ.get('MLP_CLIENT_THREAD', 10))
        self.mode = os.environ.get('MLP_CLIENT_MODE', MODE_CLUSTER)


client_config = ClientConfig()
