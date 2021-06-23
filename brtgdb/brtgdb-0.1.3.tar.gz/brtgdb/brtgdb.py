# -*- coding: utf-8 -*-
"""
Simple database connector using sqlalchemy.

Peter Raso
Created on Fri Jun 18 12:35:32 2021
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL


class BrtgDB:
    
    def __init__(self):
        driver = 'mysql+pymysql'
        user = os.environ['DB_USER']
        pwd = os.environ['DB_PASS']
        host = os.environ['DB_HOST']
        port = os.environ['DB_PORT']
        self.url = URL.create(driver, user, pwd, host, port, 'brtg')
        self.conn = self.connect()

    def connect(self):
        engine = create_engine(self.url,
                               connect_args={'ssl': {'ssl_verify_cert': 'true'}},
                               encoding='utf-8')
        return engine.connect()

    def execute(self, query):
        return self.conn.execute(query)

    def __del__(self):
        self.conn.close()

