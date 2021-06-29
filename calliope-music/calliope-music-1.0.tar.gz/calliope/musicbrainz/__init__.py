# Calliope
# Copyright (C) 2017-2021  Sam Thursfield <sam@afuera.me.uk>
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

"""Access data from `Musicbrainz <https://musicbrainz.org/>`_.

See also: :program:`cpe musicbrainz` command.

This module wraps the `musicbrainzngs <https://python-musicbrainzngs.readthedocs.io>`_ library.

Authentication
--------------

Musicbrainz access requires that you set a User Agent string. A default is set
by the :obj:`MusicbrainzContext` object which can be overridden using its
config.

Caching
-------

Caching of data is handled using the :mod:`calliope.cache` module.

"""


import musicbrainzngs

import logging

import calliope.cache
import calliope.config
import calliope.playlist

from . import annotate_helpers
from . import resolve

log = logging.getLogger(__name__)


class MusicbrainzContext():
    """Configuration for Musicbrainz APIs."""

    def __init__(self, config):
        self.config = config

        app = config.get('musicbrainz', 'app') or "Calliope"
        version = config.get('musicbrainz', 'version') or "1"
        contact = config.get('musicbrainz', 'contact') or \
            "https://gitlab.com/samthursfield/calliope"

        musicbrainzngs.set_useragent(app, version, contact)

        self.cache = calliope.cache.open(namespace='musicbrainz')


def annotate(context, playlist, include):
    for item in playlist:
        item = resolve.artist_id_from_creator(context, item)

        if 'album' in item and 'musicbrainz.album_id' not in item:
            pass

        if 'title' in item and 'musicbrainz.identifier' not in item:
            pass

        if 'areas' in include:
            item = annotate_helpers.add_musicbrainz_artist_areas(context.cache, item)

        if 'release' in include:
            item = annotate_helpers.add_musicbrainz_album_release(context.cache, item)

        if 'urls' in include:
            item = annotate_helpers.add_musicbrainz_artist_urls(context.cache, item)

        yield item


def resolve_ids(context, playlist):
    """Resolve Musicbrainz identifiers for each item in ``playlist``."""
    for item in playlist:
        if 'album' in item:
            item = resolve.release_ids_from_album(context, item)
        elif 'creator' in item:
            item = resolve.artist_id_from_creator(context, item)
        yield item


def resolve_image(context, playlist, max_size=250):
    """Resolve a cover image using the Cover Art API.

    See https://musicbrainz.org/doc/Cover_Art_Archive/API for more info."""

    assert str(max_size) in ['250', '500', 'None']

    for item in playlist:
        if 'image' not in item:
            item = resolve.image_for_item(context, item, max_size)
        yield item
