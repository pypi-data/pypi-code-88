import sys

import pytest
import logging

from warden_sdk.integrations.logging import LoggingIntegration

other_logger = logging.getLogger("testfoo")
logger = logging.getLogger(__name__)


@pytest.fixture(autouse=True)
def reset_level():
   other_logger.setLevel(logging.DEBUG)
   logger.setLevel(logging.DEBUG)


@pytest.mark.parametrize("logger", [logger, other_logger])
def test_logging_works_with_many_loggers(warden_inited, capture_events, logger):
   warden_inited()
   events = capture_events()

   logger.info("bread")
   logger.critical("LOL")
   (event,) = events
   assert event["level"] == "fatal"
   assert not event["logentry"]["params"]
   assert event["logentry"]["message"] == "LOL"
