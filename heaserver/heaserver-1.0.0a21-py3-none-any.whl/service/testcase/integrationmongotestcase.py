from aiohttp.web import Application
from .mongotestcase import MongoTestCase
from ..db.mongo import Mongo
from .. import runner
from .. import wstl
import logging
from typing import Union, Dict, List, Any, Optional, Type
from testcontainers.mongodb import MongoDbContainer
from yarl import URL
import bson
from .expectedvalues import expected_values, ActionSpec


def get_test_case_cls(href: Union[URL, str],
                      wstl_package: str,
                      fixtures: Dict[str, List[dict]],
                      body_post: Optional[Dict[str, Dict[str, Any]]] = None,
                      body_put: Optional[Dict[str, Dict[str, Any]]] = None,
                      expected_one: Optional[Dict[str, Any]] = None,
                      expected_one_wstl: Optional[Dict[str, Any]] = None,
                      expected_one_duplicate_form: Optional[Dict[str, Any]] = None,
                      expected_all: Optional[Dict[str, Any]] = None,
                      expected_all_wstl: Optional[Dict[str, Any]] = None) -> Type[MongoTestCase]:
    """
    This function configures mocks. It returns a base test case class for testing a mongodb-based service with the
    provided fixtures. The test case class is a subclass of aiohttp.test_utils.AioHTTPTestCase, and the provided
    fixtures can be found in the following fields: _resource_path, _body_post, _body_put, _expected_all, and
    _expected_one.

    :param href: the resource being tested. Required.
    :param wstl_package: the name of the package containing the wstl data package. Required.
    :param fixtures: data to insert into the mongo database before running each test. Should be a dict of
    collection -> list of objects. Required.
    :param body_post: JSON dict for data to be posted.
    :param body_put: JSON dict for data to be put. If None, the value of body_post will be used for PUTs.
    :param expected_one: The expected JSON dict for GET calls. If None, the value of expected_all will be used.
    :param expected_one_wstl: The expected JSON dict for GET calls that return the
    application/vnd.wstl+json mime type.
    :param expected_one_properties_form: The expected JSON dict for GET calls that return the
    object's properties form.
    :param expected_one_duplicate_form: The expected JSON dict for GET calls that return the
    object's duplicate form.
    :param expected_all: The expected JSON dict for GET-all calls.
    :param expected_all_wstl: The expected JSON dict for GET-all calls that return the
    application/vnd.wstl+json mime type.
    :return the base test case class.
    """

    class RealMongoTestCase(MongoTestCase):
        """
        Test case class for testing a mongodb-based service.
        """

        def __init__(self, methodName: str = 'runTest') -> None:
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
            """
            Runs a test using a freshly created MongoDB Docker container. The container is destroyed upon concluding
            the test.

            :param result: a TestResult object into which the test's result is collected.
            :return: the TestResult object.
            """
            with MongoDbContainer('mongo:4.2.2') as mongo_:
                with self._caplog.at_level(logging.DEBUG):
                    config_file = f"""
[MongoDB]
ConnectionString = mongodb://localhost:{mongo_.get_exposed_port(27017)}/test
                    """
                    self.__config = runner.init(config_string=config_file)
                    db = mongo_.get_connection_client().test
                    for k in fixtures or {}:
                        lst = []
                        for f in fixtures[k]:
                            if 'id' in f:
                                f_ = dict(f)
                                f_['_id'] = bson.ObjectId(f_.pop('id', None))
                                lst.append(f_)
                            else:
                                lst.append(f)
                        db[k].insert_many(lst)
                    return super().run(result)

        async def get_application(self) -> Application:
            return await runner.get_application(db=Mongo,
                                                wstl_builder_factory=wstl.builder_factory(wstl_package, href=href),
                                                config=self.__config)

    return RealMongoTestCase


def get_test_case_cls_default(coll: str,
                              wstl_package: str,
                              fixtures: Dict[str, List[Dict[str, Any]]],
                              duplicate_action_name: str,
                              include_root=False,
                              href: Optional[Union[str, URL]] = None,
                              get_actions: Optional[List[ActionSpec]] = None,
                              get_all_actions: Optional[List[ActionSpec]] = None) -> Type[MongoTestCase]:
    if href is None:
        href = URL(f'/{coll}')
    return get_test_case_cls(href=href, wstl_package=wstl_package, fixtures=fixtures,
                             **expected_values(fixtures, coll, wstl.builder(package=wstl_package),
                                               duplicate_action_name,
                                               include_root=include_root,
                                               get_actions=get_actions, get_all_actions=get_all_actions)
                             )
