"""Declares :class:`PKCSPublic`."""
from cryptography.exceptions import InvalidSignature

from ..public import PublicKey
from .base import PKCSObject


class PKCSPublic(PKCSObject, PublicKey):

    async def encrypt(self, pt, padding):
        return self._public.encrypt(bytes(pt), padding)

    async def verify(self, digest: bytes, blob: bytes,
        padding, algorithm) -> bytes:
        try:
            self._public.verify(bytes(digest), blob, padding, algorithm)
            return True
        except InvalidSignature:
            return False

