from app.models.credentials_model import Credentials
import json

import os


class CredentialsController:

    def __init__(self):
        pass

    def create(self, base_path, cluster_path, aws_region, aws_access_key_id, aws_secret_access_key, customer_ca_key_password,
               crypto_officer_password, crypto_user_username, crypto_user_password, cluster_id, instance_id, ssh_key_name):
        credentials_file_path = os.path.join(
            cluster_path, 'credentials.json')
        data = {
            'base_path': base_path,
            'cluster_path': cluster_path,
            'aws_region': aws_region,
            'aws_access_key_id': aws_access_key_id,
            'aws_secret_access_key': aws_secret_access_key,
            'customer_ca_key_password': customer_ca_key_password,
            'crypto_officer_password': crypto_officer_password,
            'crypto_user_username': crypto_user_username,
            'crypto_user_password': crypto_user_password,
            'cluster_id': cluster_id,
            'instance_id': instance_id,
            'ssh_key_name': ssh_key_name
        }

        credentials = Credentials.create(
            credentials_file_path=credentials_file_path, data=data)
        return credentials

    def create_from_file(self, credentials_file_path):
        return Credentials.read(credentials_file_path=credentials_file_path)

    def show(self, credentials_file_path):
        credentials = Credentials.read(
            credentials_file_path=credentials_file_path)

        return json.dumps(
            {
                'credentials_file_path': credentials.credentials_file_path,
                'data': credentials.data
            }
        )

    def update(self, credentials_file_path, **kwargs):
        credentials = Credentials.read(
            credentials_file_path=credentials_file_path)
        credentials.update(**kwargs)

        return json.dumps(
            {
                'credentials_file_path': credentials.credentials_file_path,
                'data': credentials.data
            }
        )
