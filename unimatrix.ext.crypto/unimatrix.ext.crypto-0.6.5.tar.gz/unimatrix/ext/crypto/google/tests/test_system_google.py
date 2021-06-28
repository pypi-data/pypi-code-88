# pylint: skip-file
import asyncio
import os
import unittest

from ...algorithms import AES256GCM
from ...algorithms import RSAPKCS1v15SHA256
from ...algorithms import RSAOAEPSHA256
from ...defaultkeystore import DefaultKeystore
from ...tests.base import EncryptionTestCase
from ...tests.base import SigningTestCase
from ...tests.base import async_test
from ..googlemanagedkey import GoogleManagedKey


ks = DefaultKeystore({
    'google_sign': {
        'class': "unimatrix.ext.crypto.google.GoogleManagedKey",
        'keyid': "dbdbc0427ec5f0c3f667c7bacff574c9",
        'options': {
            'project': "unimatrixtesting",
            'location': "europe-west4",
            'keyring': "default",
            'key': "rsa_sign_pkcs1_4096_sha256",
            'version': 3
        }
    },
    'google_encrypt': {
        'class': "unimatrix.ext.crypto.google.GoogleManagedKey",
        'keyid': "867546f4b1bb775bc0c649bae98d10cb",
        'options': {
            'project': "unimatrixtesting",
            'location': "europe-west4",
            'keyring': "default",
            'key': "rsa_decrypt_oaep_4096_sha256",
            'version': 1
        }
    },
    'google_symmetric': {
        'class': "unimatrix.ext.crypto.google.GoogleManagedKey",
        'keyid': "925ce93259128e244da9e30c8c677e5a",
        'options': {
            'project': "unimatrixtesting",
            'location': "europe-west4",
            'keyring': "default",
            'key': "google_symmetric_encryption"
        }
    },
})


@unittest.skipIf(not os.getenv('GOOGLE_APPLICATION_CREDENTIALS'),
    "GOOGLE_APPLICATION_CREDENTIALS is not supplied.")
class RSAPKCS1v15SHA256TestCase(SigningTestCase):
    __test__ = True
    algorithm = RSAPKCS1v15SHA256

    @async_test
    async def get_private_key(self):
        return await ks.get('google_sign')


@unittest.skipIf(not os.getenv('GOOGLE_APPLICATION_CREDENTIALS'),
    "GOOGLE_APPLICATION_CREDENTIALS is not supplied.")
class RSAOAEPSHA256TestCase(EncryptionTestCase):
    __test__ = True
    algorithm = RSAOAEPSHA256

    @async_test
    async def get_private_key(self):
        return await ks.get('google_encrypt')


@unittest.skipIf(not os.getenv('GOOGLE_APPLICATION_CREDENTIALS'),
    "GOOGLE_APPLICATION_CREDENTIALS is not supplied.")
class AES256GCMTestCase(EncryptionTestCase):
    __test__ = True
    algorithm = AES256GCM

    @async_test
    async def get_private_key(self):
        return await ks.get('google_symmetric')
