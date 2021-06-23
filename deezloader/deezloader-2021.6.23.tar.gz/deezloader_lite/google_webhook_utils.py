#!/usr/bin/python3

from os import getcwd
from random import choice
from deezloader_lite import Login
from configparser import ConfigParser
from deezloader.__dee_api__ import API
from deezloader.__utils__ import set_path
from deezloader_lite.__utils__ import tracking
from deezloader.exceptions import NoDataApi, TrackNotFound

settings_file = ".deez_settings.ini"
config = ConfigParser()
config.read(settings_file)

try:
	deezer_token = config['login']['token']
except KeyError:
	print("Something went wrong with configuration file")
	exit()

output = "%s/Songs/" % getcwd()
song_quality = "320"
file_format = ".mp3"
method_save = "1"
downloa = Login(deezer_token)
dee_api = API()
image_size = "1200x1200"
cover = f"https://e-cdns-images.dzcdn.net/images/cover/%s/{image_size}-000000-80-0-0.jpg"
dee_api_link = "https://api.deezer.com/"

def play(name, what):
	try:
		if what == "playlist":
			data = dee_api.search_playlist(name)['data'][:5]
			choosen_one = choice(data)['id']
			link = f"{dee_api_link}/playlist/{choosen_one}"
			data = dee_api.get_playlist(choosen_one)
			title = data['title']
			datas = []

			for a in data['tracks']['data'][:25]:
				album = a['album']
				image = cover % album['md5_image']
				detas = tracking(a)
				detas['ids'] = album['id']
				album_name = album['title']
				song = a['title']

				path = set_path(
					detas, output,
					song_quality, file_format, 1
				)

				json = {
					"image": image,
					"album_name": album_name,
					"artist": detas['artist'],
					"song": song,
					"path": path
				}

				datas.append(json)

		elif what == "artist":
			data = dee_api.search_artist(name)['data']
			name1 = None

			while name.lower() != name1:
				c = choice(data)
				choosen_one = c['id']
				name1 = c['name'].lower()

			datas = []
			link = f"{dee_api_link}/album/{choosen_one}"

			try:
				data = dee_api.get_artist_top_tracks(choosen_one)
				title = "TOP di %s" % name

				for a in data['data']:
					album = a['album']
					image = cover % album['md5_image']
					detas = tracking(a)
					detas['ids'] = album['id']
					album_name = album['title']
					song = a['title']

					path = set_path(
						detas, output,
						song_quality, file_format, 1
					)

					json = {
						"image": image,
						"album_name": album_name,
						"artist": detas['artist'],
						"song": song,
						"path": path
					}

					datas.append(json)
			except NoDataApi:
				data = dee_api.get_artist_top_albums(choosen_one)['data']
				choosen_one = choice(data)['id']
				data = dee_api.get_album(choosen_one)
				title = data['title']
				image = cover % data['md5_image']
				ids = data['id']

				for a in data['tracks']['data']:
					detas = tracking(a, True)
					detas['album'] = title
					detas['ids'] = ids
					song = a['title']

					path = set_path(
						detas, output,
						song_quality, file_format, 1
					)

					json = {
						"image": image,
						"album_name": title,
						"artist": detas['artist'],
						"song": song,
						"path": path
					}

					datas.append(json)

		elif "song" in what:
			if what == "artist-song":
				name = "{} {}".format(name['song'], name['artist'])

			data = dee_api.search_track(name)['data']
			choosen_one = data[0]['id']
			link = f"{dee_api_link}/track/{choosen_one}"
			data = dee_api.get_track(choosen_one)
			title = data['title']
			image = cover % data['md5_image']
			datas = []
			album = data['album']
			image = cover % album['md5_image']
			detas = tracking(data)
			detas['ids'] = album['id']
			album_name = album['title']
			song = data['title']

			path = set_path(
				detas, output,
				song_quality, file_format, 1
			)

			json = {
				"image": image,
				"album_name": album_name,
				"artist": detas['artist'],
				"song": song,
				"path": path
			}

			datas.append(json)

		return datas, title, link
	except (NoDataApi, TrackNotFound):
		pass

def start_download_track(URL):
	downloa.download_trackdee(URL, output, recursive_download = True)

def start_download_album(URL):
	downloa.download_albumdee(URL, output, recursive_download = True)

def start_download_artist_top(URL):
	downloa.download_artisttopdee(URL, output, recursive_download = True)

def start_download_playlist(URL):
	downloa.download_playlistdee(URL, output, recursive_download = True)

def hello_json():
	json = {
		"payload": {
			"google": {
				"expectUserResponse": True,
				"richResponse": {
					"items": [{
						"simpleResponse": {
							"textToSpeech": "<speak>Benvenuto in GoogleDeezloader. Cosa vuoi ascoltare?</speak>",
							"displayText": "Benvenuto in GoogleDeezloader. Cosa vuoi ascoltare?"
						}
					}]
				}
			}
		}
	}

	return json

def not_found_json():
	json = {
		"payload": {
			"google": {
				"expectUserResponse": True,
				"richResponse": {
					"items": [{
						"simpleResponse": {
							"textToSpeech": "<speak>Non ho trovato niente di quello che hai cercato, puoi ripetere?</speak>",
							"displayText": "Non ho trovato niente di quello che hai cercato, puoi ripetere?"
						}
					}]
				}
			}
		}
	}

	return json

def check_user(datas, chat_id):
	try:
		datas[chat_id]
	except KeyError:
		datas[chat_id] = {
			"datas": [],
			"thread": None
		}

	return datas