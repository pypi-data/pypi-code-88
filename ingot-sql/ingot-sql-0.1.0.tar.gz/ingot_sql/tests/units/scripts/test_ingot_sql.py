import typing as t

from ingots.tests.units.scripts import test_base

from ingot_sql.scripts.ingot_sql import IngotSqlDispatcher

__all__ = ("IngotSqlDispatcherTestCase",)


class IngotSqlDispatcherTestCase(test_base.BaseDispatcherTestCase):
    """Contains tests for the IngotSqlDispatcher class and checks it."""

    tst_cls: t.Type = IngotSqlDispatcher
    tst_builder_name = "test"
