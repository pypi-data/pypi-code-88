# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, division, absolute_import
from mypackage1.settings import DEFAULT_BASE_URL_FOR_TEXT
from mypackage1.base1 import Classifications


class mypackage1(object):
	def __init__(self,accountId,apikey,emailId, base_url=DEFAULT_BASE_URL_FOR_TEXT):

		self.accountId = accountId
		self.apikey = apikey
		self.emailId = emailId
		self.base_url = base_url
		


	@property
	def classifiers(self):
		if not hasattr(self, '_classifiers'):
			self._classifiers = Classifications(accountId=self.accountId,apikey=self.apikey,emailId=self.emailId,base_url=self.base_url)
			
		return self._classifiers


	