import logging
from enum import IntEnum, auto
from typing import Dict

import attr
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker


class DBConfigType(IntEnum):
    INSTANCE = auto()
    TEMPLATE = auto()


@attr.s(kw_only=True, frozen=False, eq=True, auto_attribs=True)
class SQLAlchemyDBConfig:
    type: DBConfigType = None
    identifier: str = None
    # scheme contain the database type name and optionally a driver name. Eg: postgresql+psyops2
    connection_uri: str = None
    # scheme only contain the database type name
    connection_uri_plain: str = None
    engine: Engine = None
    session_maker: sessionmaker = None
    logger: logging.Logger = None
    options: Dict = None
