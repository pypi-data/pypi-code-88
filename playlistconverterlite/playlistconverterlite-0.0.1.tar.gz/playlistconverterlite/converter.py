import applemusicpy
import json
import re
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def convert(pl_id, am_key, am_kid, am_team_id, sp_username):

	# Get Apple Music playlist
	am_pl_object = get_am_playlist(am_key, am_kid, am_team_id, pl_id)

	# Get tracklist from playlist object
	am_tracklist = get_am_tracklist(am_pl_object)

	# Create spotipy object
	sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope='playlist-modify-public', username=sp_username))
	# Create playlist
	new_playlist = sp.user_playlist_create(user=sp_username, name='Converted Playlist')
	new_playlist_id = new_playlist['id']

	# Get spotify track IDs (and list of any non-matching titles) from tracklist
	sp_track_ids, non_matches = get_sp_ids(am_tracklist, sp)

	# Add songs by IDs
	sp.playlist_add_items(new_playlist_id, sp_track_ids)

	# Return link to spotify playlist
	return new_playlist['external_urls']['spotify']


def get_am_playlist(am_key, am_kid, am_team_id, pl_id):
	am = applemusicpy.AppleMusic(am_key, am_kid, am_team_id)
	pl_object = am.playlist(pl_id)
	return pl_object


def get_am_tracklist(playlist):
	"""
	Get a list of tracks from a playlist object as returned by get_am_playlist()
	"""

	tracks = []

	for track in playlist['data'][0]['relationships']['tracks']['data']:
		# get title and artist name, combine into a string
		artist = track['attributes']['artistName']
		title = track['attributes']['name']
		title_artist_string = title + ' ' + artist
		# convert to lowercase
		title_artist_string = title_artist_string.lower()
		# remove parens
		title_artist_string = re.sub(r'[(|)]', '', title_artist_string)
		# remove non-alphanumeric characters (but keep spaces)
		title_artist_string = re.sub(r'[^(a-z0-9|\s)]', '', title_artist_string)
		# remove 'feat'
		title_artist_string = re.sub('feat ', '', title_artist_string)
		# remove double spaces
		title_artist_string = re.sub(r'\s\s+', ' ', title_artist_string)
		tracks.append(title_artist_string)

	return tracks

def get_sp_ids(tracks, sp):
	"""
	Given a list of tracks, return a list of track ids by using spotipy's search endpoint
	tracks: list of title artist strings
	sp: spotipy object
	"""

	track_ids = []
	no_matches = []

	# loop through tracks
	for track in tracks:
		search_results = sp.search(track, limit=1)
		try:
			track_id = search_results['tracks']['items'][0]['id']
			track_ids.append(track_id)
		except IndexError:
			no_matches.append(track)

	return track_ids, no_matches





