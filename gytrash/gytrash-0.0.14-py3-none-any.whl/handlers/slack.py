from logging import (
    StreamHandler,
    CRITICAL,
    ERROR,
    WARNING,
    INFO,
    FATAL,
    DEBUG,
    NOTSET,
    Formatter,
)

import logging
import os
import traceback

from slack_sdk.web import WebClient

ERROR_COLOR = "danger"  # color name is built in to Slack API
WARNING_COLOR = "warning"  # color name is built in to Slack API
INFO_COLOR = "#439FE0"

COLORS = {
    CRITICAL: ERROR_COLOR,
    FATAL: ERROR_COLOR,
    ERROR: ERROR_COLOR,
    WARNING: WARNING_COLOR,
    INFO: INFO_COLOR,
    DEBUG: INFO_COLOR,
    NOTSET: INFO_COLOR,
}


class SlackHandler(StreamHandler):
    """Slack log handler Class

    Inherits:
        logging.StreamHandler: Base log StreamHandler class.
    """

    def __init__(
        self, channel: str, slack_bot_token: str = None, username: str = "Gytrash"
    ):
        """Initialize the stream handler with some specifics for slack.

        Args:
            channel (str): Slack channel to publish logs
            slack_bot_token (str, optional): Slack bot token to use the slack published app. Defaults to None.
            username (str, optional): Username of the Slack bot. Defaults to "Gytrash".
        """
        StreamHandler.__init__(self)
        # Initialize a Web API client
        if slack_bot_token:
            self.slack_web_client = WebClient(token=slack_bot_token)
        else:
            self.slack_web_client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
        self.channel = channel
        self.username = username

    def _send_log(self, message: dict):
        """Posts the formatted message to slack via the web client.

        Args:
            message (dict): Slack message dictionary. Follows the blocks API.
        """
        self.slack_web_client.chat_postMessage(**message)

    def emit(self, message: "logging.LogRecord"):
        """Emits a message from the handler.

        Args:
            message (logging.LogRecord): Log record from the stream.
        """
        assert isinstance(message, logging.LogRecord)

        slack_message = self.format(message)

        # List of LogRecord attributes expected when reading the
        # documentation of the logging module:
        expected_attributes = (
            "args,asctime,created,exc_info,filename,funcName,levelname,"
            "levelno,lineno,module,msecs,message,msg,name,pathname,"
            "process,processName,relativeCreated,stack_info,thread,threadName"
        )
        for ea in expected_attributes.split(","):
            if not hasattr(message, ea):
                print("UNEXPECTED: LogRecord does not have the '{}' field!".format(ea))

        slack_message["channel"] = self.channel
        slack_message["username"] = self.username

        self._send_log(slack_message)
