"""Declares :class:`Network`."""
from sqlalchemy import Column
from sqlalchemy import SmallInteger
from sqlalchemy import String

from .base import Base


class Network(Base):
    """Maps numeric ids to network Uniform Resource Names (URNs)."""
    __tablename__ = 'networks'
    __module__ = 'ibrb.ext.meta.orm'

    id = Column(
        SmallInteger,
        primary_key=True,
        nullable=False,
        name='id'
    )

    protocol = Column(
        String,
        nullable=False,
        name='protocol'
    )

    urn = Column(
        String,
        unique=True,
        nullable=False,
        name='urn'
    )

    #: The preferred data source for a network client represented as a
    #: Data Source Name (DSN).
    dsn = Column(
        String,
        nullable=False,
        name='dsn'
    )

