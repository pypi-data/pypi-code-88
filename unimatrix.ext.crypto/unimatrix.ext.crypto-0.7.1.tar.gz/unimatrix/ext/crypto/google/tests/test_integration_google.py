# pylint: skip-file
from unittest.mock import AsyncMock
from unittest.mock import MagicMock

import google.api_core.exceptions
from unimatrix.lib.test import AsyncTestCase

from ..kmsloader import KMSLoader


class KMSLoaderTestCase(AsyncTestCase):

    async def test_list_crypto_keys_survives_404(self):
        loader = KMSLoader({
            'project': 'foo',
            'location': 'bar',
            'keyring': 'baz'
        })
        loader._get_kms_client = MagicMock(
            side_effect=google.api_core.exceptions.NotFound("Foo")
        )
        result = await loader._list_crypto_keys()
        self.assertEqual(result, None)
