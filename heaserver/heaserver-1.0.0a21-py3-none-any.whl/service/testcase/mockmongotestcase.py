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

from ..db.mockmongo import MockMongo
from . import mongotestcase
from aiohttp import web
import configparser
import logging
from typing import Type, Dict, List, Any, Optional, Union
from heaserver.service import runner, wstl
from .expectedvalues import expected_values, ActionSpec
from yarl import URL


def get_test_case_cls(href: Union[str, URL],
                      wstl_package: str,
                      fixtures: Dict[str, List[Dict[str, Any]]],
                      body_post: Optional[Dict[str, Dict[str, Any]]] = None,
                      body_put: Optional[Dict[str, Dict[str, Any]]] = None,
                      expected_one: Optional[Dict[str, Any]] = None,
                      expected_one_wstl: Optional[Dict[str, Any]] = None,
                      expected_one_duplicate_form: Optional[Dict[str, Any]] = None,
                      expected_all: Optional[Dict[str, Any]] = None,
                      expected_all_wstl: Optional[Dict[str, Any]] = None) -> Type[mongotestcase.MongoTestCase]:
    """
    This function configures mocks. It returns a base test case class for testing a mongodb-based service with the
    provided fixtures. The test case class is a subclass of aiohttp.test_utils.AioHTTPTestCase, and the provided
    fixtures can be found in the following fields: _resource_path, _body_post, _body_put, _expected_all, and
    _expected_one.

    :param href: the resource being tested.
    :param wstl_package: the name of the package containing the wstl data package. Required.
    :param fixtures: data to insert into the mongo database before running each test. Should be a dict of
    collection -> list of objects. Required.
    :param body_post: JSON dict for data to be posted.
    :param body_put: JSON dict for data to be put. If None, the value of body_post will be used for PUTs.
    :param expected_one: The expected JSON dict for GET calls. If None, the value of expected_all will be used.
    :param expected_one_wstl: The expected JSON dict for GET calls that return the
    application/vnd.wstl+json mime type.
    :param expected_one_duplicate_form: The expected JSON dict for GET calls that return the
    object's duplicate form.
    :param expected_all: The expected JSON dict for GET-all calls.
    :param expected_all_wstl: The expected JSON dict for GET-all calls that return the
    application/vnd.wstl+json mime type.
    :return the base test case class.
    """

    def mock_mongo(app: web.Application, config: configparser.ConfigParser):
        return MockMongo(app, config, fixtures)

    class MockMongoTestCase(mongotestcase.MongoTestCase):
        """
        Test case class for testing a mongodb-based service.
        """

        def __init__(self, methodName=None):
            """
            Initializes a test case.

            :param methodName: the name of the method to test.
            """
            super().__init__(methodName=methodName,
                             href=href,
                             body_post=body_post,
                             body_put=body_put,
                             expected_all=expected_all,
                             expected_one=expected_one or expected_all,
                             expected_one_wstl=expected_one_wstl or expected_all_wstl,
                             expected_all_wstl=expected_all_wstl,
                             expected_one_duplicate_form=expected_one_duplicate_form,
                             wstl_package=wstl_package)

        def run(self, result=None):
            with self._caplog.at_level(logging.DEBUG):
                return super().run(result)

        async def get_application(self):
            return await runner.get_application(db=mock_mongo,
                                                wstl_builder_factory=wstl.builder_factory(wstl_package, href=href))

    return MockMongoTestCase


def get_test_case_cls_default(coll: str,
                              wstl_package: str,
                              fixtures: Dict[str, List[Dict[str, Any]]],
                              duplicate_action_name: str,
                              include_root=False,
                              href: Optional[Union[str, URL]] = None,
                              get_actions: Optional[List[ActionSpec]] = None,
                              get_all_actions: Optional[List[ActionSpec]] = None) -> Type[mongotestcase.MongoTestCase]:
    if href is None:
        href = URL(f'/{coll}')
    return get_test_case_cls(href=href, wstl_package=wstl_package, fixtures=fixtures,
                             **expected_values(fixtures, coll, wstl.builder(package=wstl_package),
                                               duplicate_action_name,
                                               include_root=include_root, get_actions=get_actions,
                                               get_all_actions=get_all_actions)
                             )
