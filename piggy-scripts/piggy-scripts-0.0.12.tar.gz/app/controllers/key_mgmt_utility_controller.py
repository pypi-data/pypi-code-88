import app.scripts.terminal_scripts as term
import app.scripts.key_mgmt_utility_scripts as kmu
import time
import json


def genECCKeyPair(eni_ip, username, password, key_label):
    term.configure_cloudhsm_client(eni_ip=eni_ip)
    time.sleep(1)

    key_handles = kmu.generate_key_pair(
        username=username, password=password, key_label=key_label)
    time.sleep(1)

    pub_key_handle = key_handles['public_key']
    pub_key_pem_file_name = kmu.export_public_key(
        username=username, password=password, pub_key_handle=pub_key_handle)

    with open(pub_key_pem_file_name, 'r') as file:
        pub_key_pem = file.read()

    return json.dumps({
        'data':
            {
                'label': key_label,
                'pem': pub_key_pem,
                'handle': key_handles['public_key'],
                'private_key_handle': key_handles['private_key']
            },
        'status_code': 200
    })


def sign(eni_ip, username, password, tx_file, pub_key_handle, private_key_handle, count):
    term.configure_cloudhsm_client(eni_ip=eni_ip)
    time.sleep(1)

    signed_tx_file = kmu.sign(
        username=username,
        password=password,
        tx_file=tx_file,
        pub_key_handle=pub_key_handle,
        private_key_handle=private_key_handle,
        count=count
    )

    return signed_tx_file
