import requests.exceptions
import spotipy
from Spotipy import Spotify, User
from UserSummary import Person


# Spotify Web API authorization

def Authorization():
    # Moodipy Client Environment Variables
    client_id = "17c9e6c9abe14de9bbfbb10c7d89afa4"
    client_secret = "1a8fdfd3501a4c2da9e6bd3fe300b7c8"
    redirect_uri = "http://localhost:8080"

    # User Environent Variables
    #user_id = "igjsqvqpbxeuhoxlgvplj68qf"
    #user_id = "xxqueendianaxx"
    user_id = Person.userID

    scope = "user-library-read  playlist-modify-public"

    # INTERFACE
    try:
        client = Spotify(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
        user = User(user_id=user_id, scope=scope, client=client)
        #user.create_playlist("test", True, False, "tesing this broooo")
        return user, client
    except (spotipy.exceptions.SpotifyException, requests.exceptions.HTTPError,spotipy.oauth2.SpotifyOauthError):
        return None

#if __name__=="__main__":
  #  print(Authorization())