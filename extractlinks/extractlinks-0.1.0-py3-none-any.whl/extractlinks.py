#!/usr/bin/python3

# last updated 2021-06-26

# python3 -m pip install urlbreakdown beautifulsoup4 lxml

import json
import requests
import uuid
from datetime import datetime
from urllib.parse import urlparse
from bs4 import BeautifulSoup as bs

class ExtractLinks:
	def __init__(self, content=None, pguid=""):
		"""expects a requests object (content), and optionally a parent guid (pguid); initialize variables, generate a top_level_url used to repair relative links"""
		self.content = content
		if self.content:
			try:
				self.url = self.content.url
				self.urlp = urlparse(self.url)
				self.top_level_url = self.urlp.scheme+"://"+self.urlp.netloc # reconstruct the scheme+domain for link extraction and reconstruction if necessary
			except Exception as e:
				print(str(e))
				print("processing empty URL")
				self.top_level_url = ""
		if len(pguid) == 0:
			self.pguid = str(uuid.uuid4())
		else:
			self.pguid = pguid
		self.output = [] # will hold dictionaries of each item in the request chain
		self.links_all = [] # hold all unique "assumed" links (full and repaired relatives)
		self.types_all = [] # hold all unique tag-attribute combos found
		self.tags_all = [] # hold all unique tags found
		self.attributes_all = [] # hold all unique attributes found
		self.run() # run() calls requestUrl() then handles processing results into self.output
		self.json = json.dumps(self.output)

	def getUtcTimestampNow(self) -> str:
		"""returns a timestamp string"""
		return(str(datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3])+"Z")

	def fix_links(self, h, top_level_url) -> dict:
		"""expects a dict and the reconstructed scheme+domain to repair relative URLs; returns a dictionary"""
		# links_count is not reflective of a unique count, and includes all objects identified including non-URLs in otherwise link-related tag attributes
		if h["links_count"] > 0:
			# sort data and relative links
			for i in h["links"]:
				if not i.startswith("http://") and not i.startswith("https://"):
					if i.startswith("data:"):
						h["data"].append(i)
					elif i.startswith("/"):
						if i.startswith("//"):
							# just "//" without "http(s):" means let the remote server decide what protocol to serve
							h["doublewhack"].append(i)
							h["doublewhack_modified"].append("https:"+i)
						else:
							h["relative"].append(i)
					elif i.lower().startswith("android-app://") or i.lower().startswith("twitter://") or i.lower().startswith("fb://") or i.lower().startswith("youtube://"):
						# https://en.wikipedia.org/wiki/Mobile_deep_linking
						h["mobile"].append(i)
					else:
						h["other"].append(i)
			# trim links to just full URLs
			h["links"] = list(set(set(h["links"]) - set(h["relative"]) - set(h["mobile"]) - set(h["data"]) - set(h["other"]) - set(h["doublewhack"])))
			# remove empty items and dedup
			for k,v in h.items():
				if type(v) is list:
					h[k] = list(set(v))
			# attempt to repair relative paths
			if len(top_level_url) > 0:
				if len(h["relative"]) > 0:
					for i in h["relative"]:
						h["relative_modified"].append(top_level_url+i)
			# intersection detection
			intersection = list(set(h["links"]) & set(h["relative_modified"]))
			if len(intersection) > 0:
				h["relative_modified_intersection"] = intersection
			# make one giant final list of all assumed links
			h["assumed_links_all"] = list(set(h["links"] + h["relative_modified"] + h["doublewhack_modified"]))
			#
			#
			return(h)

	def extractLinks(self, tb, top_level_url) -> dict:
		"""expects a Requests text body object "tb", chainitem counter "c", pguid, and guid; returns a dict"""
		# using link_dict
		link_dict = {"a":["href"], "applet":["archive","codebase"], "area":["href"], "audio":["src"], "base":["href"], "blockquote":["cite"], "body":["background"], "button":["formaction"],"command":["icon"], "del":["cite"], "embed":["src"], "form":["action"], "frame":["longdesc", "src"], "head":["profile"], "html":["manifest"],"iframe":["longdesc", "src"], "image":["href"], "img":["longdesc", "src", "srcset", "usemap"], "input":["formaction", "src", "usemap"], "ins":["cite"],"link":["href"], "meta":["content"], "object":["archive", "classid", "codebase", "data", "usemap"], "q":["cite"], "script":["src"], "source":["src", "srcset"], "track":["src"], "video":["poster", "src"]}
		# construct the placeholder dictionary
		# links_count is not reflective of a unique count, and includes all objects identified including non-URLs in otherwise link-related tag attributes
		h = {"links_count":0, "types":[], "tags":[], "attributes":[], "links":[], "relative":[], "mobile":[], "data":[], "doublewhack":[], "doublewhack_modified":[], "other":[], "relative_modified":[]}
		soup = bs(tb, 'lxml') # pip install lxml
		try:
			for tag,attribute_list in link_dict.items(): # top-level tag items in link_dict
				tag_of_interest = soup.find_all(tag) # get every tag in the soup body
				# for every individual tag in link_dict found (a, href, img, etc)
				for current_tag in tag_of_interest:
					# for each attribute in the value list, get all of the occurrences of the current attribute
					for current_attr in attribute_list:
						# list to hold links if found
						ll = []
						ll.append(current_tag.get(current_attr))
						# clean the list
						ll = [i for i in ll if i is not None]
						if ll is not None:
							if len(ll) > 0:
								h["links_count"] += len(ll)
								h["types"].append("{}-{}".format(tag, current_attr))
								h["tags"].append(tag)
								h["attributes"].append(current_attr)
								h["links"].extend(ll)
		except Exception as e:
			pass # explicitly silence
			#print(str(e))
		if h["links_count"] > 0:
			# perform link reconstruction if relative links are found
			h = self.fix_links(h, top_level_url)
		elif h["links_count"] == 0:
			# prune results with empty lists
			remove = []
			for k,v in h.items():
				if isinstance(v, list):
					if len(v) == 0:
						remove.append(k)
			for r in remove:
				h.pop(r, None)
		return(h)

	def result(self, h, c, pguid, guid) -> dict:
		"""gets called multiple times by run(); expects a Requests history object, chainitem counter, pguid, and guid; returns a dict"""
		ll = self.extractLinks(h.text, self.top_level_url) # extract all links from the history object
		ll["@timestamp"] = self.getUtcTimestampNow()
		# add Elastic Common Schema-aligned metadata for added machine handling scenarios
		if h.url:
			ll["url"] = {}
			ll["url"]["full"] = h.url
			ll["url"]["original"] = h.url
			uuu=urlparse(h.url)
			ll["url"]["scheme"] = uuu.scheme
			ll["url"]["domain"] = uuu.netloc
			ll["url"]["path"] = uuu.path
			if len(uuu.query) > 0:
				ll["url"]["query"] = uuu.query
			if len(uuu.fragment) > 0:
				ll["url"]["fragment"] = uuu.fragment
			if uuu.username:
				ll["url"]["username"] = uuu.username
			if uuu.password:
				ll["url"]["password"] = uuu.password
		if h.status_code:
			ll["http"] = {}
			ll["http"]["response"] = {}
			ll["http"]["response"]["status_code"] = h.status_code
			if h.reason:
				ll["http"]["response"]["status_code_reason"] = h.reason
			if h.text:
				ll["http"]["response"]["body_bytes"] = len(h.text)
		ll["chainitem"] = c
		ll["pguid"] = pguid
		ll["guid"] = guid
		return(ll) # return the dict, which will then be appended to the self.output list

	def run(self):
		"""sets calls requestUrl() then sets self.output, which is a list of dictionaries"""
		chainitem = 0 # first item in the request chain
		if self.content.history: # if there are redirects, handle them and assign pguid/guid as necessary
			for h in self.content.history:
				if chainitem == 0:
					guid = self.pguid # first item gets matching pguid/guid
				else:
					guid = str(uuid.uuid4()) # subsequent items get their own guids (history tracking done by chainitem)
				e = self.result(h, chainitem, self.pguid, guid)
				self.output.append(e)
				chainitem += 1 # increment chain counter for next item to be processed
		if chainitem > 0:
			g = str(uuid.uuid4())
			ee = self.result(self.content, chainitem, self.pguid, g)
		else:
			ee = self.result(self.content, 0, self.pguid, self.pguid)
		self.output.append(ee)
		#
		#
		# make big lists for links/types/tags/attributes
		for i in self.output:
			if "assumed_links_all" in i:
				self.links_all.extend(i["assumed_links_all"])
			if "types" in i:
				self.types_all.extend(i["types"])
			if "tags" in i:
				self.tags_all.extend(i["tags"])
			if "attributes" in i:
				self.attributes_all.extend(i["attributes"])
		# clean those lists
		if len(self.links_all) > 0:
			self.links_all = list(set(self.links_all))
		if len(self.types_all) > 0:
			self.types_all = list(set(self.types_all))
		if len(self.tags_all) > 0:
			self.tags_all = list(set(self.tags_all))
		if len(self.attributes_all) > 0:
			self.attributes_all = list(set(self.attributes_all))

	def urlbreakdown_generator_dict(self):
		"""produce a dictionary for each URL, containing non-verbose URLBreakdown analysis, with the pguid applied to each object"""
		try:
			from urlbreakdown import URLBreakdown
			for i in self.links_all:
				u = URLBreakdown(i, pguid=self.pguid)
				yield(u.output)
		except ImportError:
			print("cannot find URLBreakdown, try running: pip install urlbreakdown / python3 -m pip install urlbreakdown")

	def urlbreakdown_generator_json(self):
		"""produce a JSON string for each URL, containing non-verbose URLBreakdown analysis, with the pguid applied to each object"""
		try:
			from urlbreakdown import URLBreakdown
			for i in self.links_all:
				u = URLBreakdown(i, pguid=self.pguid)
				yield(u.json)
		except ImportError:
			print("cannot find URLBreakdown, try running: pip install urlbreakdown / python3 -m pip install urlbreakdown")
