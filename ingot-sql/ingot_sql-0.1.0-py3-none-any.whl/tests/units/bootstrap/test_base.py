import typing as t

from ingots.tests.units.bootstrap import test_base

from ingot_sql.bootstrap import IngotSqlBaseBuilder

__all__ = ("IngotSqlBaseBuilderTestCase",)


class IngotSqlBaseBuilderTestCase(test_base.BaseBuilderTestCase):
    """Contains tests for the IngotSqlBuilder class."""

    tst_cls: t.Type = IngotSqlBaseBuilder
    tst_entity_name: str = "ingot_sql"
    tst_entity_name_upper: str = "INGOT_SQL"
    tst_entity_name_class_name: str = "IngotSql"
    tst_entity_description = "Provides SQS functionality for Ingots projects."
