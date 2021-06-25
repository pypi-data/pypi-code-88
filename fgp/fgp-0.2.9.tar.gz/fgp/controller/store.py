import datetime
import pandas
from typing import List, Dict, Tuple
from .client import Client
from fgp.utils import datetime_to_ms
import dateutil.parser as parser

class Store:

    _client: Client = None

    def __init__(self, client: Client):
        self._client = client

    @staticmethod
    def parse_get_data(data: Dict[str, Dict], fields=None) -> pandas.DataFrame:
        devices = list(data.keys())
        dfs: List[pandas.DataFrame] = list()
        for device_name in devices:
            rows = data[device_name].get('data')
            if len(rows) == 0:
                continue
            df = pandas.DataFrame.from_dict(rows)
            cols_initial = [k for k in list(df.columns) if k != 'timestamp']
            df['device_name'] = device_name
            df['device_key'] = data[device_name].get('deviceKey')
            cols_final = ['device_name', 'device_key', 'timestamp'] + cols_initial

            if fields is not None:
                fields_to_add = [f for f in fields if f not in cols_final]
                for f in fields_to_add:
                    df[f] = None
                    cols_final.append(f)

            dfs.append(df[cols_final])

        if len(dfs):
            return pandas.concat(dfs)
        else:
            return None

    def get_data(
            self,
            device_type: str,
            store_name: str,
            date_from: datetime.datetime,
            date_to: datetime.datetime,
            fields: List[str]=None,
            devices: List[str]=None
        ) -> List[Dict[str, str]]:
        payload = {
            'start': datetime_to_ms(date_from),
            'end': datetime_to_ms(date_to),
            'fields': fields,
            'devices': devices
        }
        res = self._client.post(route=f'{device_type}/{store_name}', data=payload)
        data = self.parse_get_data(res, fields=fields)
        return data

    @staticmethod
    def parse_get_first_last(data):
        first = datetime.datetime.utcfromtimestamp(data.get('first', {}).get('timeKey') / 1000)
        last = datetime.datetime.utcfromtimestamp(data.get('last', {}).get('timeKey') / 1000)
        return (first, last)

    def get_first_last(self, device_type: str, store_name: str, device_name: str) -> Tuple[datetime.datetime, datetime.datetime]:
        res = self._client.get(route=f'{device_type}/{store_name}/{device_name}/first-last')
        return self.parse_get_first_last(res)

    def get_latest(self, device_type: str, device_name: str, store_name: str) -> dict:
        res = self._client.get(route=f'{device_type}/name/{device_name}/{store_name}/{device_name}/last')
        if 'last' in res:
            return res.get('last')
        return None

    # def get_range(self, device_type: str, device_name: str, store_name: str, date_from: datetime.datetime, date_to: datetime.datetime) -> List[dict]:
    #     res = self._client.post(
    #         route=f'{device_type}/{store_name}',
    #         data={
    #             'devices': [device_name],
    #             'start': datetime_to_ms(date_from),
    #             'end': datetime_to_ms(date_to)
    #         }
    #     )
    #     if device_name in res:
    #         return res.get(device_name, {}).get('data')
    #     return None