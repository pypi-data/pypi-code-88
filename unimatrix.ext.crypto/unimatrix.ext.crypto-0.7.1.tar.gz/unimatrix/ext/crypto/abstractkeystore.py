# pylint: disable=line-too-long
"""Declares :class:`AbstractKeystore`."""
import hashlib

import ioc.loader
from unimatrix.lib.datastructures import ImmutableDTO


class AbstractKeystore:
    """The base class for all :term:`Key Store` implementations. A Key Store
    provides an interface to lookup private or public keys.
    """

    @property
    def keys(self):
        return self.__keys

    @property
    def masked(self):
        return self.__masked

    def __init__(self):
        self.__keys = {}
        self.__masked = {}

    def get(self, keyid):
        key = self.keys.get(keyid) or self.masked.get(keyid)
        if key is None:
            raise LookupError
        return key

    def mask_keyid(self, keyid):
        return hashlib.sha1(str.encode(keyid)).hexdigest() # nosec

    def register(self, key, force=False):
        if key.keyid in self.masked and not force:
            raise ValueError(f"Key already registered: {key.keyid}")
        self.masked[key.keyid] = key
        self.keys[key.name] = key

    def register_deferred(self, config):
        key = Key.new(self, **config)
        self.register(Key.new(self, **config))


class Key:
    __loaders = {
        'urn:unimatrix:cloud:azure': 'unimatrix.ext.crypto.azure.loader.AzureKeyVaultLoader'
    }

    @property
    def name(self):
        return self.__name

    @property
    def keyid(self):
        return self.__key.keyid

    @classmethod
    def new(cls, chain, **config):
        key = cls(chain, **config)
        key.load()
        return key

    def __init__(self, chain, name, usage, loader):
        self.__chain = chain
        self.__name = name
        self.__usage = usage
        self.__loader_class, self.__loader__opts = self.__get_loader(**loader)
        self.__key = None

    def __get_loader(self, backend, opts):
        return (
            ioc.loader.import_symbol(self.__loaders[backend]),
            ImmutableDTO.fromdict(opts)
        )

    async def can_use(self, *args, **kwargs):
        return await self.__key.can_use(*args, **kwargs)

    def get_public_key(self, *args, **kwargs):
        return self.__key.get_public_key(*args, **kwargs)

    async def sign(self, *args, **kwargs):
        return await self.__key.sign(*args, **kwargs)

    def load(self):
        """Loads the actual key from the backend."""
        backend = self.__loader_class(self.__loader__opts)
        self.__key = key = backend.get_sync(self.__name)
