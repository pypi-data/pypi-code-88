from app.utilities.bitcoin.tx_scripts import SigScript
from app.utilities import ssh

import os


class SignedTx:

    def __init__(self, pem, unsigned_tx, signatures):
        self.pem = pem
        self.unsigned_tx = unsigned_tx
        self.signatures = signatures

    @classmethod
    def create(cls, unsigned_tx, address, credentials, ip_address, eni_ip):
        unsigned_tx_files = _unsigned_tx_files(
            unsigned_tx=unsigned_tx, cluster_path=credentials.data['cluster_path'])

        ssh_key_file_path = os.path.join(
            credentials.data['cluster_path'], f"{credentials.data['ssh_key_name']}.pem")

        signatures = _get_signatures(
            unsigned_tx_files=unsigned_tx_files,
            ssh_key_file_path=ssh_key_file_path,
            eni_ip=eni_ip,
            ip_address=ip_address,
            pub_key_handle=address.pub_key_handle,
            private_key_handle=address.private_key_handle,
            crypto_user_username=credentials.data['crypto_user_username'],
            crypto_user_password=credentials.data['crypto_user_password'],
            cluster_path=credentials.data['cluster_path']
        )

        return cls(
            pem=address.pub_key_pem,
            unsigned_tx=unsigned_tx,
            signatures=signatures
        )

    @property
    def hex(self):
        tx = bytearray()

        tx += self.unsigned_tx.version
        tx += self.unsigned_tx.tx_in_count
        for tx_in in self.unsigned_tx.tx_inputs:

            sig_script = SigScript(
                self.signatures, self.unsigned_tx, tx_in, self.pem)

            tx += self.unsigned_tx.previous_output(tx_in)
            tx += sig_script.script_bytes
            tx += sig_script.script
            tx += self.unsigned_tx.sequence
        tx += self.unsigned_tx.tx_out_count
        for tx_out in self.unsigned_tx.tx_outs.outputs:
            tx += tx_out
        tx += self.unsigned_tx.lock_time

        return tx.hex()


def _unsigned_tx_files(unsigned_tx, cluster_path):
    n, to_sign_files = 0, []
    for sign in unsigned_tx.to_sign:
        n += 1
        to_sign_file_path = os.path.join(cluster_path, f'unsigned_tx_{n}.bin')
        with open(to_sign_file_path, 'wb') as file:
            file.write(sign)
            to_sign_files.append(
                {'file_path': to_sign_file_path, 'file_name': f'unsigned_tx_{n}.bin'})

    return to_sign_files


def _get_signatures(unsigned_tx_files, ssh_key_file_path, eni_ip, ip_address, pub_key_handle,
                    private_key_handle, crypto_user_username, crypto_user_password, cluster_path):
    count = 0
    signatures = []
    for unsigned_tx_file in unsigned_tx_files:
        count += 1
        signature_file_path = ssh.sign_tx(
            ip_address=ip_address,
            ssh_key_file_path=ssh_key_file_path,
            eni_ip=eni_ip,
            unsigned_tx_file=unsigned_tx_file,
            pub_key_handle=pub_key_handle,
            private_key_handle=private_key_handle,
            crypto_user_username=crypto_user_username,
            crypto_user_password=crypto_user_password,
            count=count,
            cluster_path=cluster_path
        )

        with open(signature_file_path, 'rb') as file:
            signature = file.read()
        signatures.append(signature)
        os.remove(unsigned_tx_file['file_path'])
        os.remove(signature_file_path)

    return signatures
