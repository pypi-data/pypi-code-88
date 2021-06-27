"""The module contains the class Misty which represents a Misty II robot.
"""
from misty2py.action import *
from misty2py.information import *
from misty2py.misty_event import MistyEventHandler
from misty2py.response import *


class Misty:
    """A class representing a Misty robot.

    Attributes:
        ip (str): The IP address of this Misty robot.
        infos (Info): The object of Info class that belongs to this Misty.
        actions (Action): The object of Action class that belongs to this Misty.
        events (dict): A dictionary of active event subscriptions (keys being the event name, values the MistyEvent() object).
    """

    def __init__(
        self,
        ip: str,
        custom_info: Dict = {},
        custom_actions: Dict = {},
        custom_data: Dict = {},
        rest_protocol: str = "http",
        websocket_protocol: str = "ws",
        websocket_endpoint: str = "pubsub",
    ) -> None:
        """Initialises an instance of a Misty class representing a Misty robot.

        Args:
            ip (str): The IP address of a Misty robot.
            custom_info (Dict, optional): Custom information keywords in the form of dictionary with key being the keyword and value being the API endpoint that allows a `GET` request method. Defaults to {}.
            custom_actions (Dict, optional): Custom actions keywords in the form of dictionary with key being the keyword and value being a dictionary of the endpoint (key `"endpoint"`) and the method (key `"method"`) whose value is not `GET`. Defaults to {}.
            custom_data (Dict, optional): Custom data shortcuts in the form of dictionary with keys being the shortcuts and values being the json data in the form of a dictionary. Defaults to {}.
            rest_protocol (str, optional): The protocol to use when communicating with Misty's REST API. Defaults to "http".
            websocket_protocol (str, optional): The protocol to use when communicating with Misty's WebSocket API. Defaults to "ws".
            websocket_endpoint (str, optional): Misty's WebSocket API endpoint. Defaults to "pubsub".
        """
        self.ip = ip
        self.infos = Info(ip, rest_protocol, custom_allowed_infos=custom_info)
        self.actions = Action(
            ip,
            rest_protocol,
            custom_allowed_actions=custom_actions,
            custom_allowed_data=custom_data,
        )
        self.event_handler = MistyEventHandler(
            ip, websocket_protocol, websocket_endpoint
        )

    def __str__(self) -> str:
        """Parses the Misty object into a string.

        Returns:
            str: A string identifiyng the Misty object.
        """

        return "A Misty II robot with IP address %s" % self.ip

    def perform_action(self, action_name: str, data: Dict = {}) -> Misty2pyResponse:
        """Sends a request to perform an action to Misty's REST API.

        Args:
            action_name (str): The keyword specifying the action to perform.
            data (Dict, optional): The data to send in the request body in the form of a data shortcut or a json dictionary. Defaults to `{}`.

        Returns:
            Misty2pyResponse: A Misty2pyResponse object with Misty2py sub-response and Misty REST API sub-response.
        """

        return self.actions.action_handler(action_name, data)

    def get_info(self, info_name: str, params: Dict = {}) -> Misty2pyResponse:
        """Sends a request to obtain information from Misty's REST API.

        Args:
            info_name (str): The information keyword specifying which information to retrieve.
            params (Dict): A dictionary of parameter names and parameter values. Defaults to `{}`.

        Returns:
            Misty2pyResponse: A Misty2pyResponse object with Misty2py sub-response and Misty REST API sub-response.
        """

        return self.infos.get_info(info_name, params)

    def event(self, action: str, **kwargs) -> Misty2pyResponse:
        """Handles event-related actions by sending messeges to Misty's WebSocket API and receiving messages from it.

        Supports following actions:

        - **event subscripton** - requires an action keyword `"subscribe"` and an argument `type` (str) which is the name of the event type to subscribe to. Optional arguments are:
            - `name` (str) for a custom, unique event name.
            - `return_property` (str) for the property to return from Misty's WebSocket API. All properties are returned if `return_property` is not supplied.
            - debounce (int) for the interval at which new information is sent in ms. Defaults to `250`.
            - len_data_entries (int) for the maximum number of data entries to keep (discards in FIFO style). Defaults to `10`.
            - event_emitter (Callable) for an event emitter function which emits an event upon message recieval. Defaults to `None`.
        - **obtaining the data from an event** - requires an action keyword `"get_data"` and an argument `name` (str) specifying the event name.
        - **obtaining the log from an event** - requires an action keyword `"get_log"` and an argument `name` (str) specifying the event name.
        - **unsubscribing from an event** - requires an action keyword `"unsubscribe"` and an argument `name` (str) specifying the event name.

        Args:
            action (str): The action keyword. One of `"subscribe"`, `"get_data"`, `"get_log"` and `"unsubscribe"`.

        Returns:
            Misty2pyResponse: A Misty2pyResponse object with Misty2py sub-response and Misty WebSocket API sub-response.
        """

        if action == "subscribe":
            return self.event_handler.subscribe_event(kwargs)

        if action == "get_data":
            return self.event_handler.get_event_data(kwargs)

        if action == "get_log":
            return self.event_handler.get_event_log(kwargs)

        if action == "unsubscribe":
            return self.event_handler.unsubscribe_event(kwargs)

        return Misty2pyResponse(
            False,
            error_type=Misty2pyErrorType.COMMAND,
            error_msg="The event action `%s` is not supported." % action,
        )
