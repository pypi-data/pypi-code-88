import requests
from .models.authentication import MulticoisasAuthentication

class MultiCoisasErp:

	url = 'https://multicoisasnapp.gateway.linkapi.com.br/v1'
	limit = 100

	@classmethod
	def get_digital_stock(cls, authentication: MulticoisasAuthentication, shop_id: int, page) -> dict:

		if not page or page < 0:
			raise ValueError('"page" must be greater than 0')

		headers = { 'Authorization' : str(authentication) }

		result = cls.__get(f'{cls.url}/estoqueDigital/{shop_id}/{page * cls.limit - cls.limit}/{cls.limit}', headers)

		if not result:
			return

		return result.json()


	@classmethod
	def get_comercial_products(cls, authentication: MulticoisasAuthentication, page: int) -> dict:

		if not page or page < 0:
			raise ValueError('"page" must be greater than 0')

		headers = { 'Authorization' : str(authentication) }

		result = cls.__get(f'{cls.url}/produtosComercial/{page * cls.limit - cls.limit}/{cls.limit}', headers)

		if not result:
			return

		return result.json()


	@staticmethod
	def __get(url: str, headers: str):

		result = requests.get(url, headers=headers)

		if result.status_code == 404:
			raise Exception('404 - Page Not Found')

		if result.status_code == 204:
			return None

		if result.status_code != 200:
			raise Exception(result.content.decode())

		return result
