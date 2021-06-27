"""Declares :class:`SigningAlgorithm`."""
import abc

from ..signature import Signature
from .base import Algorithm


class SigningAlgorithm(Algorithm):
    signature_class = Signature
    IncompatibleKey = type('IncompatibleKey', (Exception,), {})

    async def sign(self, key, data: bytes) -> Signature:
        if not await key.can_use(self.oid):
            raise self.IncompatibleKey
        digest = await key.sign(data, **self.get_sign_parameters(key))
        return self.signature_class(digest, self, keyid=key.id)

    async def verify(self, key, digest: bytes, data: bytes) -> bool:
        if not await key.can_use(self.oid):
            raise self.IncompatibleKey
        return await key.verify(digest, data, **self.get_verify_parameters(key))

    @abc.abstractmethod
    def get_sign_parameters(self, key) -> dict:
        """Return a dictionary containing the parameters supplied to the
        :meth:`~unimatrix.ext.crypto.PrivateKey.sign()` method.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_verify_parameters(self, key) -> dict:
        """Return a dictionary containing the parameters supplied to the
        :meth:`~unimatrix.ext.crypto.PrivateKey.verify()` method.
        """
        raise NotImplementedError
