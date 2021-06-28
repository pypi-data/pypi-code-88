from typing import Callable, Dict
from .pytest_mock_fixtures import _LambdaContextMock, _get_sns_lambda_event_mock
import json


def call_handler(handler: Callable, event: Dict):
    return json.loads(json.dumps(handler(event, _LambdaContextMock())))


def notify_handler(handler: Callable, message: Dict):
    return json.loads(json.dumps(handler(
        json.loads(_get_sns_lambda_event_mock(json.dumps(message)).json()),
        _LambdaContextMock()
    )))
