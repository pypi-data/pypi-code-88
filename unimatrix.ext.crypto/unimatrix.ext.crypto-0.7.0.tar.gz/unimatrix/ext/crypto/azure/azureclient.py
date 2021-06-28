"""Declares :class:`AzureClient`."""
from azure.identity.aio import DefaultAzureCredential
from azure.keyvault.keys.aio import KeyClient
from azure.keyvault.keys.crypto.aio import CryptographyClient
from azure.keyvault.keys.crypto.aio import SignatureAlgorithm


class AzureClient:
    """Abstraction for Azure Cloud operations."""
    __signature_mapping = {
        'P-256K'    : SignatureAlgorithm.es256_k,
        'SECP256K1' : 'ECDSA256',
    }

    @property
    def credential(self) -> DefaultAzureCredential:
        """Return a :class:`azure.identity.aio.DefaultAzureCredential`
        instance.
        """
        return DefaultAzureCredential()

    @property
    def key_client(self) -> KeyClient:
        """Return a :class:`azure.identity.aio.KeyClient` instance."""
        return KeyClient(vault_url=self.vault_url, credential=self.credential)

    @property
    def vault_url(self) -> str:
        """Return a string containing the Azure Key Vault URL."""
        return f"https://{self.vault}.vault.azure.net/"

    def get_crypto_client(self, keyid) -> CryptographyClient:
        """Return a :class:`CryptographyClient` instance."""
        return CryptographyClient(keyid, self.credential)

    async def _sign(self, client, algorithm: str, blob: bytes) -> bytes:
        result = await client.sign(
            self.__signature_mapping[algorithm],
            blob
        )
        return result.signature
