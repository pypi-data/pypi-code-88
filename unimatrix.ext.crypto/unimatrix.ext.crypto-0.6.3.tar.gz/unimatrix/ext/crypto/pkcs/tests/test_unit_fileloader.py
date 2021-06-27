# pylint: skip-file
import os

from unimatrix.lib.test import AsyncTestCase

from ... import chain
from ... import trust
from ...tests import const
from .. import FileLoader


class FileLoaderTestCase(AsyncTestCase):

    async def setUp(self):
        self.loader = FileLoader({
            'keys': [
                {
                    "path": const.RSA_PRIVATE_KEY
                }
            ]
        })
        await self.loader.load()

    async def test_load_without_id_uses_filename(self):
        _, fn = os.path.split(const.RSA_PRIVATE_KEY)
        chain.get(fn)
        trust.get(fn)
