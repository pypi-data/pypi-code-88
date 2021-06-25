from wcd_geo_db.modules.client import NestedClient
from .divisions import DivisionsClient


__all__ = 'NamesClient',


class NamesClient(NestedClient):
    divisions: DivisionsClient = DivisionsClient.as_property()
