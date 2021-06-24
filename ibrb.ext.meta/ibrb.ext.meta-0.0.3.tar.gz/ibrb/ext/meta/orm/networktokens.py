"""Declares :class:`NetworkToken`."""
import decimal

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Numeric
from sqlalchemy import String

from .smartcontracts import SmartContract


class NetworkToken(SmartContract):
    """Describes a token on a specific network."""
    __tablename__ = 'networktokens'
    __module__ = 'ibrb.ext.meta.orm'

    id = Column(
        ForeignKey(SmartContract.id),
        primary_key=True,
        nullable=False,
        name='id'
    )

    symbol = Column(
        String,
        nullable=False,
        name='symbol'
    )

    decimals = Column(
        Integer,
        nullable=False,
        name='decimals'
    )

    supply = Column(
        Numeric,
        nullable=False,
        default=decimal.Decimal('-1'),
        name='supply'
    )
