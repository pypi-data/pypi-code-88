#  sensoria_io_client.py
#  Project: sensorialytics
#  Copyright (c) 2021 Sensoria Health Inc.
#  All rights reserved

import getpass
import logging

import requests
from requests_oauthlib import OAuth2

__all__ = ['SensoriaIoClient', 'TokenRetrievingFailed']

N_MAX_AUTH_TRIALS = 5
TOKEN_URL = 'https://auth.sensoriafitness.com/oauth20/token/'
TOKEN_HEADERS = {
    'Host': 'auth.sensoriafitness.com',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'application/x-www-form-urlencoded, application/json',
    'Authorization': 'Basic '
                     'NjM1MjE3NDE5NzAwN'
                     'jA5ODc1OjQ4ZWIxY2'
                     'E2OTkyODQ1ODU5M2J'
                     'mYjc1NTEyYWM4ZmMx'
}


class SensoriaIoClient:
    __token = None

    @staticmethod
    def token() -> OAuth2:
        if not SensoriaIoClient.__has_token():
            SensoriaIoClient.__authenticate()

        return SensoriaIoClient.__token

    @staticmethod
    def __has_token() -> bool:
        return SensoriaIoClient.__token is not None

    @staticmethod
    def __authenticate():
        n_trials = 0

        while n_trials < N_MAX_AUTH_TRIALS and \
                not SensoriaIoClient.__has_token():
            n_trials += 1

            username = input('username: ')
            password = getpass.getpass('password: ')

            try:
                SensoriaIoClient.__token = SensoriaIoClient.__get_token(
                    username=username,
                    password=password
                )
            except TokenRetrievingFailed as e:
                logging.error(f'{e}. {N_MAX_AUTH_TRIALS - n_trials} '
                              f'attempts remaining')

    @staticmethod
    def __get_token(username: str, password: str) -> OAuth2:
        response = SensoriaIoClient.__get_token_response(password, username)

        if response.reason == 'OK':
            access_token = response.json()['access_token']

            return OAuth2(token={'access_token': access_token})
        else:
            raise TokenRetrievingFailed(f'Token retrieving failed. '
                                        f'Reason: {response.reason}')

    @staticmethod
    def __get_token_response(password, username) -> requests.Response:
        user, domain = username.split('@')
        body = (f'grant_type=password&username={user}%40{domain}&'
                f'password={password}&scope=sessions.read%20sessions.write%20'
                f'users.read%20users.write%20workspaces.read%20'
                f'workspaces.write%20shoes.read%20shoes.write%20shoes.delete%20'
                f'firmware.read%20settings.read',)[0]

        token_response = requests.post(
            url=TOKEN_URL,
            headers=TOKEN_HEADERS,
            data=body.encode('utf-8')
        )

        return token_response


class TokenRetrievingFailed(Exception):
    def __init__(self, message: str):
        super().__init__(message)
