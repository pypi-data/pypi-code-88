# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, division, absolute_import

import json
import time
import pkg_resources

import six
from six.moves.urllib.parse import urlencode
import requests
from mypackage1.response import mypackage1Response

from mypackage1.settings import DEFAULT_BASE_URL_FOR_TEXT

class Endpoint(object):
	
	def __init__(self,accountId,apikey,emailId, base_url=DEFAULT_BASE_URL_FOR_TEXT):

		self.accountId = accountId
		self.apikey = apikey
		self.emailId = emailId
		self.base_url = base_url
	
	
	
class Classifications(Endpoint):
	def sentiment(self, data):


		response=mypackage1Response()
		
		raw_responses = requests.get(self.base_url,verify=False)

		response.add_raw_response(raw_responses)

		return response

	
		raw_responses = requests.get(url, data,verify=False)
		
		response.add_raw_response(raw_responses)

		return response

	