import requests
import json
from dadastock.trade import Trade
from dadastock.tick import Tick
from dadastock.inventory import Inventory
import datetime
import pandas as pd
from dadastock.stockEnum import StockEnum
from dadastock.apiException import secretClientIdException, \
						secretTokenException, \
						InternalServerException, \
						LoginException, \
						TradeException, \
						OrderParameterException, \
						BalanceAPIException, \
						InventoryException, \
						TickException
class stockApi():
	def __init__(self,url,port):
		self.secretClientId = ''
		self.secretToken = ''
		self.backendUrl = "http://%s:%s/" % (url,port)
		self.data = {}
		self.constant = StockEnum
	def login(self,secretClientId,secretToken):
		data = {
			"secretClientId":secretClientId,
			"secretToken":secretToken,
		}
		response = requests.post(self.backendUrl + "api/login/API",json = data)
		try:
			jsondata = json.loads(response.text)
		except Exception as e:
			raise InternalServerException()
		else:
			if jsondata["status"] == 200:
				self.secretClientId = secretClientId
				self.secretToken = secretToken
				self.data = data
				return response.text
			else:
				jsondata = json.loads(response.text)
				raise LoginException(jsondata["status"],jsondata["message"])

	def getBalance(self):
		if not self.secretClientId:
			raise secretClientIdException()
		if not self.secretToken:
			raise secretTokenException()
		data = {
			"secretClientId":self.secretClientId,
			"secretToken":self.secretToken
		}
		response = requests.post(self.backendUrl + "api/user/balanceAPI",json = data)
		try:
			jsondata = json.loads(response.text)
		except Exception as e:
			raise InternalServerException()
		else:
			if jsondata["status"] == 200:
				return jsondata["data"]
			else:
				raise BalanceAPIException(jsondata["status"],jsondata["error"])

	def createOrder(self,stockno,amount, \
		orderType,price,tradeCategory, \
		tradeType,takeprice,pendingType):
		if not self.secretClientId:
			raise secretClientIdException()
		if not self.secretToken:
			raise secretTokenException()
		if (tradeType == "Common") or (tradeType == "Fixing"):
			if amount < 1000:
				raise TradeException("400","選取Common但數量小於1000!")
		else:
			if amount >= 1000:
				raise TradeException("400","選取Common以外但數量大於1000!")
		data = {
			"secretClientId":self.secretClientId,
			"secretToken":self.secretToken,
			"stockno":stockno,
			"amount":amount,
			"orderType":orderType,
			"price":price,
			"tradeCategory":tradeCategory,
			"tradeType":tradeType,
			"takeprice":takeprice,
			"pendingType":pendingType, 
		}
		response = requests.post(self.backendUrl + "api/order",json = data)
		try:
			jsondata = json.loads(response.text)
		except Exception as e:
			raise InternalServerException()
		if jsondata["status"] == 200:
			return Trade(**jsondata["data"])
		else:
			if jsondata["status"] == 704 or jsondata["status"] == 703:
				raise OrderParameterException(jsondata["status"],jsondata["error"])
			raise TradeException(jsondata["status"],jsondata["error"]) 


	def checkOrder(self,orderno):
		if not self.secretClientId:
			raise secretClientIdException()
		if not self.secretToken:
			raise secretTokenException()
		data = {
			"secretClientId":self.secretClientId,
			"secretToken":self.secretToken
		}
		response = requests.post(self.backendUrl + "api/order/APIOrder/%s"%orderno,json = data)
		try:
			jsondata = json.loads(response.text)
		except Exception as e:
			raise InternalServerException()
		else:
			if jsondata["status"] == 200:
				return Trade(**jsondata["data"])
			else:
				raise TradeException(jsondata["status"],jsondata["error"])


	def checkAllOrder(self):
		if not self.secretClientId:
			raise secretClientIdException()
		if not self.secretToken:
			raise secretTokenException()
		data = {
			"secretClientId":self.secretClientId,
			"secretToken":self.secretToken
		}
		response = requests.post(self.backendUrl + "api/order/APIOrder",json = data)
		try:
			jsondata = json.loads(response.text)
		except Exception as e:
			raise InternalServerException()
		else:
			if jsondata["status"] == 200:
				data = []
				for o in jsondata["data"]:
					data.append(Trade(**o))
				return data
			else:
				raise TradeException(jsondata["status"],jsondata["error"])


	def checkOrderByDate(self,requestDate = datetime.datetime.now().strftime('%Y-%m-%d')):
		if not self.secretClientId:
			raise secretClientIdException()
		if not self.secretToken:
			raise secretTokenException()
		data = {
			"secretClientId":self.secretClientId,
			"secretToken":self.secretToken
		}
		response = requests.post(self.backendUrl + "api/order/APIOrder/%s"%requestDate,json = data)
		try:
			jsondata = json.loads(response.text)
		except Exception as e:
			raise InternalServerException()
		else:
			if jsondata["status"] == 200:
				data = []
				for o in jsondata["data"]:
					data.append(Trade(**o))
				return data
			else:
				raise TradeException(jsondata["status"],jsondata["error"])

	def checkOrderByInterval(self,startDate,endDate):
		if not self.secretClientId:
			raise secretClientIdException()
		if not self.secretToken:
			raise secretTokenException()
		data = {
			"secretClientId":self.secretClientId,
			"secretToken":self.secretToken
		}
		response = requests.post(self.backendUrl + "api/order/APIOrder/%s/%s"%(startDate,endDate),json = data)
		try:
			jsondata = json.loads(response.text)
		except Exception as e:
			raise InternalServerException()
		else:
			if jsondata["status"] == 200:
				data = []
				for o in jsondata["data"]:
					data.append(Trade(**o))
				return data
			else:
				raise TradeException(jsondata["status"],jsondata["error"])

	def cancelOrder(self,trade):
		if not self.secretClientId:
			raise secretClientIdException()
		if not self.secretToken:
			raise secretTokenException()
		orderno = trade.orderno
		data = {
			"secretClientId":self.secretClientId,
			"secretToken":self.secretToken,
			"orderno":orderno
		}
		response = requests.put(self.backendUrl + "api/order",json = data)
		try:
			jsondata = json.loads(response.text)
		except Exception as e:
			raise InternalServerException()
		else:
			if jsondata["status"] == 200:
				return Trade(**jsondata["data"])
			else:
				raise TradeException(jsondata["status"],jsondata["message"])

	def modifyOrder(self,trade,modifyType,modifyValue):
		if not self.secretClientId:
			raise secretClientIdException()
		if not self.secretToken:
			raise secretTokenException()
		orderno = trade.orderno
		data = {
			"orderno":orderno,
			"secretClientId":self.secretClientId,
			"secretToken":self.secretToken,
			"modifyType":modifyType,
			"modifyValue":modifyValue
		}
		response = requests.put(self.backendUrl + "api/order",json = data)
		try:
			jsondata = json.loads(response.text)
		except Exception as e:
			raise InternalServerException()
		else:		
			if jsondata["status"] == 200:
				return Trade(**jsondata["data"])
			else:
				raise TradeException(jsondata["status"],jsondata["message"])

	def stockdata(self,stockno):
		response = requests.post(self.backendUrl + "api/stocks/" + str(stockno))
		try:
			jsondata = json.loads(response.text)
		except Exception as e:
			raise InternalServerException()
		else:
			if jsondata["status"] == 200:
				data = jsondata["data"]
				returndata = [[i[j] for i in data] for j in range(8)]
				return Tick(*returndata)
			else:
				raise TickException(jsondata["status"],jsondata["error"])

	def getKBardata(self,stockno,startDate,endDate):
		# datetime format: 20200101
		response = requests.post(self.backendUrl + "api/stocks/{}/{}/{}".format(stockno,startDate,endDate))
		try:
			jsondata = json.loads(response.text)
		except Exception as e:
			raise InternalServerException()
		else:
			if jsondata["status"] == 200:
				data = jsondata["data"]
				if not data:
					return pd.DataFrame()
				df = pd.DataFrame(data)
				df.columns = ["stockno","stockname","ts","Open","Close","Low","High","Volume"]
				df = df.drop(columns = ["stockno","stockname"])
				return df
			else:
				raise TickException(jsondata["status"],jsondata["error"])

	def getInventory(self):
		if not self.secretClientId:
			raise secretClientIdException()
		if not self.secretToken:
			raise secretTokenException()
		data = {
			"secretClientId":self.secretClientId,
			"secretToken":self.secretToken
		}
		response = requests.post(self.backendUrl + "api/inventory/api",json = data)
		try:
			jsondata = json.loads(response.text)
		except Exception as e:
			raise InternalServerException()
		else:
			if jsondata["status"] == 200:
				data = jsondata["data"]
				return [Inventory(**data[i]) for i in range(len(data))]
			else:
				raise InventoryException(jsondata["status"],jsondata["error"])


				