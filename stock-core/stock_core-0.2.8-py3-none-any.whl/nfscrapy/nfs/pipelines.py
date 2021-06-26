# reference from https://livedata.tistory.com/27?category=1026425 (scrapy pipeline usage)
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
from load_db import Settings, Corps

import datetime
from pymongo import MongoClient
from . import items
from sqlalchemy.orm import sessionmaker
from .sqlite_db import make_engine, save_df_to_db, stamping, Base, C101

import logging
logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(levelname)s: [%(name)s] %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.setLevel(logging.WARNING)


class C101Pipeline:
    # c101에서 eps, bps, per, pbr을 수동으로 계산하여 입력하는 파이프라인
    def process_item(self, item, spider):
        if isinstance(item, items.C101items):
            print(f"\tIn the C101 pipeline...custom calculating EPS, BPS, PER, PBR")
            logger.info('*** Start c101 pipeline ***')
            logger.info(f"Raw data - EPS:{item['EPS']} BPS:{item['BPS']} PER:{item['PER']} PBR:{item['PBR']}")
            # eps, bps, per, pbr을 직접 계산해서 바꾸기 위해 c104 page를 찾는다.
            try:
                logger.info('Try to get c104 page for calculate values..')
                mydb_c104q = Corps(item['코드'], 'c104q')
                cal_eps = mydb_c104q.sum_recent_4q('EPS')[1]     # 최근 4분기 eps값을 더한다.
                cal_bps = mydb_c104q.latest_value('BPS')[1]      # 마지막 분기 bps값을 찾는다.
                # per, pbr을 구하는 람다함수
                cal_ratio = (lambda eps_bps, pprice:
                             None if eps_bps is None or eps_bps == 0 else round(int(pprice) / int(eps_bps), 2))
                cal_per = cal_ratio(cal_eps, item['주가'])
                cal_pbr = cal_ratio(cal_bps, item['주가'])
                logger.info(f"After calc data - EPS:{cal_eps} BPS:{cal_bps} PER:{cal_per} PBR:{cal_pbr}")
                logger.info(f"*** End c101 calculation pipeline {item['코드']} ***")
            except:
                logger.warning("Error on calculating custom EPS, BPS, PER, PBR, maybe DB hasn't c104q collection.")
                logger.warning(f"We will use default scraped values -  EPS:{item['EPS']} BPS:{item['BPS']} PER:{item['PER']} PBR:{item['PBR']}")
                return item
            item['EPS'], item['BPS'], item['PER'], item['PBR'] = cal_eps, cal_bps, cal_per, cal_pbr
        return item


class MongoPipeline:
    # 데이터 베이스에 저장하는 파이프라인
    def __init__(self):
        self.setting = Settings()
        if 'mongo' in self.setting.contents['activated_db']:
            # mongodb에 연결
            mongo_addr = self.setting.contents['mongo_addr']
            logger.info(f"mongodb addr : {mongo_addr}")
            self.cluster = MongoClient(mongo_addr)

    def process_item(self, item, spider):
        if 'mongo' in self.setting.contents['activated_db']:
            print(f"\tIn the MongoPipeline pipeline...{item['코드']} ({spider.name} _save to db)")
            mongodb = self.cluster[item['코드']]
            if isinstance(item, items.C101items):
                # sava c101 data to db
                col = mongodb.c101
                # 스크랩한 날짜이후의 데이터는 조회해서 먼저 삭제한다.
                query = {'date': {"$gte": item['date']}}
                col.delete_many(query)
                data = {
                    "date": item['date'],
                    "코드": item['코드'],
                    "종목명": item['종목명'],
                    "업종": item['업종'],
                    "주가": item['주가'],
                    "거래량": item['거래량'],
                    "EPS": item['EPS'],
                    "BPS": item['BPS'],
                    "PER": item['PER'],
                    "업종PER": item['업종PER'],
                    "PBR": item['PBR'],
                    "배당수익률": item['배당수익률'],
                    "최고52주": item['최고52주'],
                    "최저52주": item['최저52주'],
                    "거래대금": item['거래대금'],
                    "시가총액": item['시가총액'],
                    "베타52주": item['베타52주'],
                    "발행주식": item['발행주식'],
                    "유통비율": item['유통비율'],
                    "intro": item['intro1'] + item['intro2'] + item['intro3']
                }
                col.insert_one(data)
            elif isinstance(item, items.C103items):
                '''
                각 c103의 3개페이지를 한 컬렉션에 담는것은 항목의 이름이 유일하지 않기 때문에 불가능함.
                따라서 예전처럼 6개의 컬렉션에 담는것으로 유지
                '''
                # sava c103 data to db
                title = 'c103' + item['title']  # collection title - c103손익계산서q c103재무상태표y
                col = mongodb[title]
                data = item['df'].to_dict('records')  # [{'col1': 1, 'col2': 0.5}, {'col1': 2, 'col2': 0.75}]
                data.append({'stamp': datetime.datetime.utcnow()})  # data가 리스트라서 append 사용
                col.delete_many({})  # delete all documents in a collection
                col.insert_many(data)
            elif isinstance(item, items.C104items):
                '''
                c104는 y와 q의 두개 컬렉션으로 담기로함.
                저장시 동시에 저장되는 이전데이터를 삭제하는 것을 방지하기 위해 stamp를 검사함
                '''
                # sava c104 data to db
                if item['title'].endswith('y'):
                    col_name = 'c104y'
                elif item['title'].endswith('q'):
                    col_name = 'c104q'
                else:
                    raise
                col = mongodb[col_name]
                data = item['df'].to_dict('records')  # [{'col1': 1, 'col2': 0.5}, {'col1': 2, 'col2': 0.75}]
                data.append({'stamp': datetime.datetime.utcnow()})  # data가 리스트라서 append 사용
                # stamp를 검사하여 12시간전보다 이전에 저장된 자료가 있으면 삭제한다.
                if col.find_one({'stamp': {'$lt': datetime.datetime.utcnow() - datetime.timedelta(days=.5)}}):
                    col.delete_many({})  # delete all documents in a collection
                col.insert_many(data)
            elif isinstance(item, items.C106items):
                # sava c106 data to db
                title = 'c106'+item['title']        # document title - c106y or c106q
                col = mongodb['c106']
                item['df'].set_index('항목', inplace=True)
                data = item['df'].to_dict('index')   # {'row1': {'col1': 1, 'col2': 0.5}, 'row2': {'col1': 2, 'col2': 0.75}}
                data['title'] = title
                data['stamp'] = datetime.datetime.utcnow()      # timestamp
                col.delete_one({'title': title})     # 이전 도큐먼트를 삭제한다.
                col.insert_one(data)
            elif isinstance(item, items.C108items):
                # sava c108 data to db
                col = mongodb['c108']
                data = item['df'].to_dict('records')  # [{'col1': 1, 'col2': 0.5}, {'col1': 2, 'col2': 0.75}]
                col.delete_many({})  # delete all documents in a collection
                if len(data) == 0:
                    col.insert_one({})
                else:
                    data.append({'stamp': datetime.datetime.utcnow()})  # data가 리스트라서 append 사용
                    col.insert_many(data)
            return item
        else:
            print(f"\tIn the MongoPipeline...skipping save to db ", flush=True)
            return item


class SqlitePipeline:
    def process_item(self, item, spider):
        def save_and_stamping(name, title, df):
            tablename = ''.join([name, title])
            save_df_to_db(engine, df, tablename)
            stamping(session, tablename)

        setting = Settings()
        if 'sqlite' in setting.contents['activated_db']:
            print(f"\tIn the SqlitePipeline...{item['코드']} ({spider.name} save to db)", flush=True)
            logger.info('*** Start DB pipeline for saving to db ***')

            # making engine
            sqlite_path = setting.contents['sqlite_path']
            logger.debug(f"sqlite3 path : {sqlite_path}")
            engine = make_engine(sqlite_path, item['코드'])

            Base.metadata.create_all(engine)
            Session = sessionmaker(bind=engine)
            session = Session()

            # c101의 경우
            if isinstance(item, items.C101items):
                # sava c101 data to db
                session.query(C101).filter(C101.date >= item['date']).delete()
                c101 = C101(date=item['date'], 코드=item['코드'], 종목명=item['종목명'],
                                     업종=item['업종'], 주가=item['주가'], 거래량=item['거래량'],
                                     EPS=item['EPS'], BPS=item['BPS'], PER=item['PER'],
                                     업종PER=item['업종PER'], PBR=item['PBR'], 배당수익률=item['배당수익률'],
                                     최고52주=item['최고52주'], 최저52주=item['최저52주'], 거래대금=item['거래대금'],
                                     시가총액=item['시가총액'], 베타52주=item['베타52주'], 발행주식=item['발행주식'],
                                     유통비율=item['유통비율'], intro1=item['intro1'], intro2=item['intro2'],
                                     intro3=item['intro3'])
                session.add(c101)
                logger.info(session.query(C101).filter_by(date=item['date']).first())
                session.commit()
            # c103의 경우
            elif isinstance(item, items.C103items):
                logger.info(f"item['title']: {item['title']}")
                save_and_stamping('c103', item['title'], item['df'])
            # c104의 경우
            elif isinstance(item, items.C104items):
                logger.info(f"item['title']: {item['title']}")
                save_and_stamping('c104', item['title'], item['df'])
            # c106의 경우
            elif isinstance(item, items.C106items):
                logger.info(f"item['title']: {item['title']}")
                save_and_stamping('c106', item['title'], item['df'])
            # c108의 경우
            elif isinstance(item, items.C108items):
                save_and_stamping('c108', '', item['df'])
            logger.info(f"*** End DB pipeline {item['코드']} ***")
            return item
        else:
            print(f"\tIn the SqlitePipeline...skipping save to db ", flush=True)
            return item
