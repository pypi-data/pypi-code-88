# pylint: disable=line-too-long
"""Declares :class:`AbstractKeystore`."""
import functools
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

    def register(self, keyid: str, key, force=False):
        if keyid in self.keys and not force:
            raise ValueError(f"Key already registered: {keyid}")
        self.keys[keyid] = key

    def register_deferred(self, config):
        key = DeferredKey(self, **config)
        self.register(key.keyid, key)


class DeferredKey:
    __loaders = {
        'urn:unimatrix:cloud:azure': 'unimatrix.ext.crypto.azure.loader.AzureKeyVaultLoader'
    }

    def ensure_key(func):
        @functools.wraps(func)
        async def f(self, *args, **kwargs):
            await self.load()
            return await func(self, *args, **kwargs)
        return f

    @property
    def keyid(self):
        return self.__name

    @property
    def keyid(self):
        return self.__name

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

    @ensure_key
    async def can_use(self, *args, **kwargs):
        return await self.__key.can_use(*args, **kwargs)

    def get_public_key(self, *args, **kwargs):
        return self.__key.get_public_key(*args, **kwargs)

    @ensure_key
    async def sign(self, *args, **kwargs):
        return await self.__key.sign(*args, **kwargs)

    async def load(self):
        """Loads the actual key from the backend."""
        backend = self.__loader_class(self.__loader__opts)
        self.__key = key = await backend.get(self.__name)
        self.__chain.register(key.keyid, key, force=True)
        self.__chain.register(self.__name, key, force=True)
