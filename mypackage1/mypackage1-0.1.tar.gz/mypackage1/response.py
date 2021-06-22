# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, division, absolute_import

import requests
import simplejson
class mypackage1Response(object):
	def __init__(self, raw_response=None):
		if raw_response is None:
			raw_response=[]
		elif isinstance(raw_response,requests.Response):
			raw_response=[raw_response]
		self.raw_response = []
		for resp in raw_response:
			self.add_raw_response(resp)

		self.catched_content = None

	def get_request_header(self, header_name):
		try:
			last_response = self.raw_response[-1]

		except IndexError:
			return None

		return last_response.headers.get(header_name)
			
	@property
	def query_count(self):

		return len(self.raw_response)

	@property
	def content(self):
		if not self.catched_content:
			if self.query_count==1:
				if self.raw_response[0].content:
					content = self.raw_response[0].json()
				else:
					None
				
			else:
				content = [result for resp in self.raw_response for result in resp.json() if resp.content]

			self.catched_content = content

		return self.catched_content

	
	def add_raw_response(self,rawresponse):
		self.cached_content = None
		self.raw_response.append(rawresponse)


		
