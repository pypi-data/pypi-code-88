# -*- coding:utf-8 -*-
"""
@desc: 
"""
import scrapy
from scrapy.item import Item


class BaseItem(Item):
    def __setitem__(self, key, value):
        self._values[key] = value


class ElasticsearchItem(BaseItem):
    pass


class ElasticsearchBulkItem(BaseItem):
    actions = scrapy.Field()


class MysqlInsertItem(BaseItem):
    pass


class MysqlUpdateItem(BaseItem):
    pass


class MysqlUpdateFlagItem(BaseItem):
    pass
