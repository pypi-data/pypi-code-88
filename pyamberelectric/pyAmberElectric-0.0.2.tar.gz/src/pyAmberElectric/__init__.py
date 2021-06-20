import boto3
from .aws_srp import AWSSRP
import json
import requests
import time

class pyAmberElectric():

	#nabbed from website, subject to change without notice.
	__region = 'ap-southeast-2'
	__poolID = 'ap-southeast-2_vPQVymJLn'
	__clientID = '11naqf0mbruts1osrjsnl2ee1'
	_URL = 'https://backend.amberelectric.com.au/graphql'

	#Offical website makes requests with the following body. Attempts to tailor the request to only get specific data failed, so we'll just get everything everytime.
	__payload = {"operationName":"LivePrice","variables":{},"query":"query LivePrice($period: String) {\n  whoami\n  sitePricing(period: $period) {\n    remark\n    solarRemark\n    spikeRemark\n    meterWindows {\n      usageType\n      forecastInformation {\n        start\n        end\n        level\n        title\n        message\n        __typename\n      }\n      currentPeriod {\n        ...periodFields\n        __typename\n      }\n      previousPeriods {\n        ...periodFields\n        __typename\n      }\n      forecastPeriods {\n        ...periodFields\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  settings {\n    customerInfo {\n      address {\n        state\n        postcode\n        __typename\n      }\n      fullName\n      featureFlags\n      __typename\n    }\n    __typename\n  }\n  snapshots {\n    periodSummary {\n      ...UsagePeriodSummaryFields\n      __typename\n    }\n    billingDays {\n      ...UsageMissingBillingDayFields\n      ...UsageCompleteBillingDayFields\n      ...UsageEstimatedBillingDayFields\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment UsagePeriodSummaryFields on CombinedSummary {\n  costDiff {\n    text\n    indicator\n    __typename\n  }\n  costInCents\n  renewableGridComparison {\n    text\n    indicator\n    __typename\n  }\n  renewablePercentage\n  usageDiff {\n    text\n    indicator\n    __typename\n  }\n  usageKwh\n  usageType\n  __typename\n}\n\nfragment UsageMissingBillingDayFields on MissingBillingDay {\n  marketDate\n  __typename\n}\n\nfragment UsageEstimatedBillingDayFields on EstimatedBillingDay {\n  marketDate\n  stackedUsage {\n    controlled\n    feedIn\n    general\n    __typename\n  }\n  usagePeriods {\n    controlled {\n      end\n      kwh\n      start\n      __typename\n    }\n    feedIn {\n      end\n      kwh\n      start\n      __typename\n    }\n    general {\n      end\n      kwh\n      start\n      __typename\n    }\n    __typename\n  }\n  usageSummaries {\n    combined {\n      costDiff {\n        text\n        indicator\n        __typename\n      }\n      costInCents\n      renewablePercentage\n      renewableGridComparison {\n        text\n        indicator\n        __typename\n      }\n      suppliedDiff {\n        text\n        indicator\n        __typename\n      }\n      suppliedKwh\n      usageDiff {\n        text\n        indicator\n        __typename\n      }\n      usageType\n      usageKwh\n      __typename\n    }\n    controlled {\n      costDiff {\n        text\n        indicator\n        __typename\n      }\n      costInCents\n      renewableGridComparison {\n        text\n        indicator\n        __typename\n      }\n      renewablePercentage\n      usageDiff {\n        text\n        indicator\n        __typename\n      }\n      usageKwh\n      usageType\n      averagePriceDiff {\n        text\n        indicator\n        __typename\n      }\n      averagePriceInCents\n      pricePeriods {\n        ...UsagePeriodFields\n        __typename\n      }\n      __typename\n    }\n    feedIn {\n      averagePriceDiff {\n        text\n        indicator\n        __typename\n      }\n      averagePriceInCents\n      carbonDisplaced\n      carbonDisplacedDiff {\n        text\n        indicator\n        __typename\n      }\n      earningsDiff {\n        text\n        indicator\n        __typename\n      }\n      earningsInCents\n      suppliedDiff {\n        text\n        indicator\n        __typename\n      }\n      suppliedKwh\n      usageType\n      pricePeriods {\n        ...UsagePeriodFields\n        __typename\n      }\n      __typename\n    }\n    general {\n      costDiff {\n        text\n        indicator\n        __typename\n      }\n      costInCents\n      renewableGridComparison {\n        text\n        indicator\n        __typename\n      }\n      renewablePercentage\n      usageDiff {\n        text\n        indicator\n        __typename\n      }\n      usageKwh\n      usageType\n      averagePriceDiff {\n        text\n        indicator\n        __typename\n      }\n      averagePriceInCents\n      pricePeriods {\n        ...UsagePeriodFields\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment UsagePeriodFields on MarketPeriod {\n  end\n  kwhPriceInCents\n  renewablePercentage\n  start\n  __typename\n}\n\nfragment UsageCompleteBillingDayFields on CompleteBillingDay {\n  marketDate\n  stackedUsage {\n    controlled\n    feedIn\n    general\n    __typename\n  }\n  usagePeriods {\n    controlled {\n      end\n      kwh\n      start\n      __typename\n    }\n    feedIn {\n      end\n      kwh\n      start\n      __typename\n    }\n    general {\n      end\n      kwh\n      start\n      __typename\n    }\n    __typename\n  }\n  usageSummaries {\n    combined {\n      costDiff {\n        text\n        indicator\n        __typename\n      }\n      costInCents\n      renewablePercentage\n      renewableGridComparison {\n        text\n        indicator\n        __typename\n      }\n      suppliedDiff {\n        text\n        indicator\n        __typename\n      }\n      suppliedKwh\n      usageDiff {\n        text\n        indicator\n        __typename\n      }\n      usageType\n      usageKwh\n      __typename\n    }\n    controlled {\n      costDiff {\n        text\n        indicator\n        __typename\n      }\n      costInCents\n      renewableGridComparison {\n        text\n        indicator\n        __typename\n      }\n      renewablePercentage\n      usageDiff {\n        text\n        indicator\n        __typename\n      }\n      usageKwh\n      usageType\n      averagePriceDiff {\n        text\n        indicator\n        __typename\n      }\n      averagePriceInCents\n      pricePeriods {\n        ...UsagePeriodFields\n        __typename\n      }\n      __typename\n    }\n    feedIn {\n      averagePriceDiff {\n        text\n        indicator\n        __typename\n      }\n      averagePriceInCents\n      carbonDisplaced\n      carbonDisplacedDiff {\n        text\n        indicator\n        __typename\n      }\n      earningsDiff {\n        text\n        indicator\n        __typename\n      }\n      earningsInCents\n      suppliedDiff {\n        text\n        indicator\n        __typename\n      }\n      suppliedKwh\n      usageType\n      pricePeriods {\n        ...UsagePeriodFields\n        __typename\n      }\n      __typename\n    }\n    general {\n      costDiff {\n        text\n        indicator\n        __typename\n      }\n      costInCents\n      renewableGridComparison {\n        text\n        indicator\n        __typename\n      }\n      renewablePercentage\n      usageDiff {\n        text\n        indicator\n        __typename\n      }\n      usageKwh\n      usageType\n      averagePriceDiff {\n        text\n        indicator\n        __typename\n      }\n      averagePriceInCents\n      pricePeriods {\n        ...UsagePeriodFields\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment periodFields on MarketPeriod {\n  start\n  kwhPriceInCents\n  kwhPriceRange {\n    minInCents\n    maxInCents\n    __typename\n  }\n  renewablePercentage\n  indicator\n  __typename\n}\n"}

	def __init__(self, username=None, password=None, maxAge=None):
		if maxAge:
			self.maxAge = maxAge
		else:
			self.maxAge = 300
		if username:
			self.username = username
		if password:
			self.password = password
		if username and password:
			self.__client = boto3.client('cognito-idp', region_name=self.__region)
			self.__aws = AWSSRP(username=self.username, password=self.password, pool_id=self.__poolID, client_id=self.__clientID, client=self.__client)
			self.auth()
			self.update()
	
	#Wrapper to check if the local data is older than the maxAge allowed. If too old it will be updated.
	def checkLocalAge(func):
		def wrapper(self):
			if (self.updateTime + self.maxAge) < time.time():
				self.update()
			return func(self)
		return wrapper
	
	def auth(self):
		self.tokens = self.__aws.authenticate_user()
		self.expiryTime = (time.time() + (self.tokens["AuthenticationResult"]["ExpiresIn"] - 300))
		
	def update(self):
		if time.time() > self.expiryTime:
			self.auth()
		self._jsondata = (requests.post(self._URL, headers={'Authorization': ('Bearer ' + self.tokens["AuthenticationResult"]["IdToken"])}, json=self.__payload)).json()
		self.updateTime = time.time()
		
	@property
	@checkLocalAge
	def json(self):
		return self._jsondata
		
	@property
	@checkLocalAge
	def currentPrice(self):
		values = []
		for meter in self._jsondata["data"]["sitePricing"]["meterWindows"]:
			values.append(meter["currentPeriod"]["kwhPriceInCents"])
		return values
	
	@property
	@checkLocalAge
	def currentRenewable(self):
		values = []
		for meter in self._jsondata["data"]["sitePricing"]["meterWindows"]:
			values.append(meter["currentPeriod"]["renewablePercentage"])
		return values
	
	@property
	@checkLocalAge
	def currentValue(self):
		values = []
		for meter in self._jsondata["data"]["sitePricing"]["meterWindows"]:
			values.append(meter["currentPeriod"]["indicator"])
		return values
	
	@property
	@checkLocalAge
	def periodCost(self):
		return self._jsondata["data"]["snapshots"]["periodSummary"]["costInCents"]
	
	@property
	@checkLocalAge
	def periodUsage(self):
		return self._jsondata["data"]["snapshots"]["periodSummary"]["usageKwh"]
		
	@property
	@checkLocalAge
	def periodRenewable(self):
		return self._jsondata["data"]["snapshots"]["periodSummary"]["renewablePercentage"]
