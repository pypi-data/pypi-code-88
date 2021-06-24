"""Declares :class:`SmartContract`."""
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import UniqueConstraint

from .base import Base
from .networks import Network


class SmartContract(Base):
    """Describes a smart contract on a blockchain network."""
    __tablename__ = 'smartcontracts'
    __module__ = 'ibrb.ext.meta.orm'

    #: A surrogate primary used for internal references.
    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        name='id'
    )

    #: References a :class:`Network` entity, identifying the blockchain network
    #: on which the contract lives.
    network_id = Column(
        ForeignKey(Network.id),
        nullable=False,
        name='network_id'
    )

    #: Specifies the protocol of the smart contract. The
    #: following protocols are supported:
    #:
    #: ==============================   ====================================
    #: **URN**                              **Description**
    #: ==============================   ====================================
    #: ``urn:ibrb:sc:unkown``           The protocol of the smart contract
    #:                                  is unknown
    #: ``urn:ibrb:sc:bep:20``           BEP-20 token on Binance Smart Chain
    #: ``urn:ibrb:sc:dc:pancake:2``     Pancakeswap 2 staking farm/pool
    #: ``urn:ibrb:sc:dc:uniswap``       Uniswap 2 staking farm/pool
    #: ``urn:ibrb:sc:erc:20``           ERC-20 token on Ethereum
    #: ``urn:ibrb:sc:lp:pancake:2``     Pancakeswap 2 liquidity pool
    #: ``urn:ibrb:sc:lp:uniswap``       Uniswap 2 liquidity pool
    #: ``urn:ibrb:sc:sol:token``        Solana Token Program
    #: ``urn:ibrb:sc:swap``             Unspecified token swapping contract
    #: ``urn:ibrb:sc:swap:pancake:2``   Pancakeswap 2
    #: ``urn:ibrb:sc:swap:uniswap``     Uniswap
    #: ==============================   ===================================
    protocol = Column(
        String,
        nullable=False,
        default='urn:ibrb:contract:unkown',
        name='protocol'
    )

    #: The address that created the contract.
    owner = Column(
        String,
        nullable=False,
        name='owner'
    )

    #: The contract address.
    address = Column(
        String,
        nullable=False,
        name='address'
    )

    #: A human-readable name.
    label = Column(
        String,
        nullable=False,
        default='',
        name='label'
    )

    __table_args__ = (
        UniqueConstraint('network_id', 'address',
            name='smartcontracts_unique_network_address'),
    )
