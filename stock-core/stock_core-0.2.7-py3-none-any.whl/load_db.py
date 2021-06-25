import os
import re
import pickle
import pymongo
import platform
from collections import OrderedDict
import pandas as pd
from sqlalchemy import create_engine, text
from stock_core.nfscrapy import scraper

import logging
logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(levelname)s: [%(name)s] %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.setLevel(logging.WARNING)


class Settings:
    FILENAME = 'db_settings.pickle'
    FULL_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), FILENAME)
    pickle_template = {'mongo_addr': '',
                       'sqlite_path': '',
                       'activated_db': []}

    def __init__(self, echo=False):
        self.echo = echo
        self.contents = self._load()

    def set_mongo(self, mongo_addr):
        self.contents['mongo_addr'] = mongo_addr
        self.contents['activated_db'].append('mongo')
        self._refresh()

    def unset_mongo(self):
        self.contents['mongo_addr'] = ''
        try:
            self.contents['activated_db'].remove('mongo')
        except ValueError:
            pass
        self._refresh()

    def set_sqlite(self, sqlite_path):
        self.contents['sqlite_path'] = sqlite_path
        self.contents['activated_db'].append('sqlite')
        self._refresh()

    def unset_sqlite(self):
        self.contents['sqlite_path'] = ''
        try:
            self.contents['activated_db'].remove('sqlite')
        except ValueError:
            pass
        self._refresh()

    def get_settings(self) -> dict:
        if self.echo:
            print(self)
        return self.contents

    def clear_setting(self):
        self.unset_mongo()
        self.unset_sqlite()
        print('Deactivated mongodb and sqlite3.')

    def _refresh(self):
        self._save()
        self.contents = self._load()
        if self.echo:
            print(self)

    def _load(self) -> dict:
        try:
            with open(self.FULL_PATH, "rb") as fr:
                obj = pickle.load(fr)
                logger.debug(f'Load from pickle : {obj}')
                return obj
        except (EOFError, FileNotFoundError) as e:
            logger.error(e)
            with open(self.FULL_PATH, "wb") as fw:
                pickle.dump(self.pickle_template, fw)
            with open(self.FULL_PATH, "rb") as fr:
                obj = pickle.load(fr)
                logger.debug(f'Load from pickle : {obj}')
                return obj

    def _save(self):
        # 중복 등록되는 것을 방지하기 위해 집합을 사용한다.
        self.contents['activated_db'] = list(set(self.contents['activated_db']))
        logger.debug(f'Save to pickle : {self.contents}')
        with open(self.FULL_PATH, "wb") as fw:
            pickle.dump(self.contents, fw)

    def set_default_mongo_if_not_preset(self):
        if 'mongo' in self.contents['activated_db']:
            if self.echo:
                print(self)
        else:
            default_addr = 'mongodb://localhost:27017'
            print(f"You should set db first. We will set mongo db on {default_addr}")
            self.set_mongo(default_addr)
            print(self)

    def set_default_sqlite_if_not_preset(self):
        if 'sqlite' in self.contents['activated_db']:
            if self.echo:
                print(self)
        else:
            if 'Windows' in platform.platform():
                default_addr = 'C:\\_db'
            elif 'Linux' in platform.platform():
                default_addr = 'home/hj3415/Stock/_db'
            else:
                raise
            print(f"You should set db first. We will make sqlite3 db on {default_addr}")
            self.set_sqlite(default_addr)
            print(self)

    def __str__(self):
        return (f"mongo_addr : {self.contents['mongo_addr']}\n"
                f"sqlite_path : {self.contents['sqlite_path']}\n"
                f"activated_db : {self.contents['activated_db']}")


class MI:
    """
    mongodb에 저장된 market index를 가져오는 클래스
    <<구조>>
    데이터베이스 - mi
    컬렉션 - aud, chf, gbond3y, gold, kosdaq, kospi, sp500, usdkrw, wti, avgper, yieldgap, silver
    도큐멘트 - date, value
    """
    col_list = ('aud', 'chf', 'gbond3y', 'gold', 'silver', 'kosdaq', 'kospi', 'sp500', 'usdkrw', 'wti', 'avgper', 'yieldgap')

    def __init__(self, col=None):
        self.setting = Settings()
        if 'mongo' not in self.setting.contents['activated_db']:
            default_addr = 'mongodb://localhost:27017'
            logger.warning(f"You should register mongodb first. We will make db on {default_addr}")
            self.setting.set_mongo(default_addr)
        # mongodb에 연결
        mongo_addr = self.setting.contents['mongo_addr']
        logger.info(f"mongodb addr : {mongo_addr}")
        self.db = pymongo.MongoClient(mongo_addr).mi
        logger.info(f'Set col : {col}')
        self.col = col

    def set_col(self, col):
        if col in self.col_list:
            logger.info(f'Set col : {self.col} -> {col}')
            self.col = col
        else:
            raise Exception(f'Invalid collection - {col}')

    def show_cols(self):
        print(f'cols : {sorted(self.db.list_collection_names())}')

    def drop_col(self):
        if self.col is None:
            raise Exception("drop_col -> col doesn't set yet.")
        else:
            print(f'<<< Drop {self.col} in {self.db} db >>>')
            self.show_cols()
            self.db[self.col].drop()
            self.show_cols()

    def show_docs(self):
        for item in self.db[self.col].find({}).sort('날짜', pymongo.DESCENDING):
            del item['_id']
            print(item)
        print(f'Total {self.db[self.col].count_documents({})} items')

    def get_recent(self) -> tuple:
        """
        리턴 - ('날짜', '값')
        """
        d = self.db[self.col].find({'date': {'$exists': True}}).sort('date', pymongo.DESCENDING).next()
        del d['_id']
        return d['date'], d['value']

    def yield_all(self) -> tuple:
        """
        리턴 - ('날짜', '값')
        """
        for record in self.db[self.col].find({'date': {'$exists': True}}).sort('date', pymongo.ASCENDING):
            del record['_id']
            yield record['date'], record['value']


class Corps:
    """
    mongodb에 저장된 재무데이터를 가져오는 클래스
    <<구조>>
    데이터베이스 - 6자리 코드명
    컬렉션 - c101, c103손익계산서qy, c103재무상태표qy, c103현금흐름표qy, c104qy, c106, c108
    도큐멘트참고
        - c106은 q와 y의 2개의 도큐먼트로 구성
        - c104는 중복되는 항목이 없어 2개의 페이지로 나눔
        - c103는 중복되는 항목이 있어 6개의 페이지로 나눔
    """
    COL_LIST = ('c101', 'c104y', 'c104q', 'c106', 'c108',
                'c103손익계산서q', 'c103재무상태표q', 'c103현금흐름표q',
                'c103손익계산서y', 'c103재무상태표y', 'c103현금흐름표y')

    @staticmethod
    def _validate_db_name(dbname: str) -> bool:
        import re
        # db 이름이 6자리 숫자인지 확인
        p = re.compile('^\d{6}$')
        if p.match(dbname):
            return True
        else:
            return False

    @staticmethod
    def get_all_dbs() -> list:
        db_setting = Settings()
        if 'mongo' in db_setting.contents['activated_db']:
            mongo_addr = db_setting.contents['mongo_addr']
            client = pymongo.MongoClient(mongo_addr)
            return_list = []
            for name in client.list_database_names():
                if Corps._validate_db_name(name):
                    return_list.append(name)
            return sorted(return_list)

    def __init__(self, code, col=None):
        """
        code:str
        col:str in [c101, c103손익계산서qy, c103재무상태표qy, c103현금흐름표qy, c104qy, c106, c108]
        """
        self.code = code
        self.setting = Settings()
        self.setting.set_default_mongo_if_not_preset()
        # mongodb 에 연결
        mongo_addr = self.setting.contents['mongo_addr']
        logger.info(f"mongodb addr : {mongo_addr}")
        self.client = pymongo.MongoClient(mongo_addr)
        if self._validate_db_name(code):
            logger.info(f'Set db : {code}')
            self.db = code
            logger.info(f'Set col : {col}')
            self.col = col
        else:
            raise ValueError(f'Invalid db name : {code}')

    def set_db(self, code):
        if self._validate_db_name(code):
            logger.info(f'Set db : {self.db} -> {code}')
            self.db = code
        else:
            raise ValueError(f'Invalid db name : {code}')

    def set_col(self, col):
        if col in self.COL_LIST:
            logger.info(f'Set col : {self.col} -> {col}')
            self.col = col
        else:
            raise ValueError(f'Invalid col name : {col}')

    def get_status(self) -> tuple:
        """
        현재 설정된 (db, col)을 반환한다. - ex)('005930', 'c103재무상태표q')
        """
        return self.db, self.col

    def show_cols(self):
        print(f'{self.db} cols : {sorted(self.client[self.db].list_collection_names())}')

    def drop_all_dbs(self):
        print(f'<<< Drop all {len(self.client.list_database_names()) - 3} corp dbs >>>')
        print(self.get_all_dbs())
        for db in self.client.list_database_names():
            if self._validate_db_name(db):
                self.client.drop_database(db)
                print('.', end='')
        print('')
        print(self.get_all_dbs())

    def drop_col(self):
        if self.col is None:
            raise Exception("drop_col -> col doesn't set yet.")
        else:
            print(f'<<< Drop {self.col} in {self.db} db >>>')
            self.show_cols()
            self.client[self.db][self.col].drop()
            self.show_cols()

    def drop_db(self):
        print(f'<<< Drop {self.db} db >>>')
        print(self.get_all_dbs())
        self.client.drop_database(self.db)
        print(self.get_all_dbs())

    def show_docs(self):
        if self.col is None:
            raise Exception("show_docs -> col doesn't set yet.")
        else:
            for item in self.client[self.db][self.col].find({}):
                import pprint
                del item['_id']
                pprint.pprint(item)
            print(f'Total {self.client[self.db][self.col].count_documents({})} items')

    def find_c101(self, date: str) -> dict:
        """
        date 입력형식 예 - 20201011(6자리숫자)
        """
        p = re.compile('^20[0-9][0-9][0,1][0-9][0-3][0-9]$')
        if p.match(date) is None:
            raise Exception
        else:
            converted_date = date[:4]+'.'+date[4:6]+'.'+date[6:]
        try:
            d = self.client[self.db]['c101'].find({'date': converted_date}).next()
            del d['_id']
        except StopIteration:
            d = None
        return d

    def yield_all_c101(self) -> dict:
        for record in self.client[self.db]['c101'].find({'date': {'$exists': True}}).sort('date', pymongo.ASCENDING):
            del record['_id']
            yield record

    def find_c103(self, page: str, title: str, leave_ratio=False) -> dict:
        """
        page - ['손익계산서q', '재무상태표q', '현금흐름표q', '손익계산서y', '재무상태표y', '현금흐름표y']
        title - 항목 타이틀, 중복되는 경우(ex-배당금 수입)는 값을 합친다.
        leave_ratio - 전분기또는 전년대비를 남길것인가 삭제할 것인가
        """
        page_list = ['손익계산서q', '재무상태표q', '현금흐름표q', '손익계산서y', '재무상태표y', '현금흐름표y']
        if page in page_list:
            '''
            c103의 경우는 항목의 이름이 동일한 경우가 있다.
            ex) 현금흐름표 -> 배당금수입
            '''
            datas = self.client[self.db]['c103'+page].find({'항목': title})
            if datas is None:
                return {}
            else:
                # 인자로 c103의 딕셔너리를 받으면 서로 값을 합쳐서 반환
                return_dict = {}
                for data in datas:
                    #print(data)
                    del data['_id']
                    del data['항목']

                    # leave_ratio -> 전분기대비 또는 전년대비를 남길것인가 삭제할 것인가..
                    # 데이터의 갯수가 1이상에서 비율의 합은 의미가 없어 삭제한다.
                    if leave_ratio is False or self.client[self.db]['c103'+page].count_documents({'항목': title}) > 1:
                        del_targets = []
                        # 전년대비, 전년대비1처럼 복수의 갯수를 처리하기 위해
                        for key, value in data.items():
                            if key.startswith('전'):
                                del_targets.append(key)
                        for del_target in del_targets:
                            del data[del_target]

                    # 각 분기또는 연도별자료를 합하는 알고리즘
                    for key in data.keys():
                        import numpy as np
                        if np.isnan(data.get(key)):
                            continue
                        else:
                            return_dict[key] = return_dict.get(key, 0) + data.get(key)
                return return_dict
        else:
            raise Exception(f'Invalid page..{page}')

    def find_c104(self, period: str, title: str, leave_ratio=False) -> dict:
        """
        period - ['q', 'y']
        title - 항목
        leave_ratio - 전분기또는 전년대비를 남길것인가 삭제할 것인가
        """
        period_list = ['q', 'y']
        if period in period_list:
            data = self.client[self.db]['c104'+period].find_one({'항목': title})
            logger.info(data)
            if data is None:
                return {}
            else:
                del data['_id']
                del data['항목']
                if leave_ratio:
                    pass
                else:
                    del_targets = []
                    for key, value in data.items():
                        if key.startswith('전'):
                            del_targets.append(key)
                    for del_target in del_targets:
                        del data[del_target]
                return data
        else:
            raise Exception(f'Invalid page..{period}')

    def find_c106(self, period, title) -> dict:
        """
        period - ['q', 'y']
        title - 항목 타이틀
        """
        # c104와 저장 방식의 차이로 y, q가 함께 c106 컬렉션의 도큐먼트로 저장되어 있다.
        period_list = ['q', 'y']
        if period in period_list:
            page_dict = self.client[self.db]['c106'].find_one({'title': 'c106' + period})
            logger.debug(page_dict)
            if page_dict is None:
                return {}
            else:
                return page_dict[title]
        else:
            raise Exception(f'Invalid page..{period}')

    def get_recent(self) -> list:
        """
        c101또는 c108의 최근값을 리스트로 반환한다.
        c108을 위해서 딕셔너리를 포함하는 리스트로 반환함.
        따라서 c101은 리스트를 한번 벗겨내서 사용해야함.
        """
        # c108을 위해서 딕셔너리를 포함하는 리스트로 반환함. c101은 리스트를 한번 벗겨내서 사용해야함.
        if self.col == 'c101':
            try:
                self.rc101 = self._recent_c101()[0]
            except StopIteration:
                # 데이터베이스에 c101자료가 없는 경우는 직접 스크래핑을 시도한다.
                scraper.run('c101', [self.code, ])
                self.set_col('c101')
                self.rc101 = self._recent_c101()[0]
            logger.debug(f'rc101:{self.rc101}')
            return [self.rc101, ]
        elif self.col == 'c108':
            return self._recent_c108()
        else:
            raise Exception('This method can work when collection set c101 or c108')

    def _recent_c108(self) -> list:
        if self.client[self.db]['c108'].count_documents({'날짜': {'$exists': True}}) == 0:
            return []
        else:
            recent_date = self.client[self.db]['c108'].find({'날짜': {'$exists': True}}).sort('날짜', pymongo.DESCENDING).next()['날짜']
            return_list = []
            for recent_c108 in self.client[self.db]['c108'].find({'날짜': {'$eq': recent_date}}):
                del recent_c108['_id']
                return_list.append(recent_c108)
            return return_list

    def _recent_c101(self) -> list:
        # 리턴값의 일관성을 위해서 list로 한번 포장한다.
        d = self.client[self.db]['c101'].find({'date': {'$exists': True}}).sort('date', pymongo.DESCENDING).next()
        del d['_id']
        return [d, ]

    def sum_recent_4q(self, title) -> tuple:
        """
        c103q 또는 c104q 한정 해당 타이틀의 최근 4분기의 합을 (계산된 4분기 중 최근분기, 총합)의 튜플형식으로 반환한다.
        """
        if self.col is None:
            raise Exception("drop_col -> col doesn't set yet.")

        if self.col.startswith('c103') and self.col.endswith('q'):
            # reverse = False 이면 오래된것부터 최근순으로 정렬한다.
            od_q = OrderedDict(sorted(self.find_c103(self.col[4:], title, leave_ratio=False).items(), reverse=False))
            if len(od_q) < 4:
                # q의 값이 4개 이하이면 그냥 최근 연도의 값으로 반환한다.
                od_y = OrderedDict(sorted(self.find_c103(self.col[4:-1]+'y', title, leave_ratio=False).items(), reverse=False))
                logger.debug(f"{self.col[:-1]+'y'} {title} {od_y}")
                try:
                    logger.debug(f"{self.col[:-1] + 'y'} {title} {list(od_y.items())[-1]}")
                    return list(od_y.items())[-1]
                except IndexError:
                    return None, 0
        elif self.col.startswith('c104') and self.col.endswith('q'):
            od_q = OrderedDict(sorted(self.find_c104(self.col[4:], title, leave_ratio=False).items(), reverse=False))
            if len(od_q) < 4:
                od_y = OrderedDict(sorted(self.find_c104(self.col[4:-1]+'y', title, leave_ratio=False).items(), reverse=False))
                logger.debug(f"{self.col[:-1]+'y'} {title} {od_y}")
                try:
                    logger.debug(f"{self.col[:-1] + 'y'} {title} {list(od_y.items())[-1]}")
                    return list(od_y.items())[-1]
                except IndexError:
                    return None, 0
        else:
            raise Exception(f'Invalid page..{self.col}')

        logger.debug(f"{self.col} {title} {od_q}")
        r_date = list(od_q.items())[-1][0]
        r_value = 0
        for i in range(4):
            # last = True 이면 최근의 값부터 꺼낸다.
            d, v = od_q.popitem(last=True)
            logger.debug(f'd:{d} v:{v}')
            r_value += v
        return r_date, round(r_value, 2)        # value_list[0][0] -> 합산 기준이 되는 최근값

    def latest_value(self, title) -> tuple:
        """
        c103, c104한정 title에 해당하는 가장 최근의 값을 ('2020/09', 39617.5)와 같은 튜플로 반환한다.
        """
        if self.col is None:
            raise Exception("drop_col -> col doesn't set yet.")

        if self.col.startswith('c103'):
            # reverse = False 이면 오래된것부터 최근순으로 정렬한다.
            od = OrderedDict(sorted(self.find_c103(self.col[4:], title, leave_ratio=False).items(), reverse=False))
            logger.debug(f"{self.col} {title} {od}")
            try:
                logger.debug(f"{self.col} {title} {list(od.items())[-1]}")
                return list(od.items())[-1]
            except IndexError:
                return None, 0
        elif self.col.startswith('c104'):
            od = OrderedDict(sorted(self.find_c104(self.col[4:], title, leave_ratio=False).items(), reverse=False))
            logger.debug(f"{self.col} {title} {od}")
            try:
                logger.debug(f"{self.col} {title} {list(od.items())[-1]}")
                return list(od.items())[-1]
            except IndexError:
                return None, 0
        else:
            raise Exception(f'Invalid page..{self.col}')


class Dart:
    sqlite_filename = 'dart.db'
    tablename_in_corps = 'dart'

    def __init__(self):
        self.setting = Settings()

    def get_corp_df_from_mongo(self, code: str) -> pd.DataFrame:
        # mongodb에 연결
        self.setting.set_default_mongo_if_not_preset()
        mongo_addr = self.setting.contents['mongo_addr']
        logger.info(f"mongodb addr : {mongo_addr}")
        cluster = pymongo.MongoClient(mongo_addr)
        mongodb = cluster[code]

        # 컬렉션 이름은 dart임
        col = mongodb.dart
        df = pd.DataFrame(list(col.find())).drop(columns=['_id'])
        return df

    def get_date_df_from_mongo(self, edate: str, title=None) -> pd.DataFrame:
        # mongodb에 연결
        self.setting.set_default_mongo_if_not_preset()
        mongo_addr = self.setting.contents['mongo_addr']
        logger.info(f"mongodb addr : {mongo_addr}")
        cluster = pymongo.MongoClient(mongo_addr)
        mongodb = cluster.dart

        # 컬렉션 이름은 날짜임 - 20201011
        col = mongodb[edate]
        try:
            df = pd.DataFrame(list(col.find())).drop(columns=['_id'])
        except KeyError:
            return pd.DataFrame()

        if title is not None:
            df = df[df['report_nm'].str.contains(title)]
        return df

    # 본함수는 sqlite에서 df를 받아옴
    def get_date_df_from_sqlite(self, edate: str, title=None) -> pd.DataFrame:
        """
        analysis를 제작하는 동안 dart를 매번 받아오지 않도록 하는 개발전용 함수
        """
        def make_engine(db_path, fname, echo=False):
            if not os.path.isdir(db_path):
                os.makedirs(db_path)
            dsn = f"sqlite:///{os.path.join(db_path, fname)}"
            return create_engine(dsn, echo=echo)

        self.setting.set_default_sqlite_if_not_preset()
        sqlite_path = self.setting.contents['sqlite_path']
        logger.info(f"sqlite3 path : {sqlite_path}")
        engine = make_engine(db_path=sqlite_path, fname=self.sqlite_filename)

        df = pd.read_sql_query(text(f"SELECT * FROM t{edate}"), con=engine)
        if title is not None:
            df = df[df['report_nm'].str.contains(title)]
        return df


class Noti:
    """
    노티된 Dart 레코드를 받아오는 클래스
    """
    sqlite_filename = 'noti_record.db'
    mongo_db_name = 'noti'
    mongo_col_name = 'noti'
    tablename = 'noti'

    def __init__(self):
        self.setting = Settings()

    def get_record_from_mongo(self) -> pd.DataFrame:
        # mongodb에 연결
        self.setting.set_default_mongo_if_not_preset()
        mongo_addr = self.setting.contents['mongo_addr']
        logger.info(f"mongodb addr : {mongo_addr}")
        cluster = pymongo.MongoClient(mongo_addr)
        mongodb = cluster[self.mongo_db_name]

        # 컬렉션 이름은 dart임
        col = mongodb[self.mongo_col_name]
        try:
            df = pd.DataFrame(list(col.find())).drop(columns=['_id'])
        except KeyError:
            df = pd.DataFrame()
        return df

    def get_record_from_sqlite(self) -> pd.DataFrame:
        def make_engine(db_path, fname, echo=False):
            if not os.path.isdir(db_path):
                os.makedirs(db_path)
            dsn = f"sqlite:///{os.path.join(db_path, fname)}"
            return create_engine(dsn, echo=echo)

        self.setting.set_default_sqlite_if_not_preset()
        sqlite_path = self.setting.contents['sqlite_path']
        logger.info(f"sqlite3 path : {sqlite_path}")
        engine = make_engine(db_path=sqlite_path, fname=self.sqlite_filename)

        df = pd.read_sql_query(text(f"SELECT * FROM t{self.tablename}"), con=engine)
        return df

