#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import logging

import requests
from coshed_model.naming import cfapp_base_url

ENVIRONMENT_ITEMS = ("prod", "dev", "qa")

DEFAULT_ENVIRONMENT = "dev"

DUMMY_API_KEY = (
    "you are superior in only one respect -- you are better at dying"
)


class SPOFRoster:
    def __init__(self, hostname, *args, **kwargs):
        self.log = logging.getLogger(__name__)
        self.env_name = kwargs.get("env_name", "prod")
        api_keys = dict()
        self._session_store = dict()
        self.roster = dict()

        if kwargs.get("api_keys"):
            api_keys = kwargs.get("api_keys")
        else:
            for key in ENVIRONMENT_ITEMS:
                env_key = "SPOF_API_KEY_{!s}".format(key.upper())
                try:
                    api_keys[key] = os.environ[env_key]
                except KeyError:
                    self.log.warning(
                        "No API Key for {!s} found in environment variable {!s}".format(
                            key, env_key
                        )
                    )

        for env_name in ENVIRONMENT_ITEMS:
            self.roster[env_name] = dict()
            if not api_keys.get(env_name):
                api_keys[env_name] = DUMMY_API_KEY

            session_data = dict(
                base_url=cfapp_base_url(hostname, env_name=env_name),
                session=requests.Session(),
            )
            headers = dict(
                accept="application/json", authorization=api_keys[env_name]
            )
            session_data["session"].headers.update(headers)
            # self.log.debug(session_data["session"].headers)
            self._session_store[env_name] = session_data

    def fetch(self, serial_number, env_name=None):
        data = list()
        if env_name is None:
            env_name = DEFAULT_ENVIRONMENT
        s_data = self._session_store[env_name]
        the_url = "{base_url}/v1/{serial_number}/NOTIFICATION_SERVICE/NotificationsForMachine".format(
            base_url=s_data["base_url"], serial_number=serial_number
        )
        try:
            req = s_data["session"].get(the_url)

            for raw in req.json():
                data.append(raw["userId"])
        except Exception:
            return None

        return data

    def __getitem__(self, key):
        if isinstance(key, tuple):
            env_name, item_key = key
        else:
            env_name = DEFAULT_ENVIRONMENT
            item_key = key

        if item_key not in self.roster[env_name]:
            value = self.fetch(item_key, env_name=env_name)
            if value is not None:
                self[key] = value

        return self.roster[env_name][item_key]

    def __setitem__(self, key, value):
        if isinstance(key, tuple):
            env_name, item_key = key
        else:
            env_name = DEFAULT_ENVIRONMENT
            item_key = key

        self.roster[env_name][item_key] = value

    def get_user_items(self, serial_number, env_name):
        assert env_name in ENVIRONMENT_ITEMS

        try:
            return self[(env_name, serial_number)]
        except KeyError:
            return []

