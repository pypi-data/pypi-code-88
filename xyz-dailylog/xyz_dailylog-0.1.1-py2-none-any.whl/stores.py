# -*- coding:utf-8 -*- 
# author = 'denishuang'
from __future__ import unicode_literals
from six import string_types
from xyz_util.mongoutils import Store

from xyz_util.datautils import access
from xyz_util.dateutils import format_the_date


class ObjectLog(Store):
    name = 'object_log'
    timeout = 1000

    def log(self, model, id, metics={'views': 1}):
        vs = dict([(k, int(v))for k, v in metics.items()])
        self.inc({'model': model, 'id': int(id)}, vs)

    def find(self, model, ids, metics='views'):
        return self.collection.find({'model': model, 'id': {'$in': ids}}, {'_id': '$id', 'count': '$' + metics})


class UserLog(Store):
    name = 'user_log'
    timeout = 1000

    def log(self, id, metics='online_time', delta=1):
        self.inc({'id': int(id)}, {metics: int(delta)})
        a = self.collection.find_one({'id': int(id)}, {metics: 1})
        return access(a, metics) if a else None

    def max(self, id, metics='online_time', value=1):
        a = self.collection.find_one({'id': int(id)}, {metics: 1})
        old = access(a, metics) if a else None
        if old is None or old < value:
            self.upsert({'id': int(id)}, {metics: int(value)})
            return value
        return old

    def get(self, id, metics='online_time'):
        d = self.collection.find_one({'id': id}, {metics: 1})
        return access(d, metics) if d else None


class DailyLog(Store):
    name = 'daily_log'
    timeout = 1000

    def log(self, user, model, metics='done', the_date=None, delta=1):
        d = format_the_date(the_date)
        rk = dict(user=user, model=model, date=d.isoformat())
        if isinstance(delta, string_types):
            delta = int(delta)
        self.inc(rk, {metics: delta})
        # a = self.collection.find_one(rk, {metics: 1})
        # r = access(a, metics)