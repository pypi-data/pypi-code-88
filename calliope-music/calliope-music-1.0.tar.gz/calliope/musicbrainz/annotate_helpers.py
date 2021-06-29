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

import musicbrainzngs

import logging

log = logging.getLogger(__name__)


def add_musicbrainz_album_release(cache, item):
    if 'musicbrainz.album_id' in item:
        album_musicbrainz_id = item['musicbrainz.album_id']
        key = 'release:{}'.format(album_musicbrainz_id)
        try:
            result = cache.wrap(key,
                lambda: musicbrainzngs.get_release_by_id(album_musicbrainz_id)['release'])
        except musicbrainzngs.ResponseError as e:
            if str(e.cause).startswith('HTTP Error 404'):
                item.add_warning('musicbrainz', 'Invalid album ID')
                return item
            else:
                raise

        if 'date' in result:
            item['musicbrainz.release_date'] = result['date']
    return item


def add_musicbrainz_artist_areas(cache, item):
    def get_areas(result):
        result_main_area = result['artist'].get('area')
        if result_main_area:
            result_areas = [result_main_area]
        else:
            result_areas = []
        return result_areas

    if 'musicbrainz.artist_id' in item:
        artist_musicbrainz_id = item['musicbrainz.artist_id']
        key = 'creator:{}:areas'.format(artist_musicbrainz_id)
        result = cache.wrap(key,
            lambda: get_areas(musicbrainzngs.get_artist_by_id(item['musicbrainz.artist_id'], includes='area-rels')))

        item_areas = item.get('musicbrainz.creator_areas', [])
        for area in result:
            item_areas.append(area)
        item['musicbrainz.creator_areas'] = item_areas
    return item


def add_musicbrainz_artist_urls(cache, item):
    if 'musicbrainz.artist_id' in item:
        artist_musicbrainz_id = item['musicbrainz.artist_id']
        key = 'creator:{}:urls'.format(artist_musicbrainz_id)
        result = cache.wrap(key,
            lambda: musicbrainzngs.get_artist_by_id(
                artist_musicbrainz_id, includes='url-rels')['artist'].get('url-relation-list', []))

        item_urls = item.get('musicbrainz.creator_urls', [])
        for result_url in result:
            item_urls.append(
                { 'musicbrainz.url.type': result_url['type'], 'musicbrainz.url.target': result_url['target'] })
        item['musicbrainz.creator_urls'] = item_urls
    return item
