#!/usr/bin/python3

from mutagen.flac import FLAC, Picture

from mutagen.id3 import (
	ID3NoHeaderError,
	ID3, APIC, COMM, TIT2,
	TLEN, TEXT, TALB, TPE1,
	TCOM, IPLS
)

def __write_flac(song, data):
	tag = FLAC(song)
	tag.delete()
	images = Picture()
	images.type = 3
	images.data = data['image']
	tag.clear_pictures()
	tag.add_picture(images)
	tag['artist'] = data['artist']
	tag['title'] = data['music']
	tag['album'] = data['album']
	tag['author'] = data['author']
	tag['composer'] = data['composer']
	tag['length'] = data['duration']
	tag['version'] = data['version']
	tag.save()

def __write_mp3(song, data):
	try:
		audio = ID3(song)
		audio.delete()
	except ID3NoHeaderError:
		audio = ID3()

	audio.add(
		APIC(
			mime = "image/jpeg",
			type = 3,
			desc = "album front cover",
			data = data['image']
		)
	)

	audio.add(
		COMM(
			lang = "eng",
			desc = "my comment",
			text = "DO NOT USE FOR YOUR OWN EARNING"
		)
	)

	audio.add(
		TIT2(
			text = data['music']
		)
	)

	audio.add(
		TLEN(
			text = "%s" % data['duration']
		)
	)

	audio.add(
		TEXT(
			text = data['lyricist']
		)
	)

	audio.add(
		TALB(
			text = data['album']
		)
	)

	audio.add(
		TPE1(
			text = data['artist']
		)
	)

	audio.add(
		TCOM(
			text = data['composer']
		)
	)

	audio.add(
		IPLS(
			people = [data['author']]
		)
	)

	audio.save(song)

def write_tags(song, data, f_format):
	if f_format == ".flac":
		__write_flac(song, data)
	else:
		__write_mp3(song, data)