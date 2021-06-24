"""
Sets up a testing environment for testing HEA services, including mock modules and classes. To use this module, do the
following in order:
1) Import this module before importing anything else to insure that all mocks are are used in subsequently imported
modules.
2) Import the service to be tested.
3) Call the get_test_case_cls with the fixtures to use in the unit tests.
4) Create subclasses of the returned unit test class to implement actual test cases. The mixin module in this package
contains implementations of unit tests to run for testing GET, POST, PUT and DELETE. Add these mixins as superclasses
of your test cases.
"""

from aiohttp.test_utils import AioHTTPTestCase
from aiohttp.web import Application
import pytest
import abc
from yarl import URL
from typing import Dict, Any, Union



class MongoTestCase(abc.ABC, AioHTTPTestCase):
    """
    Test case class for testing a mongodb-based service.
    """

    @pytest.fixture(autouse=True)
    def inject_fixtures(self, caplog):
        self._caplog = caplog

    def __init__(self, href: Union[URL, str],
                 wstl_package: str,
                 body_post: Dict[str, Dict[str, Any]] = None,
                 body_put: Dict[str, Dict[str, Any]] = None,
                 expected_all: Dict[str, Any] = None,
                 expected_one: Dict[str, Any] = None,
                 expected_one_wstl: Dict[str, Any] = None,
                 expected_all_wstl: Dict[str, Any] = None,
                 expected_one_duplicate_form: Dict[str, Any] = None,
                 methodName: str = 'runTest') -> None:
        """
        Initializes a test case.

        :param href: the resource being tested. Required.
        :param wstl_package: the name of the package containing the wstl data package. Required.
        :param body_post: JSON dict for data to be posted.
        :param body_put: JSON dict for data to be put. If None, the value of body_post will be used for PUTs.
        :param expected_all: The expected JSON dict for GET-all calls.
        :param expected_one: The expected JSON dict for GET calls. If None, the value of expected_all will be used.
        :param expected_one_wstl: The expected JSON dict for GET calls that return the
        application/vnd.wstl+json mime type.
        :param expected_all_wstl: The expected JSON dict for GET-all calls that return the
        application/vnd.wstl+json mime type.
        :param expected_one_properties_form: The expected JSON dict for GET calls that return the
        object's properties form.
        :param expected_one_duplicate_form: The expected JSON dict for GET calls that return the
        object's duplicate form.
        :param methodName: the name of the method to test.
        """
        super().__init__(methodName=methodName)
        self._href = URL(href)
        self._body_post = body_post
        self._body_put = body_put
        self._expected_all = expected_all
        self._expected_one = expected_one
        self._expected_one_wstl = expected_one_wstl
        self._expected_all_wstl = expected_all_wstl
        self._expected_one_duplicate_form = expected_one_duplicate_form
        self._wstl_package = wstl_package
        self.maxDiff = None

    @abc.abstractmethod
    async def get_application(self) -> Application:
        pass
