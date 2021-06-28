"""Sets constants for the :mod:`unimatrix.ext.crypto.lib.google`
package.
"""
from google.cloud.kms import CryptoKeyVersion

from .. import oid


GoogleAlgorithm = CryptoKeyVersion.CryptoKeyVersionAlgorithm
CRYPTO_KEY_ALGORITHMS_OIDS = {
    GoogleAlgorithm.RSA_SIGN_PKCS1_2048_SHA256: oid.RSAPKCS1v15SHA256,
    GoogleAlgorithm.RSA_SIGN_PKCS1_3072_SHA256: oid.RSAPKCS1v15SHA256,
    GoogleAlgorithm.RSA_SIGN_PKCS1_4096_SHA256: oid.RSAPKCS1v15SHA256,
    GoogleAlgorithm.RSA_SIGN_PKCS1_4096_SHA512: oid.RSAPKCS1v15SHA512,
    GoogleAlgorithm.RSA_DECRYPT_OAEP_2048_SHA256: oid.RSAOAEP,
    GoogleAlgorithm.RSA_DECRYPT_OAEP_3072_SHA256: oid.RSAOAEP,
    GoogleAlgorithm.RSA_DECRYPT_OAEP_4096_SHA256: oid.RSAOAEP,
    GoogleAlgorithm.GOOGLE_SYMMETRIC_ENCRYPTION: oid.AES256GCM,
}


GOOGLE_SYMMETRIC_ENCRYPTION = GoogleAlgorithm.GOOGLE_SYMMETRIC_ENCRYPTION
