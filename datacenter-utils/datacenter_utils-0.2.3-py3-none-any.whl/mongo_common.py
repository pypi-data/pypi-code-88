# -*- encoding:utf-8 -*-
import pandas as pd
from pymongo import MongoClient, ASCENDING, DESCENDING
import time
from datetime import datetime, timedelta
from pymongo.errors import OperationFailure


class MongoObject(object):
    """
    class MongoObject
    """
    def __init__(self, host, port, username, password, auth_db='admin'):
        self.insert_bench = 6000
        self.client = MongoClient(f"mongodb://{host}:{port}")
        db = self.client[auth_db]
        db.authenticate(username, password)

    def upsert_many_df(self, collection, df_data, key_field, update_field):
        """

        :param collection: collection connect object
        :param df_data: dataframe
        :param key_field: list
        :param update_field: list
        """
        df_data_js = df_data.to_dict(orient='records')  # json.loads(df_data.T.to_json())
        # 添加需要的索引，即主键
        for index_field in key_field:
            collection.create_index(index_field)
        # 写入操作
        bulk = collection.initialize_unordered_bulk_op()

        for num in range(len(df_data_js)):
            item = df_data_js[num]
            insert_data = self._join_upsert_dict(item, key_field, update_field)

            bulk.find(insert_data['key_data']).upsert().update_one(insert_data['change_data'])

            if num % self.insert_bench == 0:
                bulk.execute()
                bulk = collection.initialize_unordered_bulk_op()
            if num == len(df_data_js) - 1:
                bulk.execute()

    @staticmethod
    def _join_upsert_dict(item, key_field, update_field):
        # key_data_dict: if key data exist remain else insert new
        key_data_dict = {}
        for field in key_field:
            joint_dict = {field: item[field]}
            key_data_dict = {**key_data_dict, **joint_dict}

        # change_data_dict ,data need to be update
        change_data_dict = {}
        for field in update_field:
            joint_dict = {field: item[field]}
            change_data_dict = {**change_data_dict, **joint_dict}
        joint_dict = {"updateTime": datetime.utcfromtimestamp(time.time())}
        change_data_dict = {**change_data_dict, **joint_dict}
        change_data_dict = {'$set': change_data_dict}

        # join key_data and change_data
        insert_data = {"key_data": key_data_dict, "change_data": change_data_dict}
        return insert_data

    @staticmethod
    def remove(collection, filter_dict):
        try:
            collection.remove(filter_dict)
        except:
            collection.delete_many(filter_dict)

    @staticmethod
    def insert_one(collection, data):
        """

        :param collection: collection connect object
        :param data: dict
        :return:
        """
        res = collection.insert_one(data)
        return res.inserted_id

    @staticmethod
    def insert_many(collection, data):
        """

        :param collection: collection connect object
        :param data: list
        :return:
        """
        res = collection.insert_many(data)
        return res.inserted_ids

    @staticmethod
    def update_one(collection, condition, data):
        """

        :param collection: collection connect object
        :param condition: dict
        :param data: dict
        """
        res = collection.find_one(condition)
        if not res:
            data.update(condition)
            insert_res = collection.insert_one(data)
            return 0, insert_res
        else:
            update_result = collection.update(condition, {'$set': data})
            return 1, update_result

    @staticmethod
    def find_many_df(collection, filter_dict=None, projection=None, order_by=None,
                     offset=0, limit=20
                     ):
        """

        :param collection: collection connect object
        :param filter_dict: dict
        :param projection: dict
        :param order_by: str
        :param offset: int
        :param limit: int
        :return:
        """
        cursor = None
        if filter_dict and not projection:
            projection = dict()
            projection.update({'_id': 0})
            cursor = collection.find(filter_dict).limit(limit).skip(offset)
        if filter_dict and projection:
            projection.update({'_id': 0})
            cursor = collection.find(filter_dict, projection).limit(limit).skip(offset)
        if not filter_dict and not projection:
            cursor = collection.find({}).limit(limit).skip(offset)

        if order_by:
            order = -1 if '-' in order_by else 1
            order_by = order_by.replace('-', '')
            cursor.sort([(order_by, order)])

        if cursor:
            docs = list(cursor)
            return pd.DataFrame(docs)
