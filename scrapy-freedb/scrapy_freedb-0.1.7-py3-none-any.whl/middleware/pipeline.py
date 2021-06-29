import logging
from .freedb import FreedbClient


logger = logging.getLogger(__name__)


class FreedbSaveItemPipeline():
    def __init__(self, db_name, col_name, client: FreedbClient, id_field, exist_policy=None):
        self.db_name = db_name
        self.col_name = col_name
        self.client = client
        self._id_field = id_field
        self.exist_policy = exist_policy
    
    def process_item(self, item, spider):
        logger.debug('FreedbSaveItemPipeline process_item')
        item_dict = dict(item)
        if 'id' not in item_dict and self._id_field:
            item_dict['id'] = item_dict.get(self._id_field)
        self.client.save_document(self.db_name, self.col_name, item_dict, exist=self.exist_policy)
        spider.logger.debug('FreedbSaveItemPipeline process_item done')
        return item

    @classmethod
    def from_crawler(cls, crawler):
        logger.info('FreedbSaveItemPipeline.from_crawler')
        settings = crawler.settings
        base_url = settings.get("FREEDB_BASEURL")
        token = settings.get('FREEDB_TOKEN')
        db_name = settings.get('FREEDB_DBNAME')
        col_name = settings.get('FREEDB_COLNAME')
        id_field = settings.get('FREEDB_ID_FIELD')
        exist_policy = settings.get('FREEDB_EXIST_POLICY')
        
        client = FreedbClient(base_url, token)
        return cls(db_name, col_name, client, id_field, exist_policy=exist_policy)
