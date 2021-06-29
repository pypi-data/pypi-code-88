# Calliope
# Copyright (C) 2018-2020  Sam Thursfield <sam@afuera.me.uk>
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

'''Calliope command line interface.

This module provides the public command line interface for Calliope.

'''

import click
import parsedatetime

import datetime
import logging
import os
import sys
import time

import calliope   # pylint: disable=cyclic-import


# The CLI is defined using the Click module. Every command is declared
# in this module.
#
# CLI documentation is auto-generated from this module using 'sphinx-click'.
# There is a special flag that can be set to stub out the actual code, which
# exists so that this module can be imported by `sphinx-build` without pulling
# in the rest of Calliope and the many external dependencies that it requires.
# This makes it simple to build and host our documentation on readthedocs.org.


class App:
    def __init__(self, debug=False):
        self.debug = debug
        self.config = None


def string_to_datetime(cal, string):
    dt, success = cal.parse(string)
    if success:
        return datetime.datetime.fromtimestamp(time.mktime(dt))
    else:
        return None


@click.group()
@click.option('-d', '--debug', is_flag=True)
@click.pass_context
def cli(context, **kwargs):
    '''Calliope is a set of tools for processing playlists.'''

    context.obj = App(**kwargs)

    context.obj.config = calliope.config.Configuration()

    if context.obj.debug:
        formatter = logging.Formatter(fmt='%(name)s %(message)s')
        handler = logging.StreamHandler(stream=sys.stderr)
        handler.setFormatter(formatter)
        log = logging.getLogger()
        log.addHandler(handler)
        log.setLevel(logging.DEBUG)


@cli.group(name='bandcamp', help="Query Bandcamp")
@click.option('--user', help="show data for the given Bandcamp user")
@click.pass_context
def bandcamp_cli(context, user):
    context.obj.bandcamp = calliope.bandcamp.BandcampContext(
        context.obj.config, user=user)


@bandcamp_cli.command(name='collection')
@click.pass_context
def cmd_bandcamp_collection(context):
    '''Show all albums in the collection of the given Bandcamp user.'''
    calliope.playlist.write(calliope.bandcamp.collection(context.obj.bandcamp),
                            sys.stdout)


@cli.group(name='beets', help="Query the Beets media database")
@click.pass_context
def beets_cli(context):
    pass


@beets_cli.command(name='albums')
@click.option('--include-tracks', is_flag=True, default=False,
              help="List tracks for each album.")
@click.argument('query', type=str, default='album+')
@click.pass_context
def cmd_beets_albums(context, include_tracks, query):
    '''Show all albums available locally..'''
    calliope.playlist.write(
        calliope.beets.albums(query, include_tracks=include_tracks),
        sys.stdout)


@beets_cli.command(name='artists')
@click.argument('query', type=str, default='artist+')
@click.pass_context
def cmd_beets_artists(context, query):
    '''Show artists stored in Beets database.'''
    calliope.playlist.write(calliope.beets.artists(query), sys.stdout)


@beets_cli.command(name='tracks')
@click.argument('query', type=str, default='artist+ title+')
@click.pass_context
def cmd_beets_tracks(context, query):
    '''Show tracks stored in Beets database.'''
    calliope.playlist.write(calliope.beets.tracks(query), sys.stdout)


#@beets_cli.command(name='resolve-content')
#@click.argument('playlist', type=click.File(mode='r'))
#@click.pass_context
#def cmd_beets_resolve_content(context, playlist):
#    '''Resolve the 'location' field using Beets, if possible.'''
#    output = calliope.beets.resolve_content(calliope.playlist.read(playlist))
#    calliope.playlist.write(output, sys.stdout)



@cli.command(name='diff', help="Compare multiple collections")
@click.option('--scope', 'scope',
              type=click.Choice(['creator', 'album', 'song', 'track']),
              default='track')
@click.argument('playlist1', type=click.File(mode='r'))
@click.argument('playlist2', type=click.File(mode='r'))
@click.pass_context
def cmd_diff(context, scope, playlist1, playlist2):
    equal_function = {
        'creator': calliope.diff.creator_equal,
        'album': calliope.diff.album_equal,
        'song': calliope.diff.song_equal,
        'track': calliope.diff.track_equal,
    }[scope]

    result = calliope.diff.diff(calliope.playlist.read(playlist1),
                                calliope.playlist.read(playlist2),
                                equal_function=equal_function)
    calliope.playlist.write(result, sys.stdout)


EXPORT_FORMATS = ['cue', 'm3u', 'jspf', 'xspf']

@cli.command(name='export')
@click.option('-f', '--format', 'format_', type=click.Choice(EXPORT_FORMATS),
              default='xspf')
@click.option('-t', '--title', type=str,
              help="Set title of playlist")
@click.argument('playlist', nargs=1, type=click.File('r'))
@click.pass_context
def cmd_export(context, format_, title, playlist):
    '''Convert to a different playlist format'''

    format_id = calliope.export.get_format_id(format_)
    result = calliope.export.export_single_playlist(
        calliope.playlist.read(playlist),
        format_id, title=title)
    sys.stdout.write(result)


@cli.command(name='export-split')
@click.option('-f', '--format', 'format_', type=click.Choice(EXPORT_FORMATS),
              default='xspf')
@click.argument('stream', nargs=1, type=click.File('r'))
@click.argument('output_path', nargs=1,
                type=click.Path(file_okay=False, dir_okay=True))
@click.pass_context
def cmd_export_split(context, format_, stream, output_path):
    '''Export multiple playlists from a stream based on `playlist.title`.'''

    format_id = calliope.export.get_format_id(format_)
    calliope.export.export_many_playlists(
        calliope.playlist.split(calliope.playlist.read(stream)),
        format_id, output_path)


@cli.command(name='import')
@click.argument('playlist', nargs=1, type=click.File('r'))
@click.pass_context
def cmd_import(context, playlist):
    """Import playlists from other formats

    Supported formats:

        * pls: Common INI-based playlist format
        * xspf: The XML Shareable Playlist Format
        * jspf: JSON variant of xspf

    """

    text = playlist.read()
    try:
        playlist = calliope.import_.import_(text)
        calliope.playlist.write(playlist, sys.stdout)
    except RuntimeError as e:
        raise RuntimeError(f"{playlist.name}: {e.args[0]}") from e


@cli.group(name='lastfm', help="Interface to the Last.fm music database")
@click.option('--user', metavar='NAME',
              help="show data for the given Last.fm user")
@click.pass_context
def lastfm_cli(context, user):
    context.obj.lastfm = calliope.lastfm.LastfmContext(config=context.obj.config, user=user)


@lastfm_cli.command(name='annotate-tags')
@click.argument('playlist', type=click.File(mode='r'))
@click.pass_context
def lastfm_annotate_tags(context, playlist):
    '''Annotate playlist with tags from Last.fm'''

    context.obj.lastfm.authenticate()
    result_generator = calliope.lastfm.annotate_tags(
        context.obj.lastfm, calliope.playlist.read(playlist))
    calliope.playlist.write(result_generator, sys.stdout)


@lastfm_cli.command(name='similar-artists')
@click.pass_context
@click.option('-c', '--count', type=int, default=20,
              help="Maximum number of artists to return")
@click.argument('ARTIST')
def cmd_lastfm_similar_artists(context, count, artist):
    '''Return similar artists for a given artist name.'''

    output = calliope.lastfm.similar_artists(context.obj.lastfm, count,
                                             artist)
    calliope.playlist.write(output, sys.stdout)


@lastfm_cli.command(name='similar-tracks')
@click.pass_context
@click.option('-c', '--count', type=int, default=20,
              help="Maximum number of tracks to return")
@click.argument('ARTIST')
@click.argument('TRACK')
def cmd_lastfm_similar_tracks(context, count, artist, track):
    '''Return similar tracks for a given track.'''

    output = calliope.lastfm.similar_tracks(context.obj.lastfm, count,
                                            artist, track)
    calliope.playlist.write(output, sys.stdout)


@lastfm_cli.command(name='top-artists')
@click.pass_context
@click.option('-c', '--count', type=int, default=20,
              help="Maximum number of artists to return")
@click.option('--time-range', default='overall',
              type=click.Choice(['overall', '7day', '1month', '3month',
                                 '6month', '12month']))
@click.option('--include', '-i', type=click.Choice(['images']), multiple=True)
def cmd_lastfm_top_artists(context, count, time_range, include):
    '''Return user's top artists.'''

    context.obj.lastfm.authenticate()
    result = calliope.lastfm.top_artists(context.obj.lastfm, count, time_range,
                                         include)
    calliope.playlist.write(result, sys.stdout)


@cli.group(name='lastfm-history',
           help="Scrape and query user's LastFM listening history")
@click.option('--sync/--no-sync', default=True,
              help="update the local copy of the LastFM history")
@click.option('--user', metavar='NAME',
              help="show data for the given Last.fm user")
@click.option('--server', default='last.fm',
              help="Server to fetch track info from, default is last.fm")
@click.option('--retry-on-error/--no-retry-on-error', default=True,
              help="try again if a network error occurs.")
@click.pass_context
def lastfm_history_cli(context, sync, user, server, retry_on_error):
    if not user:
        user = context.obj.config.get('lastfm', 'user')
    if not user:
        raise RuntimeError("Please specify a username.")

    lastfm_history = calliope.lastfm.history.load(user, server=server,
                                                  retry_on_error=retry_on_error)

    context.obj.lastfm_history = lastfm_history

    def sync_callback():
        if sync:
            op = lastfm_history.prepare_sync()
            with click.progressbar(iter(op.pages_to_sync),
                                   length=len(op.pages_to_sync),
                                   label="Updating scrobbles from last.fm server") as pages:
                for page in pages:
                    lastfm_history.sync_page(page)

    context.obj.sync = sync_callback


@lastfm_history_cli.command(name='annotate',
                            help="Annotate a playlist with lastfm listening "
                                 "stats for a user")
@click.argument('playlist', nargs=1, type=click.File('r'))
@click.pass_context
def cmd_lastfm_history_annotate(context, playlist):
    lastfm_history = context.obj.lastfm_history
    context.obj.sync()

    for item in calliope.playlist.read(playlist):
        result = lastfm_history.annotate(item)
        calliope.playlist.write([result], sys.stdout)


@lastfm_history_cli.command(name='artists',
                            help="Query artists from the listening history")
@click.option('--first-play-before', metavar='DATE',
              help="show artists that were first played before DATE")
@click.option('--first-play-since', metavar='DATE',
              help="show artists that were first played on or after DATE")
@click.option('--last-play-before', metavar='DATE',
              help="show artists that were last played before DATE")
@click.option('--last-play-since', metavar='DATE',
              help="show artists that were last played on or after DATE")
@click.option('--min-listens', default=1, metavar='N',
              help="show only artists that were played N times")
@click.option('--show-listens-since', metavar='DATE',
              help="query the number of listens since the given date")
@click.pass_context
def cmd_lastfm_history_artists(context, first_play_before, first_play_since,
                               last_play_before, last_play_since, min_listens,
                               show_listens_since):
    lastfm_history = context.obj.lastfm_history
    context.obj.sync()

    cal = parsedatetime.Calendar()

    if first_play_before is not None:
        first_play_before = string_to_datetime(cal, first_play_before)
    if first_play_since is not None:
        first_play_since = string_to_datetime(cal, first_play_since)
    if last_play_before is not None:
        last_play_before = string_to_datetime(cal, last_play_before)
    if last_play_since is not None:
        last_play_since = string_to_datetime(cal, last_play_since)

    if show_listens_since is not None:
        show_listens_since = string_to_datetime(cal, show_listens_since)

    artists = lastfm_history.artists(
        first_play_before=first_play_before,
        first_play_since=first_play_since,
        last_play_before=last_play_before,
        last_play_since=last_play_since,
        min_listens=min_listens,
        show_listens_since=show_listens_since)
    calliope.playlist.write(artists, sys.stdout)

@lastfm_history_cli.command(name='scrobbles',
                            help="Export individual scrobbles as a playlist")
@click.pass_context
def cmd_lastfm_history_scrobbles(context):
    lastfm_history = context.obj.lastfm_history
    context.obj.sync()
    tracks = lastfm_history.scrobbles()
    calliope.playlist.write(tracks, sys.stdout)


@lastfm_history_cli.command(name='tracks',
                            help="Query tracks from the listening history")
@click.option('--first-play-before', metavar='DATE',
              help="show tracks that were first played before DATE")
@click.option('--first-play-since', metavar='DATE',
              help="show tracks that were first played on or after DATE")
@click.option('--last-play-before', metavar='DATE',
              help="show tracks that were last played before DATE")
@click.option('--last-play-since', metavar='DATE',
              help="show tracks that were last played on or after DATE")
@click.option('--min-listens', default=1, metavar='N',
              help="show only tracks that were played N times")
@click.option('--show-listens-since', metavar='DATE',
              help="query the number of listens since the given date")
@click.pass_context
def cmd_lastfm_history_tracks(context, first_play_before, first_play_since,
                              last_play_before, last_play_since, min_listens,
                              show_listens_since):
    lastfm_history = context.obj.lastfm_history
    context.obj.sync()

    cal = parsedatetime.Calendar()

    if first_play_before is not None:
        first_play_before = string_to_datetime(cal, first_play_before)
    if first_play_since is not None:
        first_play_since = string_to_datetime(cal, first_play_since)
    if last_play_before is not None:
        last_play_before = string_to_datetime(cal, last_play_before)
    if last_play_since is not None:
        last_play_since = string_to_datetime(cal, last_play_since)

    if show_listens_since is not None:
        show_listens_since = string_to_datetime(cal, show_listens_since)

    tracks = lastfm_history.tracks(
        first_play_before=first_play_before,
        first_play_since=first_play_since,
        last_play_before=last_play_before,
        last_play_since=last_play_since,
        min_listens=min_listens,
        show_listens_since=show_listens_since)
    calliope.playlist.write(tracks, sys.stdout)


@cli.group(name='musicbrainz', help="Query data from Musicbrainz")
@click.pass_context
def musicbrainz_cli(context):
    context.obj.musicbrainz = calliope.musicbrainz.MusicbrainzContext(
        context.obj.config)


@musicbrainz_cli.command(name='annotate')
@click.argument('playlist', type=click.File(mode='r'))
@click.option('--include', '-i', type=click.Choice(['areas', 'release', 'urls']), multiple=True)
@click.pass_context
def cmd_musicbrainz_annotate(context, playlist, include):
    '''Annotate playlists with data from Musicbrainz'''

    result_generator = calliope.musicbrainz.annotate(
        context.obj.musicbrainz, calliope.playlist.read(playlist), include)
    calliope.playlist.write(result_generator, sys.stdout)


@musicbrainz_cli.command(name='resolve-ids')
@click.argument('playlist', type=click.File(mode='r'))
@click.pass_context
def cmd_musicbrainz_resolve_ids(context, playlist):
    """Resolve Musicbrainz identifiers for each item in ``playlist``."""

    result_generator = calliope.musicbrainz.resolve_ids(
        context.obj.musicbrainz, calliope.playlist.read(playlist))
    calliope.playlist.write(result_generator, sys.stdout)


@musicbrainz_cli.command(name='resolve-image')
@click.argument('playlist', type=click.File(mode='r'))
@click.option('--max-size', '-s', type=click.Choice(['250', '500', 'none']), default='250',
              help="set a size limit in pixels for the returned image")
@click.pass_context
def cmd_musicbrainz_resolve_image(context, playlist, max_size):
    '''Resolve the 'image' property using the Cover Art API.'''

    result_generator = calliope.musicbrainz.resolve_image(
        context.obj.musicbrainz, calliope.playlist.read(playlist), max_size)
    calliope.playlist.write(result_generator, sys.stdout)


@cli.command(name='play')
@click.option('-o', '--output', type=click.Path(), required=True)
@click.argument('playlist', type=click.File(mode='r'))
@click.pass_context
def cmd_play(context, output, playlist):
    '''Render a Calliope playlist to an audio file'''

    output_playlist = calliope.play.play(calliope.playlist.read(playlist),
                                         output)
    if output_playlist is not None:
        calliope.playlist.write(output_playlist, sys.stdout)


@cli.command(name='select')
@click.option('--constraint', 'constraints_list', type=str, multiple=True,
              help="A single constraint.")
@click.argument('playlist', type=click.File(mode='r'))
@click.pass_context
def cmd_select(context, constraints_list, playlist):
    '''Select tracks from input playlist following a set of constraints.

    Each constraint is defined by a key/value string. Here are some examples:

    \b
       * --constraint=type:playlist-duration,vmin:60m,vmax:120m
       * --constraint=type:fraction-global,prop:tags,values:rock;punk,fraction:0.5

    '''

    constraints = [calliope.select.constraint_from_string(c)
                   for c in constraints_list]

    try:
        output = calliope.select.select(calliope.playlist.read(playlist), constraints)
    except calliope.select.SelectError as e:
        raise RuntimeError(e) from e
    calliope.playlist.write(output, sys.stdout)


@cli.command(name='shuffle')
@click.option('--count', '-c', type=int, default=None,
              help="number of songs to output")
@click.argument('playlist', type=click.File(mode='r'))
@click.pass_context
def cmd_shuffle(context, count, playlist):
    '''Shuffle a playlist or collection.'''

    output = calliope.shuffle.shuffle(calliope.playlist.read(playlist), count)
    calliope.playlist.write(output, sys.stdout)


@cli.group(name='spotify',
           help="Interface to the Spotify online streaming service")
@click.option('--user', help="show data for the given Spotify user")
@click.pass_context
def spotify_cli(context, user):
    if os.environ.get('CALLIOPE_SPOTIFY_MOCK') == 'yes':
        # This is for testing; we used to run the tests in a subprocess
        # so we couldn't use mock.patch(). Now we could.
        import unittest.mock  # pylint: disable=import-outside-toplevel
        context.obj.spotify = unittest.mock.MagicMock()
    else:
        context.obj.spotify = calliope.spotify.SpotifyContext(
            context.obj.config, user=user)


@spotify_cli.command(name='annotate')
@click.argument('playlist', type=click.File(mode='r'))
@click.pass_context
def cmd_spotify_annotate(context, playlist):
    '''Add Spotify-specific information to tracks in a playlist.'''
    context.obj.spotify.authenticate()
    api = context.obj.spotify.api
    for track in calliope.spotify.annotate(api, calliope.playlist.read(playlist)):
        calliope.playlist.write([track], sys.stdout)


@spotify_cli.command(name='export')
@click.pass_context
def cmd_spotify_export(context):
    '''Query user playlists from Spotify'''
    context.obj.spotify.authenticate()
    calliope.spotify.export(context.obj.spotify)


@spotify_cli.command(name='import')
@click.pass_context
def cmd_spotify_import(context):
    '''Upload one or more playlists to Spotify'''
    raise NotImplementedError


@spotify_cli.command(name='top-artists')
@click.pass_context
@click.option('-c', '--count', type=int, default=20,
              help="Maximum number of artists to return")
@click.option('--time-range', default='long_term',
              type=click.Choice(['short_term', 'medium_term', 'long_term']))
def cmd_spotify_top_artists(context, count, time_range):
    '''Return user's top artists.'''
    context.obj.spotify.authenticate()
    result = calliope.spotify.top_artists(context.obj.spotify, count, time_range)

    calliope.playlist.write(result, sys.stdout)


@cli.command(name='stat')
@click.option('--size', '-s', is_flag=True,
              help="show the total size on disk of the playlist contents")
@click.argument('playlist', type=click.File(mode='r'))
@click.pass_context
def cmd_stat(context, size, playlist):
    '''Information about the contents of a playlist'''

    input_playlist = list(calliope.playlist.read(playlist))

    if size:
        calliope.stat.measure_size(input_playlist)
    else:
        print("Please select a mode.")


@cli.group(name='suggest', help="Suggest items or annotations")
@click.pass_context
def suggest_cli(context):
    pass


@suggest_cli.command(name='tracks')
@click.option('--from', 'from_', required=True, type=click.File(mode='r'),
              help="playlist from which tracks should be suggested")
@click.option('--count', type=int, default=10,
              help="number of track suggestions to generate")
@click.option('--training-input', multiple=True,
              type=(click.File(mode='r'), float),
              help="a playlist used to train the recommender. "
                   "A training input requires two arguments, the first is the "
                   "path to the file, the second is how it should weight the "
                   "training. Weight should be a value between -1.0 and 1.0, "
                   "where 1.0 is the most positive weighting and -1.0 the "
                   "most negative.")
@click.pass_context
def cmd_suggest_tracks(context, from_, count, training_input):
    '''Suggest tracks from a collection based on the given training inputs.'''

    # First we need a 'user-item' interaction matrix. Each 'item' is a track in
    # the input collection. Each 'user' is one of the input playlists.

    corpus_playlist = calliope.playlist.read(from_)
    calliope.suggest.suggest_tracks(corpus_playlist, count, training_input)


@cli.command(name='sync')
@click.option('--dry-run', is_flag=True,
              help="don't execute commands, only print what would be done")
@click.option('--target', '-t', type=click.Path(exists=True, file_okay=False),
              required=True,
              help="path to target device's filesystem")
@click.option('--allow-formats', '-f', type=click.Choice(['all', 'mp3']),
              multiple=True, default=[],
              help="specify formats that the target device can read; "
                   "transcoding can be done if needed.")
@click.option('--album-per-dir', is_flag=True,
              help="organise the files on the target device so each album is "
                   "in its own directory")
@click.option('--number-dirs', is_flag=True,
              help="ensure directory sort order matches desired playback "
                   "order")
@click.option('--number-files', is_flag=True,
              help="ensure filename sort order matches desired playback order")
@click.argument('playlist', type=click.File(mode='r'))
@click.pass_context
def cmd_sync(context, dry_run, target, allow_formats, album_per_dir,
             number_dirs, number_files, playlist):
    '''Copy playlists & collections between devices'''
    calliope.sync.sync(dry_run, target, allow_formats, album_per_dir,
                       number_files, number_files,
                       calliope.playlist.read(playlist))


@cli.group(name='tracker', help="Query the Tracker media database")
@click.pass_context
def tracker_cli(context):
    context.obj.tracker = calliope.tracker.TrackerClient()


@tracker_cli.command(name='annotate-images')
@click.argument('playlist', type=click.File(mode='r'))
@click.pass_context
def cmd_tracker_annotate_images(context, playlist):
    '''Add images from the local media-art cache.'''
    output = calliope.tracker.annotate_images(context.obj.tracker, calliope.playlist.read(playlist))
    calliope.playlist.write(output, sys.stdout)


@tracker_cli.command(name='expand-tracks')
@click.argument('playlist', type=click.File(mode='r'))
@click.pass_context
def cmd_tracker_expand_tracks(context, playlist):
    '''Convert any 'artist' or 'album' type playlist items into 'track' items'''
    result = calliope.tracker.expand_tracks(context.obj.tracker, calliope.playlist.read(playlist))
    calliope.playlist.write(result, sys.stdout)


@tracker_cli.command(name='albums')
@click.option('--artist', nargs=1, type=str,
              help="Limit to albums by the given artist")
@click.option('--include-tracks', is_flag=True, default=False,
              help="List tracks for each album.")
@click.pass_context
def cmd_tracker_albums(context, artist, include_tracks):
    '''Show all albums available locally.'''
    tracker = context.obj.tracker
    if include_tracks:
        result = tracker.tracks_grouped_by_album(filter_artist_name=artist)
    else:
        result = tracker.albums(filter_artist_name=artist)
    calliope.playlist.write(result, sys.stdout)


@tracker_cli.command(name='artists')
@click.pass_context
def cmd_tracker_artists(context):
    '''Show all artists whose music is available locally.'''
    tracker = context.obj.tracker
    calliope.playlist.write(tracker.artists(), sys.stdout)


@tracker_cli.command(name='tracks')
@click.pass_context
def cmd_tracker_tracks(context):
    '''Show all tracks available locally.'''
    tracker = context.obj.tracker
    calliope.playlist.write(tracker.tracks(), sys.stdout)


@tracker_cli.command(name='resolve-content')
@click.argument('playlist', type=click.File(mode='r'))
@click.pass_context
def cmd_tracker_resolve_content(context, playlist):
    '''Resolve the 'location' field using Tracker, if possible.'''
    output = calliope.tracker.resolve_content(context.obj.tracker, calliope.playlist.read(playlist))
    calliope.playlist.write(output, sys.stdout)


@tracker_cli.command(name='resolve-image')
@click.argument('playlist', type=click.File(mode='r'))
@click.pass_context
def cmd_tracker_resolve_image(context, playlist):
    '''Resolve 'image' property using the local media-art cache.'''
    output = calliope.tracker.resolve_image(context.obj.tracker, calliope.playlist.read(playlist))
    calliope.playlist.write(output, sys.stdout)


@tracker_cli.command(name='search')
@click.argument('text', nargs=1, type=str)
@click.pass_context
def cmd_tracker_search(context, text):
    '''Search for tracks in the Tracker database matching 'text'.

    Append '*' to enable partial matching of a search term.'''
    tracker = context.obj.tracker
    calliope.playlist.write(tracker.search(search_text=text), sys.stdout)


@tracker_cli.command(name='top-artists')
@click.pass_context
@click.option('-c', '--count', type=int, default=20,
              help="Maximum number of artists to return")
def cmd_tracker_top_artists(context, count):
    '''Query the top artists in a Tracker database'''
    tracker = context.obj.tracker
    result = list(tracker.artists_by_number_of_songs(limit=count))
    calliope.playlist.write(result, sys.stdout)


@cli.command(name='validate')
@click.argument('playlist', type=click.File(mode='r'))
@click.pass_context
def cmd_validate(context, playlist):
    '''Validate a Calliope playlist stream.'''
    for item in calliope.playlist.read(playlist):
        calliope.validate.validate(item)
        calliope.playlist.write([item], sys.stdout)


@cli.group(name='youtube',
           help="Interface to the Youtube online streaming service")
@click.option('--client-secrets', type=click.File(mode='r'),
              help="Credentials file from Google developer console")
@click.pass_context
def youtube_cli(context, client_secrets):
    context.obj.youtube = calliope.youtube.YoutubeContext(
        config=context.obj.config)


@youtube_cli.command(name='export')
@click.argument('username', type=str)
@click.pass_context
def cmd_youtube_export(context, username):
    '''Query user playlists from Youtube'''
    api = context.obj.youtube.authenticate()
    channel_id = calliope.youtube.get_channel_id(api, username)
    result = calliope.youtube.export(api, channel_id)
    calliope.playlist.write(result, sys.stdout)
