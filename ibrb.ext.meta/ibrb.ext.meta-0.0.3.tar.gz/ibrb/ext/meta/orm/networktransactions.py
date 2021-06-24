"""Declares :class:`NetworkTransaction`."""
from sqlalchemy import Column
from sqlalchemy import BigInteger
from sqlalchemy import ForeignKey
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy import UniqueConstraint

from .base import Base
from .networkaddresses import NetworkAddress


class NetworkTransaction(Base):
    """Describes a transaction on a blockchain network."""
    __tablename__ = 'networktransactions'
    __module__ = 'ibrb.ext.meta.orm'

    address_id = Column(
        ForeignKey(NetworkAddress.id),
        primary_key=True,
        nullable=False,
        name='address_id'
    )

    transaction_id = Column(
        String,
        primary_key=True,
        nullable=False,
        name='transaction_id'
    )

    block = Column(
        BigInteger,
        nullable=False,
        name='block'
    )

    timestamp = Column(
        BigInteger,
        nullable=False,
        name='timestamp'
    )

    sender = Column(
        String,
        nullable=False,
        name='sender'
    )

    receiver = Column(
        String,
        nullable=False,
        name='receiver'
    )

    #: The cost of the transaction, in the networks' native token.
    cost = Column(
        Numeric,
        nullable=False,
        name='cost'
    )

    #: The amount of the networks' native token transferred, if any.
    amount = Column(
        Numeric,
        nullable=False,
        name='amount'
    )

    __table_args__ = (
        UniqueConstraint('address_id', 'transaction_id'),
    )
