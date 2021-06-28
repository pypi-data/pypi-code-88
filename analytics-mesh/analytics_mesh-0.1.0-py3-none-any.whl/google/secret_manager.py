import logging
from google.cloud import secretmanager


log = logging.getLogger(__name__)


class SecretManager(object):
    """
    a wrapper of the google secret manager client
    """

    def __init__(self, **kwargs):
        """
        :param service_key_filename: path to or name of a google cloud service_key_file
        :param project: A google cloud project
        """
        try:
            log.debug("Connecting to secret manager service")
            self.project = kwargs['project']
            self.service_key_file = kwargs['service_key_filename']
            self.client = secretmanager.SecretManagerServiceClient().from_service_account_file(self.service_key_file)
        except KeyError as e:
            log.error('no project or service key provided --- see class definition')
            raise

    def get_secret(self, secret_id: str = None, version_id: str = 'latest') -> str:
        """
        Access the payload for the given secret version if one exists. The version
        can be a version number as a string (e.g. "5") or an alias (e.g. "latest").
        :param secret_id: the id of the secret requiring access
        :param version_id: the version id of the secret requiring access
        return the payload which is the value of the secret
        """
        # Build the resource name of the secret version.
        name = f"projects/{self.project}/secrets/{secret_id}/versions/{version_id}"
        # Access the secret version.
        response = self.client.access_secret_version(request={"name": name})
        payload = response.payload.data.decode("UTF-8")
        return payload
