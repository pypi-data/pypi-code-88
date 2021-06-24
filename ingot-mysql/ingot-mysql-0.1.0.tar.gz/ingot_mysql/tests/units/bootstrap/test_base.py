import typing as t

from ingots.tests.units.bootstrap import test_base

from ingot_mysql.bootstrap import IngotMysqlBaseBuilder

__all__ = ("IngotMysqlBaseBuilderTestCase",)


class IngotMysqlBaseBuilderTestCase(test_base.BaseBuilderTestCase):
    """Contains tests for the IngotMysqlBuilder class."""

    tst_cls: t.Type = IngotMysqlBaseBuilder
    tst_entity_name: str = "ingot_mysql"
    tst_entity_name_upper: str = "INGOT_MYSQL"
    tst_entity_name_class_name: str = "IngotMysql"
    tst_entity_description = (
        "Provides integration with the MySQL DB for Ingots projects"
    )
