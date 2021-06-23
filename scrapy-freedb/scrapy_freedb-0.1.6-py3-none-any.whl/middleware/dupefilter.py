import logging
import importlib
from scrapy.dupefilters import BaseDupeFilter
from scrapy.utils.request import request_fingerprint
from .freedb import FreedbClient, DocumentDotExist


logger = logging.getLogger(__name__)


def null_id_mapper(request):
    return None


def meta_id_mapper(request):
    meta = request.meta
    return meta.get('id')


class FreedbDupefilter(BaseDupeFilter):
    '''SpiderStateService request duplicates filter.
    '''
    logger = logger
    visit_cache = None

    def __init__(self, db_name, col_name, client: FreedbClient, settings, debug=False, stats=None):
        self.db_name = db_name
        self.col_name = col_name
        self.client = client
        self.debug = debug
        self.settings = settings
        self.logdupes = True
        self.stats = stats
        self.visit_cache = set()
        self.docs_existence_cache = {} # dict[str, bool]
        
        free_id_mapper_setting = settings.get('FREEDB_ID_MAPPER')
        self.id_field = settings.get('FREEDB_ID_FIELD')
        if free_id_mapper_setting:
            id_mapper_module_name, id_mapper_func_name = free_id_mapper_setting.split(':')
            id_mapper_module = importlib.import_module(id_mapper_module_name)
            self.id_mapper = getattr(id_mapper_module, id_mapper_func_name)
        else:
            self.id_mapper = meta_id_mapper

    @classmethod
    def from_settings(cls, settings):
        '''
        This method is for older scrapy version which does not support
        a spider context when building a dupefilter instance. The spider name
        will be assumed as 'spider'
        :param settings:
        :return:
        '''
        base_url = settings.get("FREEDB_BASEURL")
        token = settings.get('FREEDB_TOKEN')
        db_name = settings.get('FREEDB_DBNAME')
        col_name = settings.get('FREEDB_COLNAME')
        client = FreedbClient(base_url, token)
        return cls(db_name, col_name, client, settings)

    @classmethod
    def from_crawler(cls, crawler):
        logger.debug('FreedbDupefilter from_crawler')
        return cls.from_spider(crawler.spider)

    @classmethod
    def from_spider(cls, spider):
        settings = spider.settings
        return cls.from_settings(settings)

    def document_exists(self, doc_id):
        cached_doc_existence = self.docs_existence_cache.get(doc_id)
        if cached_doc_existence is not None:
            return cached_doc_existence

        doc_existence = False
        try:
            doc = self.client.get_document(self.db_name, self.col_name, doc_id)
            doc_existence = True
        except DocumentDotExist:
            doc_existence = False
        
        self.docs_existence_cache[doc_id] = doc_existence
        return doc_existence

    def request_seen(self, request):
        """Returns True if request was already seen.
        Parameters
        ----------
        request : scrapy.http.Request
        Returns
        -------
        bool
        """
        fp = self.request_fingerprint(request)
        if fp in self.visit_cache:
            return True
        
        doc_id = self.get_doc_id(request)
        doc_existence = doc_id and self.document_exists(doc_id)

        self.visit_cache.add(fp)
        return doc_existence

    def get_doc_id(self, request):
        if 'item' in request.meta and self.id_field:
            item = request.meta['item']
            item_id = item.get(self.id_field)
            if item_id:
                return item_id

        if self.id_mapper:
            id_ = self.id_mapper(request)
            logger.debug(f'id for request {request.method} {request.url} is {id_}')
            return id_


    def request_fingerprint(self, request):
        """Returns a fingerprint for a given request.
        Parameters
        ----------
        request : scrapy.http.Request
        Returns
        -------
        str
        """
        return request_fingerprint(request)

    def open(self):
        #self.client.create
        pass

    def close(self, reason=''):
        pass

    def clear(self):
        pass

    def log(self, request, spider):
        if self.debug:
            msg = "Filtered duplicate request: %(request)s"
            self.logger.debug(msg, {'request': request}, extra={'spider': spider})
        elif self.logdupes:
            msg = ("Filtered duplicate request: %(request)s"
                   " - no more duplicates will be shown"
                   " (see DUPEFILTER_DEBUG to show all duplicates)")
            self.logger.debug(msg, {'request': request}, extra={'spider': spider})
            self.logdupes = False

        spider.crawler.stats.inc_value('dupefilter/filtered', spider=spider)
