"""This module's function is to send information requests via the information keywords matching to Misty's API endpoints, sending information requests and matching data shortcuts.
"""
import json
from os import path
from typing import Dict

import requests

from misty2py.response import *

this_directory = path.abspath(path.dirname(__file__))
INFOS_JSON = str(path.join(this_directory, "allowed_infos.json"))


class Get:
    """A class representing the GET url request method.

    Attributes:
        ip (str): The IP address for the URL where the requests are sent.
        protocol (str): The protocol for the URL where the requests are sent.
        allowed_infos (dict): The dictionary of information keywords matching to the Misty's API endpoints.
    """

    def __init__(self, ip: str, protocol: str, custom_allowed_infos: Dict = {}) -> None:
        """Initialises a Get object.

        Args:
            ip (str): The IP address for the URL where the requests are sent.
            protocol (str): The protocol for the URL where the requests are sent.
            custom_allowed_infos (Dict, optional): The dictionary of custom information keywords. Defaults to `{}`.
        """

        self.ip = ip
        self.protocol = protocol

        allowed_infos = custom_allowed_infos
        f = open(INFOS_JSON)
        allowed_infos.update(json.loads(f.read()))
        f.close()

        self.allowed_infos = allowed_infos

    def get_info(self, endpoint: str, params: Dict) -> Misty2pyResponse:
        """Sends a GET request.

        Args:
            endpoint (str): The API endpoint to which the request is sent.

        Returns:
            Misty2pyResponse: A Misty2pyResponse object with Misty2py sub-response and Misty REST API sub-response.
        """

        r = requests.get(
            "%s://%s/%s" % (self.protocol, self.ip, endpoint), params=params
        )
        try:
            return Misty2pyResponse(True, rest_response=r.json())

        except Exception as e:
            return Misty2pyResponse(
                False,
                rest_response=r.content,
                error_msg=e,
                error_type=Misty2pyErrorType.UNKNOWN,
            )


class Info(Get):
    """A class representing an information request from Misty.
    A subclass of Get()."""

    def get_info(self, info_name: str, params: Dict = {}) -> Misty2pyResponse:
        """Sends an information request to Misty.

        Args:
            info_name (str): The information keyword specifying which information is requested.
            params (Dict): dict of parameter name and parameter value. Defaults to `{}`.

        Returns:
            Misty2pyResponse: A Misty2pyResponse object with Misty2py sub-response and Misty REST API sub-response.
        """

        if info_name not in self.allowed_infos.keys():
            return Misty2pyResponse(
                False,
                error_msg="Command `%s` not supported." % info_name,
                error_type=Misty2pyErrorType.COMMAND,
            )

        endpoint = self.allowed_infos[info_name]

        try:
            return super().get_info(endpoint, params)

        except Exception as e:
            return unknown_error(e)
