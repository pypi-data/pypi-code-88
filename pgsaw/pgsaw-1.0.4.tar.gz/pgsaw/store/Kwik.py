import requests
from bs4 import BeautifulSoup, Tag

from pgsaw.Item import Item
from pgsaw.ItemNotFound import ItemNotFound
from pgsaw.Store import Store

class Kwik(Store):
	"""
	Kwik Star and Kwik Trip fuel prices.
	"""
	__parser = None

	def __init__(self, parser="html.parser"):
		super().__init__()
		self.__parser = parser

	def getItem(self, identifier, storeIdentifier):
		"""
		:param identifier: Fuel grade name (ex "UNLEADED")
		:param storeIdentifier: Store number (ex 1099)
		:returns Item object for the fuel.
		"""
		url = f"https://www.kwiktrip.com/locator/store?id={storeIdentifier}"
		response = requests.get(url)
		htmlObj = BeautifulSoup(response.text, self.__parser)
		name: Tag
		item = Item()
		try:
			name = htmlObj.body.find('div', attrs={'class':'Store__fuelName'}, string=identifier)
		except AttributeError:
			raise ItemNotFound()
		item.description = name.next_sibling.next_sibling.text[1:-1]
		priceStr:str = name.next_sibling.next_sibling.next_sibling.next_sibling.find(attrs={'class': 'Store__priceAmount'}).text
		price = (int(priceStr[0:priceStr.index(".")]) * 100) + (int(priceStr[priceStr.index(".")+1:priceStr.index(".")+3]))
		item.tagPrice = price
		item.basePrice = price
		return item