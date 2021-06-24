"""Connectivity to a MongoDB database for HEA resources.
"""
from motor import motor_asyncio
from aiohttp import web
from .mongoexpr import mongo_expr, sub_filter_expr, GETTER_PERMS
import bson
import pymongo
from bson.codec_options import CodecOptions
import logging
import configparser
from typing import Optional, List, Dict, Any
from heaobject import user, root
from pymongo.results import UpdateResult, DeleteResult
from .database import Database
from yarl import URL

_codec_options = CodecOptions(tz_aware=True)


class Mongo(Database):
    """
    Connectivity to a MongoDB database for HEA resources.
    """
    def __init__(self, app: web.Application, config: Optional[configparser.ConfigParser]) -> None:
        """
        Performs initialization.

        :param app: the aiohttp app object (required).
        :param config: a configparser.ConfigParser object, which should have a MongoDB section with two properties:

                ConnectionString = the MongoDB connection string, default is http://localhost:5432
                Name = the database name, default is heaserver

                If the MongoDB section is missing or config argument is None, the default database name will be heaserver, and
                the default connection string will be http://localhost:27017.
        """
        super().__init__(app, config)
        logger = logging.getLogger(__name__)
        logger.debug('Initializing mongo module')

        default_connection_string = 'mongodb://heauser:heauser@localhost:27017/hea'

        if config and 'MongoDB' in config:
            logger.debug('Parsing MongoDB section of config file')
            database_section = config['MongoDB']
            connection_string = database_section.get('ConnectionString', default_connection_string)
            conn_url = URL(connection_string)
            logger.debug('\tUsing connection string %s',
                         str(conn_url.with_password('xxxxxxxx')) if conn_url.password is None else str(conn_url))
            name = database_section.get('Name')
            client = motor_asyncio.AsyncIOMotorClient(connection_string)
            logger.debug('\tUsing database %s', name or 'default from connection string')
            self.__connection_pool = client.get_database(name=name)
        else:
            logger.debug('Using default mongo connection string')
            self.__connection_pool = motor_asyncio.AsyncIOMotorClient(default_connection_string).get_database()

    async def get(self, request: web.Request, collection: str, var_parts=None, mongoattributes=None, sub: str = None) -> Optional[dict]:
        """
        Gets an object from the database.

        :param request: the aiohttp Request object (required).
        :param collection: the mockmongo collection (required).
        :param var_parts: the names of the dynamic resource's variable parts (required).
        :param mongoattributes: the attribute to query by. The default value is None. If None, the var_parts will be
        used as the attributes to query by.
        :param sub: the user to filter by.
        :return: a HEA name-value pair dict, or None if not found.
        """
        logger = logging.getLogger(__name__)
        coll = self.__connection_pool.get_collection(collection, codec_options=_codec_options)
        try:
            extra_ = sub_filter_expr(sub or user.NONE_USER, permissions=GETTER_PERMS)
            q = Mongo.__filter_by(mongo_expr(request,
                                             var_parts,
                                             mongoattributes,
                                             extra_))
            logger.debug('Query is %s', q)
            result = await coll.find_one(q)
            if result is not None:
                result['id'] = str(result['_id'])
                del result['_id']
                for k, v in result.items():
                    if k.endswith('_id'):
                        result[k] = str(v)
            logger.debug('Got from mongo: %s', result)
            return result
        except bson.errors.InvalidId as e:
            logger.debug('Skipped mongo query: %s', e)
            return None

    async def get_all(self, request: web.Request, collection: str, var_parts=None, mongoattributes=None,
                      sub: str = None) -> List[dict]:
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
        logger = logging.getLogger(__name__)
        coll = self.__connection_pool.get_collection(collection, codec_options=_codec_options)
        if var_parts is not None or mongoattributes is not None:
            q = Mongo.__filter_by(mongo_expr(request,
                                             var_parts,
                                             mongoattributes,
                                             sub_filter_expr(sub or user.NONE_USER, permissions=GETTER_PERMS))
                                  )
            logger.debug('Query is %s', q)
            results = await coll.find(q).to_list(10)
        else:
            q = sub_filter_expr(sub or user.NONE_USER, permissions=GETTER_PERMS)
            logger.debug('Query is %s', q)
            results = await coll.find(q).to_list(10)
        for result in results:
            result['id'] = str(result['_id'])
            del result['_id']
            for k, v in result.items():
                if k.endswith('_id'):
                    result[k] = str(v)
        logger.debug('Got from mongo: %s', results)
        return results

    async def post(self, request: web.Request, obj: root.HEAObject, collection: str) -> Optional[str]:
        """
        Handle a post request.

        :param request: the HTTP request (required).
        :param obj: the HEAObject instance to post.
        :param collection: the MongoDB collection containing the requested object (required).
        :return: the generated id of the created object, or None if the object could not be inserted or was None.
        """
        if obj is None:
            return None
        coll = self.__connection_pool.get_collection(collection, codec_options=_codec_options)
        try:
            result = await coll.insert_one(document=obj.to_dict())
            return str(result.inserted_id)
        except pymongo.errors.DuplicateKeyError:
            return None

    async def put(self, request: web.Request, obj: root.HEAObject, collection: str) -> Optional[UpdateResult]:
        """
        Handle a put request.

        :param request: the HTTP request (required).
        :param obj: the HEAObject instance to put.
        :param collection: the MongoDB collection containing the requested object (required).
        :return: an instance of pymongo.results.UpdateResult.
        TODO: check that the user has the needed permissions to replace the object.
        """
        coll = self.__connection_pool.get_collection(collection, codec_options=_codec_options)
        try:
            return await coll.replace_one(Mongo.__filter_by_id(request), obj.to_dict())
        except bson.errors.InvalidId:
            return None

    async def delete(self, request: web.Request, collection: str) -> Optional[DeleteResult]:
        """
        Handle a delete request.

        :param request: the HTTP request.
        :param collection: the MongoDB collection containing the requested object (required).
        :return: an instance of pymongo.results.DeleteResult.
        TODO: check that the user has the permissions needed to delete the item.
        """
        coll = self.__connection_pool.get_collection(collection, codec_options=_codec_options)
        try:
            return await coll.delete_many(Mongo.__filter_by_id(request))
        except bson.errors.InvalidId:
            return None

    @staticmethod
    def __filter_by(filter_criteria) -> Dict[str, Any]:
        """
        Returns a filter for objects with an attribute value of interest.

        :param filter_criteria: the and'ed attribute-value pairs to filter by. Throws bson.errors.InvalidId if the the
        provided id is not a 12-byte input or a 24-character hex string.
        :return: a filter dict.
        """
        return {
            ('_id' if nm == 'id' else nm): (bson.objectid.ObjectId(val) if nm == 'id' else val)
            for nm, val in filter_criteria.items()}

    @staticmethod
    def __filter_by_id(request) -> Dict[str, Any]:
        """
        Returns a filter by the id variable in the request.

        :param request: a HTTP request.
        :return: a filter dict.
        """
        return Mongo.__filter_by({'id': request.match_info['id']})
