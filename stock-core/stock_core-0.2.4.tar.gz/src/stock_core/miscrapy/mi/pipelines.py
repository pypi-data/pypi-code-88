import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
from load_db import Settings

from pymongo import MongoClient
from sqlalchemy.orm import sessionmaker
from .sqlite_db import make_engine, Kospi, Kosdaq, Gbond3y, Sp500, Usdkrw, Wti, Aud, Chf, Gold, Base, Silver


import logging
logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(levelname)s: [%(name)s] %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.setLevel(logging.WARNING)


class MongoPipeline:
    def __init__(self):
        self.setting = Settings()
        if 'mongo' in self.setting.contents['activated_db']:
            # mongodb에 연결
            mongo_addr = self.setting.contents['mongo_addr']
            logger.info(f"mongodb addr : {mongo_addr}")
            self.db = MongoClient(mongo_addr).mi

    def process_item(self, item, spider):
        """
        아이템 구조
            title = scrapy.Field()
            date = scrapy.Field()
            value = scrapy.Field()
        """
        if 'mongo' in self.setting.contents['activated_db']:
            print(f"\tIn the MongoPipeline...{item['date']} ({item['title']} _save to db)", flush=True)
            logger.info('*** Start DB pipeline for saving to db ***')
            col = self.db[item['title']]
            query = {'date': {"$eq": item['date']}}
            col.delete_many(query)
            data = {
                "date": item['date'],
                "value": item['value'],
            }
            col.insert_one(data)
            logger.info(f"*** End DB pipeline {item['title']} ***")
            return item
        else:
            print(f"\tIn the MongoPipeline...skipping save to db ", flush=True)
            return item


class SqlitePipeline:
    def __init__(self):
        self.setting = Settings()
        if 'sqlite' in self.setting.contents['activated_db']:
            # sqlite3에 연결
            sqlite_path = self.setting.contents['sqlite_path']
            logger.info(f"sqlite3 path : {sqlite_path}")
            self.engine = make_engine(sqlite_path)

    def process_item(self, item, spider):
        """
        아이템 구조
            title = scrapy.Field()
            date = scrapy.Field()
            value = scrapy.Field()
        """
        if 'sqlite' in self.setting.contents['activated_db']:
            print(f"\tIn the SqlitePipeline...{item['date']} ({item['title']} _save to db)", flush=True)
            logger.info('*** Start DB pipeline for saving to db ***')
            Base.metadata.create_all(self.engine)
            Session = sessionmaker(bind=self.engine)
            session = Session()
            if item['title'] == 'kospi':
                mi_table = Kospi
            elif item['title'] == 'kosdaq':
                mi_table = Kosdaq
            elif item['title'] == 'gbond3y':
                mi_table = Gbond3y
            elif item['title'] == 'sp500':
                mi_table = Sp500
            elif item['title'] == 'usdkrw':
                mi_table = Usdkrw
            elif item['title'] == 'wti':
                mi_table = Wti
            elif item['title'] == 'aud':
                mi_table = Aud
            elif item['title'] == 'chf':
                mi_table = Chf
            elif item['title'] == 'gold':
                mi_table = Gold
            elif item['title'] == 'silver':
                mi_table = Silver
            else:
                raise Exception('Unknown Error')
            # 해당테이블에서 날짜에 해당하는 데이터를 쿼리한다.
            mi_item = session.query(mi_table).filter(mi_table.date == item['date']).first()
            logger.info(f'Query result : {mi_item}')
            if mi_item:
                setattr(mi_item, 'value', item['value'])
            else:
                session.add(mi_table(date=item['date'], value=item['value']))
            session.commit()
            logger.info(f"*** End DB pipeline {item['title']} ***")
            return item
        else:
            print(f"\tIn the SqlitePipeline...skipping save to db ", flush=True)
            return item
