#!/usr/bin/python3
import argparse
import os
import random
import threading
import time
import vlc
from pypresence import Presence

from . import tools

Song = tools.Song


def info(*args):
    """Print info-level log"""
    print('[INFO] ', *args, sep='')


class Player:
    """Main player class

    args:
        songs (list, str):      one or more song titles/urls
        playlists (list, str):  one or more urls to youtube playlists/paths to local playlist files
        shuffle (bool):         whether or not to randomise the song queue
        volume (int >= 0):      volume level (>100 gets distorted and LOUD)
        rich_presence (bool):   whether or not to use discord rich presence to display the current song
        muted (bool):           whether or not to start the player muted
        enable_input (bool):    whether or not to allow users to control the player through commandline input
        vlclogs (bool):         whether or not to print VLC logs
        debuglogs (bool):       whether or not to print pYTerm debug logs
        legacystreams (bool):   whether or not to use legacy streams, enable if some songs dont load
        """
    # vvv variables that can't be changed in initialisation
    rich_presence_id: str = '737813623967318077'
    current_song: Song = None
    songs: [Song] = []
    song_index: int = 0
    exiting: bool = False
    muted: bool = False
    pending_action: bool = False
    input_commands = {  # all user input commands and their corrosponding action
        'next': lambda self, cmd: self.next(),
        'previous': lambda self, cmd: self.previous(),
        'scrub': lambda self, cmd: self.scrub(int(cmd[0])),
        'pause': lambda self, cmd: self.toggle_pause(),
        'mute': lambda self, cmd: self.toggle_mute(),
        'goto': lambda self, cmd: self.play_at_index(int(cmd[0])),
        'volume': lambda self, cmd: self.set_volume(int(cmd[0])),
        'exit': lambda self, cmd: self.stop(),
    }
    
    def __init__(self,
                 songs=None,  # list of song titles/urls or single song title/url
                 playlists=None,
                 # list of urls to youtube playlist/paths of local playlist file or single url to youtube
                 # playlist/path of local playlist file
                 shuffle: bool = False,  # whether or not to randomise the song queue
                 volume: int = 100,  # starting volume
                 muted: bool = False,  # whether or not to start the player muted
                 rich_presence: bool = True,  # whether or not to use discord rich presence to display the current song
                 enable_input: bool = True,
                 # whether or not to allow users to control the player through commandline input
                 vlclogs: bool = False,  # whether or not to print VLC logs
                 debuglogs: bool = False,  # whether or not to print pYTerm debug logs
                 legacystreams: bool = False,
                 # whether or not to use legacy streams, disabling might improve sound quality at the cost of some
                 # songs not working
                 ):
        self.shuffle_state = shuffle
        self.volume = volume
        self.rich_presence = rich_presence
        self.enable_input = enable_input
        self.vlclogs = vlclogs
        self.debuglogs = debuglogs
        self.legacystreams = legacystreams
        if not vlclogs:
            os.environ[
                'VLC_VERBOSE'] = '-1'  # sets the env var for vlc logging to -1, seems to not obey it fully tho :\
            self.vlc = vlc.Instance('--no-video', '--quiet', 'vout=none')
        else:
            self.vlc = vlc.Instance('--no-video', 'vout=none')
        # vlc instance, really only needed to spawn the player and create media objects, but handy to keep around ig
        self.vlc_player = self.vlc.media_player_new()
        if songs:
            self.add_song(songs)
        if playlists:
            self.add_playlist(playlists)
        if self.rich_presence:
            try:
                self.rich_presence_client = Presence(self.rich_presence_id)
                self.rich_presence_client.connect()
            except:
                pass
        if self.enable_input:
            threading.Thread(target=self.run_input, daemon=True).start()
    
    def play(self, song, halting=False):
        """Play a single song

            args:
                song (str, Song):       keyword or url of a song on YouTube
                halting = False (bool): set to False to not halt the program
        """
        def _play(self, song):
            if type(song) != Song:
                song = tools.get_song_obj(song)
            self.current_song = song
            stream_url = song.get_stream(legacy=self.legacystreams)
            vlc_media = self.vlc.media_new(stream_url, 'vout=none', '--no-video')
            self.vlc_player.set_media(vlc_media)
            self.vlc_player.play()
            # if self.muted:
            #     self.vlc_player.audio_set_volume(0)
            # else:
            #     self.vlc_player.audio_set_volume(self.volume)
            self.wait_on_song_load()
            if self.muted:
                self.vlc_player.audio_set_volume(0)
            else:
                self.vlc_player.audio_set_volume(self.volume)
            if song.length is None:
                song.length = int(self.vlc_player.get_length() / 100)
                # if song is missing length attribute, get it from vlc
            print(f'\rPlaying {song.title} by {song.artist} [{self.get_total_time()}]')  # print, to avoid [Info]  and add \r
            while self.is_alive():
                time.sleep(0.1)
            self.current_song = None

        if halting:
            _play(self, song)
        else:
            threading.Thread(target=_play, args=(self,song),daemon=True).start()
    
    def play_all(self, halting=False, **kwargs):
        """play entire song queue.

        args:
            halting = False (bool):     set to False to not halt the program
            keep_alive = True (bool):   keep loop running even when the queue has ended, useful if you want to add more songs later
            loop = False (bool):        whether or not to restart the song queue once its played the final song
            """
        
        def run(self, keep_alive=True, loop=False):
            while True:
                while self.song_index < len(self.songs) or loop:
                    self.play_current_song(halting=False)
                    self.wait_on_song_load()
                    while self.is_alive():  # loop while the song is playing to update discord
                        self.update_rich_presence()
                        if self.exiting: return
                        time.sleep(0.25)
                    if self.exiting: return
                    if self.pending_action:
                        self.pending_action = False
                    else:
                        self.increment_song_index(wrap=loop)
                if self.exiting: return
                if not keep_alive:
                    return
        
        x = threading.Thread(target=run, daemon=True, args=(self,), kwargs=kwargs)
        if halting:
            x.run()
        else:
            x.start()
    
    def increment_song_index(self, positive=True, wrap=True):
        """increments or decrements the `song_index` by one, with optional wrapping"""
        number = -1 + (2 * bool(positive))
        new_index = self.song_index + number
        queue_length = len(self.songs)
        if new_index >= queue_length and wrap:
            new_index = new_index - (queue_length - 1)
        elif new_index < 0:
            if wrap:
                new_index = new_index + (queue_length - 1)
            else:
                new_index = 0
        self.song_index = new_index
    
    def run_input(self):
        """allows user input. halts if called, initialise Player with `enable_input = True` to not halt"""
        print('Commands:', ' - '.join(self.input_commands.keys()))  # list commands
        
        def ignore(*args, **kwargs):
            # print('No such command')
            pass
        
        self.wait_on_song_load()
        time.sleep(0.1)
        
        while self.enable_input and not self.exiting:
            full = input(':').split(' ')
            # tools.previous_line() # for when command output is added
            if len(full) > 1:
                key = full[0]
                cmd = full[1:]
            else:
                key = full[0]
                cmd = ''
            try:
                self.input_commands.get(key, ignore)(self, cmd)
            except Exception as e:
                pass
            tools.clear_previous_line()

    def stop(self):
        """Stops player and exits"""
        self.exiting = True
        self.vlc_player.stop()
    
    def next(self):
        """play next song in the queue"""
        # self.pending_action = True
        # self.increment_song_index()
        self.vlc_player.stop()
    
    def previous(self):
        """play previous song in the queue"""
        self.pending_action = True
        self.increment_song_index(positive=False)
        self.vlc_player.stop()
    
    def play_at_index(self, index):
        """plays the song at the given position in the queue"""
        self.pending_action = True
        self.song_index = index
        self.vlc_player.stop()
    
    def pause(self):
        """pauses the player"""
        self.set_volume(0, desync_volume=self.volume)
        self.vlc_player.set_pause(1)
    
    def unpause(self):
        """unpauses the player"""
        self.set_volume(self.volume, desync_volume=0)
        self.vlc_player.set_pause(0)
    
    def toggle_pause(self):
        """toggles between paused and unpaused player"""
        if self.is_vlc_alive():
            if self.vlc_player.is_playing():
                self.pause()
            else:
                self.unpause()
    
    def is_alive(self):
        """returns true if vlc is either paused or playing"""
        try:
            if str(self.vlc_player.get_state()) == 'State.Playing' or str(
                    self.vlc_player.get_state()) == 'State.Paused':
                return True
            else:
                return False
        except Exception:
            return False

    def is_paused(self):
        """returns true if the player is paused, False if playing or if there is no song at all"""
        if self.is_vlc_alive:
            return self.vlc_player.is_playing()
        return False
        
    
    def toggle_mute(self):
        """toggles between muted and unmuted player"""
        if self.muted:
            self.unmute()
        else:
            self.mute()
    
    def mute(self):
        """mutes player and fades music out"""
        if not self.muted:
            self.set_volume(0, desync_volume=self.volume)
            self.muted = True
            self.debug('muted')
    
    def unmute(self):
        """unmutes player and fades music back in"""
        if self.muted:
            self.muted = False
            self.set_volume(self.volume, desync_volume=0)
            self.debug('unmuted')
    
    def scrub(self, seconds):
        """scrub the current song left or right in seconds

        args:
            seconds (int): positive or negative int indicating seconds to fast forward/backwards
        """
        self.vlc_player.set_time(round(self.vlc_player.get_time() + seconds * 1000))
    
    def set_volume(self, new_volume, fadetime=0.5, desync_volume=None):
        """change volume smoothly over `fadetime` seconds

        args:
            new_volume (int): volume to transition to
            fadetime (foat): transition time in seconds
            desync_volume (int): don't use this, its for muting
        """
        current_volume = self.volume
        if desync_volume is not None:
            current_volume = desync_volume
        if (new_volume != self.volume or desync_volume is not None) and 200 >= new_volume >= 0:
            if fadetime and not self.muted:
                if new_volume > current_volume:
                    step = +1
                else:
                    step = -1
                fadedelay = fadetime / abs(new_volume - current_volume)
                for i in range(current_volume, new_volume, step):
                    self.vlc_player.audio_set_volume(i)
                    time.sleep(fadedelay)
            
            if not self.muted:
                self.vlc_player.audio_set_volume(new_volume)
            if desync_volume is None:
                self.volume = new_volume
    
    def play_current_song(self, *args, **kwargs):
        """play queue song at the current index"""
        self.play(self.songs[self.song_index], *args, **kwargs)
    
    def shuffle(self):
        """shuffle song queue"""
        random.shuffle(self.songs)
        self.song_index = 0
    
    def add_song(self, songs):
        """Add one or multiple songs to the queue

        args:
            songs (list, str): one or more songs or youtube urls to add to the queue
        """
        songs = tools.ensure_list(songs)
        out = []
        for song in songs:
            out.append(tools.get_song_obj(song))
        if self.shuffle_state:
            random.shuffle(out)
        self.songs += out
    
    def add_playlist(self, playlists):
        """Checks type of playlist and hands it off to the right function,
        which will then add it's songs to the queue

        args:
            playlists (str, list): one or more urls to youtube playlists or paths to local playlist files
        """
        playlists = tools.ensure_list(playlists)
        for playlist in playlists:
            playlist = str(playlist)
            if tools.is_url(playlist):
                if tools.is_youtube_url(playlist):
                    self.add_youtube_playlist(playlist)
                else:
                    self.add_local_playlist(playlist)
            else:
                self.add_youtube_playlist(tools.url_from_playlist_search(playlist))
    
    def add_youtube_playlist(self, url):
        """Adds songs from a youtube playlist to the queue

        args:
            url (str): url to youtube playlist
        """
        songs = tools.songs_from_yt_playlist(url)
        if self.shuffle_state:
            random.shuffle(songs)
        self.songs += songs
    
    def add_local_playlist(self, file):
        """Adds songs from a local playlist file to the queue.
        playlist files are a list of youtube URLs or search words, with each entry on its own line

        args:
            file (str): path to local playlist file
        """
        with open(file, 'r') as f:
            lines = f.read().split('\n')
        songs = []
        for line in lines:
            if line[0] != '#' and len(line) > 1:
                songs.append(line)
        if self.shuffle_state:
            random.shuffle(songs)
        self.add_song(songs)
    
    def is_vlc_alive(self):
        """compatibility alias for is_alive"""
        return self.is_alive()
    
    def debug(self, *args):
        """Print debug-level log"""
        if self.debuglogs:
            print('[DBUG] ', *args, sep='')
    
    def wait_on_song_end(self):
        """waits until the current song has ended playing"""
        while self.is_alive():
            time.sleep(0.05)
    
    def wait_on_song_load(self):
        """waits until the current song is loaded"""
        while not self.is_alive():
            time.sleep(0.05)
    
    def update_rich_presence(self):
        """Update discord rich presence if `self.rich_presence == True`"""
        if self.rich_presence:
            try:
                self.rich_presence_client.update(details=self.current_song.title,
                                                 state=f'by ' + self.current_song.artist, large_image="logo-2",
                                                 small_image='clock',
                                                 small_text=f'{self.get_current_time()}/'
                                                            f'{self.get_total_time()}')
                                                #  large_text=';)')
            except Exception as e:
                print(e)
                self.rich_presence = False
    
    def get_total_time(self):
        """
        Returns a nicely formatted string of the total duration of the current song
        """
        return tools.secs_to_string(self.current_song.length)
    
    def get_current_time(self):
        """
        Returns a nicely formatted string of the current timestamp of the playing song
        """
        return tools.secs_to_string(tools.get_position(self.vlc_player))


def get_args():
    """Parses argparse arguments from commandline and returns the namespace object mapped to the correct .play_all()
    and Player() kwargs """
    parser = argparse.ArgumentParser(
        description="Play youtube audio from the commandline / écouter l'audio des vidéos youtube sur la ligne de "
                    "commande")
    parser.add_argument('--version', help='Prints version / version imprimé', action='store_true')
    parser.add_argument('-v', '--volume',
                        help='Starts with <value> volume / le programme démarrer avec un niveau de volume <value>',
                        action='store', type=int, default=100)
    parser.add_argument('-l', '--loop', help='Enable queue looping', action='store_true')
    parser.add_argument('-s', '--shuffle', help='Enable queue shuffling', action='store_true')
    parser.add_argument('-p', '--playlist',
                        help="Add local or youtube playlist / utiliser une playlist à partir d'un fichier",
                        action='append', type=str, dest='playlists')
    
    parser.add_argument('--nopresence', dest='rich_presence',
                        help='Disable discord rich presence', action='store_false')
    parser.add_argument('--muted', dest='muted',
                        help='Start player muted', action='store_true')
    parser.add_argument('--noinput', help='Disable player controls / désactiver les contrôles',
                        action='store_false', dest='enable_input')
    parser.add_argument('--legacy', dest='legacystreams', action='store_true',
                        help='Forces the use legacy streams, use this if some songs dont load')
    parser.add_argument('--verbose', help='Enable debug logging', action='store_true', dest='debuglogs')
    parser.add_argument('--vlclogs', help='Enable vlc logging', action='store_true')
    parser.add_argument('songs',
                        help='Name or url of the song(s) you want to play / nom de la chanson à jouer tu veux jouer',
                        action='store', type=str, nargs=argparse.REMAINDER)
    # parser.add_argument('--fr', help='enable french output / activer mode français', action='store_true')
    # french isn't a thing in this version yet, need to have a proper translation system
    return parser.parse_args()


def commandline():
    """Handles arguments if run from the commandline"""
    name_args = get_args()
    dict_args = vars(name_args)
    
    # version and loop are not kwargs for the player object, so gotta get them out before passing it along
    if dict_args['version']:
        print('0.5b10')
        return
    else:
        del dict_args['version']
    loop = dict_args['loop']
    del dict_args['loop']
    try:
        player = Player(**dict_args)
        player.play_all(halting=True, loop=loop)  # halting = True so it runs until the queue ends
    except OSError as e:
        print(e)
        print('Try updating youtube-dl with "pip3 install -U youtube-dl"')
    except Exception as e:
        raise e


if __name__ == '__main__':
    commandline()
