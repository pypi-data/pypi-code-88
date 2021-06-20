"""This module contains message parsing utility functions."""
from typing import Dict, List, Optional, Tuple


def message_parser(
    data: Dict,
    success_message: str = "Operation successful.",
    fail_message: str = "Operation failed.",
) -> str:
    """Parses a message from misty2py JSON dict reply to a string.

    Args:
        data (Dict): Thr JSON Dict to parse.
        message_if_success (str, optional): Brief success-indicating message/keyword. Defaults to `"Operation successful."`.
        message_if_fail (str, optional): Brief failure-indicating message/keyword. Defaults to `"Operation failed."`.

    Returns:
        str: Brief success-or-failure-indicating sentence/eyword and detailed information in the next sentence if available.
    """
    potential_message = data.get("message")
    if data.get("status") == "Success":
        return compose_str(success_message, potential_message)
    return compose_str(
        fail_message, potential_message,
        fallback="No further details provided."
    )


def compose_str(
    main_str: str, potential_str: Optional[str], fallback: Optional[str] = None
) -> str:
    """Composes a single string from `main_str`, `potential_str` and `fallback`.

    - If `potential_str` and `fallback` are both `None`, the final string is `main_str`. 
    - If `potential_str` is a string, the final string is `main_str` followed by a space and `potential_str`. 
    - If `potential_str` is `None` and `fallback` is a string, the final string is `main_str` followed by a space and `fallback`.

    Args:
        main_str (str): The main string.
        potential_str (Optional[str]): Data that may be a string or `None`.
        fallback (Optional[str], optional): A string to attach to `main_str` if `potential_str` is not a string. `None` if nothing should be attached. Defaults to `None`.

    Returns:
        str: The final string (the composed string).
    """
    if isinstance(potential_str, str):
        return "%s %s" % (main_str, potential_str)
    if isinstance(fallback, str):
        return "%s %s" % (main_str, fallback)
    return main_str


def compose_json_reply(
    data: Dict,
    success_message: str = "Operation successful.",
    fail_message: str = "Operation failed.",
) -> Dict:
    """Enhances the JSON reply from Misty's REST API with `success_message` in case of success and with `fail_message` otherwise.

    Args:
        data (Dict): JSON dict to enhance.
        success_message (str, optional): A message/keyword to append in case of success. Defaults to `"Operation successful."`.
        fail_message (str, optional): A message/keyword to append in case of failure. Defaults to `"Operation failed."`.

    Returns:
        Dict: The enhanced JSON dictionary.
    """
    potential_message = data.get("message")
    status = data.get("status")
    if status == "Success":
        message = compose_str(success_message, potential_message)
    else:
        message = compose_str(
            fail_message, potential_message,
            fallback="No further details provided."
        )
    return {"status": status, "message": message}


def success_parser_message(message: Dict) -> Tuple[Dict, bool]:
    """Parses the successfulness of an action from the server's JSON reply.

    Args:
        message (Dict): The JSON dict to parse.

    Returns:
        Tuple[Dict, bool]: A tuple of a dictionary with keys `"successful"`
        (bool) and `"message"` (Dict) and a boolean indicating successfulness.
    """
    st = message.pop("status", None)
    if st == "Success":
        return {"successful": True, "message": message}, True
    return {"successful": False, "message": message}, False


def success_parser_from_dicts(**messages) -> Dict:
    """Parses the successfulness of a dictionary of actions, where the keyword is the action name and the value is the json reply from the server. `overall_success` is only true if all actions were successful.

    Returns:
        Dict: The dictionary of the keys `"overall_success"` (bool) and action names that contain the success-parsed message (a dict with keys `"successful"` (bool) and `"message"` (dict)).
    """
    status_dict = {}
    overall_success = True
    for name, message in messages.items():
        new_message, success = success_parser_message(message)
        status_dict[name] = new_message
        if not success:
            overall_success = False
    status_dict["overall_success"] = overall_success
    return status_dict


def success_parser_from_list(message_list: List[Dict]) -> Dict:
    """Parses the successfulness of a list of dictionaries of an action, where the keyword is the action name and the value is the JSON reply from the server. Overall success is only true if all actions were successful.

    Args:
        message_list (List[Dict]): The list of dictionaries of an action, where the keyword is the action name and the value is the JSON reply from the server.

    Returns:
        Dict: The dictionary of the keys `"overall_success"` (bool) and `"actions"` whose value is a list of dictionaries with names that contain the success-parsed message (a dict with keys `"successful"` (bool) and `"message"` (dict)).
    """
    status_dict = {"actions": []}
    overall_success = True
    for event in message_list:
        for name, message in event.items():
            new_message, success = success_parser_message(message)
        status_dict["actions"].append((name, new_message))
        if not success:
            overall_success = False
    status_dict["overall_success"] = overall_success
    return status_dict
