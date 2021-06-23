#!/usr/bin/python3

from spotipy import Spotify
from .exceptions import InvalidLink
from spotipy.exceptions import SpotifyException
from spotipy.cache_handler import CacheFileHandler
from spotipy.oauth2 import SpotifyClientCredentials

from .__others_settings__ import (
	spotify_client_id, spotify_client_secret
)

class Spo:
	def __generate_token(self):
		return SpotifyClientCredentials(
			client_id = spotify_client_id,
			client_secret = spotify_client_secret,
			cache_handler = CacheFileHandler(".cache_spoty_token"),
		)

	def __init__(self):
		self.__error_codes = [404, 400]

		self.__api = Spotify(
			client_credentials_manager = self.__generate_token()
		)

	def __lazy(self, results):
		albums = results['items']

		while results['next']:
			results = self.__api.next(results)
			albums.extend(results['items'])

		return results

	def track(self, URL):
		URL = URL.split("?")[0]

		try:
			url = self.__api.track(URL)
		except SpotifyException as error:
			if error.http_status in self.__error_codes:
				raise InvalidLink(URL)

		return url

	def album_tracks(self, URL):
		URL = URL.split("?")[0]

		try:
			tracks = self.__api.album(URL)
		except SpotifyException as error:
			if error.http_status in self.__error_codes:
				raise InvalidLink(URL)

		self.__lazy(tracks['tracks'])
		return tracks

	def playlist_tracks(self, URL):
		URL = (
			URL
			.split("?")[0]
			.split("/")
		)

		try:
			tracks = self.__api.user_playlist_tracks(URL[-3], URL[-1])
		except SpotifyException as error:
			if error.http_status in self.__error_codes:
				raise InvalidLink(URL)

		self.__lazy(tracks)
		return tracks

	def search(self, query):
		search = self.__api.search(query)
		return search