"""This module defines Misty2pyResponse class to handle responses from Misty2py when it communicates with Misty's REST API or Misty's WebSocket API.
"""

from typing import Any, Dict, List, Optional
from enum import Enum


class Misty2pyErrorType(Enum):
    """This class represents the types of errors originating in the Misty2py.
    """
    DATA_FORMAT = "incorrect data format"
    """Represents an error originating from the user supplying incorrect data format to any method, class or function."""
    DATA_SHORTCUT = "unsupported data shortcut"
    """Represents an error originating from the user supplying an unsupported data shortcut to any method, class or function."""
    UNKNOWN = "unknown"
    """Represents an error originating from the user supplying an unsupported command string to methods or functions that take commands as strings."""
    COMMAND = "unsupported command"
    """Represents an error originating from the user supplying unsupported HTTP request method or an unsupported command type to methods, classes or functions handling HTTP requests to Misty's REST API."""
    REQUEST_METHOD = "unsupported request method"
    """Represents an error whose origin is not known to the application."""
    MISSING = "missing argument or parameter"
    """Represents an error originating from missing arguments or parameters."""
    NONE = None
    """Represents that no error is present."""

    def __str__(self) -> str:
        """Parses an error type into a string."""
        return str(self.value)


class Misty2pyResponse:
    """A class representing a response from any function or method of Misty2py that communicates with Misty's REST API or Misty's WebSocket API.

    Attributes:
        misty2py_status (bool): Indicates whether any error originating in Misty2py was encountered.
        rest_response (Any): The response from Misty's REST API. `None` if this response does not contain a sub-response from Misty's REST API.
        ws_response (Optional[Dict]): The response from Misty's WebSocket API. `None` if this response does not contain a sub-response from Misty's WebSocket API.
        error_type (Misty2pyErrorType): The type of Misty2py error encountered. `Misty2pyErrorType.NONE` if no error in Misty2py was encountered.
        error_msg (Optional[str]): The error message for a Misty2py error. `None` if no error in Misty2py was encountered.
    """

    def __init__(
        self,
        misty2py_status: bool,
        rest_response: Any = None,
        ws_response: Optional[Dict] = None,
        error_type: Misty2pyErrorType = Misty2pyErrorType.NONE,
        error_msg: Optional[str] = None,
    ) -> None:
        """Creates a Misty2pyResponse object for a specific action.

        Args:
            misty2py_status (bool): Indicates whether any error originating in Misty2py was encountered.
            rest_response (Any, optional): The response from Misty's REST API. `None` if this response does not contain a sub-response from Misty's REST API. Defaults to `None`.
            ws_response (Optional[Dict], optional): The response from Misty's WebSocket API. `None` if this response does not contain a sub-response from Misty's WebSocket API. Defaults to `None`.
            error_type (Misty2pyErrorType, optional): The type of Misty2py error encountered. `Misty2pyErrorType.NONE` if no error in Misty2py was encountered. Defaults to `Misty2pyErrorType.NONE`.
            error_msg (Optional[str], optional): The error message for a Misty2py error. `None` if no error in Misty2py was encountered. Defaults to `None`.
        """
        self.misty2py_status = misty2py_status
        self.rest_response = rest_response
        self.error_type = error_type
        self.error_msg = error_msg
        self.ws_response = ws_response

    def parse_to_dict(self) -> Dict:
        """Parses this Misty2py object into a dictionary.

        Returns:
            Dict: A dictionary with keys `"misty2py_response"` (Dict) for the response of the Misty2py package, `"overall_success"` (bool) and optional keys `"rest_response"` (Dict) and `"ws_response"` (Dict).
        """
        dct = {
            "misty2py_response": self.get_misty2py_response(),
            "overall_success": self._is_successful(),
        }

        if self.rest_response is not None:
            dct["rest_response"] = self.get_rest_response()

        if self.ws_response is not None:
            dct["ws_response"] = self.ws_response

        return dct

    def get_rest_response(self) -> Dict:
        """Returns the REST API sub-response of this Misty2pyResponse with keys `"success"` and optional keys `"message"` or `"content"`."""
        if isinstance(self.rest_response, Dict):
            dct = self.rest_response.copy()
            st = dct.pop("status", None)
            if st == "Success":
                dct["success"] = True
            else:
                dct["success"] = False
            return dct

        return self.rest_response

    def get_ws_response(self) -> Dict:
        """Returns the WebSocket API sub-response of this Misty2pyResponse."""
        return self.ws_response

    def get_misty2py_response(self) -> Dict:
        """Parses the Misty2py part of this Misty2pyResponse to a dictionary containing keys `"success"` and, if the value of `"success"` is `False`, the `"error_msg"` (str) and `"error_type"` (str)."""
        success = self.misty2py_status
        dct = {"success": success}

        if not success:
            dct["error_msg"] = self.error_msg
            dct["error_type"] = str(self.error_type)

        return dct

    def _is_successful(self) -> bool:
        """Returns `True` if every sub-response present in this Misty2pyResponse is successful. Returns `False` otherwise."""
        success = self.misty2py_status
        if self.ws_response is not None:
            success = success and self.ws_response.get("success")
        if self.rest_response is not None:
            success = success and self.rest_response.get("status") == "Success"
        return success


def unknown_error(e: Exception) -> Misty2pyResponse:
    """Generates a Misty2pyResponse for an error `e` originating in unknown circumstances."""
    return Misty2pyResponse(False, error_msg=e, error_type=Misty2pyErrorType.UNKNOWN)


def success_of_action_list(msg_list: List[Dict[str, Dict]]) -> Dict:
    """Parses the overall success of a list of dictionaries where the keyw is an action name and the value is a dictionarised Misty2pyResponse. `overall_success` is only true if all actions were successful.

    Args:
        msg_list (List[Dict[str, Dict]]): The list of dictionaries where the keyword is an action name and the value is a Misty2pyResponse.

    Returns:
        Dict: The dictionary of the keys `"overall_success"` (bool) and `"actions"` whose value is a list of dictionaries with keys being action names and values being Misty2pyResponses.

    """
    dct = {"actions": []}
    success = True
    for event in msg_list:
        for name, message in event.items():
            if not message.get("overall_success"):
                success = False
        dct["actions"].append((name, message))
    dct["overall_success"] = success
    return dct


def success_of_action_dict(**messages) -> Dict:
    """Parses the overall success of a dictionary of actions, where the key is an action name and the value is a dictionarised Misty2pyResponse. `overall_success` is only true if all actions were successful.

    Returns:
        Dict: The dictionary of the keys `"overall_success"` (bool) and action names that contain the dictionarised Misty2pyResponses.
    """
    status_dict = {}
    overall_success = True
    for name, message in messages.items():
        status_dict[name] = message
        if not message.get("overall_success"):
            overall_success = False
    status_dict["overall_success"] = overall_success
    return status_dict


def compose_custom_response(
    resp: Dict,
    success_message: str = "Operation successful.",
    fail_message: str = "Operation failed.",
) -> Dict:
    """Enhances a dictionarised Misty2pyResponse with `success_message` in case of success and with `fail_message` otherwise.

    Args:
        resp (Dict): The dictionarised Misty2pyResponse.
        success_message (str, optional): A message/keyword to append in case of success. Defaults to `"Operation successful."`.
        fail_message (str, optional): A message/keyword to append in case of failure. Defaults to `"Operation failed."`.

    Returns:
        Dict: The enhanced version.
    """

    def compose_str(
        main_str: str, potential_str: Optional[str], fallback: Optional[str] = None
    ) -> str:
        """Composes a single string from main_str, potential_str and fallback.
        - If `potential_str` and `fallback` are both `None`, the final string is `main_str`.
        - If `potential_str` is a string, the final string is `main_str` followed by a space and `potential_str`.
        - If `potential_str` is `None` and `fallback` is a string, the final string is `main_str` followed by a space and `fallback`.
        """
        if isinstance(potential_str, str):
            return "%s %s" % (main_str, potential_str)
        if isinstance(fallback, str):
            return "%s %s" % (main_str, fallback)
        return main_str

    success = resp.get("overall_success")
    dct = {"overall_success": success}
    potential_resp = resp.get("rest_response")

    if potential_resp:
        potential_message = potential_resp.get("message")

        if success:
            message = compose_str(success_message, potential_message)
        else:
            message = compose_str(
                fail_message, potential_message, fallback="No further details provided."
            )
        dct["rest_response"] = {
            "success": potential_resp.get("success"),
            "message": message,
        }

    return dct
