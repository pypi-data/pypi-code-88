from logging import getLogger

from ingots.bootstrap.base import BaseBuilder

import ingot_sql as package

__all__ = ("IngotSqlBaseBuilder",)


logger = getLogger(__name__)


class IngotSqlBaseBuilder(BaseBuilder):

    package = package
