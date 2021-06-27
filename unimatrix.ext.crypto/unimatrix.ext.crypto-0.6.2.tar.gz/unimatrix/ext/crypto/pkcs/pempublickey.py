"""Declares :class:`PEMPublicKey`."""
from cryptography.hazmat.primitives import serialization

from .pkcspublic import PKCSPublic


class PEMPublicKey(PKCSPublic):

    @property
    def bytes(self) -> bytes:
        """Return a byte sequence holding the public key."""
        return self._public.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

    def __init__(self, key):
        self._public = key
