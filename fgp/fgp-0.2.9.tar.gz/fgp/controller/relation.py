from typing import List, Dict
from .client import Client
from fgp.model.model import FGModel
from fgp.utils.datetime_to_ms import datetime_to_ms
import urllib.parse
import datetime


class Relation:

    _client: Client = None

    def __init__(self, client: Client):
        self._client = client

    def get_at(
            self,
            device_type: str,
            device_name: str,
            relation_name: str,
            timestamp: datetime.datetime = None
    ) -> dict:
        params = {
            'isParent': True
        }
        if timestamp:
            params['timestamp']: datetime_to_ms(timestamp)
        res = self._client.get(route=f'{device_type}/{device_name}/relation/{relation_name}', params=params)
        return res

    # def get_schema(self, extension_name) -> FGModel:
    #     data = self._client.get(route=f'{reference_name}')
    #     return FGModel.from_object(reference_name, data.get('links', {}).get('persistenceInfo', []))

