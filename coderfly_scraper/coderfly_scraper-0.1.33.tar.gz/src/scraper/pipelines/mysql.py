# -*- coding:utf-8 -*-
"""
@desc: 
"""
import logging
from copy import deepcopy

from twisted.enterprise import adbapi
from ..items import MysqlInsertItem, MysqlUpdateItem, MysqlUpdateFlagItem

logger = logging.getLogger(__name__)

UPDATE_SQL = ("UPDATE {table} SET crawled=%s WHERE url_md5=%s")


class MySQLPipeline:
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_crawler(cls, crawler):
        dbparams = dict(
            host=crawler.settings.get('MYSQL_HOST'),
            port=crawler.settings.get('MYSQL_PORT'),
            user=crawler.settings.get('MYSQL_USER'),
            passwd=crawler.settings.get('MYSQL_PASSWORD'),
            database=crawler.settings.get('MYSQL_DATABASE'),
            charset=crawler.settings.get('MYSQL_CHARSET'),
            use_unicode=True
        )
        dbpool = adbapi.ConnectionPool("pymysql", **dbparams)
        return cls(dbpool)

    def open_spider(self, spider):
        spider.logger.info("已经连接至mysql...")

    def close_spider(self, spider):
        self.dbpool.close()
        spider.logger.info("mysql连接已断开...")

    def process_item(self, item, spider):
        sync_item = deepcopy(item)
        tables = spider.settings.get("MYSQL_TABLENAMES")
        for table in tables:
            if isinstance(item, MysqlUpdateItem):
                query = self.dbpool.runInteraction(self.update, table, sync_item)
                query.addErrback(self.handle_error, spider, sync_item)
            elif isinstance(item, MysqlInsertItem):
                query = self.dbpool.runInteraction(self.insert, table, sync_item)
                query.addErrback(self.handle_error, spider, sync_item)

            return sync_item

    def insert(self, cursor, table, item):
        sql = self.get_insert_sql_from_dict(table=table, item=item)
        cursor.execute(sql)

    def update(self, cursor, table, item):
        if item.get('sql'):
            # sql更新
            cursor.execute(item['sql'], item['args'])
        else:
            # 更新falg
            cursor.execute(UPDATE_SQL.format(table=table), [item.get("crawled"), item.get("url_md5")])

    def handle_error(self, failure, spider, item):
        if failure.value.args[0] == 1062:
            pass
        else:
            spider.logger.error(failure.value)
            spider.logger.error(item)

    @staticmethod
    def get_insert_sql_from_dict(table, item):
        keys, values = list(item.keys()), list(item.values())
        keys = ['`{}`'.format(key) for key in keys]
        key_str = ','.join(keys)
        value_str = ','.join(["'{}'".format(str('' if i == None else i)) for i in values])
        sql = 'insert into {table}({key_str}) values({value_str})'.format(table=table, key_str=key_str,
                                                                          value_str=value_str)
        return sql
