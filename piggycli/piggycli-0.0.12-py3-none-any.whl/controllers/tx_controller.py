from app.controllers.credentials_controller import CredentialsController
from app.controllers.addresses_controller import AddressController

from app.models.instance_model import Instance
from app.models.cluster_model import Cluster
from app.models.unsigned_tx_model import UnsignedTx
from app.models.signed_tx_model import SignedTx

from app.adapters import Explorer
import boto3
from botocore.exceptions import ClientError

import os


class TxController:

    def __init__(self, credentials):

        self.credentials = credentials

    def create(self, address, recipient, fee, value, change_address=None, change=None, balance=None):
        unsigned_tx = UnsignedTx(
            address=address,
            recipient=recipient,
            fee=fee,
            value=value,
            change_address=change_address
        )

        instance = Instance(resource=self.credentials.resource,
                            id=self.credentials.data['instance_id'])

        cluster = Cluster(client=self.credentials.cloudhsmv2,
                          id=self.credentials.data['cluster_id'])
        eni_ip = cluster.hsms[0]['EniIp']

        signed_tx = SignedTx.create(
            unsigned_tx=unsigned_tx,
            address=address,
            credentials=self.credentials,
            ip_address=instance.public_ip_address,
            eni_ip=eni_ip
        )

        return signed_tx.hex

    def validate(self, all, address_id, recipient, fee, value, change_address):
        try:
            controller = AddressController(credentials=self.credentials)
            resp = controller.update(id=address_id)
            address = resp['data']['address']
            confirmed_balance = address.confirmed_balance
            assert confirmed_balance > 0, f"Address {address.address} has a zero confirmed balance."
            assert fee > 0, f"Mining fee is zero."

            if all:
                assert fee < confirmed_balance, f"The mining fee of {fee} is greater than the confirmed balance of {confirmed_balance} in address {address.address}."
                assert _is_address_valid(
                    address=recipient),  f"Recipient address {recipient} does not appear to be valid."
                return {
                    'address': address,
                    'balance': confirmed_balance,
                    'recipient': recipient,
                    'value': confirmed_balance - fee,
                    'fee': fee
                }

            else:
                assert fee + \
                    value < confirmed_balance, f"The mining fee of {fee} and the quantiy of {value} are greater than the confirmed balance of {confirmed_balance} in address {address.address}."
                assert _is_address_valid(
                    address=recipient), f"Recipient address {recipient} does not appear to be valid."
                assert _is_address_valid(
                    address=change_address), f"Change address {change_address} does not appear to be valid."
                return {
                    'address': address,
                    'balance': confirmed_balance,
                    'recipient': recipient,
                    'value': value,
                    'fee': fee,
                    'change': confirmed_balance - fee - value,
                    'change_address': change_address
                }

        except ClientError:
            return {'error': f"Address ID {address_id} was not found"}

        except Exception as e:
            return {'error': e.args[0]}


def _unsigned_tx_files(unsigned_tx, path):
    n, to_sign_files = 0, []
    for sign in unsigned_tx.to_sign:
        n += 1
        to_sign_file = os.path.join(path, f'unsigned_tx_{n}.bin')
        with open(to_sign_file, 'wb') as file:
            file.write(sign)
            to_sign_files.append(to_sign_file)

    return to_sign_files


def _is_address_valid(address):
    explorer = Explorer(address=address)
    try:
        resp = explorer.spent
        return True
    except Exception as e:
        return False
