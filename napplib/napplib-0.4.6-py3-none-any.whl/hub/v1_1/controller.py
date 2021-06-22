import json
import logging
import requests

from typing import List
from .models.product import HubPrice, HubProduct, HubStock, HubStockPrice, HubStoreProductMarketplace, HubStock, HubPrice

class HubController:

    @staticmethod
    def get_store_product_marketplace_limit(server_url, token, marketplace_id, store_id, page=0, status=None, updated_after=None, limit=20):
        # create headers
        headers = dict()
        headers['Authorization'] = f'Bearer {token}'
        status_list = ['pending_register_product', 'done']

        url = '/storeProductsMarketplace/'
        offset = page * limit
        params = {
            "marketplaceId": marketplace_id,
            "storeId": store_id,
            "offset": offset,
            "limit": limit
        }

        if status:
            if not status in status_list:
                raise Exception(f'{status} Status is not in the default list')
            params["statusProcessing"] = status
        if updated_after:
            params["updatedAfter"] = updated_after

        response = requests.get(f"{server_url}{url}", headers=headers, params=params)

        if response.status_code != 200:
            logging.error(f"/storeProductsMarketplace/ ERROR - {response.status_code} - {response.content if not 'html' in str(response.content) else 'Error'} - {status if status else ''}")
            return {
                "total": 0,
                "data": None
            }

        if json.loads(response.content)['total'] == 0:
            logging.info(f"/storeProductsMarketplace/ is empty - {status if status else ''}")
            return {
                "total": 0,
                "data": None
            }

        return json.loads(response.content)

    @staticmethod
    def patch_store_product_marketplace(server_url, token, storeProducts: List[HubStoreProductMarketplace]):
        headers = dict()
        headers['Authorization'] = f'Bearer {token}'

        payload = json.dumps(storeProducts, default = lambda o: o.__dict__)

        return requests.patch(f'{server_url}/storeProductsMarketplace/?list=true&type=2', headers=headers, data=payload)

    @classmethod
    def post_products(cls, server_url, token, store_id, products: List[HubProduct]):
        return cls.__post_integrate_products(server_url, token, products, store_id, fillInventory=False)

    @classmethod
    def post_store_products(cls, server_url, token, store_id, products: List[HubProduct]):
        return cls.__post_integrate_products(server_url, token, products, store_id, fillInventory=True)

    @classmethod
    def post_store_products_marketplace(cls, server_url, token, store_id, marketplace_id, products: List[HubProduct]):
        return cls.__post_integrate_products(server_url, token, products, store_id, marketplace_id, fillInventory=True)

    def __post_integrate_products(server_url, token, products: List[HubProduct], store_id=None, marketplace_id=None, fillInventory=True):
        headers = dict()
        headers['Authorization'] = f'Bearer {token}'

        payload = json.dumps(products, default = lambda o: o.__dict__)

        url = '/integrateProducts/'
        params = {'fillInventory': fillInventory}

        if store_id:
            url += f'{store_id}'

            if marketplace_id:
                url += f'/{marketplace_id}'

        return requests.post(f'{server_url}{url}', headers=headers, data=payload, params=params)

    @classmethod
    def patch_stocks_prices(cls, server_url, token, store_id, marketplace_id, stocksPrices: List[HubStockPrice]):
        payload = json.dumps(stocksPrices, default = lambda o: o.__dict__)

        return cls.__patch_inventories(server_url, token, store_id, marketplace_id, payload, 'stockAndPrice')

    @classmethod
    def patch_prices(cls, server_url, token, store_id, marketplace_id, prices: List[HubPrice]):
        payload = json.dumps(prices, default = lambda o: o.__dict__)

        return cls.__patch_inventories(server_url, token, store_id, marketplace_id, payload, 'price')

    @classmethod
    def patch_stocks(cls, server_url, token, store_id, marketplace_id, stocks: List[HubStock]):
        payload = json.dumps(stocks, default = lambda o: o.__dict__)

        return cls.__patch_inventories(server_url, token, store_id, marketplace_id, payload, 'stock')

    def __patch_inventories(server_url, token, store_id, marketplace_id, payload, type):
        headers = dict()
        headers['Authorization'] = f'Bearer {token}'

        return requests.patch(f'{server_url}/updateInventory/{store_id}/{marketplace_id}/{type}', headers=headers, data=payload)
