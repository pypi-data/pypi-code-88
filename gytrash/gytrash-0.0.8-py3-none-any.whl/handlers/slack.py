from slack_sdk.web import WebClient
from logging import StreamHandler
import logging
import os


class SlackHandler(StreamHandler):
    def __init__(self, channel: str, slack_bot_token: str = None):
        StreamHandler.__init__(self)
        # Initialize a Web API client
        if slack_bot_token:
            self.slack_web_client = WebClient(token=slack_bot_token)
        else:
            self.slack_web_client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
        self.channel = channel

    def _send_log(self, message: str, channel: str):
        # Create a new onboarding tutorial.
        onboarding_tutorial = LogMessage(channel, message)

        # Get the onboarding message payload
        slack_payload = onboarding_tutorial.get_message_payload()

        # Post the onboarding message in Slack
        response = self.slack_web_client.chat_postMessage(**slack_payload)

    def emit(self, message: str):
        assert isinstance(message, logging.LogRecord)

        self.format(message)

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

        self._send_log(message, self.channel)


class LogMessage:
    """Constructs the onboarding message and stores the state of which tasks were completed."""

    ERROR_TYPES_EMOJI = {
        "CRITICAL": ":interrobang:",
        "ERROR": ":red_circle:",
        "WARNING": ":large_orange_diamond:",
        "INFO": ":large_blue_circle:",
        "DEBUG": ":white_circle:",
    }

    DIVIDER_BLOCK = {"type": "divider"}

    def __init__(self, channel, message):
        self.channel = channel
        self.message = message
        self.username = "pythonboardingbot"
        self.icon_emoji = self.ERROR_TYPES_EMOJI[message.levelname]
        self.timestamp = ""
        self.reaction_task_completed = False
        self.pin_task_completed = False

    def get_message_payload(self):
        return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [*self._create_log_block(), self.DIVIDER_BLOCK,],
        }

    def _create_log_block(self):
        emoji = f"{self.ERROR_TYPES_EMOJI[self.message.levelname]}"
        text = f"```{self.message.getMessage()}```"
        information = f"{self.message.asctime}-{self.message.name}[{self.message.process}]-{self.message.module}-{self.message.levelname}"
        return self._get_log_block(emoji, text, information)

    @staticmethod
    def _get_log_block(emoji, text, information):
        return [
            {"type": "section", "text": {"type": "mrkdwn", "text": emoji}},
            {"type": "context", "elements": [{"type": "mrkdwn", "text": information}],},
            {"type": "section", "text": {"type": "mrkdwn", "text": text}},
        ]
