"""
Holds utility functions adn Classes for authentification via cognito and interaction with AWS.
"""
import datetime
import os
import time
import json
import logging
from sys import exit
from typing import Dict, Optional
from threading import Thread

import boto3

from paraloq.installer.exceptions import SessionError


class ConnThread(Thread):
    def __init__(self):
        super(ConnThread, self).__init__()
        self.connect = True

    def run(self):
        while self.connect:
            time.sleep(60 * 55)
            Session.refresh()


class MetaSession(type):
    @property
    def _SESSION_(cls) -> Dict[str, str]:
        """
        Make the login appear when the _SESSION_ is called for the first time.
        """
        if os.environ.get("LOCAL_ACCOUNT", False):
            return None
        cls.connect()
        return cls._SESSION_

    @property
    def _CONFIG_(cls) -> Dict[str, str]:
        """
        Make the login appear when the _CONFIG_ is called for the first time.
        """
        if os.environ.get("LOCAL_ACCOUNT", False):
            return None
        cls.connect()
        return cls._CONFIG_


class Session(metaclass=MetaSession):
    """
    The Session handles your credentials to access your Cloud Infrastructure and Data that is
     stored in the Cloud.
    """

    _BEARER_: Optional[str] = None
    """The bearer token to sign API requests with."""
    _ACCESS_AWS_: bool = True
    """Indicates if the client should use :py:class:`alpha.core.stubs.StubMethod` or try to call
    boto3 directly"""
    __SESSION_THREAD__: Thread = None

    @classmethod
    def connected(cls) -> bool:
        return cls._CONFIG_ is not None

    @classmethod
    def connect(cls, stay_connected: int = True):
        from paraloq.installer.prompt import ParaloqConfig

        pq_config = ParaloqConfig.from_disc()

        cls._connect(pq_config=pq_config)

        if stay_connected:
            cls.__SESSION_THREAD__ = ConnThread()
            cls.__SESSION_THREAD__.start()
            logging.info(
                "Automatic Session refreshment is activated! Your Session will not time out. "
                "Do not forget to disconnect by calling Session.diconnect() when you are "
                "done!"
            )

    @classmethod
    def _connect(cls, pq_config: "ParaloqConfig"):
        from paraloq.installer.login import LoginServer
        import requests
        import webbrowser
        from urllib.parse import parse_qs

        # Open login page
        logging.info(
            f"We tried to open {pq_config.login_url} in your default browser. \n"
            f"Please head over and log in."
        )
        webbrowser.open(pq_config.login_url)
        # Listen for authorization code
        server = LoginServer()
        auth_code = server.serve_once()
        # Complete code authorization grant
        response = requests.post(
            url=f"https://{pq_config.login_url.host}" + "/oauth2/token",
            data={
                "Content-Type": "application/x-www-form-urlencoded",
                "grant_type": "authorization_code",
                "client_id": pq_config.client_id,
                "code": auth_code,
                "redirect_uri": parse_qs(pq_config.login_url.query).get("redirect_uri")[
                    0
                ],
            },
        )
        # Extract tokens
        tokens = json.loads(response.text)
        # Save authentication for this session
        MetaSession._SESSION_ = {
            "expires_at": datetime.datetime.now()
            + datetime.timedelta(seconds=tokens["expires_in"]),
            "refresh_token": tokens["refresh_token"],
        }
        MetaSession._CONFIG_ = pq_config
        cls._BEARER_ = tokens["id_token"]
        cls._ACCESS_AWS_ = False

        print(f"Credentials accepted - Welcome!")
        print(
            r"""                                                    __
                ____     ____ _   _____   ____ _   / /  ____     ____ _
               / __ \   / __ `/  / ___/  / __ `/  / /  / __ \   / __ `/
              / /_/ /  / /_/ /  / /     / /_/ /  / /  / /_/ /  / /_/ /
             / .___/   \__,_/  /_/      \__,_/  /_/   \____/   \__, /
            /_/                                                  /_/
            """
        )

    @classmethod
    def refresh(cls):
        """
        Refresh the current Session to be valid for another hour. There must be an existing
        valid Session.
        """
        import requests
        import json

        if cls._SESSION_ is None:
            raise SessionError("No active session found.")
        pq_config = cls._CONFIG_

        response = requests.post(
            url=f"https://{pq_config.login_url.host}" + "/oauth2/token",
            data={
                "Content-Type": "application/x-www-form-urlencoded",
                "grant_type": "refresh_token",
                "client_id": pq_config.client_id,
                "refresh_token": cls._SESSION_["refresh_token"],
            },
        )
        tokens = json.loads(response.text)
        cls._SESSION_["expires_at"] = datetime.datetime.now() + datetime.timedelta(
            seconds=tokens["expires_in"]
        )
        cls._BEARER_ = tokens["id_token"]
        logging.info("Session successfully refreshed!")

    @classmethod
    def disconnect(cls):
        """
        Log out from all devices. If logout fails, calls sys.exit() for security reasons.
        :return:
        """
        try:
            if cls._SESSION_ is None:
                raise SessionError("No active session found.")
            # Global logout
            client = boto3.client("cognito-idp", region_name=cls._SESSION_["region"])
            client.global_sign_out(
                AccessToken=cls._SESSION_["AuthenticationResult"]["AccessToken"]
            )
            # Reset class attributes
            cls._SESSION_ = None
            cls._BEARER_ = None
            cls._CONFIG_ = None
            cls._ACCESS_AWS_ = True
            cls.__SESSION_THREAD__.connect = False
            logging.info("Disconnected successfully!")
        except:  # noqa
            exit()
