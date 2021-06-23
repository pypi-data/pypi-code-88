#!/usr/bin/python3

from requests import Session
from .__utils__ import request
from .exceptions import BadCredentials, TrackNotFound

class API_GW:
	def __init__(self, arl):
		self.__arl = arl
		self.__token = "null"
		self.__req = Session()
		self.__req.cookies['arl'] = arl
		self.__get_lyric = "song.getLyrics"
		self.__get_song_data = "song.getData"
		self.__get_user_data = "deezer.getUserData"
		self.__get_album_data = "song.getListByAlbum"
		self.__get_playlist_data = "playlist.getSongs"
		self.__private_api_link = "https://www.deezer.com/ajax/gw-light.php"
		self.__song_server = "https://e-cdns-proxy-{}.dzcdn.net/mobile/1/{}"
		self.__refresh_token()

	def __get_api(self, method, json_data = None):
		params = {
			"api_version": "1.0",
			"api_token": self.__token,
			"input": "3",
			"method": method
		}

		results = self.__req.post(
			self.__private_api_link,
			params = params,
			json = json_data
		).json()['results']

		if not results:
			self.__refresh_token()
			self.__get_api(method, json_data)

		return results

	def get_user(self):
		data = self.__get_api(self.__get_user_data)
		return data

	def __refresh_token(self):
		data = self.get_user()
		self.__token = data['checkForm']

	def am_I_log(self):
		data = self.get_user()
		user_id = data['USER']['USER_ID']

		if user_id == 0:
			raise BadCredentials(self.__arl)

	def get_song_data(self, ids):
		json_data = {
			"sng_id" : ids
		}

		infos = self.__get_api(self.__get_song_data, json_data)
		return infos

	def get_album_data(self, ids):
		json_data = {
			"alb_id": ids,
			"nb": -1
		}

		infos = self.__get_api(self.__get_album_data, json_data)
		return infos

	def get_lyric(self, ids):
		json_data = {
			"sng_id": ids
		}

		infos = self.__get_api(self.__get_lyric, json_data)
		return infos

	def get_playlist_data(self, ids):
		json_data = {
			"playlist_id": ids,
			"nb": -1
		}

		infos = self.__get_api(self.__get_playlist_data, json_data)
		return infos

	def song_exist(self, n, song_hash):
		crypted_audio = request(
			self.__song_server.format(n, song_hash)
		)

		if len(crypted_audio.content) == 0:
			raise TrackNotFound

		return crypted_audio