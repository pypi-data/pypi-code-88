"""Declares :class:`AzurePrivateKey`."""
import binascii
import urllib.parse

from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric import utils

from .. import oid
from ..ec import EllipticCurvePublicKey
from ..private import PrivateKey
from .azureclient import AzureClient


class AzurePrivateKey(PrivateKey, AzureClient):
    """Represents a private key in Azure Key Vault."""

    @property
    def capabilities(self) -> list:
        """Return the list of capabilities for this key."""
        return self._get_capabilities()

    @classmethod
    def fromclient(cls, client, key):
        """Create a new :class:`AzurePrivateKey` using the Azure Key Vault
        client and a key.
        """
        if key.key_type != 'EC':
            raise NotImplementedError
        return EllipticCurvePrivateKey({'key': key, 'jwk': key.key},
            keyid=str(key.id))


class EllipticCurvePrivateKey(AzurePrivateKey):
    __curve_mapping = {
        'P-256K'    : ec.SECP256K1,
        'SECP256K1' : ec.SECP256K1,
    }
    __algorithm_mapping = {
        'P-256K'    : oid.SECP256K1,
        'SECP256K1' : oid.SECP256K1,
    }

    @property
    def curve(self) -> ec.EllipticCurve:
        """Return the
        :class:`cryptography.hazmat.primitives.asymmetric.ec.EllipticCurve`
        specifying the curve used for this private key.
        """
        return self.__curve_mapping[self.__jwk.crv]

    def setup(self, opts):
        self.__key = opts.key
        self.__jwk = opts.jwk
        self.__public = self._get_public_key()

        p = urllib.parse.urlparse(opts.key.id)
        self.vault = str.replace(p.netloc, '.vault.azure.net', '')

    def has_public_key(self) -> bool:
        """Return a boolean indicating if the private key is able to
        extract and provide its public key.
        """
        return True

    async def get_public_key(self):
        """Return the public key."""
        return self.__public

    async def sign(self, blob: bytes, hasher, *args, **kwargs) -> bytes:
        """Returns the signature of byte-sequence `blob`, DER-encoded."""
        hasher.update(blob)
        digest = hasher.finalize()
        async with self.get_crypto_client(self.__key.id) as client:
            signature = await self._sign(client, self.__jwk.crv, digest)
        return utils.encode_dss_signature(
            int.from_bytes(signature[:32], 'big'),
            int.from_bytes(signature[32:], 'big'),
        )

    def _get_public_key(self):
        n = ec.EllipticCurvePublicNumbers(
            int.from_bytes(self.__jwk.x, 'big'),
            int.from_bytes(self.__jwk.y, 'big'),
            self.curve()
        )
        return EllipticCurvePublicKey(
            n.public_key(),
            capabilities=self._get_capabilities()
        )

    def _get_capabilities(self) -> list:
        return [self.__algorithm_mapping[self.__jwk.crv]]
