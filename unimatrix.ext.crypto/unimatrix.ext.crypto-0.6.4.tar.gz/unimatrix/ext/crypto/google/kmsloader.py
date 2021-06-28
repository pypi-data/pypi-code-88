"""Declares :class:`KMSLoader`."""
import asyncio
import itertools
import logging

import google.api_core.exceptions

from ..keyloader import KeyLoader
from .client import GoogleKMSClient
from .googlemanagedkey import GoogleManagedKey


class KMSLoader(KeyLoader, GoogleKMSClient):
    """A :class:`~unimatrix.ext.crypto.KeyLoader` implementation that queries
    the Google KMS API to retrieve the available keys. Keys may optionally be
    included (or excluded) by adding a predicate using the ``filter``
    parameter.

    Keys are imported into the :term:`Key Store`/:term:`Trust Store` only if
    the ``keyid`` label is specified, for each key holding value that is unique
    accross all keys imported into the application (not only the keys from
    Google Cloud KMS). If the ``keyid`` label is not supplied, the key is not
    added to any store.

    To use :class:`GoogleKeyLoader`, make sure you have enabled the
    following APIs:

    - ``cloudkms.googleapis.com``

    An example configuration is shown below:

    .. code:: python

        CRYPTO_KEYLOADERS = [
            {
                'loader': 'unimatrix.ext.crypto.google.GoogleKeyLoader',
                'public_only': False,
                'options': {
                    'project': "myproject",
                    'location': "location e.g. europe-west4",
                    'keyring': "keyring",
                    'filter': "labels.purpose=jwt-sign"
                }
            }
        ]
    """
    logger = logging.getLogger('unimatrix.runtime.boot')

    def setup(self, opts):
        """Hook called during instance initialization."""
        self.project = opts.project
        self.location = opts.location
        self.keyring = opts.keyring
        self.filter_ = None
        if opts.get('filter'):
            self.filter_ = opts.filter

    async def list(self):
        """Invoke the Google KMS to list all keys with the given predicate,
        and yield the results.
        """
        keys = await self._list_crypto_keys()
        if keys is None:
            return

        futures = []
        async for key in keys:
            if not key.labels['keyid']:
                self.logger.warning("Google KMS resource %s has no label keyid",
                    key.name)
                continue
            futures.append(self._get(key.name, key.labels['keyid']))

        for x in itertools.chain(*await asyncio.gather(*futures)): yield x

    async def _get(self, resource_id, keyid):
        keys = []
        for version in (await self._list_crypto_key_versions(resource_id)):
            opts = self.unpack_resource_id(version.name)
            opts['resource'] = version
            keyid = f"{keyid}@{opts['version']}"
            keys.append(GoogleManagedKey(opts, keyid=keyid))
            self.logger.debug("Imported Google KMS key %s", version.name)
        return keys

    async def _list_crypto_key_versions(self, name):
        items = await self.kms.list_crypto_key_versions({
            'parent': name,
            'filter': 'state=ENABLED'
        })
        return sorted(
            [x async for x in items],
            key=lambda x: -x.generate_time.timestamp()
        )

    async def _list_crypto_keys(self):
        keyring = self.key_ring_path(
            self.project, self.location, self.keyring)
        request = {
            'parent': keyring,
            'version_view': 'FULL'
        }
        if self.filter_:
            request['filter'] = self.filter_
        try:
            return await self.kms.list_crypto_keys(request)
        except google.api_core.exceptions.NotFound:
            self.logger.warning(
                "Google KMS keyring %s does not exist, not importing any "
                "keys", keyring
            )
            return None
