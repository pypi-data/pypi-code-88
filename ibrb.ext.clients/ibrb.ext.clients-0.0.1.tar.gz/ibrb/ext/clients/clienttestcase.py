# pylint: skip-file
"""Declares :class:`ClientTestCase`."""
import unittest
from asyncio import run

from .utils import get


class ClientTestCase(unittest.TestCase):
    __test__ = False

    @classmethod
    def factory(cls, child_class):
        return type(child_class.__name__, (cls,), {
            '__test__': True,
            **child_class.__dict__
        })

    def setUp(self):
        self.client = run(get(self.network))

    def test_lookup_latest_block(self):
        result = run(self.client.get_latest_block())

    def test_lookup_balance(self):
        result = run(self.client.get_balance(self.balance_address))
