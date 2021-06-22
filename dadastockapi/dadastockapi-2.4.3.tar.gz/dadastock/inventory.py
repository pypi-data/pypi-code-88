class Inventory:
	def __init__(self,unRealize,nowPrice,stockno,stockname,amount,price):
		self.__stockno = stockno
		self.__stockname = stockname
		self.__amount = amount
		self.__price = price
		self.__unRealize = unRealize
		self.__nowPrice = nowPrice

	@property
	def stockno(self):
		return self.__stockno
	@property
	def stockname(self):
		return self.__stockname
	@property
	def amount(self):
		return self.__amount
	@property
	def price(self):
		return self.__price

	@property
	def unRealize(self):
		return self.__unRealize

	@property
	def nowPrice(self):
		return self.__nowPrice
	
	

	def __str__(self):
		return """
			{
				stockno:%s,
				stockname:%s,
				amount:%s,
				price:%s,
				unRealize:%s,
				nowPrice:%s,
			}
		""" % (self.__stockno,self.__stockname,self.__amount,self.__price,self.__unRealize,self.__nowPrice)

	def toDict(self):
		return {
			"stockno":self.__stockno,
			"stockname":self.__stockname,
			"amount":self.__amount,
			"price":self.__price,
			"unRealize":self.__unRealize,
			"nowPrice":self.__nowPrice,
		}