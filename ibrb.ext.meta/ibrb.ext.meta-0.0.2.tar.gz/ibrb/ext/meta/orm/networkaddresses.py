"""Declares :class:`NetworkAddress`."""
import sqlalchemy
from sqlalchemy import Column
from sqlalchemy import BigInteger
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Numeric
from sqlalchemy import UniqueConstraint
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.dialects.postgresql import JSONB
from unimatrix.lib import timezone

from .base import Base
from .networks import Network


class NetworkAddress(Base):
    """Describes an address on a blockchain network that is of interest to
    us.
    """
    __tablename__ = 'networkaddresses'

    id = Column(
        BigInteger,
        primary_key=True,
        nullable=False,
        name='id'
    )

    network_id = Column(
        ForeignKey(Network.id),
        nullable=False,
        name='network_id'
    )

    address = Column(
        String,
        nullable=False,
        name='address'
    )

    label = Column(
        String,
        nullable=False,
        server_default=sqlalchemy.text("''"),
        default='',
        name='label'
    )

    imported = Column(
        BigInteger,
        nullable=False,
        default=timezone.now,
        server_default=sqlalchemy.text('0'),
        name='imported'
    )

    #: The list of events that should be observed for this address. Valid events
    #: are:
    #:
    #: ===============  ========================================================
    #: **Event**        **Description**
    #: ===============  ========================================================
    #: ``transaction``  A transaction i.e. a native token transfer or a smart
    #:                  contract invocation that does not transfer tokens.
    #: ``transfer``     Value transfers using standardized token protocols.
    #: ``balance``      Periodically inspect the balance of the address.
    #: ===============  ========================================================
    observe = Column(
        ARRAY(String),
        nullable=False,
        default=list,
        server_default=sqlalchemy.text("ARRAY[]::varchar[]"),
        name='observe'
    )

    #: The maximum balance in the networks' native token that this address
    #: may have before its marked as dirty. An address is dirty
    #: when an (unspecified) action has to be performed when
    #: a certain balance is present.
    max_balance = Column(
        Numeric,
        nullable=False,
        server_default=sqlalchemy.text('0'),
        default=0,
        name='max_balance'
    )

    annotations = Column(
        JSONB,
        nullable=False,
        server_default=sqlalchemy.text("'{}'"),
        default=dict,
        name='annotations'
    )

    __table_args__ = (
        UniqueConstraint('network_id', 'address'),
    )
