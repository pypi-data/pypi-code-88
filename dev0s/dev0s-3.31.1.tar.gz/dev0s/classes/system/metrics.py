#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# imports.
from dev0s.classes.defaults.files import *
from dev0s.classes.response import response as _response_
from dev0s.classes import code
from dev0s.classes.defaults.defaults import defaults

# the metrics object class.
class Metrics(object):
	def __init__(self):

		# docs.
		DOCS = {
			"module":"dev0s.system.metrics", 
			"initialized":True,
			"description":[], 
			"chapter": "Metrics", }

		#

	# get ram metrics.
	def ram(self):

		# vars.
		info = {}

		# get memory & swap.
		response = code.execute("""free -m | awk '{print $2"|"$3"|"$4}' """)
		if not response: return response
		output = response.output.split("\n")[1:]
		for index, type in [
			[0, "memory"],
			[0, "swap"],
		]:
			total, used, free = output[index].split("|")
			info[type] = {
				"free":round( (float(free) / float(total)) * 100, 2),
				"used":round( (float(used) / float(total)) * 100, 2),
				"total":f"{total} MB",
			}

		# handler.
		return _response_.success("Successfully retrieved the ram metrics.", {
			"info":info,
		})

	#





		
