"""Declares :class:`PublicKey`."""
import abc


class PublicKey(metaclass=abc.ABCMeta):
    """Declares the interface for public key."""
    capabilities = []

    @property
    def bytes(self) -> bytes:
        """Return a byte sequence holding the public key."""
        raise NotImplementedError

    def is_private(self) -> bool:
        """Return a boolean indicating if the key is private."""
        return False

    def is_public(self) -> bool:
        """Return a boolean indicating if the key is public."""
        return True

    async def can_use(self, oid: str) -> bool:
        """Return a boolean if the key can use the algorithm identified by
        the provided `oid`.
        """
        return oid in self.capabilities

    @abc.abstractmethod
    async def encrypt(self, pt: bytes, *args, **kwargs) -> bytes:
        """Encrypt byte-sequence `pt` using the specified parameters."""
        raise NotImplementedError

    @abc.abstractmethod
    async def verify(self, digest: bytes, blob: bytes,
        *args, **kwargs) -> bytes:
        """Verifies that `digest` is a valid signature with this public
        key on `blob`.
        """
        raise NotImplementedError


def load_pem_public_key(blob):
    """Load byte-sequence `blob` holding a PEM-serialized PKCS#1 DER encoded
    public key as a :class:`PublicKey` instance.
    """
    from .lib.pkcs import PEMPublicKey
    return PEMPublicKey.frompem(blob)
