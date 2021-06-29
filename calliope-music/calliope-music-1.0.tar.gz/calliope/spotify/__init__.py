# Calliope
# Copyright (C) 2017,2020  Sam Thursfield <sam@afuera.me.uk>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


"""Access data from the `Spotify music streaming service <https://www.spotify.com>`_.

This module wraps the `Spotipy <https://spotipy.readthedocs.io/>`_ library.

Authentication
--------------

You will need an API key to access Spotify. Register at the `My
Dashboard <https://developer.spotify.com/dashboard/applications>`_ page.

You will be asked to set a redirect URI. This is only used as a way to get an
access token, so you can use any site you like, but it must be in the list of
authorised redirect URIs in your Spotify application settings.

The credentials should be provided via a :class:`calliope.config.Configuration`
instance when creating the :class:`calliope.spotify.SpotifyContext`.

The first time :func:`calliope.spotify.SpotifyContext.authenticate` is called,
it will open a browser window to authorize with Spotify. It will then ask you
to paste the redirected URI::

    $ cpe spotify export
    Couldn't read cache at: /home/sam/.cache/calliope/spotify/credentials.json
    Enter the URL you were redirected to:

The authorization code will be saved in the cache so future API access will
work without a prompt, until the cached code expires.

Caching
-------

By default, all new HTTP requests are saved to disk. Cache expiry is done
following ``etags`` and ``cache-control`` headers provided by the Spotify API.
"""

import cachecontrol
import cachecontrol.caches
import requests
import spotipy
import spotipy.util

import logging
import sys

import calliope.cache
import calliope.config
import calliope.playlist

log = logging.getLogger(__name__)


class SpotifyContext():
    def __init__(self, config: calliope.config.Configuration, user: str=None,
                 caching: bool=True):
        """Context for accessing Spotify Web API.

        The :meth:`authenticate` function must be called to obtain a
        :class:`spotipy.client.Spotify` object.

        Args:
            config: Provides ``spotify.client_id``, ``spotify.client_secret`` and ``spotify.redirect_uri``
            user: Default user for requests
            caching: Enables caching to ``$XDG_CACHE_HOME/calliope/spotify``

        """
        self.config = config
        self.caching = caching

        if not user:
            user = self.config.get('spotify', 'user')
        if not user:
            raise RuntimeError("Please specify a username.")

        self.user = user
        log.debug("Spotify user: {}".format(user))

        self.api = None

    def _get_session(self):
        session = requests.Session()
        if self.caching:
            cache_path = calliope.cache.save_cache_path('calliope/spotify')
            filecache = cachecontrol.caches.FileCache(cache_path.joinpath('webcache'))
            session.mount('https://api.spotify.com/',
                          cachecontrol.CacheControlAdapter(cache=filecache))
        return session

    def authenticate(self) -> spotipy.client.Spotify:
        """Authenticate against the Spotify API.

        See above for details on how this works.

        """
        client_id = self.config.get('spotify', 'client-id')
        client_secret = self.config.get('spotify', 'client-secret')
        redirect_uri = self.config.get('spotify', 'redirect-uri')

        scope = 'user-top-read'

        try:
            cache_path = calliope.cache.save_cache_path('calliope/spotify')
            credentials_cache_path = cache_path.joinpath('credentials.json')
            auth_manager = spotipy.oauth2.SpotifyOAuth(
                username=self.user, scope=scope, client_id=client_id,
                client_secret=client_secret, redirect_uri=redirect_uri,
                cache_path=credentials_cache_path)
            self.api = spotipy.Spotify(auth_manager=auth_manager,
                                       requests_session=self._get_session())
        except spotipy.client.SpotifyException as e:
            raise RuntimeError(e) from e

        self.api.trace = False


# FIXME: should be called resolve_content
def canonicalize_spotify(sp, cache, item):
    """Find a matching Spotify track for our local track."""
    track_name = item['track']

    found, entry = cache.lookup('track:{}'.format(track_name))

    if found:
        logging.debug("Found track:{} in cache".format(track_name))
    else:
        # We canonicalize in a simple & dumb way: search for the track by name,
        # then pick the 1st result.
        log.debug("Searching for track: %s", track_name)
        result = sp.search(q=track_name, type='track')
        if result['tracks']['items']:
            entry = result['tracks']['items'][0]
        else:
            entry = None

        cache.store('track:{}'.format(track_name), entry)

    if entry is None:
        warnings = item.get('spotify.warnings', [])
        warnings += ["Unable to find track on Spotify"]
        item['spotify.warnings'] = warnings
    else:
        first_artist = entry['artists'][0]
        item['spotify.artist'] = first_artist['name']
        item['spotify.artist.id'] = first_artist['id']
        if entry['name'] != item['track']:
            item['spotify.track'] = entry['name']
        item['spotify.url'] = entry['external_urls']['spotify']
    return item


def annotate_artist(sp, cache, item):
    if 'spotify.artist' not in item:
        # We assume canonicalize_spotify() was already called and it must have
        # been unable to find the artist.
        pass
    else:
        artist_name = item['artist']
        artist_spotify_id = item['spotify.artist.id']
        found, result = cache.lookup('artist:{}'.format(artist_spotify_id))
        if found:
            log.debug("Found artist info for {} in cache".format(artist_name))
        else:
            log.debug("Didn't find artist info for {} ({}) in cache, running remote query"
                      .format(artist_name, artist_spotify_id))

            result = sp.artist(artist_spotify_id)

            cache.store('artist:{}'.format(artist_spotify_id), result)

        item['spotify.artist.popularity'] = result['popularity']
    return item


def annotate(api, playlist):
    cache = calliope.cache.open(namespace='spotify')
    for track in playlist:
        track = canonicalize_spotify(api, cache, track)
        track = annotate_artist(api, cache, track)
        yield track

def _export_spotify_playlist(playlist, tracks):
    playlist_metadata = {
        'playlist.title': playlist['name'],
    }

    playlist_info_url = playlist['external_urls'].get('spotify')
    if playlist_info_url:
        playlist_metadata['playlist.location'] = playlist_info_url

    for i, track in enumerate(tracks['items']):
        item = {
            'title': track['track']['name'],
            'creator': track['track']['artists'][0]['name'],
        }

        location = track['track']['external_urls'].get('spotify')
        if location:
            item['location'] = location

        if i == 0:
            item.update(playlist_metadata)

        yield item


def export(spotify: SpotifyContext) -> calliope.playlist.Playlist:
    """Export all playlists."""
    sp = spotify.api
    user = spotify.user

    playlists = sp.current_user_playlists()
    for playlist in playlists['items']:
        if playlist['owner']['id'] == user:
            tracks = sp.user_playlist_tracks(user, playlist_id=playlist['id'])
            calliope.playlist.write(_export_spotify_playlist(playlist, tracks), stream=sys.stdout)


def top_artists(spotify: SpotifyContext, count: int, time_range: str) -> calliope.playlist.Playlist:
    """Return top artists for the context user."""
    sp = spotify.api
    response = sp.current_user_top_artists(limit=count, time_range=time_range)['items']

    if count > 50:
        # This is true as of 2018-08-18; see:
        # https://developer.spotify.com/documentation/web-api/reference/personalization/get-users-top-artists-and-tracks/
        raise RuntimeError("Requested {} top artists, but the Spotify API will "
                           "not return more than 50.".format(count))

    output = []
    for i, artist_info in enumerate(response):
        output_item = {
            'creator': artist_info['name'],
            'spotify.artist_id': artist_info['id'],
            'spotify.creator_user_ranking': i+1,
            'spotify.creator_image': artist_info['images']
        }
        output.append(output_item)

    return output
