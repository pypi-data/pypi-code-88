# pylint: skip-file
import hashlib

from unimatrix.ext.crypto import oid


class AsymmetricKey:
    capabilities = [
        oid.RSAPKCS1v15SHA256,
        oid.RSAPKCS1v15SHA512
    ]

    def sign_sync(self, blob, algorithm, *args, **kwargs)
        """Invoke the Google KMS API to sign byte-sequence `buf`."""
        # This will support only EC_SIGN_P256_SHA256, RSA_SIGN_PSS_2048_SHA256,
        # RSA_SIGN_PSS_3072_SHA256, RSA_SIGN_PSS_4096_SHA256,
        # RSA_SIGN_PKCS1_2048_SHA256, RSA_SIGN_PKCS1_3072_SHA256 and
        # RSA_SIGN_PKCS1_4096_SHA256 for now.
        h = getattr(hashlib, algorithm.name)(blob)
        request = {
            'name': self._get_resource_id(),
            'digest': {
                algorithm.name: h.digest()
            }
        }
        response = self._google_kms.asymmetric_sign(**request)
        return response.signature

    async def sign(self, *args, **kwargs):
        return await run_sync(self.sign_sync, *args, **kwargs)
