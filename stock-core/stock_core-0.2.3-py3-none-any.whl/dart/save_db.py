import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from load_db import Settings, Dart, Noti
from nfscrapy.nfs import sqlite_db as nfs_db

import requests
import re
import time
import pandas as pd
from util_hj3415 import noti, utils

from sqlalchemy import create_engine, text
from sqlalchemy.exc import IntegrityError
from pymongo import MongoClient

import logging
logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(levelname)s: [%(name)s] %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.setLevel(logging.WARNING)


class MakeDF:
    """
    Dart의 양식대로 날짜 및 제목으로 아이템을 추출하여 데이터프레임으로 반환한다.
    sdate: 공시 검색 시작 날짜
    edate: 공시 검색 끝날짜 생략시 오늘날짜로 검색됨
    code: 종목코드
    title: 검색하고자하는 타이틀 문자열
    echo: echo
    """
    def __init__(self, sdate=None, edate=None, code=None, title=None, echo=True):
        self.setting = Settings()
        if sdate is not None:
            if not utils.chk_date_format_Ymd(sdate):
                raise Exception(f"Invalid date - {sdate}(YYYYMMDD)")
            else:
                self.sdate = sdate
        else:
            self.sdate = sdate
        if edate is not None:
            if not utils.chk_date_format_Ymd(edate):
                raise Exception(f"Invalid date - {edate}(YYYYMMDD)")
            else:
                self.edate = edate
        self.edate = edate
        self.code = code
        self.title = title
        self.echo = echo

    @staticmethod
    def islive_opendart() -> bool:
        # opendart 사이트의 연결여부 확인
        url = 'https://opendart.fss.or.kr/api/list.json'
        key = '?crtfc_key=f803f1263b3513026231f4eff69312165e6eda90'
        first_url = url + key
        try:
            r = requests.get(first_url, timeout=3).json()
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
            print("Connection Error on opendart.fss.or.kr..")
            noti.telegram_to(botname='dart', text="Connection Error on opendart.fss.or.kr..")
            return False
        return True

    @staticmethod
    def _make_first_url(sdate=None, edate=None, code=None, title=None, echo=True) -> str:
        def _match_title_with_title_code(t: str) -> str:
            logger.info('<<<  _match_title_with_title_code() >>>')
            if t is None:
                t_code = None
            elif t in ['분기보고서', '반기보고서', '사업보고서']:
                t_code = 'A'  # 정기공시
            elif t in ['무상증자결정', '자기주식취득결정', '자기주식처분결정', '유상증자결정', '전환사채권발행결정',
                           '신주인수권부사채권발행결정', '교환사채권발행결정', '회사합병결정', '회사분할결정']:
                t_code = 'B'  # 주요사항보고
            elif t in ['공급계약체결', '주식분할결정', '주식병합결정', '주식소각결정', '만기전사채취득', '신주인수권행사',
                           '소송등의', '자산재평가실시결정', '현물배당결정', '주식배당결정', '매출액또는손익구조', '주주총회소집결의']:
                t_code = 'I'  # 거래소공시
            elif t in ['공개매수신고서', '특정증권등소유상황보고서', '주식등의대량보유상황보고서']:
                t_code = 'D'  # 지분공시
            else:
                raise
            return t_code

        # 모든 인자를 생략할 경우 오늘 날짜의 공시 url를 반환한다.
        logger.info('<<<  _make_first_url() >>>')
        logger.info(f'corp_code : {code}\ttitle_code : {title}'
                    f'\tstart_date : {sdate}\tend_date : {edate}')

        title_code = _match_title_with_title_code(title)

        # 최종 url을 만들기 위한 문장 요소들
        url = 'https://opendart.fss.or.kr/api/list.json'
        key = '?crtfc_key=f803f1263b3513026231f4eff69312165e6eda90'
        is_last = f'&last_reprt_at=Y'
        page_no = f'&page_no=1'
        page_count = f'&page_count=100'
        start_date = f'&bgn_de={sdate}' if sdate else ''
        end_date = f'&end_de={edate}' if edate else ''
        corp_code = f'&corp_code={code}' if code else ''
        pblntf_ty = f'&pblntf_ty={title_code}' if title_code else ''

        first_url = url + key + is_last + page_no + page_count + start_date + end_date + corp_code + pblntf_ty
        logger.info(f'first url : {first_url}')
        if echo:
            print(f'\tDart first url : {first_url}')
        return first_url

    @staticmethod
    def _make_dart_list(first_url: str, echo=True) -> list:
        logger.info('<<<  _make_dart_list() start >>>')
        logger.info(f'first url : {first_url}')
        first_dict = requests.get(first_url).json()
        if first_dict['status'] != '000':
            raise Exception(first_dict['message'])
        total_page = first_dict['total_page']
        logger.info(f'total {total_page} page..')
        # reference from https://wikidocs.net/4308#match_1(정규표현식 사용)
        # [0-9]+ 숫자가 1번이상 반복된다는 뜻
        p = re.compile('&page_no=[0-9]+')
        list_raw_dict = []
        # 전체페이지만큼 반복하여 하나의 전체 공시리스트를 만들어 반환한다.
        if echo:
            print(f'\tExtracting all pages({total_page}) ', end='', flush=True)
        for i in range(total_page):
            each_page_url = p.sub(f'&page_no={i + 1}', first_url)
            if echo:
                print(f'{i + 1}..', end='', flush=True)
            list_raw_dict += requests.get(each_page_url).json()['list']
            time.sleep(1)
        if echo:
            print(f'total {len(list_raw_dict)} pre-filtered items..', flush=True)
        return list_raw_dict

    @staticmethod
    def _make_df(items_list: list) -> pd.DataFrame:
        logger.info('<<<  _make_df() start >>>')
        # 전체데이터에서 Y(유가증권),K(코스닥)만 고른다.
        # reference by https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#selection-by-callable
        yk_df = pd.DataFrame(items_list).loc[lambda df: df['corp_cls'].isin(['Y', 'K']), :]
        logger.info(f"Number of items before restricted('기재정정', '첨부정정', '자회사의', '종속회사의', '기타경영사항') : {len(yk_df)}")
        return yk_df

    def get_df(self, filtered=True) -> pd.DataFrame:
        """
        filtered: ['기재정정', '첨부정정', '자회사의', '종속회사의', '기타경영사항'] 이 타이틀에 포함되면 생략할지 결정
        :return: pd.Dataframe
        """

        # 공시는 오전 7시부터 오후 6시까지 나온다.
        logger.info('<<<  get_df() start >>>')

        # opendart 사이트의 연결여부 확인
        if not self.islive_opendart():
            return pd.DataFrame()

        filtered_words = ['기재정정', '첨부정정', '자회사의', '종속회사의', '기타경영사항']
        logger.info(f'restrict_words : {filtered_words}')
        if self.echo:
            print('>>>>> Making a dataframe from dart website..')
            print(f'\tSetting.. Code: {self.code}\tTitle:{self.title}\tStart date: {self.sdate}\tEnd date: {self.edate}')
        try:
            first_url = self._make_first_url(self.sdate, self.edate, self.code, self.title, self.echo)
            item_list = self._make_dart_list(first_url, self.echo)
            df = self._make_df(item_list)
        except:
            return pd.DataFrame()
        if self.title is not None:
            df = df[df['report_nm'].str.contains(self.title)]
        if filtered:
            for word in filtered_words:
                df = df[~df['report_nm'].str.contains(word)]
        if self.echo:
            print('*'*40, f'total {len(df)} items', '*'*40)
            print(df.to_string())
            print()
        return df

    def _make_edate_df(self) -> pd.DataFrame:
        """
        아래 두 데이터베이스 저장 함수를 위한 edate 날짜의 데이터프레임을 받아오는 함수.
        """
        if self.sdate is not None or self.code is not None or self.title is not None:
            logger.warning(f'We will ignore sdate({self.sdate}), code({self.code}), title({self.title}) argument')
        self.sdate = None
        self.code = None
        self.title = None
        return self.get_df()

    def get_edate_df_and_save_mongo(self) -> int:
        df = self._make_edate_df()

        # mongodb에 연결
        self.setting.set_default_mongo_if_not_preset()
        mongo_addr = self.setting.contents['mongo_addr']
        logger.info(f"mongodb addr : {mongo_addr}")
        cluster = MongoClient(mongo_addr)
        mongodb = cluster.dart

        print(f"Save dataframe to dart db and {self.edate} collection on mongodb ...")

        col = mongodb[self.edate]
        col.drop()
        col.insert_many(df.to_dict('records'))
        return len(df)

    def get_edate_df_and_save_sqlite(self) -> int:
        def make_engine(db_path, fname, echo=False):
            if not os.path.isdir(db_path):
                os.makedirs(db_path)
            dsn = f"sqlite:///{os.path.join(db_path, fname)}"
            return create_engine(dsn, echo=echo)

        df = self._make_edate_df()

        tablename = 't' + self.edate

        # sqlite3에 연결
        self.setting.set_default_sqlite_if_not_preset()
        sqlite_path = self.setting.contents['sqlite_path']
        logger.info(f"sqlite3 path : {sqlite_path}")
        engine = make_engine(db_path=sqlite_path, fname=Dart.sqlite_filename)

        # 전체 공시 마감후 저녁 8시경 한번 실행함.
        if df.empty:
            print('Dataframe is empty..So we will skip saving db..')
            return 0

        # 테이블을 저장한다.
        print(f"Save dataframe on {tablename} table on {os.path.join(sqlite_path, Dart.sqlite_filename)}...", flush=True)
        df.to_sql(tablename, con=engine, index=False, if_exists='replace')
        return len(df)


class SaveToEachCorps:
    """
    data dict의 구조
    data = {'code': dart_dict['code'],
            'rcept_no': dart_dict['rno'],
            'rcept_dt': dart_dict['rdt'],
            'report_nm': dart_dict['rtitle'],
            'point': cls.point,
            'text': cls.text,
            'is_noti': is_noti}
    Analysis에서 분석한 data를 하나씩 개별 종목의 테이블에 저장하는 클래스
    """
    def __init__(self, data: dict):
        self.setting = Settings()
        logger.info(data)
        self.data = data

    def to_mongo(self):
        # mongodb에 연결
        self.setting.set_default_mongo_if_not_preset()
        mongo_addr = self.setting.contents['mongo_addr']
        logger.info(f"mongodb addr : {mongo_addr}")
        cluster = MongoClient(mongo_addr)
        mongodb = cluster[self.data['code']]

        print(f"Save dart to {self.data['code']} collection on mongodb ...")
        col = mongodb[Dart.tablename_in_corps]
        # 이전에 저장된 rcept_no가 있으면 삭제한다.
        query = {'rcept_no': {"$eq": self.data['rcept_no']}}
        col.delete_many(query)
        data = {'rcept_no': self.data['rcept_no'],
                'rcept_dt': self.data['rcept_dt'],
                'report_nm': self.data['report_nm'],
                'point': self.data['point'],
                'text': self.data['text'],
                'is_noti': 1 if self.data['is_noti'] else 0}
        col.insert_one(data)

    def to_sqlite(self):
        # sqlite3에 연결
        self.setting.set_default_sqlite_if_not_preset()
        sqlite_path = self.setting.contents['sqlite_path']
        logger.info(f"sqlite3 path : {sqlite_path}")
        engine = nfs_db.make_engine(db_path=sqlite_path, code=self.data['code'])

        print(f"Save dart to {self.data['code']}.db on {os.path.basename(sqlite_path)} directory...")
        with engine.connect() as conn:
            # t+코드명의 테이블이 없으면 만든다.
            conn.execute(text(f"""CREATE TABLE IF NOT EXISTS {Dart.tablename_in_corps} (
                                                    rcept_no VARCHAR(14) NOT NULL PRIMARY KEY, 
                                                    rcept_dt VARCHAR(8), 
                                                    report_nm VARCHAR, 
                                                    point INT,
                                                    text VARCHAR,
                                                    is_noti INT
                                                    );"""))
            try:
                # 텍스트 내부에 작은따옴표를 sqlite로 저장하기 위해서 작은따옴표를 하나더 붙인다. https://lovedb.tistory.com/331
                c_text = self.data['text'].replace("'", "''")
                conn.execute(text(f"INSERT INTO {Dart.tablename_in_corps} VALUES "
                                  f"({self.data['rcept_no']}, "
                                  f"{self.data['rcept_dt']}, "
                                  f"'{self.data['report_nm']}', "
                                  f"{self.data['point']}, "
                                  f"'{c_text}', "
                                  f"{1 if self.data['is_noti'] else 0});"))
                logger.info(f"stock_code : {self.data['code']}, "
                            f"table : {Dart.tablename_in_corps}"
                            f"rcept_no : {self.data['rcept_no']}, "
                            f"rcept_dt : {self.data['rcept_dt']}, "
                            f"report_nm :{self.data['report_nm']}, "
                            f"point :{self.data['point']}, "
                            f"text :{self.data['text']}, "
                            f"is_noti : {1 if self.data['is_noti'] else 0}")
            except IntegrityError:
                logger.info(f"stock_code : {self.data['code']}, rcept_no : {self.data['rcept_no']} - saved already.")


class SaveNotiRecord:
    """
    data dict의 구조
    data = {'code': dart_dict['code'],
            'rcept_no': dart_dict['rno'],
            'rcept_dt': dart_dict['rdt'],
            'report_nm': dart_dict['rtitle'],
            'point': cls.point,
            'text': cls.text}
    """
    def __init__(self, data: dict):
        self.setting = Settings()
        logger.info(data)
        self.data = data

    def to_mongo(self):
        # mongodb에 연결
        self.setting.set_default_mongo_if_not_preset()
        mongo_addr = self.setting.contents['mongo_addr']
        logger.info(f"mongodb addr : {mongo_addr}")
        cluster = MongoClient(mongo_addr)
        mongodb = cluster[Noti.mongo_db_name]

        print(f"Save notified dart to {Noti.mongo_db_name} db, {Noti.mongo_col_name} collection on mongodb ...")
        col = mongodb[Noti.mongo_col_name]
        # 이전에 저장된 rcept_no가 있으면 삭제한다.
        query = {'rcept_no': {"$eq": self.data['rcept_no']}}
        col.delete_many(query)
        col.insert_one(self.data)

    def to_sqlite(self):
        def make_engine(db_path, fname, echo=False):
            if not os.path.isdir(db_path):
                os.makedirs(db_path)
            dsn = f"sqlite:///{os.path.join(db_path, fname)}"
            return create_engine(dsn, echo=echo)

        # sqlite3에 연결
        self.setting.set_default_sqlite_if_not_preset()
        sqlite_path = self.setting.contents['sqlite_path']
        logger.info(f"sqlite3 path : {sqlite_path}")
        engine = make_engine(db_path=sqlite_path, fname=Noti.sqlite_filename)

        print(f"Save notified dart to {Noti.sqlite_filename} on {os.path.basename(sqlite_path)} directory...")
        with engine.connect() as conn:
            # t+코드명의 테이블이 없으면 만든다.
            conn.execute(text(f"""CREATE TABLE IF NOT EXISTS {Noti.tablename} (
                                                            rcept_no VARCHAR(14) NOT NULL PRIMARY KEY,
                                                            code VARCHAR(6), 
                                                            rcept_dt VARCHAR(8), 
                                                            report_nm VARCHAR, 
                                                            point INT,
                                                            text VARCHAR
                                                            );"""))
            try:
                # 텍스트 내부에 작은따옴표를 sqlite로 저장하기 위해서 작은따옴표를 하나더 붙인다. https://lovedb.tistory.com/331
                c_text = self.data['text'].replace("'", "''")
                conn.execute(text(f"INSERT INTO {Noti.tablename} VALUES "
                                  f"({self.data['rcept_no']}, "
                                  f"{self.data['code']}, "
                                  f"{self.data['rcept_dt']}, "
                                  f"'{self.data['report_nm']}', "
                                  f"{self.data['point']}, "
                                  f"'{c_text}');"))
                logger.info(f"stock_code : {self.data['code']}, "
                            f"table : {Noti.tablename}"
                            f"rcept_no : {self.data['rcept_no']}, "
                            f"rcept_dt : {self.data['rcept_dt']}, "
                            f"report_nm :{self.data['report_nm']}, "
                            f"point :{self.data['point']}, "
                            f"text :{self.data['text']}")
            except IntegrityError:
                logger.info(f"stock_code : {self.data['code']}, rcept_no : {self.data['rcept_no']} - saved already.")
