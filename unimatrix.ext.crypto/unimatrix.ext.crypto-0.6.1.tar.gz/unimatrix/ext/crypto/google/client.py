"""Declares :class:`GoogleKMSClient`."""
from google.cloud import kms
from google.cloud import secretmanager


class GoogleKMSClient:

    @property
    def kms(self):
        if not hasattr(self, '_kms'):
            self._kms = self._get_kms_client()
        return self._kms

    @property
    def secretmanager(self):
        if not hasattr(self, '_kms'):
            self._secretmanager = self._get_secretmanager_client()
        return self._secretmanager

    @staticmethod
    def _get_kms_client():
        return kms.KeyManagementServiceAsyncClient()

    @staticmethod
    def _get_secretmanager_client():
        return secretmanager.SecretManagerServiceAsyncClient()

    @staticmethod
    def key_ring_path(*args):
        return kms.KeyManagementServiceAsyncClient.key_ring_path(*args)

    @staticmethod
    def unpack_resource_id(resource_id):
        parts = str.split(resource_id, '/')
        return {
            'project': parts[1],
            'location': parts[3],
            'keyring': parts[5],
            'key': parts[7],
            'version': int(parts[9]),
        }
