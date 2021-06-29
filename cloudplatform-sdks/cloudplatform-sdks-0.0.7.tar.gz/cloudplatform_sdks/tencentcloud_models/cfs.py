from .clients import cfs_client


class TencentCfs:
    STATUS_MAPPER = {
        "available": "started"
    }

    def __init__(self, object):
        self.object = object

    @classmethod
    def list(cls, **kwargs):
        resp = cfs_client.describe_cfs_file_systems(**kwargs)['FileSystems']
        return [cls(cfs_object) for cfs_object in resp]

    @classmethod
    def get(cls, id):
        resp = cfs_client.describe_cfs_file_systems(FileSystemId=id)['FileSystems']
        if len(resp) > 0:
            return cls(resp[0])
        else:
            return None

    @classmethod
    def create(cls, **kwargs):
        resp = cfs_client.create_cfs_file_system(**kwargs)
        return cls(resp)

    def fresh(self):
        self.object = self.get(self.external_id).object

    def delete(self):
        return cfs_client.delete_cfs_file_system(FileSystemId=self.external_id)

    @property
    def external_id(self):
        return self.object.get('FileSystemId')

    @property
    def external_name(self):
        return self.object.get('FsName')

    @property
    def storage_type(self):
        return self.object.get('StorageType')

    @property
    def status(self):
        status = self.object.get('LifeCycleState')
        return self.STATUS_MAPPER.get(status, status)

    @property
    def storage_protocol(self):
        return self.object.get('Protocol')

    @property
    def created_time(self):
        return self.object.get('CreationTime')

    def __repr__(self):
        return "<TencentCfs object:{}>".format(self.external_id)
