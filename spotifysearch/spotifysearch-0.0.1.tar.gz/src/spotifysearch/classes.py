
# THIS FILE IS RESPONSABLE FOR MANY CLASS DECLARATIONS

import json
from base64 import b64encode
from urllib.request import urlretrieve
from . import constructor
from . import calls


# AUTHENTICATION AND TOKENS
class Authenticator:

    def __init__(self, client_id:str, client_secret:str):
        self.credentials = self.encode_credentials(client_id, client_secret)
    

    def encode_credentials(self, client_id, client_secret):
        credentials = f'{client_id}:{client_secret}'
        encoded_credentials = b64encode(credentials.encode('utf-8'))
        return str(encoded_credentials, 'utf-8')


    def get_acess_token(self):
        response = calls.call_acess_token(self.credentials)
        return response.json()['access_token']


# OBJECTS
class Base:
    
    def __init__(self, data, type, name, url, id):
        self.data = data
        self.type = type
        self.name = name
        self.url = url
        self.id = id
    

    def export_json(self, path:str):
        file = open(path, 'w')
        json.dump(self.data, file, indent=4)
        file.close()


class Artist(Base):

    def __init__(self, data:dict, type:str, name:str, url:str, id:str):
        super().__init__(data, type, name, url, id)


class AlbumCover:

    def __init__(self, width, height, url):
        self.width = width
        self.height = height
        self.url = url
    

    def export_image(self, path):
        urlretrieve(self.url, path)


class Album(Base):

    def __init__(self, data:dict, type:str, name:str, url:str, id:str, 
    images:list[AlbumCover], artists:list[Artist], available_markets:list, release_date:str, total_tracks:int):
        
        super().__init__(data, type, name, url, id)
        self.images = images
        self.artists = artists
        self.available_markets = available_markets
        self.release_date = release_date
        self.total_tracks = total_tracks
        

class TrackPreview:

    def __init__(self, url):
        self.url = url
    

    def export_audio(self, path):
        urlretrieve(self.url, path)


class Track(Base):

    def __init__(self, data:dict, type:str, name:str, url:str, id:str, artists:list[Artist], 
    album:Album, preview:TrackPreview, available_markets:list, explicit:bool, 
    disc_number:int, popularity:int, duration:int):
        
        super().__init__(data, type, name, url, id)
        self.artists = artists
        self.album = album
        self.preview = preview
        self.available_markets = available_markets
        self.explicit = explicit
        self.disc_number = disc_number
        self.popularity = popularity
        self.duration = duration


    def get_formated_duration(self):
        duration = round(self.duration / 1000)
        mins = duration // 60
        secs = duration % 60
        return {'minutes':mins, 'seconds':secs}


# CLIENT
class Results(Base):

    def __init__(self, data):
        self.data = data
    

    def __get_items(self, type):
        if type == 'artist':
            try:
                data = self.data['artists']['items']
                func = constructor.artist
            except KeyError:
                return []
        elif type == 'track':
            try:
                data = self.data['tracks']['items']
                func = constructor.track
            except KeyError:
                return []
        elif type == 'album':
            try:
                data = self.data['albums']['items']
                func = constructor.album
            except KeyError:
                return []
        return [func(item) for item in data]


    def get_tracks(self) -> list[Track]:
        return self.__get_items('track')
    

    def get_artists(self) -> list[Artist]:
        return self.__get_items('artist')
    

    def get_albums(self) -> list[Album]:
        return self.__get_items('album')
