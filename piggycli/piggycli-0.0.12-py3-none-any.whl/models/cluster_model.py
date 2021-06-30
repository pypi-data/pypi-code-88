import app.utilities.ssh as ssh
import json


class Cluster:

    def __init__(self, client, id):
        self.client = client
        self.id = id

    @classmethod
    def all(cls, client):
        resp = client.describe_clusters()
        return resp['Clusters']

    @property
    def hsms(self):
        return self.read()['Hsms']

    @property
    def azs(self):
        subnet_mapping = self.read()['SubnetMapping']
        azs = []
        for key, value in subnet_mapping.items():
            azs.append(key)
        return azs

    @property
    def csr(self):
        return self.read()['Certificates']['ClusterCsr']

    @property
    def state(self):
        return self.read()['State']

    def initialize(self, certs):
        assert self.state == 'UNINITIALIZED', 'Cluster state is not UNITIALIZED'
        assert certs.valid, 'Certificates not valid'
        self.client.initialize_cluster(
            ClusterId=self.id,
            SignedCert=certs.pem_hsm_cert.decode('UTF-8'),
            TrustAnchor=certs.pem_ca_cert.decode('UTF-8')
        )
        return

    def activate(
            self, instance, crypto_officer_username, crypto_officer_password, crypto_user_username, crypto_user_password, ssh_key):
        eni_ip = self.hsms[0]['EniIp']
        resp_json = ssh.activate_cluster(
            ip_address=instance.public_ip_address,
            ssh_key_file_path=ssh_key.ssh_key_file_path,
            eni_ip=eni_ip,
            crypto_officer_username=crypto_officer_username,
            crypto_officer_password=crypto_officer_password,
            crypto_user_username=crypto_user_username,
            crypto_user_password=crypto_user_password
        )

        resp = json.loads(resp_json)

        assert resp.get(
            'error') is None, f"Activate cluster error: {resp['error']}"
        assert resp['crypto_officer']['username'] == crypto_officer_username
        assert resp['crypto_officer']['password'] == crypto_officer_password

        return True

    def read(self):
        resp = self.client.describe_clusters(
            Filters={'clusterIds': [self.id]})
        return resp['Clusters'][0]

    def destroy(self):
        return False
