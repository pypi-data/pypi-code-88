from re import match as compararRegex
from decouple import config
from requests import get

class My_IP_Address:
	def setIp(self, ip: str):
		if(compararRegex(r'[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}',ip)):
			self.ip = ip
			self.setURL()
		else:
			print('Endereço de IP inválido')
			
	def setURL(self):
		url = self.getUrlEnv()
		port = self.getPortEnv()
		ip = self.getIP()
		if(port != False and url != False):
			self.url = "%s:%s/ip2location/ip/%s" % (url, port, ip)
		else:
			print("Variáveis de Ambiente Inválidas")

	def getIP(self):
		return self.ip

	def getUrlEnv(self):
		return config('URL')

	def getPortEnv(self):
		return config('PORT')

	def getURL(self):
		return self.url

	def makeRequest(self):
		url = self.getURL()
		print(url)
		r = get(url)
		return r.json()

