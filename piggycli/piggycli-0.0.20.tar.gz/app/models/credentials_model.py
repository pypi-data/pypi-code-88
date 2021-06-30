import json
import os
import boto3


class CredentialsData:
    def __init__(self, **kwargs):
        self.base_path = kwargs['base_path']
        self.cluster_path = kwargs['cluster_path']
        self.aws_region = kwargs['aws_region']
        self.ssh_key_name = kwargs['ssh_key_name']
        self.cluster_id = kwargs['cluster_id']
        self.aws_access_key_id = kwargs['aws_access_key_id']
        self.aws_secret_access_key = kwargs['aws_secret_access_key']
        self.customer_ca_key_password = kwargs['customer_ca_key_password']
        self.crypto_officer_password = kwargs['crypto_officer_password']
        self.crypto_user_username = kwargs['crypto_user_username']
        self.crypto_user_password = kwargs['crypto_user_password']
        self.instance_id = kwargs['instance_id']


def get_credentials_data(**kwargs):
    credentials_data = CredentialsData(**kwargs)
    return credentials_data.__dict__


class Credentials:
    def __init__(self, credentials_file_path, data):
        self.credentials_file_path = credentials_file_path
        self.data = data
        self.ec2 = boto3.client(
            'ec2',
            aws_access_key_id=self.data['aws_access_key_id'],
            aws_secret_access_key=self.data['aws_secret_access_key'])
        self.cloudhsmv2 = boto3.client('cloudhsmv2',
                                       aws_access_key_id=self.data['aws_access_key_id'],
                                       aws_secret_access_key=self.data['aws_secret_access_key'])
        self.resource = boto3.resource('ec2',
                                       aws_access_key_id=self.data['aws_access_key_id'],
                                       aws_secret_access_key=self.data['aws_secret_access_key'])
        self.s3 = boto3.client('s3',
                               aws_access_key_id=self.data['aws_access_key_id'],
                               aws_secret_access_key=self.data['aws_secret_access_key'])

    @classmethod
    def create(cls, credentials_file_path, data):

        _write_credentials_to_file(
            credentials_file_path=credentials_file_path, data=data)

        credentials = Credentials(
            credentials_file_path=credentials_file_path, data=data)

        return credentials

    @classmethod
    def read(cls, credentials_file_path):
        with open(credentials_file_path, 'r') as file:
            json_file_data = file.read()
        file_data = json.loads(json_file_data)
        data = get_credentials_data(**file_data)
        credentials = Credentials(
            credentials_file_path=credentials_file_path, data=data)

        return credentials

    def update(self, **kwargs):
        credentials_data = CredentialsData(**self.data)
        for key, value in kwargs.items():
            setattr(credentials_data, key, value)
        self.data = credentials_data.__dict__
        _write_credentials_to_file(
            credentials_file_path=self.credentials_file_path, data=self.data)
        return self


def _write_credentials_to_file(credentials_file_path, data):
    if os.path.exists(data['cluster_path']) is False:
        os.mkdir(data['cluster_path'])
    with open(credentials_file_path, 'w') as file:
        file.write(json.dumps(data))

    return
