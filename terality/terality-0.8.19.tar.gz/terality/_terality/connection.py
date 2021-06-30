import atexit
import time
import os
import sys
from typing import Any, Optional
import platform  # noqa

import backoff
from common_client_scheduler.requests_responses import PendingComputationResponse
import numpy as np
import pandas as pd
from pydantic import BaseModel  # pylint: disable=no-name-in-module
import requests
from requests.models import Response

from terality_serde import dumps, loads
from common_client_scheduler import (
    SessionInfo,
    TeralityError,
    headers,
    AwsCredentials,
    DataTransferResponse,
)

from terality.version import __version__
from .. import TeralityNetworkError
from . import (
    logger,
    config_not_found,
    config_helper,
    TeralityConfig,
    TeralityCredentials,
)


class _Process(BaseModel):
    """Info about the Python process using Terality."""

    python_version_major: str = str(sys.version_info.major)
    python_version_minor: str = str(sys.version_info.minor)
    python_version_micro: str = str(sys.version_info.micro)
    numpy_version: str = np.__version__
    pandas_version: str = pd.__version__
    terality_version: Optional[str] = __version__
    platform: str = platform.platform()  # noqa

    def to_headers(self):
        return {f"{headers.TERALITY_CLIENT_INFO_PREFIX}{k}": v for k, v in self.dict().items()}


# pylint: disable=too-many-return-statements
def _is_non_retryable_code(e: requests.exceptions.RequestException) -> bool:
    # Temporary: we are encountering errors with the AWS API Gateway returning 404 or 403 errors
    # (ref: https://console.aws.amazon.com/support/home#/case/?displayId=8464649331&language=en)
    # While we wait for AWS support to solve this issue, also retry those calls:
    if e.response.status_code in [403, 404]:
        return False

    # Don't retry during tests, to save time
    if os.environ.get("PYTEST_CURRENT_TEST"):
        return True
    # If we did not get a response, then always retry
    if not hasattr(e, "response") or e.response is None:
        return False
    # Retry on "too many requests"
    if e.response.status_code == 429:
        return False
    # 501 means "not implemented". Retrying won't help.
    if e.response.status_code == 501:
        return True
    # Otherwise, retry on any 500 error
    if e.response.status_code >= 500:
        return False
    # Otherwise, don't retry
    return True


class Connection:
    _config: TeralityConfig
    _credentials: TeralityCredentials
    _process: _Process = _Process()
    session: Optional[SessionInfo] = None

    @classmethod
    @backoff.on_exception(
        backoff.expo,
        requests.exceptions.RequestException,
        giveup=_is_non_retryable_code,
        max_tries=5,
        # Stop retries after 2 minutes.
        # We assume that there is no value in automatically retrying
        # calls after that, because one "/compute" or one "/follow_up" call should always
        # return in less than 30 seconds, so we would have at least tried four times by that point.
        max_time=120,
        jitter=backoff.full_jitter,
    )
    def _do_api_call(cls, action: str, payload: Any, without_session: bool = False) -> Response:
        full_url = f'{"https" if cls._config.use_https else "http"}://{cls._config.url}/{action}'
        if cls._config.ignore_session:
            without_session = True
        r = requests.post(
            full_url,
            json={"session_id": None if without_session else cls.session.id, "payload": payload},  # type: ignore
            auth=(cls._credentials.user_id, cls._credentials.user_password),
            verify=cls._config.requests_ssl_verification,
            timeout=cls._config.timeout,
            headers=cls._process.to_headers(),
        )
        r.raise_for_status()
        return r

    @classmethod
    def poll_for_answer(cls, action: str, payload: Any, without_session: bool = False) -> Any:
        response = Connection.send_request(action, payload, without_session)
        while isinstance(response, PendingComputationResponse):
            function_id = response.pending_computation_id
            response = Connection.send_request("follow_up", {"function_id": function_id})
        return response

    @classmethod
    def send_request(cls, action: str, payload: Any, without_session: bool = False) -> Any:
        if cls._config is None:
            raise RuntimeError("Please specify user credentials")
        # Create new session on the fly if needed.
        if not without_session and cls.session is None:
            cls._create_session()

        try:
            payload_str = dumps(payload)
            r = cls._do_api_call(action, payload_str, without_session)
        except requests.HTTPError as e:
            try:
                server_error = loads(e.response.text)
                if not isinstance(server_error, Exception):
                    raise
            except Exception:
                # The request may have failed before reaching a Terality application.
                # In that case, try to look for a request ID in headers added by AWS
                # infrastructure.
                headers_to_search = [headers.TERALITY_REQUEST_ID, "X-Amz-Apigw-Id"]
                request_id = None
                for header in headers_to_search:
                    request_id = e.response.headers.get(header)
                additional_info = f" (request ID: {request_id})" if request_id is not None else ""
                server_error = TeralityError(e.response.text + additional_info)
            raise server_error from e
        except requests.RequestException as e:
            # Network failure at requests level
            raise TeralityNetworkError("Trouble contacting the API") from e
        except Exception as e:
            # Other cases
            raise TeralityError("An unhandled error occurred when querying the API") from e
        return loads(r.text)

    @classmethod
    def _create_session(cls) -> None:
        if cls._config.ignore_session:
            return
        cls.session = cls.send_request("create_session", None, without_session=True)

    @classmethod
    def delete_session(cls) -> None:
        if cls._config.ignore_session:
            return
        if cls.session is not None:
            cls.send_request("delete_session", {})
            cls.session = None

    @classmethod
    def set_up(cls, config: TeralityConfig, credentials: TeralityCredentials) -> None:
        cls._config = config
        cls._credentials = credentials
        cls._create_session()

    @classmethod
    def init(cls):
        if cls.session is None:
            logger.info("Initializing Terality")
            print_warning_if_not_latest_version()
            try:
                cls.set_up(TeralityConfig.load(), TeralityCredentials.load())
            except Exception as exc:
                logger.warning(exc)
                logger.warning(f"{config_not_found}\n{config_helper}")


def configure(user_id: str, user_password: str, *, check_connection: bool = True) -> None:
    """
    Provide Terality credentials and store them in the user's configuration directory.
    This also creates a configuration file if necessary.
    """
    credentials = TeralityCredentials(user_id=user_id, user_password=user_password)
    credentials.save()
    config = TeralityConfig.load(allow_missing=True)
    if config is None:
        config = TeralityConfig()
        config.save()
    if check_connection:
        Connection.set_up(config, credentials)


def latest_version_from_pypi() -> str:
    root_package_name = __name__.split(".")[0]
    r = requests.get(f"https://pypi.org/pypi/{root_package_name}/json")
    r.raise_for_status()
    return r.json()["info"]["version"]


def print_warning_if_not_latest_version() -> None:
    try:
        # Don't perform useless network requests during tests
        if "PYTEST_CURRENT_TEST" in os.environ:
            return
        latest = latest_version_from_pypi()
        if latest != __version__:
            logger.warning(
                f"You are using version {__version__} of the Terality client, but version {latest} is available. "
                "Consider upgrading your version to get the latest fixes and features."
            )
    except Exception:  # pylint:disable=broad-except  # nosec
        # If any error occurs, don't write a stack trace, just swallow the exception.
        pass


class AwsCredentialsFetcher:
    """Small utility to lazily fetch temporary AWS credentials from the Terality API.

    `get_credentials` will fetch credentials on the first call, and cache the result.

    Those credentials are used to upload files to Terality-owned S3 buckets.
    """

    def __init__(self) -> None:
        self._credentials: Optional[AwsCredentials] = None
        self._credentials_fetched_at = time.monotonic()

    def get_credentials(self) -> AwsCredentials:
        if self._credentials is None or time.monotonic() > self._credentials_fetched_at + 30 * 60:
            self._fetch_credentials()
        assert self._credentials is not None
        return self._credentials

    def _fetch_credentials(self) -> None:
        res: DataTransferResponse = Connection.send_request("transfers", {})
        self._credentials = res.temporary_upload_aws_credentials
        self._credentials_fetched_at = time.monotonic()


Connection.init()


def _atexit_delete_session():
    # Try to delete the current session, using a best effort policy. => Swallow any (Terality) exception.
    try:
        Connection.delete_session()
    except TeralityError:
        pass  # nosec: B110 (try_except_pass)


atexit.register(_atexit_delete_session)
