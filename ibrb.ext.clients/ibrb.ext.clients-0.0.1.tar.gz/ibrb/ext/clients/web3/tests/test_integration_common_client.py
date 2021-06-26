# pylint: skip-file
from ibrb.ext.clients import ClientTestCase


@ClientTestCase.factory
class BinanceSmartChainMainNetClientTestCase:
    network = 'urn:ibrb:network:bsc:main'
    balance_address = '0xd3cda913deb6f67967b99d67acdfa1712c293601'


@ClientTestCase.factory
class BinanceSmartChainTestNetClientTestCase:
    network = 'urn:ibrb:network:bsc:test'
    balance_address = '0xd3cda913deb6f67967b99d67acdfa1712c293601'


@ClientTestCase.factory
class EthereumMainNetClientTestCase:
    network = 'urn:ibrb:network:eth:main'
    balance_address = '0xd3cda913deb6f67967b99d67acdfa1712c293601'


@ClientTestCase.factory
class EthereumTestNetClientTestCase:
    network = 'urn:ibrb:network:eth:test'
    balance_address = '0xd3cda913deb6f67967b99d67acdfa1712c293601'
