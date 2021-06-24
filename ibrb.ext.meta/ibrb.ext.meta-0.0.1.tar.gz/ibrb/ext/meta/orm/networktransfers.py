"""Declares :class:`NetworkTransfer`."""
from sqlalchemy import Column
from sqlalchemy import BigInteger
from sqlalchemy import ForeignKey
from sqlalchemy import Numeric
from sqlalchemy import String

from .base import Base
from .networkaddresses import NetworkAddress


class NetworkTransfer(Base):
    __tablename__ = 'networktransfers'
    __module__ = 'ibrb.ext.meta.orm'

    id = Column(
        BigInteger,
        primary_key=True,
        nullable=False,
        name='id'
    )

    address_id = Column(
        ForeignKey(NetworkAddress.id),
        nullable=False,
        name='address_id'
    )

    transaction_id = Column(
        String,
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

    contract = Column(
        String,
        nullable=False,
        name='contract_id'
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

    value = Column(
        Numeric,
        nullable=False,
        name='value'
    )
