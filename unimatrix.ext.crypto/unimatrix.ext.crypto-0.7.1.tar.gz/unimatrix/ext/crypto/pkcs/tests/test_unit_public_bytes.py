# pylint: skip-file
import os

from unimatrix.lib.test import AsyncTestCase

from ...keychain import Keychain
from ...truststore import TrustStore
from ...tests import const
from .. import FileLoader


class PublicBytesTestCase(AsyncTestCase):

    async def setUp(self):
        self.chain = Keychain()
        self.trust = TrustStore()
        self.loader = FileLoader({
            'keys': [
                {
                    "path": const.RSA_PRIVATE_KEY
                }
            ]
        })
        await self.loader.load(chain=self.chain, trust=self.trust)

    async def test_bytes_serializes_to_subjectpublickeyinfo(self):
        _, fn = os.path.split(const.RSA_PRIVATE_KEY)
        key = self.trust.get(fn)
        self.assertTrue(bytes.startswith(key.bytes,
            b'-----BEGIN PUBLIC KEY-----'))
