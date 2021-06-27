"""This module's function is to send action requests via the action keywords matching to Misty's API endpoints, sending action requests and matching data shortcuts.
"""
import json
from os import path
from typing import Dict, Union

import requests

from misty2py.utils.colours import construct_transition_dict
from misty2py.response import *

this_directory = path.abspath(path.dirname(__file__))
ACTIONS_JSON = str(path.join(this_directory, "allowed_actions.json"))
DATA_JSON = str(path.join(this_directory, "allowed_data.json"))
VALID_HTTP_REQUEST_METHODS = ["OPTIONS", "HEAD", "POST", "PUT", "PATCH", "DELETE"]


class BodyRequest:
    """A class representing the url request methods with a body.

    Attributes:
        ip (str): The IP address for the URL where the requests are sent.
        protocol (str): The protocol for the URL where the requests are sent.
        allowed_actions (dict): The dictionary of custom action keywords matching to the Misty's REST API endpoints.
        allowed_data (dict): The dictionary of custom data shortcuts matching to the json dictionaries required by Misty's REST API.
    """

    def __init__(
        self,
        ip: str,
        protocol: str,
        custom_allowed_actions: Dict = {},
        custom_allowed_data: Dict = {},
    ) -> None:
        """Initialises a Post object.

        Args:
            ip (str): The IP address where the requests are sent.
            protocol (str): The protocol for the URL where the requests are sent.
            custom_allowed_actions (Dict, optional): The dictionary of action keywords. Defaults to `{}`.
            custom_allowed_data (Dict, optional): The dictionary of data shortcuts. Defaults to `{}`.
        """

        self.ip = ip
        self.protocol = protocol

        allowed_actions = custom_allowed_actions
        f = open(ACTIONS_JSON)
        allowed_actions.update(json.loads(f.read()))
        f.close()
        self.allowed_actions = allowed_actions

        allowed_data = custom_allowed_data
        f = open(DATA_JSON)
        allowed_data.update(json.loads(f.read()))
        f.close()
        self.allowed_data = allowed_data

    def perform_action(
        self, endpoint: str, data: Dict, request_method: str = "post"
    ) -> Misty2pyResponse:
        """Sends an action request.

        Args:
            endpoint (str): The REST API endpoint to which the request is sent.
            data (Dict): The json data supplied in the body of the request.
            request_method (str, optional): The request method. Defaults to `"post"`.

        Returns:
            Misty2pyResponse: A Misty2pyResponse object with Misty2py sub-response and Misty REST API sub-response.
        """

        if request_method.upper() not in VALID_HTTP_REQUEST_METHODS:
            return Misty2pyResponse(
                False,
                error_msg="Request method `%s` is not supported." % request_method,
                error_type=Misty2pyErrorType.REQUEST_METHOD,
            )

        response = requests.request(
            request_method.upper(),
            "%s://%s/%s" % (self.protocol, self.ip, endpoint),
            json=data,
        )

        try:
            return Misty2pyResponse(True, rest_response=response.json())

        except Exception as e:
            return Misty2pyResponse(
                False,
                rest_response=response.content,
                error_msg=e,
                error_type=Misty2pyErrorType.UNKNOWN,
            )


class Action(BodyRequest):
    """A class representing an action request for Misty."""

    def perform_action(
        self, action_name: str, data: Union[str, Dict], data_method: str
    ) -> Misty2pyResponse:
        """Sends an action request to Misty.

        Args:
            action_name (str): The action keyword specifying which action is requested.
            data (Union[str, Dict]): The data shortcut representing the data supplied in the body of the request or the json dictionary to be supplied in the body of the request.
            data_method (str): "dict" if the data is supplied as a json dictionary, "string" if the data is supplied as a data shortcut.

        Returns:
            Misty2pyResponse: A Misty2pyResponse object with Misty2py sub-response and Misty REST API sub-response.
        """

        if action_name not in self.allowed_actions.keys():
            return Misty2pyResponse(
                False,
                error_msg="Command `%s` not supported." % action_name,
                error_type=Misty2pyErrorType.COMMAND,
            )

        if data_method == "dict":
            try:
                return super().perform_action(
                    self.allowed_actions[action_name]["endpoint"],
                    data,
                    request_method=(self.allowed_actions[action_name]["method"]),
                )

            except Exception as e:
                return unknown_error(e)

        if data_method == "string" and data in self.allowed_data:
            try:
                return super().perform_action(
                    self.allowed_actions[action_name]["endpoint"],
                    self.allowed_data[data],
                    request_method=(self.allowed_actions[action_name]["method"]),
                )

            except Exception as e:
                return unknown_error(e)

        else:
            return Misty2pyResponse(
                False,
                error_type=Misty2pyErrorType.DATA_SHORTCUT,
                error_msg="Data shortcut `%s` is not supported." % data,
            )

    def action_handler(
        self, action_name: str, data: Union[Dict, str]
    ) -> Misty2pyResponse:
        """Sends Misty a request to perform an action.

        Args:
            action_name (str): The keyword specifying the action to perform.
            data (Union[Dict, str]): The data to send in the request body in the form of a data shortcut or a json dictionary.

        Returns:
            Misty2pyResponse: A Misty2pyResponse object with Misty2py sub-response and Misty REST API sub-response.
        """

        if (
            action_name == "led_trans"
            and isinstance(data, Dict)
            and len(data) >= 2
            and len(data) <= 4
        ):

            try:
                data = construct_transition_dict(data, self.allowed_data)

            except ValueError as e:
                return Misty2pyResponse(
                    False, error_msg=e, error_type=Misty2pyErrorType.DATA_FORMAT
                )

        data_method = "string"

        if isinstance(data, Dict):
            data_method = "dict"

        return self.perform_action(action_name, data, data_method)
