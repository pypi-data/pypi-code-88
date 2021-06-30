import uuid
import os


class SSHKey:

    def __init__(self, id, name, material, fingerprint):
        self.id = id
        self.name = name
        self.material = material
        self.fingerprint = fingerprint

    @classmethod
    def create(cls, client):
        name = f'Piggy_SSH_Key_{str(uuid.uuid4())[:8]}'
        resp = client.create_key_pair(KeyName=name)
        key = SSHKey(
            id=resp['KeyPairId'],
            name=resp['KeyName'],
            material=resp['KeyMaterial'],
            fingerprint=resp['KeyFingerprint']
        )
        return key

    @classmethod
    def all(cls, client):
        resp = client.describe_key_pairs()
        key_pairs = resp['KeyPairs']
        for key in key_pairs:
            if key.get('KeyFingerprint') is not None:
                del key['KeyFingerprint']
            if key.get('Tags') is not None:
                del key['Tags']
        return key_pairs

    def write_to_file(self, cluster_path):
        self.ssh_key_file_path = os.path.join(cluster_path, f'{self.name}.pem')
        with open(self.ssh_key_file_path, 'w') as file:
            file.write(self.material)
        return self.ssh_key_file_path
