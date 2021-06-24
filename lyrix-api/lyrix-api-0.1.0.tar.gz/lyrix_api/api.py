from typing import List

import requests
from requests import Response

from .meta import Song


class Api:
    @staticmethod
    def _get(user, endpoint: str, auth: bool = False) -> Response:
        """
        Helper get function
        :param endpoint: A url endpoint api
        :param auth: should provide authorization token?
        :return: response
        :rtype: dict
        """

        headers = {"Content-Type": "application/json}"}
        if auth:
            headers["Authorization"] = f"Bearer {user.token}"
        req = requests.get(f"https://{user.homeserver}{endpoint}", headers=headers)
        return req

    @staticmethod
    def _post(user, endpoint: str, data: dict, auth: bool = False) -> Response:
        """
        Helper post function
        :param endpoint: A url endpoint api
        :param auth: should provide authorization token?
        :return: response
        :rtype: dict
        """

        headers = {"Content-Type": "application/json}"}
        if auth:
            headers["Authorization"] = f"Bearer {user.token}"
        req = requests.post(
            f"https://{user.homeserver}{endpoint}", headers=headers, json=data
        )
        return req

    @staticmethod
    def get_current_local_listening_song(user) -> Song:
        """
        GET /user/player/local/current_song
        """
        data = Api._get(user, "/user/player/local/current_song", auth=True).json()
        return Song(**data)

    @staticmethod
    def get_current_local_listening_song_similar(user) -> List[Song]:
        """
        GET /user/player/local/current_song/similar
        """
        data = Api._get(user, "/user/player/local/current_song/similar").json()
        songs = list()
        for song in data:
            songs.append(Song(**song))
        return songs

    @staticmethod
    def send_spotify_token(user, spotify_token: str) -> bool:
        """
        POST /user/player/spotify/token
        """
        data = Api._post(
            user,
            "/user/player/spotify/token",
            auth=True,
            data={"spotify_token": spotify_token},
        )
        return 200 <= data.status_code <= 210

    @staticmethod
    def generate_lastfm_token(user) -> str:
        """
        GET /connect/lastfm
        """
        data = Api._get(
            user,
            "/connect/lastfm",
            auth=True,
        ).json()
        return data["redirect"]

    @staticmethod
    def get_spotify_token(user) -> str:
        """
        GET /user/player/spotify/token

        Returns the saved spotify token
        """
        data = Api._get(user, "/user/player/spotify/token", auth=True).json()
        return data["token"]

    @staticmethod
    def login(username: str, password: str, homeserver: str) -> str:
        """
        POST /login
        """
        headers = {"Content-Type": "application/json}"}

        req = requests.post(
            f"https://{homeserver}/login",
            headers=headers,
            json={"username": username, "password": password},
        )

        return req.json()["token"]

    @staticmethod
    def register(
        username: str, password: str, homeserver: str, telegram_id: int
    ) -> int:
        """
        POST /register
        """
        headers = {"Content-Type": "application/json}"}

        req = requests.post(
            f"https://{homeserver}/register",
            headers=headers,
            json={
                "username": username,
                "password": password,
                "telegram_id": telegram_id,
            },
        )

        return req.status_code


