import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials


# Class for the Spotify Client
class Spotify(object):
    # Client Variables
    _client_id = None
    _client_secret = None
    _redirect_uri = None
    _spotify_client = None

    # Constructor
    def __init__(self, client_id=None, client_secret=None, redirect_uri=None):
        if client_id == None or client_secret == None:
            raise Exception("You must set client_id and client_secret")

        if redirect_uri == None:
            raise Exception("You must set a redirect_uri")

        self._client_id = client_id
        self._client_secret = client_secret
        self._redirect_uri = redirect_uri
        self._spotify_client = spotipy.Spotify(
            client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))

        if not self._spotify_client:
            raise Exception("An error occurred on the client side")


# Class for the User
class User(Spotify):
    # User Variables
    _user_token = None
    _user_client = None
    _user_id = None

    # Constructor
    def __init__(self, user_id=None, scope=None, client=None):
        self._user_id = user_id
        self._user_token = util.prompt_for_user_token(user_id, scope, client._client_id, client._client_secret,
                                                      client._redirect_uri)
        self._user_client = spotipy.Spotify(auth=self._user_token)

        if not self._user_client:
            raise Exception("An error occurred granting access")

    # Returns a List of the Users Liked Songs
    def get_user_saved_tracks(self):
        i, items, results = 0, ['1'], []
        while (len(items) > 0):
            items = self._user_client.current_user_saved_tracks(50, 50 * i)['items']
            if (len(items) != 0):
                for item in items:
                    results.append(item['track'])

            i += 1
            if i > 10:  # FOR TESTING PURPOSES, 100 songs only
                break

        return results

    # Returns a List of the Users Songs Matching Emotion
    def get_user_emotion_tracks(self, client=None, user_tracks=None, base_emotion=None, second_emotion=""):
        emotion_tracks = []
        if base_emotion == "sadness" or base_emotion == "awful" or second_emotion == "sadness" or second_emotion == "awful":
            # float valence;                        //Metric of the positiveness of the track ( < 0.5 )
            # float energy;                         //Metric of the energy of the track ( < 0.5 )
            # bool mode;                            //Whether the track is major or minor (1 = minor?)
            # float instrumentalness;               //Metric of the track being instrumental ( > 0.5 )
            # float acousticness;                   //Metric of the track being acoustic ( > 0.5 )
            # float tempo;                          //The tempo of the track in ( < 120 BPM )
            for track in user_tracks:
                af = client._spotify_client.audio_features(track['id'])[0]
                if af['valence'] < 0.5 or af['energy'] < 0.5 or af['instrumentalness'] > 0.5 or af[
                    'acousticness'] > 0.5 or af['tempo'] < 120:
                    emotion_tracks.append(track)



        elif base_emotion == "bad" or base_emotion == "anger":
            # float loudness;                       //Metric of the loudness of the track ( > 0. 5 )
            # float energy;                         //Metric of the energy of the track ( > 0.5 )
            # float tempo;                          //The tempo of the track ( > 120 BPM )
            # float speechiness;                    //Metric of the track containing human voice ( > 0.5 )
            for track in user_tracks:
                af = client._spotify_client.audio_features(track['id'])[0]
                if af['loudness'] > 0.5 or af['energy'] > 0.5 or af['tempo'] > 120 or af[
                    'speechiness'] > 0.5:
                    emotion_tracks.append(track)

        elif base_emotion == "okay" or base_emotion == "fear":
            # float danceability;                   //Metric of the track being danceable ( < 0.5 )
            # float instrumentalness;               //Metric of the track being instrumental ( > 0.5 )
            # float loudness;                       //Metric of the loudness of the track ( > 0.5 )
            # float valence;                        //Metric of the positiveness of the track ( < 0.5 )
            # float energy;                         //Metric of the energy of the track ( <= 0.5)
            for track in user_tracks:
                af = client._spotify_client.audio_features(track['id'])[0]
                if af['danceability'] < 0.5 or af['instrumentalness'] > 0.5 or af['loudness'] > 0.5 or af[
                    'valence'] < 0.5 or af['energy'] <= 0.5:
                    emotion_tracks.append(track)

        elif base_emotion == "happy" or base_emotion == "joy":
            # float valence;                        //Metric of the positiveness of the track ( > 0.5 )
            # float danceability;                   //Metric of the track being danceable ( > 0.5 )
            # float energy;                         //Metric of the energy of the track ( > 0.5 )
            # float tempo;                          //The tempo of the track ( > 100 BPM )
            # float loudness;                       //Metric of the loudness of the track ( > 0.5)
            for track in user_tracks:
                af = client._spotify_client.audio_features(track['id'])[0]
                if af['valence'] > 0.5 or af['danceability'] > 0.5 or af['energy'] > 0.5 or af[
                    'tempo'] > 100 or af['loudness'] > 0.5:
                    emotion_tracks.append(track)

        elif base_emotion == "excited" or base_emotion == "surprise":
            # float energy;                         //Metric of the energy of the track ( > 0.5 )
            # float loudness;                       //Metric of the loudness of the track ( > 0.5 )
            # float tempo;                          //The tempo of the track ( > 120 BPM )
            # float danceability;                   //Metric of the track being danceable ( > 0.5 )
            for track in user_tracks:
                af = client._spotify_client.audio_features(track['id'])[0]
                if af['energy'] > 0.9 or af['loudness'] > 0.9 or af['tempo'] > 120 or af[
                    'danceability'] > 0.9:
                    emotion_tracks.append(track)

        elif base_emotion == "love":
            # float valence;                        //Metric of the positiveness of the track ( > 0.5 )
            # float tempo;                          //The tempo of the track ( < 120 BPM )
            # float instrumentalness;               //Metric of the track being instrumental ( < 0.5 )
            # bool mode;                            //Whether the track is major or minor (0 = major?)
            for track in user_tracks:
                af = client._spotify_client.audio_features(track['id'])[0]
                if af['valence'] > 0.5 or af['tempo'] < 120 or af['instrumentalness'] < 0.5 or af[
                    'mode'] == 0:
                    emotion_tracks.append(track)

        return emotion_tracks

    # Returns the ID of a Desired User Playlist
    def get_playlist_id(self, playlist_name=None):
        if playlist_name == None:
            raise Exception("You must enter a playlist name")

        playlist_id = None
        playlists = self._user_client.user_playlists(self._user_id)
        for playlist in playlists['items']:
            if playlist['name'] == playlist_name:
                playlist_id = playlist['id']

        if playlist_id == None:
            raise Exception("There is no playlist with that name")

        return playlist_id

    # Creates a New Playlist for the User
    def create_playlist(self, playlist_name=None, public=True, collaborative=False, description=""):
        if playlist_name == None:
            raise Exception("You must enter a playlist name")

        self._user_client.user_playlist_create(self._user_id, name=playlist_name, public=public,
                                               collaborative=collaborative, description=description)

    # Adds Tracks to a User's Playlist
    def add_to_playlist(self, playlist_name=None, playlist_tracks=None):
        if playlist_name == None:
            raise Exception("You must enter a playlist name")

        playlist_id = self.get_playlist_id(playlist_name=playlist_name)
        track_ids = []
        for track in playlist_tracks:
            track_ids.append(track['id'])

        self._user_client.user_playlist_add_tracks(self._user_id, playlist_id=playlist_id, tracks=track_ids)

        # for i in range(0, len(track_ids), 50):
        #     hundred_tracks = track_ids[i:i+50]
        #     self._user_client.user_playlist_add_tracks(self._user_id, playlist_id=playlist_id, tracks=hundred_tracks)


"""
    /* USER INPUT PARAMETERS */
    Values from 0 - 1
    float acousticness;                   //Metric of the track being acoustic
    float danceability;                   //Metric of the track being danceable
    float energy;                         //Metric of the energy of the track
    float instrumentalness;               //Metric of the track being instrumental
    float liveness;                       //Metric of the track sounding as a live performance
    float speechiness;                    //Metric of the track containing human voice
    float valence;                        //Metric of the positiveness of the track
    float tempo;                          //The tempo of the track in BPM as its reciprocal
    float loudness;                       //Metric of the loudness of the track
    bool mode;                            //Whether the track is major or minor
    float popularity;                     //Metric of the popularity of the track
"""
