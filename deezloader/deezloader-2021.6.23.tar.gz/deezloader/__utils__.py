#!/usr/bin/python3

from os import makedirs
from datetime import datetime
from requests import get as req_get
from .exceptions import InvalidLink
from .__deezer_settings__ import header
from zipfile import ZipFile, ZIP_DEFLATED
from .__others_settings__ import supported_link

from os.path import (
	isfile, isdir, basename
)

def link_is_valid(link):
	if not any(
		c_link in link
		for c_link in supported_link
	):
		raise InvalidLink(link)

def get_ids(URL):
	ids = (
		URL
		.split("?utm")[0]
		.split("/")[-1]
	)

	return ids

def request(url):
	thing = req_get(url, headers = header)
	return thing

def artist_sort(array):
	if len(array) > 1:
		for a in array:
			for b in array:
				if a in b and a != b:
					array.remove(b)

	array = list(
		dict.fromkeys(array)
	)

	artists = " & ".join(array)
	return artists

def __check_dir(directory):
	if not isdir(directory):
		makedirs(directory)

def check_md5_song(infos):
	if "FALLBACK" in infos:
		song_md5 = infos['FALLBACK']['MD5_ORIGIN']
		version = infos['FALLBACK']['MEDIA_VERSION']
	else:
		song_md5 = infos['MD5_ORIGIN']
		version = infos['MEDIA_VERSION']

	return song_md5, version

def __var_excape(string):
	string = (
		string
		.replace("\\", "")
		.replace("/", "")
		.replace(":", "")
		.replace("*", "")
		.replace("?", "")
		.replace("\"", "")
		.replace("<", "")
		.replace(">", "")
		.replace("|", "")
		.replace("&", "")
	)

	return string

def convert_to_date(date):
	date = datetime.strptime(date, "%Y-%m-%d")
	return date

def what_kind(link):
	url = request(link).url
	return url

def __get_dir(datas, output, method):
	album = __var_excape(datas['album'])

	if method == 0:
		directory = (
			"%s %s/"
			% (
				album,
				datas['upc']
			)
		)

	elif method == 1:
		artist = __var_excape(datas['ar_album'])

		directory = (
			"%s - %s/"
			% (
				album,
				artist
			)
		)

	elif method == 2:
		upc = datas['upc']
		artist = __var_excape(datas['ar_album'])

		directory = (
			"%s - %s %s/"
			% (
				album,
				artist,
				upc
			)
		)

	directory = directory[:255]
	final_dir = "{}/{}".format(output, directory)
	return final_dir

def set_path(datas, output, song_quality, file_format, method):
	album = __var_excape(datas['album'])

	if method == 0:
		name = (
			"%s CD %s TRACK %s"
			% (
				album,
				datas['discnum'],
				datas['tracknum']
			)
		)

	elif method == 1:
		artist = __var_excape(datas['artist'])
		music = __var_excape(datas['music'])

		name = (
			"%s - %s"
			% (
				music,
				artist
			)
		)

	elif method == 2:
		artist = __var_excape(datas['artist'])
		music = __var_excape(datas['music'])
		isrc = datas['isrc']

		name = (
			"%s - %s %s"
			% (
				music,
				artist,
				isrc
			)
		)

	directory = __get_dir(datas, output, method)
	__check_dir(directory)
	name = "{}{}".format(directory, name[:246])
	name += " ({}){}".format(song_quality, file_format)
	return name

def create_zip(
	nams,
	output = None,
	datas = None,
	song_quality = None,
	method = 0,
	zip_name = None
):
	if not zip_name:
		album = __var_excape(datas['album'])
		directory = __get_dir(datas, output, method)

		if method == 0:
			zip_name = (
				"%s%s (%s).zip"
				% (
					directory,
					album,
					song_quality
				)
			)

		elif method == 1:
			artist = __var_excape(datas['ar_album'])

			zip_name = (
				"%s%s %s (%s).zip"
				% (
					directory,
					album,
					artist,
					song_quality
				)
			)

		elif method == 2:
			artist = __var_excape(datas['ar_album'])
			upc = datas['upc']

			zip_name = (
				"%s%s %s %s (%s).zip"
				% (
					directory,
					album,
					artist,
					upc,
					song_quality
				)
			)

	z = ZipFile(zip_name, "w", ZIP_DEFLATED)

	for path in nams:
		song = basename(path)

		if isfile(path):
			z.write(path, song)

	z.close()
	return zip_name

def trasform_sync_lyric(lyric):
	sync_array = []

	for a in lyric:
		if "milliseconds" in a:
			arr = (
				a['line'], int(a['milliseconds'])
			)

			sync_array.append(arr)

	return sync_array