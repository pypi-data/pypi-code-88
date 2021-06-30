from datetime import datetime
from app.utilities.bitcoin.addresses import P2PKH
from app.adapters import Explorer

# import hashlib
# from base58 import b58encode_check
# from ecdsa import VerifyingKey
import json
import datetime


class Address():
    def __init__(self, id, pub_key_pem, pub_key_handle, private_key_handle, address, confirmed_balance, spent, txrefs):
        self.id = id
        self.pub_key_pem = pub_key_pem
        self.pub_key_handle = pub_key_handle
        self.private_key_handle = private_key_handle
        self.address = address
        self.confirmed_balance = confirmed_balance
        self.txrefs = txrefs
        self.spent = spent

    @classmethod
    def all(cls, bucket, s3):
        addresses = []
        resp = s3.list_objects(Bucket=bucket)
        keys = resp['Contents']
        for key in keys:
            address = cls.find(bucket=bucket, s3=s3, id=key['Key'])
            addresses.append(address)
        return addresses

    @classmethod
    def find(cls, bucket, s3, id):
        resp = s3.get_object(Bucket=bucket, Key=id)
        data_json = resp['Body'].read().decode()
        data = json.loads(data_json)

        address = cls(
            id=id,
            pub_key_pem=data.get('pub_key_pem'),
            pub_key_handle=data.get('pub_key_handle'),
            private_key_handle=data.get('private_key_handle'),
            address=data.get('address'),
            confirmed_balance=data.get('confirmed_balance'),
            txrefs=data.get('txrefs'),
            spent=data.get('spent')
        )

        return address

    @classmethod
    def create(cls, pub_key):
        address = P2PKH(pem=pub_key.pem).address
        explorer = Explorer(address=address)

        return cls(
            id=pub_key.label,
            pub_key_pem=pub_key.pem,
            pub_key_handle=pub_key.handle,
            private_key_handle=pub_key.private_key_handle,
            address=address,
            confirmed_balance=explorer.confirmed_balance,
            spent=explorer.spent,
            txrefs=explorer.txrefs
        )

    def save(self, bucket, s3, region):
        if bucket_exists(bucket=bucket, s3=s3) is False:
            create_bucket(bucket=bucket, s3=s3, region=region)
        key = self.id

        data_json = json.dumps(
            {
                'pub_key_handle': self.pub_key_handle,
                'private_key_handle': self.private_key_handle,
                'pub_key_pem': self.pub_key_pem,
                'address': self.address,
                'confirmed_balance': self.confirmed_balance,
                'spent': self.spent,
                'txrefs': self.txrefs
            }
        )
        data_bytes = bytes(data_json, 'UTF-8')
        resp = s3.put_object(
            Body=data_bytes,
            Bucket=bucket,
            Key=key
        )
        assert resp['ResponseMetadata'][
            'HTTPStatusCode'] == 200, f'Failed to save address: {self.id} to bucket: {bucket}'
        return self.id

    def refresh(self, bucket, s3, region):
        explorer = Explorer(address=self.address)
        self.confirmed_balance = explorer.confirmed_balance
        self.spent = explorer.spent
        self.txrefs = explorer.txrefs
        self.save(bucket=bucket, s3=s3, region=region)
        return self


def bucket_exists(bucket, s3):
    resp = s3.list_buckets()
    for _bucket in resp['Buckets']:
        if _bucket['Name'] == bucket:
            return True
    return False


def create_bucket(bucket, s3, region):
    location = {'LocationConstraint': region}
    resp = s3.create_bucket(
        Bucket=bucket,
        CreateBucketConfiguration=location
    )

    return resp['Location']
