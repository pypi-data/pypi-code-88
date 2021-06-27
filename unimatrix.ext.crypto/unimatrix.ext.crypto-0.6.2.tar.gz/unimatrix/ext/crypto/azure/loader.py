"""Declares :class:`AzureKeyVaultLoader`."""
from ..keyloader import KeyLoader
from .azureclient import AzureClient

from .privatekey import AzurePrivateKey


class AzureKeyVaultLoader(KeyLoader, AzureClient):
    """A :class:`~unimatrix.ext.crypto.KeyLoader` implementation that loads
    keys from Azure Key Vault.

    To load keys from an Azure Key Vault, make sure the service principal or
    managed identity has the following permissions on the vault:

    - ``List``

    An example configuration is shown below:

    .. code:: python

        CRYPTO_KEYLOADERS = [
            {
                'loader': "unimatrix.ext.crypto.azure.AzureKeyVaultLoader",
                'public_only': False,
                'options': {
                    'vault': 'example'
                }
            }
        ]
    """

    def setup(self, opts):
        """Hook called during instance initialization."""
        self.vault = opts.vault

    async def list(self):
        async with self.key_client as client:
            async for ref in client.list_properties_of_keys():
                yield AzurePrivateKey.fromclient(
                    client, await client.get_key(ref.name))
