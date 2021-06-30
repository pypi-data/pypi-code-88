from app.controllers.credentials_controller import CredentialsController
from app.models.pub_key_model import PubKey

from app.models.instance_model import Instance
from app.models.cluster_model import Cluster
from app.models.address_model import Address

import uuid
import os


class AddressController:

    def __init__(self, credentials):
        self.credentials = credentials

    def index(self):
        addresses = Address.all(bucket=self.bucket_name,
                                s3=self.credentials.s3)
        for address in addresses:
            self.update(id=address.id)

        addresses = Address.all(bucket=self.bucket_name,
                                s3=self.credentials.s3)
        return {'data': {'addresses': addresses}, 'http_status_code': 200}

    def create(self):
        pub_key = PubKey.create(
            ip_address=self.ip_address,
            ssh_key_file_path=self.ssh_key_file_path,
            eni_ip=self.eni_ip,
            crypto_user_username=self.credentials.data['crypto_user_username'],
            crypto_user_password=self.credentials.data['crypto_user_password'],
            label=_get_address_id()
        )
        address = Address.create(pub_key=pub_key)
        assert address.save(
            bucket=self.bucket_name,
            s3=self.credentials.s3,
            region=self.credentials.data['aws_region']
        ), f"Failed to save address: {address.id} to bucket: {self.bucket_name}"
        return {'data': {'address': address}, 'http_status_code': 200}

    def show(self, id):
        address = Address.find(bucket=self.bucket_name,
                               s3=self.credentials.s3, id=id)
        return {'data': {'address': address}, 'http_status_code': 200}

    def update(self, id):
        address = Address.find(
            id=id,
            bucket=self.bucket_name,
            s3=self.credentials.s3
        ).refresh(
            bucket=self.bucket_name,
            s3=self.credentials.s3,
            region=self.credentials.data['aws_region']
        )
        return {'data': {'address': address}, 'http_status_code': 200}

    @property
    def ip_address(self):
        instance_id = self.credentials.data['instance_id']
        instance = Instance(id=instance_id, resource=self.credentials.resource)
        ip_address = instance.public_ip_address
        return ip_address

    @property
    def ssh_key_file_path(self):
        ssh_key_file_path = os.path.join(
            self.credentials.data['cluster_path'],
            f"{self.credentials.data['ssh_key_name']}.pem"
        )
        return ssh_key_file_path

    @property
    def eni_ip(self):
        cluster = Cluster(
            id=self.credentials.data['cluster_id'], client=self.credentials.cloudhsmv2)
        hsms = cluster.hsms
        if bool(hsms) is False:
            raise NoHSMFoundError(f'Cluster: {cluster.id} has no HSMs')
        eni_ip = hsms[0]['EniIp']
        return eni_ip

    @property
    def bucket_name(self):
        bucket_name = f"{self.credentials.data['cluster_id']}-bucket"
        return bucket_name


def _get_address_id():
    return f'addr-{str(uuid.uuid4())[-12:]}'


class NoHSMFoundError(Exception):
    pass


class SSHKeyFileNotFoundError(Exception):
    pass
