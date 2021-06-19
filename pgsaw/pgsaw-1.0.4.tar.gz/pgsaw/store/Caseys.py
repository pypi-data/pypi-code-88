import json

import requests

from pgsaw.Item import Item
from pgsaw.ItemNotFound import ItemNotFound
from pgsaw.Store import Store
from pgsaw.StoreNotFound import StoreNotFound


class Caseys(Store):
	"""
	Casey's fuel prices.
	"""
	__clientId: str
	__clientSecret: str
	def __init__(self, clientId, clientSecret):
		super().__init__()
		self.__clientId = clientId
		self.__clientSecret = clientSecret

	def getItem(self, identifier, storeIdentifier):
		"""
		:param identifier: Fuel "productCode" (ex "87 10%E")
		:param storeIdentifier: Store number (ex 1099)
		:returns Item object for the fuel.
		"""
		url = "https://api.caseys.io/caseys-ea-public-api/api/store-fuelprice"

		payload = json.dumps({
			"storeId": [
				f"{storeIdentifier}"
			]
		})
		headers = {
			'Content-Type': 'application/json',
			'client_secret': f"{self.__clientSecret}",
			'client_id': f"{self.__clientId}"
		}

		response = requests.request("POST", url, headers=headers, data=payload)
		item = Item()
		try:
			products = response.json()["fuelPriceData"][0]["products"]
		except KeyError:
			raise StoreNotFound() from None
		for product in products:
			if product["productCode"] == identifier:
				item.description = product["fuelDescription"]
				item.productCode = product["productCode"]
				item.octane = product["octane"]
				item.streetFighter = product["streetFighter"]	# I have no idea what this is, my best guess is this indicates if the fuel has an outdoor sign
																# I've only seen it as "YES" or "NO" so I may change this to a bool at some point
				priceStr = product["price"]
				price = (int(priceStr[0:priceStr.index(".")]) * 100) + (int(priceStr[priceStr.index(".")+1:priceStr.index(".")+3]))
				item.basePrice = price
				item.tagPrice = price
				return item
		raise ItemNotFound()