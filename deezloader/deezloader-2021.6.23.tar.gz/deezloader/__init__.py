#!/usr/bin/python3

from tqdm import tqdm
from .__dee_api__ import API
from .__easy_spoty__ import Spo
from .__deegw_api__ import API_GW
from .__taggers__ import write_tags
from .__deezer_settings__ import qualities
from .__download_utils__ import genurl, decryptfile

from .exceptions import (
	InvalidLink, QualityNotFound,
	TrackNotFound, NoDataApi, AlbumNotFound
)

from .__others_settings__ import (
	answers, stock_output,
	stock_quality, stock_recursive_quality,
	stock_recursive_download, stock_not_interface,
	stock_zip, method_save
)

from .__utils__ import (
	get_ids, set_path, isfile,
	check_md5_song, trasform_sync_lyric,
	create_zip, link_is_valid,
	what_kind, convert_to_date
)

class Login:
	def __init__(self, arl):
		self.__api = API()
		self.__gw_api = API_GW(arl)
		self.__gw_api.am_I_log()
		self.__spo = Spo()
		self.__qualities = qualities

	def __download(
		self, details,
		recursive_quality,
		recursive_download,
		not_interface,
		method_save,
		zips = False
	):
		quality = details['quality']

		if not quality in self.__qualities:
			raise QualityNotFound(quality)

		link = details['link']
		ids = details['ids']
		datas = details['datas']
		output = details['output']

		def __check_quality_song(infos, datas):
			qual = self.__qualities[quality]
			num_quality = qual['n_quality']
			file_format = qual['f_format']
			song_quality = qual['s_quality']
			name = set_path(datas, output, song_quality, file_format, method_save)

			if isfile(name):
				if recursive_download:
					return name, song_quality

				ans = input("Track %s already exists, do you want to redownload it?(y or n):" % name)

				if not ans in answers:
					return name, song_quality

			ids = infos['SNG_ID']
			song_md5, version = check_md5_song(infos)
			song_hash = genurl(song_md5, num_quality, ids, version)

			if len(song_md5) == 0:
				raise TrackNotFound

			try:
				crypted_audio = self.__gw_api.song_exist(song_md5[0], song_hash)
			except TrackNotFound:
				if not recursive_quality:
					song = datas['music']
					artist = datas['artist']
					not_found_str = "{} - {}".format(song, artist)
					msg = "The {} can't be downloaded in {} quality :(".format(not_found_str, quality)
					raise QualityNotFound(msg = msg)

				for qualityy in self.__qualities:
					if details['quality'] == qualityy:
						continue

					qual = self.__qualities[qualityy]
					num_quality = qual['n_quality']
					file_format = qual['f_format']
					song_quality = qual['s_quality']
					song_hash = genurl(song_md5, num_quality, ids, infos['MEDIA_VERSION'])

					try:
						crypted_audio = self.__gw_api.song_exist(song_md5[0], song_hash)
					except TrackNotFound:
						raise TrackNotFound("Error with this song", link)

			c_crypted_audio = crypted_audio.iter_content(2048)
			decryptfile(c_crypted_audio, ids, name)
			__add_more_tags(datas, infos, ids)
			write_tags(name, datas, file_format)
			return name, song_quality

		def __add_more_tags(datas, infos, ids):
			contributors = infos['SNG_CONTRIBUTORS']

			if "author" in contributors:
				datas['author'] = " & ".join(
					contributors['author']
				)
			else:
				datas['author'] = ""

			if "composer" in contributors:
				datas['composer'] = " & ".join(
					contributors['composer']
				)
			else:
				datas['composer'] = ""

			if "lyricist" in contributors:
				datas['lyricist'] = " & ".join(
					contributors['lyricist']
				)
			else:
				datas['lyricist'] = ""

			if "composerlyricist" in contributors:
				datas['composer'] = " & ".join(
					contributors['composerlyricist']
				)
			else:
				datas['composerlyricist'] = ""

			if "version" in infos:
				datas['version'] = infos['VERSION']
			else:
				datas['version'] = ""

			datas['lyric'] = ""
			datas['copyright'] = ""
			datas['lyricist'] = ""
			datas['lyric_sync'] = []

			if infos['LYRICS_ID'] != 0:
				need = self.__gw_api.get_lyric(ids)

				if "LYRICS_SYNC_JSON" in need:
					datas['lyric_sync'] = trasform_sync_lyric(
						need['LYRICS_SYNC_JSON']
					)

				datas['lyric'] = need['LYRICS_TEXT']
				datas['copyright'] = need['LYRICS_COPYRIGHTS']
				datas['lyricist'] = need['LYRICS_WRITERS']

		def __tracking2(infos, datas):
			pic = infos['ALB_PICTURE']
			image = self.__api.choose_img(pic)
			datas['image'] = image
			song = "{} - {}".format(datas['music'], datas['artist'])

			if not not_interface:
				print("Downloading: %s" % song)

			try:
				nams, song_quality = __check_quality_song(infos, datas)
			except TrackNotFound:
				ids = self.__api.not_found(song, datas['music'])
				infos = self.__gw_api.get_song_data(ids)
				nams, song_quality = __check_quality_song(infos, datas)

			return nams, song_quality

		if "track" in link:
			infos = self.__gw_api.get_song_data(ids)
			nams, song_quality = __tracking2(infos, datas)
			return nams

		zip_name = None

		if "album" in link:
			nams = []
			detas = {}
			infos = self.__gw_api.get_album_data(ids)['data']

			image = self.__api.choose_img(
				infos[0]['ALB_PICTURE']
			)

			detas['image'] = image

			for key, item in datas.items():
				if type(item) is not list:
					detas[key] = datas[key]

			t = tqdm(
				range(
					len(infos)
				),
				desc = detas['album'],
				disable = not_interface
			)

			for a in t:
				for key, item in datas.items():
					if type(item) is list:
						detas[key] = datas[key][a]

				song = "{} - {}".format(detas['music'], detas['artist'])
				t.set_description_str(song)

				try:
					media, song_quality = __check_quality_song(infos[a], detas)
					nams.append(media)
				except TrackNotFound:
					try:
						ids = self.__api.not_found(song, detas['music'])
						song_info = self.__gw_api.get_song_data(ids)
						media, song_quality = __check_quality_song(song_info, detas)
						nams.append(media)
					except TrackNotFound:
						nams.append(song)
						print("Track not found: %s :(" % song)
						continue

			if zips:
				zip_name = create_zip(
					nams,
					output = output,
					datas = datas,
					song_quality = song_quality,
					method = method_save
				)

		elif "playlist" in link:
			infos = self.__gw_api.get_playlist_data(ids)['data']
			nams = []

			for a in range(
				len(infos)
			):
				datass = datas[a]

				if type(datass) is not dict:
					not_found_str = "Track not found %s :(" % datass
					print(not_found_str)
					continue

				try:
					track, song_quality = __tracking2(infos[a], datass)
				except TrackNotFound:
					continue

				nams.append(track)

			if zips:
				zip_name = (
					"%s/playlist %s.zip"
					% (
						output,
						ids
					)
				)

				create_zip(nams, zip_name = zip_name)

		return nams, zip_name

	def download_trackdee(
		self, URL,
		output = stock_output,
		quality = stock_quality,
		recursive_quality = stock_recursive_quality,
		recursive_download = stock_recursive_download,
		not_interface = stock_not_interface,
		method_save = method_save
	):
		link_is_valid(URL)
		ids = get_ids(URL)
		datas = self.__api.tracking(ids)

		details = {
			"link": URL,
			"datas": datas,
			"quality": quality,
			"output": output,
			"ids": ids
		}

		name = self.__download(
			details,
			recursive_quality,
			recursive_download,
			not_interface, method_save
		)

		return name

	def download_albumdee(
		self, URL,
		output = stock_output,
		quality = stock_quality,
		recursive_quality = stock_recursive_quality,
		recursive_download = stock_recursive_download,
		not_interface = stock_not_interface,
		zips = stock_zip,
		method_save = method_save
	):
		link_is_valid(URL)
		ids = get_ids(URL)

		try:
			album_json = self.__api.get_album(ids)
		except NoDataApi:
			raise AlbumNotFound(URL)

		datas = {
			"music": [],
			"artist": [],
			"tracknum": [],
			"discnum": [],
			"bpm": [],
			"duration": [],
			"isrc": [],
			"gain": [],
			"album": album_json['title'],
			"label": album_json['label'],
			"year": convert_to_date(album_json['release_date']),
			"upc": album_json['upc'],
			"nb_tracks": str(album_json['nb_tracks'])
		}

		genres = []

		if "genres" in album_json:
			for a in album_json['genres']['data']:
				genres.append(a['name'])

		datas['genre'] = " & ".join(genres)
		ar_album = []

		for a in album_json['contributors']:
			if a['role'] == "Main":
				ar_album.append(a['name'])

		datas['ar_album'] = " & ".join(ar_album)

		for track in album_json['tracks']['data']:
			c_ids = track['id']
			detas = self.__api.tracking(c_ids, True)

			for key, item in datas.items():
				if type(item) is list:
					datas[key].append(detas[key])

		details = {
			"link": URL,
			"datas": datas,
			"quality": quality,
			"output": output,
			"ids": ids
		}

		names, zip_name = self.__download(
			details,
			recursive_quality,
			recursive_download,
			not_interface, method_save, zips
		)

		if zips:
			return names, zip_name

		return names

	def download_playlistdee(
		self, URL,
		output = stock_output,
		quality = stock_quality,
		recursive_quality = stock_recursive_quality,
		recursive_download = stock_recursive_download,
		not_interface = stock_not_interface,
		zips = stock_zip,
		method_save = method_save
	):
		link_is_valid(URL)
		datas = []
		ids = get_ids(URL)
		playlist_json = self.__api.get_playlist(ids)['tracks']['data']

		for track in playlist_json:
			c_ids = track['id']

			try:
				detas = self.__api.tracking(c_ids)
				datas.append(detas)
			except NoDataApi:
				song = track['title']
				artist = track['artist']['name']
				not_found_str = "{} - {}".format(song, artist)
				datas.append(not_found_str)

		details = {
			"link": URL,
			"datas": datas,
			"quality": quality,
			"output": output,
			"ids": ids
		}

		names, zip_name = self.__download(
			details,
			recursive_quality,
			recursive_download,
			not_interface, method_save, zips
		)

		if zips:
			return names, zip_name

		return names

	def download_artisttopdee(
		self, URL,
		output = stock_output,
		quality = stock_quality,
		recursive_quality = stock_recursive_quality,
		recursive_download = stock_recursive_download,
		not_interface = stock_not_interface
	):
		link_is_valid(URL)
		ids = get_ids(URL)
		playlist_json = self.__api.get_artist_top_tracks(ids)['data']

		names = [
			self.download_trackdee(
				track['link'], output,
				quality, recursive_quality,
				recursive_download, not_interface
			)

			for track in playlist_json
		]

		return names

	def download_trackspo(
		self, URL,
		output = stock_output,
		quality = stock_quality,
		recursive_quality = stock_recursive_quality,
		recursive_download = stock_recursive_download,
		not_interface = stock_not_interface,
		method_save = method_save
	):
		link_is_valid(URL)
		url = self.__spo.track(URL)
		isrc = "isrc:%s" % url['external_ids']['isrc']
		url = self.__api.get_track(isrc)

		name = self.download_trackdee(
			url['link'], output,
			quality, recursive_quality,
			recursive_download, not_interface, method_save
		)

		return name

	def download_albumspo(
		self, URL,
		output = stock_output,
		quality = stock_quality,
		recursive_quality = stock_recursive_quality,
		recursive_download = stock_recursive_download,
		not_interface = stock_not_interface,
		zips = stock_zip,
		method_save = method_save
	):
		link_is_valid(URL)
		tracks = self.__spo.album_tracks(URL)

		try:
			upc = "0%s" % tracks['external_ids']['upc']

			while upc[0] == "0":
				upc = upc[1:]

				try:
					upc = "upc:%s" % upc
					url = self.__api.get_album(upc)

					names = self.download_albumdee(
						url['link'], output,
						quality, recursive_quality,
						recursive_download, not_interface,
						zips, method_save
					)

					break
				except NoDataApi:
					if upc[0] != "0":
						raise AlbumNotFound
		except AlbumNotFound:
			tot = tracks['total_tracks']
			tot2 = None

			for track in tracks['tracks']['items']:
				track_info = self.__spo.track(
					track['external_urls']['spotify']
				)

				isrc = track_info['external_ids']['isrc']

				try:
					isrc = "isrc:%s" % isrc
					track_data = self.__api.get_track(isrc)
					album_ids = track_data['album']['id']
					tracks = self.__api.get_album(album_ids)
					tot2 = tracks['nb_tracks']

					if tot == tot2:
						break
				except NoDataApi:
					pass

			if tot != tot2:
				raise AlbumNotFound(URL)

			names = self.download_albumdee(
				tracks['link'], output,
				quality, recursive_quality,
				recursive_download, not_interface,
				zips, method_save
			)

		return names

	def download_playlistspo(
		self, URL,
		output = stock_output,
		quality = stock_quality,
		recursive_quality = stock_recursive_quality,
		recursive_download = stock_recursive_download,
		not_interface = stock_not_interface,
		zips = stock_zip,
		method_save = method_save
	):
		link_is_valid(URL)
		array = []
		tracks = self.__spo.playlist_tracks(URL)

		for track in tracks['items']:
			url = track['track']['external_urls']['spotify']

			try:
				array.append(
					self.download_trackspo(
						url, output,
						quality, recursive_quality,
						recursive_download, not_interface, method_save
					)
				)
			except (TrackNotFound, NoDataApi):
				info = track['track']
				artist = info['artists'][0]['name']
				song = info['name']
				not_found_str = "{} - {}".format(song, artist)
				array.append(not_found_str)

		if zips:
			zip_name = "{}playlist {}.zip".format(output, URL[-1])			
			create_zip(array, zip_name = zip_name)
			return array, zip_name

		return array

	def download_name(
		self, artist, song,
		output = stock_output,
		quality = stock_quality,
		recursive_quality = stock_recursive_quality,
		recursive_download = stock_recursive_download,
		not_interface = stock_not_interface,
		method_save = method_save
	):
		query = "track:{} artist:{}".format(song, artist)
		search = self.__spo.search(query)
		items = search['tracks']['items']

		if len(items) == 0:
			raise TrackNotFound(message = "No result for %s :(" % query)

		spoty_url = items[0]['external_urls']['spotify']

		return self.download_trackspo(
			spoty_url,
			output, quality, recursive_quality,
			recursive_download, not_interface, method_save
		)

	def download_smart(
		self, URL,
		output = stock_output,
		quality = stock_quality,
		recursive_quality = stock_recursive_quality,
		recursive_download = stock_recursive_download,
		not_interface = stock_not_interface,
		zips = stock_zip,
		method_save = method_save
	):
		link_is_valid(URL)
		link = what_kind(URL)

		if "track/" in link:
			if "spotify.com" in link:
				func = self.download_trackspo
				source = "https://spotify.com"
			elif "deezer.com" in link:
				func = self.download_trackdee
				source = "https://deezer.com"
			else:
				raise InvalidLink(link)

			name = func(
				link, output, quality,
				recursive_quality, recursive_download,
				not_interface, method_save
			)

			json = {
				"type": "track",
				"link_source": source,
				"track_path": name
			}

		elif "album/" in link:
			if "spotify.com" in link:
				func = self.download_albumspo
				source = "https://spotify.com"
			elif "deezer.com" in link:
				func = self.download_albumdee
				source = "https://deezer.com"
			else:
				raise InvalidLink(link)

			names = func(
				link, output, quality,
				recursive_quality,
				recursive_download, not_interface,
				zips, method_save
			)

			zip_name = None

			if zips:
				names, zip_name = names

			json = {
				"type": "track",
				"link_source": source,
				"tracks_path": names,
				"zip_name": zip_name
			}

		elif "playlist/" in link:
			if "spotify.com" in link:
				func = self.download_playlistspo
				source = "https://spotify.com"
			elif "deezer.com" in link:
				func = self.download_playlistdee
				source = "https://deezer.com"
			else:
				raise InvalidLink(link)

			names = func(
				link, output, quality,
				recursive_quality,
				recursive_download, not_interface,
				zips, method_save
			)

			zip_name = None

			if zips:
				names, zip_name = names

			json = {
				"type": "playlist",
				"link_source": source,
				"tracks_path": names,
				"zip_name": zip_name
			}

		return json