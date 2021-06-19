from abc import ABC, abstractmethod

class Store(ABC):
	@abstractmethod
	def __init__(self):
		"""Any setup that may be needed for the store to be used"""
		pass

	@abstractmethod
	def getItem(self, identifier, storeIdentifier):
		"""
		:param identifier: Store specific identifier for the particular item.
		:type identifier: any
		:param storeIdentifier: Identifier for the store in the company (usually called "Store Number")
		:type storeIdentifier: any
		:returns: Item

		:raises: ItemNotFound
		"""
		pass