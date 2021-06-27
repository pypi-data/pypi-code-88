"""This module handles the communication of Misty2py with Misty's WebSocket API and the communication between different threads created within Misty2py for the WebSocket-related actions.
"""
import json
import threading
from typing import Callable, Dict, Union

import websocket

from misty2py.utils.generators import get_random_string
from misty2py.response import *


DEFAULT_DEBOUNCE = 250
DEFAULT_LEN_ENTRIES = 10


class MistyEvent:
    """A class that represents an event type subscribed to.
    Attributes:
        url (str): The URL of Misty's WebSocket API.
        data (list): The data entries obtained.
        type_str (str): The event type string as required by Misty's WebSockets API.
        event_name (str): A custom, unique event name.
        return_property (str): The property to return as requeired by Misty's WebSockets API.
        debounce (int): The interval at which new information is sent in ms.
        log (list): The logs.
        len_data_entries (int): The maximum number of data entries to keep.
        ee (Union[bool, Callable]): The event emitter function if one is desired, False otherwise.
    """

    def __init__(
        self,
        url: str,
        type_str: str,
        event_name: str,
        return_property: str,
        debounce: int,
        len_data_entries: int,
        event_emitter: Union[Callable, None],
    ):
        """Initialises an event object.
        Args:
            url (str): The URL of Misty's WebSocket API.
            type_str (str): The event type string as required by Misty's WebSockets API.
            event_name (str): A custom, unique event name.
            return_property (str): The property to return as required by Misty's WebSockets API.
            debounce (int): The interval at which new information is sent in ms.
            len_data_entries (int): The maximum number of data entries to keep.
            event_emitter (Union[Callable, None]): The event emitter function if one is desired, False otherwise.
        """
        self.url = url
        self.data = []
        self.type_str = type_str
        self.event_name = event_name
        self.return_property = return_property
        self.debounce = debounce
        self.log = []
        self.len_data_entries = len_data_entries
        event_thread = threading.Thread(target=self.run, daemon=True)
        event_thread.start()
        if event_emitter:
            self.ee = event_emitter
        else:
            self.ee = False

    def run(self):
        """Initialises the subscription and data collection."""
        self.ws = websocket.WebSocketApp(
            self.url,
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
        )
        self.ws.run_forever()

    def on_message(self, ws, message):
        """Saves received data and if ee is set, emits an event."""

        message = json.loads(message)
        mes = message["message"]
        if len(self.data) > self.len_data_entries:
            self.data = self.data[1:-1]
        self.data.append(mes)

        if self.ee:
            self.ee.emit(self.event_name, mes)

    def on_error(self, ws, error):
        """Logs an error and if ee is set, emits an 'error' event."""

        if len(self.log) > self.len_data_entries:
            self.log = self.log[1:-1]
        self.log.append(error)

        if self.ee:
            self.ee.emit("error_%s" % self.event_name, error)

    def on_close(self, ws):
        """Appends the closing message to the log and if ee is set, emits a 'close' event."""

        mes = "Closed"
        if len(self.log) > self.len_data_entries:
            self.log = self.log[1:-1]
        self.log.append(mes)

        if self.ee:
            self.ee.emit("close_%s" % self.event_name, mes)

    def on_open(self, ws):
        """Appends the opening message to the log and starts the subscription and if ee is set, emits an 'open' event."""

        self.log.append("Opened")
        self.subscribe()
        ws.send("")

        if self.ee:
            self.ee.emit("open_%s" % self.event_name)

    def subscribe(self):
        """Constructs the subscription message."""

        msg = {
            "Operation": "subscribe",
            "Type": self.type_str,
            "DebounceMs": self.debounce,
            "EventName": self.event_name,
            "ReturnProperty": self.return_property,
        }
        msg_str = json.dumps(msg, separators=(",", ":"))
        self.ws.send(msg_str)

    def unsubscribe(self):
        """Constructs the unsubscription message."""

        msg = {"Operation": "unsubscribe", "EventName": self.event_name, "Message": ""}
        msg_str = json.dumps(msg, separators=(",", ":"))
        self.ws.send(msg_str)
        self.ws.close()


class MistyEventHandler:
    """A class that handles all events its related Misty object subscribed to during this runtime.

    Attributes:
        events (Dict): The dictionary of all Event objects their related Misty object subscribed to during the current runtime.
        url (str): The URL for Misty's WebSocket API.
    """

    def __init__(self, ip: str, protocol: str, endpoint: str) -> None:
        """Initialises an object of class MistyEventHandler.

        Args:
            ip (str): The IP address for the URL where the requests are sent.
            protocol (str): The protocol for the URL where the requests are sent.
            endpoint (str): The endpoint for the URL where the requests are sent.
        """

        self.events = {}
        self.url = "%s://%s/%s" % (protocol, ip, endpoint)

    def subscribe_event(self, kwargs: Dict) -> Misty2pyResponse:
        """Subscribes to an event type.

        Args:
            kwargs (Dict):  requires a key `"type"` (a string representing the event type to subscribe to). Optional keys are:
            - `name` (str) for a custom event name; must be unique.
            - `return_property` (str) for the property to return from Misty's websockets; all properties are returned if return_property is not supplied.
            - `debounce` (int) for the interval at which new information is sent in ms; defaults to `250`.
            - `len_data_entries` (int) for the maximum number of data entries to keep (discards in fifo style); defaults to `10`.
            - `event_emitter` (Callable) for an event emitter function which emits an event upon message recieval.

        Returns:
            Misty2pyResponse: A Misty2pyResponse object with Misty2py sub-response and Misty WebSocket API sub-response.
        """

        event_type = kwargs.get("type")

        if not event_type:
            return Misty2pyResponse(
                False,
                error_msg="No event type specified.",
                error_type=Misty2pyErrorType.MISSING,
            )
        if not isinstance(event_type, str):
            return Misty2pyResponse(
                False,
                error_msg="Not a valid event type: `%s`." % str(event_type),
                error_type=Misty2pyErrorType.DATA_FORMAT,
            )

        event_name = kwargs.get("name")
        if not event_name:
            event_name = "event_%s_%s" % (event_type, get_random_string(8))

        return_property = kwargs.get("return_property")

        debounce = kwargs.get("debounce")
        if not debounce:
            debounce = DEFAULT_DEBOUNCE

        len_data_entries = kwargs.get("len_data_entries")
        if not len_data_entries:
            len_data_entries = DEFAULT_LEN_ENTRIES

        event_emitter = kwargs.get("event_emitter")

        try:
            new_event = MistyEvent(
                self.url,
                event_type,
                event_name,
                return_property,
                debounce,
                len_data_entries,
                event_emitter,
            )

        except Exception as e:
            return unknown_error(e)

        self.events[event_name] = new_event

        return Misty2pyResponse(
            True,
            ws_response={
                "success": True,
                "event_name": event_name,
                "message": "Subscribed to event type `%s` with name `%s`"
                % (event_type, event_name),
            },
        )

    def _obtain_event_data_or_log(
        self, event_name: Optional[str], is_log: bool = False
    ) -> Misty2pyResponse:
        """Obtains event data or event log.

        Args:
            event_name (Optional[str]): The name of the event whose data or log to obtain.
            is_log (bool, optional): `False` to obtain data, `True` to obtain log. Defaults to `False`.

        Returns:
            Misty2pyResponse: A Misty2pyResponse object with Misty2py sub-response and Misty WebSocket API sub-response.
        """
        if not event_name:
            return Misty2pyResponse(
                False,
                error_msg="No event name specified.",
                error_type=Misty2pyErrorType.MISSING,
            )

        if event_name in self.events.keys():
            try:
                if is_log:
                    return Misty2pyResponse(
                        True,
                        ws_response={
                            "success": True,
                            "message": self.events[event_name].log,
                        },
                    )

                return Misty2pyResponse(
                    True,
                    ws_response={
                        "success": True,
                        "message": self.events[event_name].data,
                    },
                )

            except Exception as e:
                return Misty2pyResponse(
                    True,
                    ws_response={
                        "success": False,
                        "message": "Error occurred while attempting to unsubscribe from event `%s`. Error message: `%s`."
                        % (event_name, e),
                    },
                )

        return Misty2pyResponse(
            True,
            ws_response={
                "success": False,
                "message": "Event type `%s` is not subscribed to." % event_name,
            },
        )

    def get_event_data(self, kwargs: Dict) -> Misty2pyResponse:
        """Obtains data from a subscribed event type.

        Args:
            kwargs (Dict): Requires a key "name" (the event name).

        Returns:
            Misty2pyResponse: A Misty2pyResponse object with Misty2py sub-response and Misty WebSocket API sub-response.
        """

        return self._obtain_event_data_or_log(kwargs.get("name"))

    def get_event_log(self, kwargs: Dict) -> Misty2pyResponse:
        """Obtains the log from a subscribed event type.

        Args:
            kwargs (Dict): Requires a key `name` (the event name).

        Returns:
            Misty2pyResponse: A Misty2pyResponse object with Misty2py sub-response and Misty WebSocket API sub-response.
        """

        return self._obtain_event_data_or_log(kwargs.get("name"), is_log=True)

    def unsubscribe_event(self, kwargs: Dict) -> Misty2pyResponse:
        """Unsubscribes from an event type.

        Args:
            kwargs (Dict): Requires a key `name` (the event name).

        Returns:
            Misty2pyResponse: A Misty2pyResponse object with Misty2py sub-response and Misty WebSocket API sub-response.
        """

        event_name = kwargs.get("name")
        if not event_name:
            return Misty2pyResponse(
                False,
                error_msg="No event name specified.",
                error_type=Misty2pyErrorType.MISSING,
            )

        if event_name in self.events.keys():
            try:
                self.events[event_name].unsubscribe()

            except Exception as e:
                return Misty2pyResponse(
                    True,
                    ws_response={
                        "success": False,
                        "message": "Error occurred while attempting to unsubscribe from event `%s`. Error message: `%s`."
                        % (event_name, e),
                    },
                )

            resp = Misty2pyResponse(
                True,
                ws_response={
                    "success": True,
                    "message": "Event `%s` of type `%s` unsubscribed"
                    % (event_name, self.events[event_name].type_str),
                    "log": self.events[event_name].log,
                },
            )
            self.events.pop(event_name)
            return resp

        return Misty2pyResponse(
            True,
            ws_response={
                "success": False,
                "message": "Event type `%s` is not subscribed to." % event_name,
            },
        )
