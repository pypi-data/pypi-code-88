import typing as t

from ingots.tests.units.scripts import test_base

from ingot_mysql.scripts.ingot_mysql import IngotMysqlDispatcher

__all__ = ("IngotMysqlDispatcherTestCase",)


class IngotMysqlDispatcherTestCase(test_base.BaseDispatcherTestCase):
    """Contains tests for the IngotMysqlDispatcher class and checks it."""

    tst_cls: t.Type = IngotMysqlDispatcher
    tst_builder_name = "test"
