from wcd_geo_db.modules.client import Client

from .modules.addresses import AddressesClient
from .modules.bank import BankClient
from .modules.names import NamesClient
from .conf import Settings


__all__ = 'GeoClient',


class GeoClient(Client):
    settings: Settings

    bank: BankClient = BankClient.as_property()
    names: NamesClient = NamesClient.as_property()
    addresses: AddressesClient = AddressesClient.as_property()
