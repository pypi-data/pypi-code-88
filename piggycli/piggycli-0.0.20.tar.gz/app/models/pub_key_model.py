import app.utilities.ssh as ssh


class PubKey:

    def __init__(self, label, handle, pem, private_key_handle):
        self.label = label
        self.handle = handle
        self.pem = pem
        self.private_key_handle = private_key_handle

    @classmethod
    def create(cls, ip_address, ssh_key_file_path, eni_ip, crypto_user_username, crypto_user_password, label):

        resp = ssh.gen_ecc_key_pair(
            ip_address=ip_address,
            ssh_key_file_path=ssh_key_file_path,
            eni_ip=eni_ip,
            crypto_user_username=crypto_user_username,
            crypto_user_password=crypto_user_password,
            key_label=label
        )
        if resp['status_code'] != 200:
            breakpoint()
        return cls(
            label=resp['data']['label'],
            pem=resp['data']['pem'],
            handle=resp['data']['handle'],
            private_key_handle=resp['data']['private_key_handle']
        )

    def read(self):
        return

    def update(self):
        return

    def delete(self):
        return
