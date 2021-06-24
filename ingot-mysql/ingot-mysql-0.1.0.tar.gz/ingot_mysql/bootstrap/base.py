from logging import getLogger

from ingots.bootstrap.base import BaseBuilder

import ingot_mysql as package

__all__ = ("IngotMysqlBaseBuilder",)


logger = getLogger(__name__)


class IngotMysqlBaseBuilder(BaseBuilder):

    package = package
