#!/usr/bin/python3

class TrackNotFound(Exception):
	def __init__(self, url = None, message = None):
		self.url = url

		if not message:
			self.message = "Track %s not found :(" % self.url
		else:
			self.message = message

		super().__init__(self.message)

class AlbumNotFound(Exception):
	def __init__(self, url = None):
		self.url = url
		self.msg = "Album %s not found :(" % self.url
		super().__init__(self.msg)

class InvalidLink(Exception):
	def __init__(self, url):
		self.url = url
		self.msg = "Invalid Link %s :(" % self.url
		super().__init__(self.msg)

class QuotaExceeded(Exception):
	def __init__(self, message = None):

		if not message:
			self.message = "TOO MUCH REQUESTS LIMIT YOURSELF !!! :)"

		super().__init__(self.message)

class QualityNotFound(Exception):
	def __init__(self, quality = None, msg = None):
		if not msg:
			self.msg = "The %s quality doesn't exist :)" % quality
			self.msg += "\nThe qualities have to be FLAC or MP3_320 or MP3_256 or MP3_128"
		else:
			self.msg = msg

		super().__init__(self.msg)

class MethodNotFound(Exception):
	def __init__(self, method):
		super().__init__(method)

class NoDataApi(Exception):
	def __init__(self, message):
		super().__init__(message)

class BadCredentials(Exception):
	def __init__(self, arl):
		self.arl = arl
		self.msg = "Wrong token: %s :(" % arl
		super().__init__(self.msg)