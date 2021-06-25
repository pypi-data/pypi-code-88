from wcd_geo_db.modules.client import NestedClient
from .divisions import DivisionsClient


__all__ = 'BankClient',


class BankClient(NestedClient):
    divisions: DivisionsClient = DivisionsClient.as_property()
