import os
import sys
from typing import Any, Callable

from assertpy import assert_that
from cloudevents.http import CloudEvent

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from devopsprocessor.processor import Processor  # noqa: E402

NO_SETUP: int = 5
SETUP: int = 10
HANDLED: int = 15


class TrivialProcessor(Processor):
    token: dict

    def mapper(self) -> Callable[[CloudEvent], Any]:
        return lambda event: self.set_token(event.data)

    def close(self) -> None:
        pass

    def set_token(self, value: dict):
        self.token = value


def test_trivial_handler() -> None:
    test: TrivialProcessor = TrivialProcessor()
    event: CloudEvent = CloudEvent(
        attributes={
            'type': 'com.davengeo.test',
            'source': 'devops'},
        data={'test': True})
    test.mapper()(event)
    assert_that(test.token['test']).is_true()
