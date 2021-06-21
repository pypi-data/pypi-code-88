import time
import sqlite3

from .BaseAdapter import BaseAdapter
from aio_tg_bot.etc.database.models import WrapCache
from .CacheException import CacheExpiredException, DBNotSetException


class Sqlite3Adapter(BaseAdapter):
    def __init__(self, timeout=-1):
        super(Sqlite3Adapter, self).__init__(timeout=timeout)

    def get(self, key, check_timeout=True):
        record = WrapCache.get_or_none(key=key)

        if record is None:
            end_time = 0
        else:
            end_time = record.time

        if check_timeout and time.time() > end_time:
            self.remove(key)
            raise CacheExpiredException(key)
        elif check_timeout is False and record is None:
            value = None
        else:
            value = record.value

        return value

    def set(self, key, value):
        WrapCache.insert(key=key, value=value, time=time.time() + self.timeout).on_conflict("replace").execute()
        return True

    def remove(self, key):
        value = self.get(key, check_timeout=False)
        WrapCache.delete().where(WrapCache.key == key).execute()
        return value

    def flush(self):
        WrapCache.delete().execute()
        return True
