from app.models.cluster_model import Cluster
from app.models.hsm_model import HSM
from app.models.instance_model import Instance
import json


class StatusController:
    def __init__(self, credentials):
        self.credentials = credentials
        self.base_path = credentials.data['base_path']
        self.ec2 = credentials.ec2
        self.resource = credentials.resource
        self.cloudhsmv2 = credentials.cloudhsmv2

    def show(self):
        # hsm states = ['CREATE_IN_PROGRESS', 'ACTIVE', 'DELETE_IN_PROGRESS']
        # instance states = ['pending', 'running', 'stopping', 'stopped' ]

        hsm_state = self.hsm.state if bool(self.hsm) else None
        instance_state = self.instance.state

        if hsm_state == 'CREATE_IN_PROGRESS' and instance_state == 'pending':
            status = 'Piggy is waking up'
        elif hsm_state == 'CREATE_IN_PROGRESS' and instance_state == 'running':
            status = 'Piggy is waking up'
        elif hsm_state == 'ACTIVE' and instance_state == 'pending':
            status = 'Piggy is waking up'

        elif hsm_state == 'ACTIVE' and instance_state == 'running':
            status = 'Piggy is awake'

        elif hsm_state == 'DELETE_IN_PROGRESS' and instance_state == 'stopping':
            status = 'Piggy is going to sleep'
        elif hsm_state == 'DELETE_IN_PROGRESS' and instance_state == 'stopped':
            status = 'Piggy is going to sleep'
        elif hsm_state is None and instance_state == 'stopping':
            status = 'Piggy is going to sleep'

        elif hsm_state is None and instance_state == 'stopped':
            status = 'Piggy is sleeping'

        else:
            status = 'groogy, please run piggy status -wake or -sleep'

        return status

    def sleep(self):
        status = self.show()
        if status == 'Piggy is sleeping':
            return 'Piggy is sleeping'
        elif status == 'Piggy is going to sleep':
            return 'Piggy is going to sleep'
        elif status == 'Piggy is waking up':
            return 'Piggy is waking up, please try agian once Piggy is awake'
        else:
            hsm_resp = self.hsm.destroy()
            instance_resp = self.instance.stop()
        return 'Piggy is going to sleep'

    def wake(self):
        status = self.show()
        if status == 'Piggy is awake':
            return 'Piggy is awake'
        elif status == 'Piggy is waking up':
            return 'Piggy is waking up'
        elif status == 'Piggy is going to sleep':
            return 'Piggy is going to sleep, please try again once Piggy is sleeping'
        else:
            cluster = self.cluster
            hsm_resp = HSM.create(
                cluster_id=cluster.id,
                availability_zone=cluster.azs[0],
                client=self.cloudhsmv2
            )
            instance_resp = self.instance.start()
        return 'Piggy is waking up'

    @property
    def instance(self):
        id = self.credentials.data['instance_id']
        instances = Instance.all(client=self.ec2)
        if len(instances) == 0:
            raise InstanceNotFoundError(f'Instance ID {id} not found.')
        elif len(instances) > 1:
            raise MultipleInstancesFoundError('Multiple instances found.')
        elif instances[0]['InstanceId'] != id:
            raise InstanceNotFoundError(f'Instance ID {id} not found.')
        else:
            instance = Instance(id=id, resource=self.resource)
            return instance

    @property
    def cluster(self):
        id = self.credentials.data['cluster_id']
        clusters = Cluster.all(client=self.cloudhsmv2)
        if len(clusters) == 0:
            raise ClusterNotFoundError(f'Cluster ID {id} not found.')
        elif len(clusters) > 1:
            raise MultipleClustersFoundError('Multiple clusters found.')
        elif clusters[0]['ClusterId'] != id:
            raise ClusterNotFoundError(f'Cluster ID {id} not found.')
        else:
            cluster = Cluster(id=id, client=self.cloudhsmv2)
            if cluster.state != 'ACTIVE':
                raise ClusterStateError('Cluster state must be ACTIVE.')
            return cluster

    @property
    def hsm(self):
        hsms = self.cluster.hsms
        if len(hsms) == 0:
            return None
        elif len(hsms) > 1:
            raise MultipleHSMsFoundError('Multiple HSMs found.')
        else:
            id = hsms[0]['HsmId']
            hsm = HSM(id=id, cluster_id=self.cluster.id,
                      client=self.cloudhsmv2)
            return hsm

    def backups(self):
        backups = []
        resp = self.cloudhsmv2.describe_backups()
        for backup in resp['Backups']:
            backups.append(
                {
                    'id': backup['BackupId'], 'state': backup['BackupState'],
                    'created': backup['CreateTimestamp'].strftime('%m/%d/%y %H:%M:%S')
                }
            )
        return backups


class InstanceNotFoundError(Exception):
    pass


class MultipleInstancesFoundError(Exception):
    pass


class ClusterNotFoundError(Exception):
    pass


class MultipleClustersFoundError(Exception):
    pass


class ClusterStateError(Exception):
    pass


class HSMNotFoundError(Exception):
    pass


class MultipleHSMsFoundError(Exception):
    pass
