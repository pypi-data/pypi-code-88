#!/usr/bin/python3

def tracking(json_track, album = False):
	datas = {}
	datas['music'] = json_track['title']
	datas['artist'] = json_track['artist']['name']
	datas['duration'] = json_track['duration']

	if not album:
		datas['album'] = json_track['album']['title']
		datas['ar_album'] = datas['artist']

	return datas