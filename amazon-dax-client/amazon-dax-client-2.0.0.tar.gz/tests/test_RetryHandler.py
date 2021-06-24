# pylint: disable=protected-access
import numbers
import time

from botocore.client import Config

import pytest

from amazondax import RetryHandler
from amazondax.DaxError import DaxServiceError, DaxClientError, DaxErrorCode, is_retryable, is_retryable_with_backoff

def test_equal_jitter_backoff_exception():
    with pytest.raises(ValueError):
        RetryHandler.equal_jitter_backoff(100, -100, 0)


def test_equal_jitter():
    assert RetryHandler.equal_jitter_backoff(1000, 10, 0) < 1000


def test_create_equal_jitter_backoff_function():
    test_func = RetryHandler.create_equal_jitter_backoff_function(
        1000, 70)
    val = test_func(attempts=0)
    assert isinstance(val, numbers.Number)
    assert test_func(attempts=0) < test_func(attempts=1)
    assert test_func(attempts=1) < test_func(attempts=2)


def test_retry_handler_config():
    retryer = RetryHandler.RetryHandler(
        Config(retries={"max_attempts": 4}), None)
    assert retryer._max_attempts == 4
    retryer2 = RetryHandler.RetryHandler(
        Config(retries={}), None)
    assert retryer2._max_attempts == RetryHandler.RetryHandler.DEFAULT_RETRIES


def test_retry_handler_onexception():
    retryer = RetryHandler.RetryHandler(
        Config(retries={}), None)
    error = DaxServiceError(None,
                            "Something went wrong.", [4, 37, 38, 39, 50], 1234, None, None)
    retryer.on_exception(error)
    assert retryer._last_exception == error


def test_retry_handler_can_retry_serviceerror():
    retryer = RetryHandler.RetryHandler(
        Config(retries={}), None)
    error = DaxServiceError(None,
                            "Something went wrong.", [4, 37, 38, 39, 50], 1234, None, None)
    assert retryer.can_retry(error) == True


def test_retry_handler_cant_retry_clienterror():
    retryer = RetryHandler.RetryHandler(
        Config(retries={}), None)
    error = DaxClientError("Something went wrong.",
                           DaxErrorCode.Decoder)
    assert retryer.can_retry(error) == False


def test_retry_handler_cant_retry_exception():
    retryer = RetryHandler.RetryHandler(
        Config(retries={}), None)
    error = Exception
    assert retryer.can_retry(error) == False


def test_retry_handler_pause_before_retry(monkeypatch):
    monkeypatch.setattr(time, 'sleep', lambda s: None)
    retryer = RetryHandler.RetryHandler(
        Config(retries={}), None)
    assert retryer._attempts == 0
    error = DaxServiceError(None,
                            "Something went wrong", [4, 37, 38, 39, 50], 1234, None, 429)
    assert is_retryable(error) == True
    assert is_retryable_with_backoff(error) == True

    retryer.pause_before_retry(error)

    assert retryer._attempts == 1


def test_retry_handler_pause_no_attempt_allowed(monkeypatch):
    monkeypatch.setattr(time, 'sleep', lambda s: None)
    retryer = RetryHandler.RetryHandler(
        Config(retries={"max_attempts": 0}), None)
    assert retryer._attempts == 0
    error = DaxServiceError(None,
                            "Something went wrong", [4, 37, 38, 39, 50], 1234, None, 429)
    assert is_retryable(error) == True
    assert is_retryable_with_backoff(error) == True

    assert retryer.can_retry(error) == False


def test_retry_handler_pause_max_attemps_reached(monkeypatch):
    monkeypatch.setattr(time, 'sleep', lambda s: None)
    retryer = RetryHandler.RetryHandler(
        Config(retries={"max_attempts": 1}), None)
    assert retryer._attempts == 0
    error = DaxServiceError(None,
                            "Something went wrong", [4, 37, 38, 39, 50], 1234, None, 429)
    assert is_retryable(error) == True
    assert is_retryable_with_backoff(error) == True

    assert retryer.can_retry(error) == True
    retryer.pause_before_retry(error)
    
    assert retryer._attempts == 1

    assert retryer.can_retry(error) == False


def test_retry_handler_pause_with_correct_time(monkeypatch):
    sleep_in_ms = 1000
    # Mock backoff to be 1000ms
    monkeypatch.setattr(RetryHandler, 'create_equal_jitter_backoff_function', lambda cap, base: (lambda attempts: sleep_in_ms))
    monkeypatch.setattr(time, 'sleep', lambda s: _assert_equal(s, sleep_in_ms/1000))
    retryer = RetryHandler.RetryHandler(
        Config(retries={}), None)
    assert retryer._attempts == 0
    error = DaxServiceError(None,
                            "Something went wrong", [4, 37, 38, 39, 50], 1234, None, 429)
    assert is_retryable(error) == True
    assert is_retryable_with_backoff(error) == True

    retryer.pause_before_retry(error)

    assert retryer._attempts == 1


def _assert_equal(expected, result):
    assert expected == result


def test_retry_handler_no_pause_before_retry():
    retryer = RetryHandler.RetryHandler(
        Config(retries={}), None)
    assert retryer._attempts == 0
    error = DaxServiceError(None,
                            "Something went wrong.", [4, 37, 38, 39, 58], 1234, None, None)
    assert is_retryable(error) == True
    assert is_retryable_with_backoff(error) == False

    retryer.pause_before_retry(error)

    assert retryer._attempts == 1


def test_retry_handler_no_pause_no_attempt_allowed():
    retryer = RetryHandler.RetryHandler(
        Config(retries={"max_attempts": 0}), None)
    assert retryer._attempts == 0
    error = DaxServiceError(None,
                            "Something went wrong.", [4, 37, 38, 39, 58], 1234, None, None)
    assert is_retryable(error) == True
    assert is_retryable_with_backoff(error) == False

    assert retryer.can_retry(error) == False


def test_retry_handler_no_pause_max_attemps_reached():
    retryer = RetryHandler.RetryHandler(
        Config(retries={"max_attempts": 1}), None)
    assert retryer._attempts == 0
    error = DaxServiceError(None,
                            "Something went wrong.", [4, 37, 38, 39, 58], 1234, None, None)
    assert is_retryable(error) == True
    assert is_retryable_with_backoff(error) == False

    assert retryer.can_retry(error) == True
    retryer.pause_before_retry(error)

    assert retryer._attempts == 1
    assert retryer.can_retry(error) == False
