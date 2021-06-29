import logging
from re import S


class SlackFormatter(logging.Formatter):
    """Formatter constructs and formats json payload for the slack log handler.

    Inherits:
        logging.Formatter: Base log formatting class
    """

    ERROR_TYPES_EMOJI = {
        "CRITICAL": ":interrobang:",
        "ERROR": ":red_circle:",
        "WARNING": ":large_orange_diamond:",
        "INFO": ":large_blue_circle:",
        "DEBUG": ":white_circle:",
    }

    DIVIDER_BLOCK = {"type": "divider"}

    def format(self, record: "logging.LogRecord"):
        """Formats a message. Required method overwrite of base class.

        Args:
            record (logging.LogRecord): A log delivered from the handler.

        Returns:
            dict: dictionary representation of a slack payload.
        """
        record.asctime = self.formatTime(record)
        record.message = record.getMessage()

        ret = {
            "ts": "",
            "icon_emoji": self.ERROR_TYPES_EMOJI[record.levelname],
            "blocks": [*self._create_log_block(record), self.DIVIDER_BLOCK,],
        }
        return ret

    def _create_log_block(self, record: "logging.LogRecord"):
        """Creates a slack message "block".
        
        [Slack Block Kit](https://api.slack.com/block-kit)

        Args:
            record (logging.LogRecord): Logging record passed in for formatting.

        Returns:
            list(dict): Returns a list of dicts through a constructor function, _get_log_block.
        """
        emoji = f"{self.ERROR_TYPES_EMOJI[record.levelname]}"
        text = f"```{record.message}```"
        information = f"{record.asctime}-{record.name}[{record.process}]-{record.module}-{record.levelname}"
        return self._get_log_block(emoji, text, information)

    @staticmethod
    def _get_log_block(emoji: str, text: str, information: str):
        """Creates a slack payload block object.

        Args:
            emoji (str): An emoji colon bound string for use in the message block.
            text (str): The text of the message to include in the message block
            information (str): The metadata about the logging message.

        Returns:
            list(dict): List of dictionaries, one for each section of the message block.
        """
        return [
            {"type": "section", "text": {"type": "mrkdwn", "text": emoji}},
            {"type": "context", "elements": [{"type": "mrkdwn", "text": information}],},
            {"type": "section", "text": {"type": "mrkdwn", "text": text}},
        ]
