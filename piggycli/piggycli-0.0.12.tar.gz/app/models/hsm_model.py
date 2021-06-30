from app.models.cluster_model import Cluster


class HSM():

    def __init__(self, id, cluster_id, client):
        self.id = id
        self.cluster_id = cluster_id
        self.client = client

    @classmethod
    def create(cls, cluster_id, availability_zone, client):
        resp = client.create_hsm(ClusterId=cluster_id,
                                 AvailabilityZone=availability_zone)
        hsm_id = resp['Hsm']['HsmId']
        return cls(id=hsm_id, cluster_id=cluster_id, client=client)

    @property
    def state(self):
        return self.read()['State']

    def read(self):
        resp = self.client.describe_clusters(
            Filters={'clusterIds': [self.cluster_id]})
        hsms = resp['Clusters'][0]['Hsms']
        for hsm in hsms:
            if hsm['HsmId'] == self.id:
                return hsm
        return False

    def destroy(self):
        resp = self.client.delete_hsm(
            ClusterId=self.cluster_id, HsmId=self.id)
        return resp['HsmId']
