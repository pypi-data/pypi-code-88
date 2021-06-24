"""Connectivity to a MongoDB database for HEA resources.
"""

import logging
from .mongoexpr import mongo_expr, sub_filter_expr, GETTER_PERMS
from mongoquery import Query
from aiohttp import web
from pymongo.results import UpdateResult, DeleteResult
from heaobject.root import HEAObject
from typing import Dict, Any, Optional, List
from unittest.mock import MagicMock
from copy import deepcopy
from .database import Database
import configparser


class MockMongo(Database):

    def __init__(self, app: web.Application, config: configparser.ConfigParser,
                 fixtures: Optional[Dict[str, List[Dict[str, Any]]]] = None) -> None:
        """
        Sets the db property of the app context with a motor MongoDB client instance.

        :param app: the aiohttp app object (required).
        :param config: a configparser.ConfigParser object, which should have a MongoDB section with two properties:

                ConnectionString = the MongoDB connection string, default is http://localhost:5432
                Name = the database name, default is heaserver

                If the MongoDB section is missing or config argument is None, the default database name will be heaserver, and
                the default connection string will be http://localhost:27017.
        """
        super().__init__(app, config)
        logger = logging.getLogger(__name__)

        self.__fixtures = deepcopy(fixtures) if fixtures else {}
        logger.debug('Initialized mockmongo')

    async def get(self, request: web.Request, collection: str, var_parts=None, mongoattributes=None, sub: Optional[str] = None) -> Optional[dict]:
        """
        Gets an object from the database.

        :param request: the aiohttp Request object (required).
        :param collection: the Mongo DB collection (required).
        :param var_parts: the names of the dynamic resource's variable parts (required).
        :param mongoattributes: the attribute to query by. The default value is None. If None, the var_parts will be
        used as the attributes to query by.
        :param sub: the user to filter by.
        :return: a HEA name-value pair dict, or None if not found.
        """
        query = Query(mongo_expr(request,
                                 var_parts=var_parts,
                                 mongoattributes=mongoattributes,
                                 extra=sub_filter_expr(sub, permissions=GETTER_PERMS)))
        return deepcopy(next((d for d in self.__fixtures.get(collection, []) if query.match(d)), None))

    async def get_all(self, request: web.Request, collection: str, var_parts=None, mongoattributes=None, sub: str = None) -> List[dict]:
        """
        Handle a get request.

        :param request: the HTTP request (required).
        :param collection: the MongoDB collection containing the requested object (required).
        :param var_parts: the names of the dynamic resource's variable parts (required).
        :param mongoattributes: the attributes to query by. The default value is None. If None, the var_parts will be
        used as the attributes to query by.
        :param sub: the user to filter by.
        :return: an iterator of HEA name-value pair dicts with the results of the mockmongo query.
        """
        query = Query(mongo_expr(request,
                                 var_parts=var_parts,
                                 mongoattributes=mongoattributes,
                                 extra=sub_filter_expr(sub, permissions=GETTER_PERMS)))
        return [deepcopy(d) for d in self.__fixtures.get(collection, []) if query.match(d)]

    async def post(self, request: web.Request, obj: HEAObject, collection: str) -> Optional[str]:
        """
        Handle a post request.

        :param request: the HTTP request (required).
        :param obj: the HEAObject instance to post.
        :param collection: the MongoDB collection containing the requested object (required).
        :return: the generated id of the created object.
        """
        obj.id = '3'
        f = self.__fixtures.get(collection, [])
        if obj is None or next((o for o in f if o['id'] == obj.id), None) is not None:
            return None
        else:
            return obj.id

    async def put(self, request: web.Request, obj: HEAObject, collection: str) -> UpdateResult:
        """
        Handle a put request.

        :param request: the HTTP request (required).
        :param obj: the HEAObject instance to put.
        :param collection: the MongoDB collection containing the requested object (required).
        :return: an object with a matched_count attribute that contains the number of records updated.
        """
        result = MagicMock(type=UpdateResult)
        result.raw_result = None
        result.acknowledged = True
        f = self.__fixtures.get(collection, [])
        result.matched_count = len([o for o in f if request.match_info['id'] == o['id']])
        result.modified_count = len([o for o in f if request.match_info['id'] == o['id']])
        return result

    async def delete(self, request: web.Request, collection: str) -> DeleteResult:
        """
        Handle a delete request.

        :param request: the HTTP request.
        :param collection: the MongoDB collection containing the requested object (required).
        :return: an object with a deleted_count attribute that contains the number of records deleted.
        """
        f = self.__fixtures.get(collection, [])
        result = MagicMock(type=DeleteResult)
        result.raw_result = None
        result.acknowledged = True
        result.deleted_count = len([o for o in f if request.match_info['id'] == o['id']])
        return result