# pylint: skip-file
import asyncio
import os
import unittest


def async_test(func):
    def f(self, *args, **kwargs):
        return self.loop.run_until_complete(func(self, *args, **kwargs))
    return f


class AlgorithmTestCase(unittest.TestCase):
    __test__ = False

    def setUp(self):
        try:
            self.loop = asyncio.get_event_loop()
        except RuntimeError:
            self.loop = asyncio.new_event_loop()
        self.key = self.get_private_key()
        self.data = b'Hello world!'

    def get_private_key(self):
        raise NotImplementedError


class SigningTestCase(AlgorithmTestCase):

    @async_test
    async def test_sign(self):
        await self.algorithm.sign(self.key, self.data)

    @async_test
    async def test_verify(self):
        sig = await self.algorithm.sign(self.key, self.data)
        self.assertTrue(sig.verify(self.key, self.data))

    @async_test
    async def test_verify_with_invalid_data(self):
        sig = await self.algorithm.sign(self.key, self.data)
        with self.assertRaises(sig.InvalidSignature):
            sig.verify(self.key, b'dsfsfs')


class EncryptionTestCase(AlgorithmTestCase):

    @async_test
    async def test_encrypt(self):
        await self.algorithm.encrypt(self.key, self.data)

    @async_test
    async def test_encrypt_decrypt(self):
        ct = await self.algorithm.encrypt(self.key, self.data)
        self.assertEqual(await ct.decrypt(self.key), self.data)
