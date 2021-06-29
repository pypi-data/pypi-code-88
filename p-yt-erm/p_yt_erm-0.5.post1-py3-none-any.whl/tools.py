import re
import vlc
import sys
import pafy
import time
import feedparser
import threading
from youtubesearchpython import VideosSearch, PlaylistsSearch


class Song():
    def __init__(self, url, length=None, channelname=None, title=None, id=None):
        """Song object that stores important song stuff
        Best constructed by calling `get_song_obj()` with either search terms or a youtube URL
        """
        self.pafyobj = None
        self.url = url
        self.length = length
        self.channel = channelname
        self.vidtitle = title
        self.id = id
        if None in [self.url, self.channel, self.vidtitle]:
            self.fill_details()
        self.extract_title_author()
    
    def __str__(self):
        return self.vidtitle
    
    def extract_title_author(self):
        """"Extracts real song title and artist from youtube title"""
        title = self.vidtitle
        artist = self.channel
        if ' - ' in title:
            title_list = title.split(' - ')
            title = exclude_from_string(title_list[1].strip())
            artist = title_list[0].strip()
            if not artist:
                artist = exclude_from_string(self.channel)
        elif ' by ' in title:
            # way less common but occasionally some titles will have "songname by artist"
            title_list = title.split(' by ')
            title = exclude_from_string(title_list[0].strip())
            artist = title_list[-1]
            if not artist:
                artist = exclude_from_string(self.channel)
        else:
            title = exclude_from_string(title)
            artist = exclude_from_string(artist)
        self.title = title
        self.artist = artist
    
    def fill_details(self):
        if None in [self.length, self.channel, self.vidtitle, self.id]:
            self.pafyobj = pafy.new(self.url)
            # if not self.length: self.length = timestamp_to_sec(self.pafyobj.duration)
            if not self.length: self.length = self.pafyobj.duration
            if not self.channel: self.channel = self.pafyobj.author
            if not self.vidtitle: self.vidtitle = self.pafyobj.title
            if not self.id: self.id = self.pafyobj.videoid
    
    def get_stream(self, legacy=False):
        if self.pafyobj is None:
            self.pafyobj = pafy.new(self.url)
        if legacy:
            return self.pafyobj.streams[0].url
        else:
            return self.pafyobj.getbestaudio(preftype='m4a').url


exclude_list = ['\\(', '\\)', '\\[', '\\]', '\\"', "\\'", 'official audio', 'official video', 'official music video',
                'lyrics', 'lyric video', ' \\- topic']


def exclude_from_string(input_):
    for i in exclude_list:
        input_ = re.sub(i, '', input_, flags=re.IGNORECASE)
    return input_


def previous_line():
    """Move cursor to previous line"""
    sys.stdout.write("\033[F")


def clear_line():
    """Clear current line"""
    sys.stdout.write("\033[K")


def clear_previous_line():
    """Clear previous line"""
    previous_line()
    clear_line()


def get_song_obj(song):
    if is_url(song) and is_youtube_url(song):
        song_obj = song_from_url(song)
        return song_obj
    else:
        song_obj = song_from_search(song)
        return song_obj


def timestamp_to_sec(timestamp):
    colcount = timestamp.count(':')
    if colcount == 1:
        minutes, seconds = timestamp.split(':')
        return int(minutes) * 60 + int(seconds)
    elif colcount == 2:
        hours, minutes, seconds = timestamp.split(':')
        return int(hours) * 3600 + int(minutes) * 60 + int(seconds)


def song_from_url(url):
    return Song(url)


def song_from_search(search):
    """Looks up a song with search terms and returns a Song object"""
    result = VideosSearch(search, limit=1).result()['result'][0]
    return Song(result['link'], timestamp_to_sec(result['duration']), result['channel']['name'], result['title'],
                result['id'])


def url_from_playlist_search(search):
    result = PlaylistsSearch(search, limit=1).result()['result'][0]
    return result['link']


def songs_from_yt_playlist(url):
    """Returns a list of songs from a youtube playlist link"""
    url = yt_playlist_to_rss_url(url)
    rss = feedparser.parse(url)
    out = []
    for item in rss['entries']:
        song = Song(item['link'], None, item['author'], item['title'], item['yt_videoid'])
        out.append(song)
    return out


def format_yt_title(title):
    return title


url_regex = '(?:(?:https?|ftp):\\/\\/|\\b(?:[a-z\\d]+\\.))(?:(?:[^\\s()<>]+|\\((?:[^\\s()<>]+|(?:\\([^\\s()<>]+\\)))?\\))+(?:\\((?:[^\\s()<>]+|(?:\\(?:[^\\s()<>]+\\)))?\\)|[^\\s`!()\\[\\]{};:\'".,<>?«»“”‘’]))?'


def is_url(url):
    """Checks if a given string is an URL using regular expression, returns a bool"""
    return bool(re.match(url_regex, url))


youtube_url_regex = '^((?:https?:)?\\/\\/)?((?:www|m)\\.)?((?:youtube\\.com|youtu.be))(\\/(?:[\\w\\-]+\\?v=|embed\\/|v\\/)?)([\\w\\-]+)(\\S+)?$'


def is_youtube_url(url):
    """Checks if a given string is a youtube url, returns a bool"""
    return bool(re.match(youtube_url_regex, url))


def ensure_list(input_object):
    """Returns any input as a list. Tuples and sets get converted to lists,
    lists are returned as-is, and all other types get returned as a single element list"""
    input_type = type(input_object)
    if input_type == list:
        return input_object
    elif input_type in [tuple, set]:
        return list(input_object)
    else:
        return [input_object]


def yt_playlist_to_rss_url(playlist_url):
    """Gets the rss url from a youtube playlist"""
    url_prefix = 'https://www.youtube.com/feeds/videos.xml?playlist_id='
    playlist_id = playlist_url.split('?list=')[-1]
    return url_prefix + playlist_id


def secs_to_string(seconds):
    """Gets time from seconds to human readable"""
    hours = -1
    minutes = 0
    seconds = int(seconds)
    out = ""
    if seconds >= 3600:
        hours = int(seconds / 3600)
        seconds = seconds % 3600
    if seconds >= 60:
        minutes = int(seconds / 60)
        seconds = seconds % 60
    
    if hours != -1:
        out += f'{hours}:'
        if minutes < 10:
            out += f'0{minutes}:'
        else:
            out += f'{minutes}:'
    else:
        out += f'{minutes}:'
    
    if seconds < 10:
        out += f'0{seconds}'
    else:
        out += f'{seconds}'
    
    return out

    

def get_position(player: vlc.MediaPlayer):
    return int(player.get_time() / 1000)
