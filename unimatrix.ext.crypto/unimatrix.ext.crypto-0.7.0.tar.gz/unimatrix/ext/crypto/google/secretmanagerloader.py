"""Declares :class:`SecretManagerKeyLoader`."""
import asyncio
import itertools
import logging

import google.api_core.exceptions
from google.cloud.secretmanager import SecretVersion

from ..keyloader import KeyLoader
from ..pkcs import RSAPrivateKey
from .client import GoogleKMSClient


class SecretManagerKeyLoader(KeyLoader, GoogleKMSClient):
    """Loads private key material from the Secret Manager API. Unlike
    :class:`GoogleKeyLoader`, :class:`SecretManagerKeyLoader` fetches
    the actual key material from the Google Cloud APIs and keeps it in
    application memory. This implementation is an alternative to the Google
    Cloud KMS loader, either from a cost-control perspective or when a
    network call for each cryptographic operation is not desirable.

    Before using :class:`SecretManagerKeyLoader`, make sure you have
    the Secret Manager API enabled by running the following command in
    a terminal:

    .. code:: sh

        gcloud services enable secretmanager.googleapis.com

    Like Google KMS keys, a Secret can have multiple versions and each
    version is imported by :class:`SecretManagerKeyLoader`. Because
    the cryptographic implementation is not known beforehand (Secrets are
    essentially blobs of data), a number of hints must be provided in order
    to correctly process the keys. These hints are configured as labels on the
    Secret resources:

    - ``format`` - Allowed values are: ``RSA``, ``AES256``.

    If no concrete key type could be determined, then the Secret content is
    treated as if it were the `secret` parameter to
    :class:`~unimatrix.ext.crypto.SecretKey`.

    Because the Secrets' name is used as the key identifier, the ``keyid``
    label is optional when using :class:`SecretManagerKeyLoader`. When
    the ``keyid`` label is given, it taked precedent over the Secrets' name.
    """
    logger = logging.getLogger('unimatrix.runtime.boot')

    def setup(self, opts):
        """Hook called during instance initialization."""
        self.project = opts.project
        self.filter_ = None
        if opts.get('filter'):
            self.filter_ = opts.filter

    async def list(self):
        futures = []
        secrets = await self._list_secrets()
        if secrets is None:
            raise StopIteration
        async for secret in secrets:
            keytype = secret.labels['keytype'] or secret.labels['format']
            futures.append(self._load_versions(keytype, secret.name))

        for key in itertools.chain(*await asyncio.gather(*futures)):
            yield key

    async def _load_versions(self, keytype, name):
        futures = []
        async for version in await self._list_secret_versions(name):
            if version.state != SecretVersion.State.ENABLED:
                continue
            futures.append(self._get_key_from_version(keytype, version))
        return await asyncio.gather(*futures)

    async def _get_key_from_version(self, keytype, version):
        *_, n, _, v = str.split(version.name, '/')
        keyid = f'{n}@{v}'
        if keytype == 'rsa':
            key = RSAPrivateKey({
                'content': await self._access_secret_version(version.name)
            }, keyid=keyid)
        else:
            raise NotImplementedError(keytype)
        self.logger.debug("Imported %s from Secret %s",
            type(key).__name__, version.name)
        return key

    async def _access_secret_version(self, name):
        response = await self.secretmanager.access_secret_version({
            'name': name
        })
        return response.payload.data

    async def _list_secrets(self):
        parent = f'projects/{self.project}'
        request = {
            'parent': parent
        }
        if self.filter_:
            request['filter'] = self.filter_
        try:
            return await self.secretmanager.list_secrets(request)
        except google.api_core.exceptions.NotFound:
            return None

    async def _list_secret_versions(self, parent):
        request = {'parent': parent}
        return await self.secretmanager.list_secret_versions(request)
