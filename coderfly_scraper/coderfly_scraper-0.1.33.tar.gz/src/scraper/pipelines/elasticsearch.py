# -*- coding:utf-8 -*-
"""
@desc:
"""
import logging
import traceback
from retry import retry
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from scrapy.exceptions import NotConfigured

from ..items import ElasticsearchItem, ElasticsearchBulkItem

logger = logging.getLogger(__name__)


class ElasticsearchPipeline(object):
    """
    save to elasticsearch
    """

    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbpool = Elasticsearch(settings['ELASTICSEARCH_URI'], http_compress=True)
        return cls(dbpool)

    @retry(tries=30)
    def process_item(self, item, spider):

        if isinstance(item, ElasticsearchItem):
            elasticsearch_index = item.pop("ELASTICSEARCH_INDEX", None) or spider.settings.get("ELASTICSEARCH_INDEX")
            elasticsearch_doctype = item.pop("ELASTICSEARCH_DOCTYPE", None) or spider.settings.get(
                "ELASTICSEARCH_DOCTYPE")
            _id = item.pop("_id")
            if not all([elasticsearch_index, elasticsearch_doctype]):
                raise NotConfigured("elasticsearch item not config index or doctype")
            self.dbpool.index(index=elasticsearch_index, body=dict(item),
                              doc_type=elasticsearch_doctype, id=_id)
        elif isinstance(item, ElasticsearchBulkItem):
            # bulk
            actions = item['actions']
            for i in range(0, len(actions), 1000):
                try:
                    bulk(self.dbpool, actions=actions[i:i + 1000], timeout=180, request_timeout=180)
                except Exception as e:
                    traceback.print_exc()
                    logger.warning('{} faild'.format(e))
                else:
                    logger.warning('actions[{}] bulk success'.format(len(actions)))

        return item
