import re

from pgsaw.UPCType import UPCType


class UPC:
	company: int = 0
	product = 0
	lead_a = 0
	lead_b = 0
	
	"""UPC
	Representation of a UPC-A (referred to simply as UPC hereon) or EAN-13
	
	:var company: (12345 in ab-12345-67890-c). The 5 digit representation of the company, ignoring the first 1 (UPC) or 2 (EAN-13) digits.
	:var product: (67890 in ab-12345-67890-c). The 5 digit representation of the product.
	:var lead_a: (a in ab-12345-67890-c). The first digit, only applicable to EAN-13.
	:var lead_b: (b in ab-12345-67890-c). The second digit in EAN-13 or first in UPC."""

	def __init__(self, company=0, product=0, lead_a=0, lead_b=0):
		self.company = company
		self.product = product
		self.lead_a = lead_a
		self.lead_b = lead_b

	@classmethod
	def parse(cls, upcString, includesCheckDigit=None):
		"""
		:param upcString: A string to attempt to parse. Accepts the following formats: 12345-67890, b-12345-67890, ab-12345-67890, 12345-67890-c, b-12345-67890-c,
		ab-12345-67890-c, 1234567890, 1234567890c, b1234567890, b1234567890c, ab1234567890, ab1234567890c. Some formats require the includesCheckDigit param to be set.
		UPC-E is not yet supported.
		:type upcString: str
		:param includesCheckDigit: (needed for some attempts) whether the given string has the check digit included.
		:type includesCheckDigit: bool
		"""
		if re.search("^[0-9]{5}-[0-9]{5}$", upcString) is not None:
			# 12345-67890
			return cls(company=int(upcString[0:5]), product=int(upcString[6:]))
		if re.search("^[0-9]-[0-9]{5}-[0-9]{5}$", upcString) is not None:
			# b-12345-67890
			return cls(lead_b=int(upcString[0]), company=int(upcString[2:7]),
					   product=int(upcString[8:]))
		if re.search("^[0-9]{2}-[0-9]{5}-[0-9]{5}$", upcString) is not None:
			# ab-12345-67890
			return cls(lead_a=int(upcString[0]), lead_b=int(upcString[1]),
					   company=int(upcString[3:8]),
					   product=int(upcString[9:]))
		if re.search("^[0-9]{5}-[0-9]{5}-[0-9]$", upcString) is not None:
			# 12345-67890-c
			# However, we ignore the check digit and calculate it ourselves later
			return cls(company=int(upcString[0:5]),
					   product=int(upcString[6:11]))
		if re.search("^[0-9]-[0-9]{5}-[0-9]{5}-[0-9]$", upcString) is not None:
			# b-12345-67890-c
			return cls(lead_b=int(upcString[0]), company=int(upcString[2:7]),
					   product=int(upcString[8:13]))
		if re.search("^[0-9]{2}-[0-9]{5}-[0-9]{5}-[0-9]$", upcString) is not None:
			# ab-12345-67890-c
			return cls(lead_a=int(upcString[0]), lead_b=int(upcString[1]),
					   company=int(upcString[3:8]),
					   product=int(upcString[9:14]))
		if re.search("^[0-9]{10}$", upcString) is not None:
			# 1234567890
			return cls(company=int(upcString[0:5]),
					   product=int(upcString[5:]))
		if re.search("^[0-9]{11}$", upcString) is not None and includesCheckDigit is True:
			# 1234567890c
			return cls(company=int(upcString[0:5]),
					   product=int(upcString[5:10]))
		if re.search("^[0-9]{11}$", upcString) is not None and includesCheckDigit is False:
			# b1234567890
			return cls(lead_b=int(upcString[0]),
					   company=int(upcString[1:6]),
					   product=int(upcString[6:11]))
		if re.search("^[0-9]{12}$", upcString) is not None and includesCheckDigit is True:
			# b1234567890c
			return cls(lead_b=int(upcString[0]),
					   company=int(upcString[1:6]),
					   product=int(upcString[6:11]))
		if re.search("^[0-9]{12}$", upcString) is not None and includesCheckDigit is False:
			# ab1234567890
			return cls(lead_a=int(upcString[0]),
					   lead_b=int(upcString[1]),
					   company=int(upcString[2:7]),
					   product=int(upcString[7:12]))
		if re.search("^[0-9]{13}$", upcString) is not None and includesCheckDigit is not False:
			# ab1234567890c
			return cls(lead_a=int(upcString[0]),
					   lead_b=int(upcString[1]),
					   company=int(upcString[2:7]),
					   product=int(upcString[7:12]))
		raise ValueError(f"UPC {upcString} format could not be inferred")

	def getCheckDigit(self):
		"""Calculate the check digit.
		:rtype: int
		:returns: check digit"""
		companyStr = str(self.company+100000)
		productStr = str(self.product+100000)
		return 10 - ((self.lead_a +
								 (self.lead_b *3) +
								 int(companyStr[1]) +
								 (int(companyStr[2]) *3) +
								 int(companyStr[3]) +
								 (int(companyStr[4]) *3) +
								 int(companyStr[5])+
								 (int(productStr[1])*3) +
								 int(productStr[2])+
								 (int(productStr[3])*3) +
								 int(productStr[4]) +
								 (int(productStr[5]) *3))%10)

	def getType(self):
		if self.lead_a == 0:
			if self.lead_b == 0:
				if self.company == 0:
					if 4999 >= self.product >= 3000 or 84999 >= self.product >= 83000\
							or 94999 >= self.product >= 93000:
						return UPCType.PRODUCE_LOOKUP
					else:
						return UPCType.LOOKUP_UNKNOWN # Commonly used for store internal lookups and store coupons
				else:
					return UPCType.STANDARD
			elif self.lead_b == 2:
				return UPCType.RANDOM_WEIGHT
			elif self.lead_b == 3:
				return UPCType.NDC # Supposed to be for drugs, but is rarely used.
			elif self.lead_b == 4:
				return UPCType.STORE_INTERNAL # Commonly used for rewards cards or coupons
			elif self.lead_b == 5:
				return UPCType.COUPON # Haven't seen this used, but I'll trust Wikipedia
			elif (self.lead_b == 1 or self.lead_b >= 6) and self.company >= 10000:
				# TODO Verify this, from what I can tell it may be possible to have a company as low as 10 but I have not seen it myself
				return UPCType.STANDARD
		else:
			if self.company >= 10000:
				# TODO more research on EAN-13 and possible prefixes
				return UPCType.STANDARD
		return UPCType.UNKNOWN
