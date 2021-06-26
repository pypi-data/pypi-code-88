# pylint: skip-file
import asyncio
import unittest

from ibrb.ext import clients


class ClientLookupTestCase(unittest.TestCase):

    def test_bsc_mainnet(self):
        self.assertCanLookupClient('urn:ibrb:network:bsc:main')

    def test_bsc_testnet(self):
        self.assertCanLookupClient('urn:ibrb:network:bsc:test')

    def test_eth_mainnet(self):
        self.assertCanLookupClient('urn:ibrb:network:eth:main')

    def test_eth_testnet(self):
        self.assertCanLookupClient('urn:ibrb:network:eth:test')

    def assertCanLookupClient(self, network):
        c = asyncio.run(clients.get(network))
        self.assertIsInstance(c, clients.IClient)
