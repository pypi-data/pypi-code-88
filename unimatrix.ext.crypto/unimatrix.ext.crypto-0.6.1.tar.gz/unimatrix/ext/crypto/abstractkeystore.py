"""Declares :class:`AbstractKeystore`."""
import hashlib


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
        return hashlib.sha1(str.encode(keyid)).hexdigest()

    def register(self, keyid: str, key):
        if keyid in self.keys:
            raise ValueError(f"Key already registered: {keyid}")
        self.keys[keyid] = self.masked[self.mask_keyid(keyid)] = key
