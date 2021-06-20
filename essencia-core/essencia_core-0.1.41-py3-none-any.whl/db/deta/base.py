#!/usr/bin/env python
# coding: utf-8

import contextlib
import typing

from deta import Deta
from typing import Tuple, Dict, Any, Union
from starlette.datastructures import Secret


class DetaCrud:
    def __init__(self, project_key: Union[Secret, str]):
        self.project_key = project_key
        self.deta = Deta(project_key=str(self.project_key))

    @property
    def project_id(self):
        return self.deta.project_id

    def sync_connect(self, table):
        return self.deta.Base(table)


    async def connect(self, table):
        return self.deta.Base(table)

    @contextlib.asynccontextmanager
    async def CountObjects(self, table):
        db = await self.connect(table)
        count = 0
        try:
            count = len(next(db.fetch({})))
        except:
            pass
        finally:
            yield count
            db.client.close()


    @contextlib.asynccontextmanager
    async def Update(self, table: str, data: Dict[str, Any]):
        key = data.get("key")
        if not key:
            raise AttributeError("a key is necessary")
        db = await self.connect(table)
        try:
            yield db.update(data, key)
        except:
            yield
        finally:
            db.client.close()


    @contextlib.asynccontextmanager
    async def ListAll(self, table):
        print(f'looking all for table {table}')
        db = await self.connect(table)
        data = []
        try:
            data = next(db.fetch({}))
        except:
            pass
        finally:
            yield data
            db.client.close()


    @contextlib.asynccontextmanager
    async def CheckCode(self, table, code):
        db = await self.connect(table)
        result = None
        try:
            result = next(db.fetch({'meta.code': code}))[0]
        except:
            pass
        finally:
            yield result
            db.client.close()


    @contextlib.asynccontextmanager
    async def Insert(self, table, data):
        key = data.get("key")
        if not key:
            raise AttributeError("a key is necessary")
        db = await self.connect(table)
        msg = ''
        try:
            db.insert(data)
            msg = 'dados inseridos com sucesso'
        except:
            msg = 'os dados não foram inseridos'
        finally:
            yield msg
            db.client.close()


    @contextlib.asynccontextmanager
    async def Delete(self, table, key):
        db = await self.connect(table)
        try:
            yield db.delete(key=key)
        except:
            yield
        finally:
            db.client.close()


    @contextlib.asynccontextmanager
    async def Put(self, table, data):
        db = await self.connect(table)
        try:
            yield db.put(data)
        except:
            yield
        finally:
            db.client.close()


    @contextlib.asynccontextmanager
    async def Get(self, table, key):
        db = await self.connect(table)
        data = None
        try:
            data = db.get(key=key)
        except:
            pass
        finally:
            yield data
            db.client.close()


    @contextlib.asynccontextmanager
    async def SearchName(self, table, name):
        db = await self.connect(table)
        data = []
        try:
            data = next(db.fetch({'fullname?contains': name}))
        except:
            pass
        finally:
            yield data
            db.client.close()


    @contextlib.asynccontextmanager
    async def Search(self, table: str, query: typing.Dict[str, typing.Any]):
        db = await self.connect(table)
        data = []
        try:
            data = next(db.fetch(query))
        except:
            pass
        finally:
            yield data
            db.client.close()


    @contextlib.asynccontextmanager
    async def First(self, table, query={}):
        db = await self.connect(table)
        try:
            yield next(db.fetch(query))[0]
        except BaseException as e:
            yield
        finally:
            db.client.close()


    @contextlib.asynccontextmanager
    async def Last(self, table: str, query: Dict[str, Any] = dict()):
        db = await self.connect(table)
        try:
            yield next(db.fetch(query))[-1]
        except BaseException as e:
            raise ValueError(e)
        finally:
            db.client.close()


    @contextlib.asynccontextmanager
    async def GetOrCreate(self, table: str, data: Dict[ str, Any ]) -> Tuple[Union[Dict[str, Any]], Union[Dict[str, Any]]]:
        '''
        This function need the code kwarg to perform search in database before saving.
        :param table:
        :param data:
        :return:
        '''
        code = data.get('code', None)
        assert code != None, 'CODE could not be found'
        exist, created = None, None
        base = await self.connect(table)
        try:
            exist = next(base.fetch({'code': code}))[0]
        except:
            created = base.put(data)
        finally:
            yield exist, created
            base.client.close()







