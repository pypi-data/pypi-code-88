import logging
import coloredlogs
from .handlers import slack

log = logging.getLogger("gytrash")


def setup_logging(
    log,
    *,
    log_level: int = 10,
    log_from_botocore: bool = False,
    log_to_slack: bool = False,
    slack_log_channel: str = None,
    slack_log_level: int = 20,
    slack_bot_token: str = None,
) -> None:
    """ Create the Logging handler for the CLI. This setups a log handler that support logging in color.

    Args:
        log: Root logging object.
        log_level: int - (keyword) console streamhandler log level
        log_from_botocore: bool - (keyword) Add botocore Logger if using boto
        log_to_slack: bool - (keyword) Add custom streamhandler to log to slack channel
        slack_log_channel: str - (keyword) Name of the slack channel to send logs
        slack_log_level: inf - (keyword) slack streamhandler log level
    Returns:
        None
    """

    log_format = "%(asctime)s %(name)s:%(module)s:%(lineno)d[%(process)d]:: %(levelname)s %(message)s"

    log.setLevel(log_level)

    generic_formatter = logging.Formatter(log_format)

    coloredlogs.install(level=log_level, logger=log, fmt=log_format)
    log.debug(f"Gytrash log level: {log.getEffectiveLevel()}")

    if log_from_botocore:
        log.debug("Tapping Botocore logger.")
        coloredlogs.install(
            level=log_level, logger=logging.getLogger("botocore"), fmt=log_format
        )

    if log_to_slack:
        sh = slack.SlackHandler(slack_log_channel, slack_bot_token)
        sh.setFormatter(generic_formatter)
        sh.setLevel(slack_log_level)
        log.addHandler(sh)

