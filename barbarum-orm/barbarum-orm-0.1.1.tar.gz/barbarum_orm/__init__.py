r"""
barbarum-orm is an ORM framework for database access.
"""

project_name = "barbarum-orm"
project_version = '0.1.1'
author_name = 'Ding Wei'
author_email = 'feedback@barbarum.com'

from .common.dialect.dialect import Dialect
from .common.dialect.mysql_dialect import MysqlDialect, MysqlDriver
from .common.database import Database, Base
from .common.repository import Repository