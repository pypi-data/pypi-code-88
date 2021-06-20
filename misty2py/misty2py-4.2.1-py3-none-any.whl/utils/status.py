"""This module contains the class Status to track the execution status of a script and the class ActionLog to track the actions performed in a script."""
from typing import Any, Dict, List


class Status:
    """Tracks the status of a behaviour."""

    def __init__(
        self,
        init_status: Any = "initialised",
        init_data: Any = "",
        init_time: float = 0,
    ) -> None:
        """Initialises the Status.

        Args:
            init_status (Any, optional): The initial status. Defaults to `"initialised"`.
            init_data (Any, optional): The initial data. Defaults to `""`.
            init_time (float, optional): The initial time. Defaults to `0`.
        """
        self.status = init_status
        self.data = init_data
        self.time = init_time

    def set_(self, **content) -> None:
        """Sets the parameter passed to the function to the value passed.

        Accepts parameters `"data"`, `"time"` and `"status"`.
        """
        potential_data = content.get("data")
        if not isinstance(potential_data, type(None)):
            self.data = potential_data

        potential_time = content.get("time")
        if not isinstance(potential_time, type(None)):
            self.time = potential_time

        potential_status = content.get("status")
        if not isinstance(potential_status, type(None)):
            self.status = potential_status

    def get_(self, content_type: str) -> Any:
        """Obtains the value of the specified parameter.

        Args:
            content_type (str): The parameter whose value to return. Accepts `"data"`, `"time"` and `"status"`.

        Returns:
            Any: The value of the requested parameter.
        """
        if content_type == "data":
            return self.data
        if content_type == "time":
            return self.time
        if content_type == "status":
            return self.status

    def parse_to_message(self) -> Dict:
        """Returns the current status as a JSON dictionary.

        Returns:
            Dict: The current status, always contains the keyword `"status"`, optionally contains the keywords `"time"` and `"data"`.
        """
        message = {}
        if isinstance(self.status, bool):
            if self.status:
                message["status"] = "Success"
            else:
                message["status"] = "Failed"
        else:
            message["status"] = self.status
        if self.time != 0:
            message["time"] = self.time
        if self.data != "":
            message["data"] = self.data
        return message


class ActionLog:
    """Logs performed actions."""

    def __init__(self) -> None:
        """Initialises the actions list."""
        self.actions = []

    def append_(self, value: Any):
        """Appends the value to the actions list."""
        self.actions.append(value)

    def get_(self) -> List:
        """Returns the actions list."""
        return self.actions
