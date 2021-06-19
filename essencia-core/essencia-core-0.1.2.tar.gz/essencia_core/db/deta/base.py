#!/usr/bin/env python
# coding: utf-8

import contextlib
from deta import Deta
from typing import Tuple, Dict, Any, Union
from starlette.datastructures import Secret
from starlette.config import Config

config = Config(env_file='.env')

PROJECT_KEY=config('PROJECT_KEY', cast=Secret, default='')

def sync_connect(table):
    return Deta(str(PROJECT_KEY)).Base(table)


async def connect(table):
    return Deta(str(PROJECT_KEY)).Base(table)


@contextlib.asynccontextmanager
async def CountObjects(table):
    db = await connect(table)
    count = 0
    try:
        count = len(next(db.fetch({})))
    except:
        pass
    finally:
        yield count
        db.client.close()


@contextlib.asynccontextmanager
async def Update(table, data):
    key = data.get("key")
    if not key:
        raise AttributeError("a key is necessary")
    db = await connect(table)
    try:
        yield db.update(data, key)
    except:
        yield
    finally:
        db.client.close()


@contextlib.asynccontextmanager
async def ListAll(table):
    print(f'looking all for table {table}')
    db = await connect(table)
    try:
        data = next(db.fetch({}))
        print(data)
        yield data
    except:
        yield
    finally:
        db.client.close()


@contextlib.asynccontextmanager
async def CheckCode(table, code):
    db = await connect(table)
    result = None
    try:
        result = next(db.fetch({'meta.code': code}))[0]
    except:
        pass
    finally:
        yield result
        db.client.close()


@contextlib.asynccontextmanager
async def Insert(table, data):
    key = data.get("key")
    if not key:
        raise AttributeError("a key is necessary")
    db = await connect(table)
    try:
        yield db.insert(data)
    except:
        yield
    finally:
        db.client.close()


@contextlib.asynccontextmanager
async def Delete(table, key):
    db = await connect(table)
    try:
        yield db.delete(key=key)
    except:
        yield
    finally:
        db.client.close()


@contextlib.asynccontextmanager
async def Put(table, data):
    db = await connect(table)
    try:
        yield db.put(data)
    except:
        yield
    finally:
        db.client.close()


@contextlib.asynccontextmanager
async def Get(table, key):
    db = await connect(table)
    data = None
    try:
        data = db.get(key=key)
    except:
        pass
    finally:
        yield data
        db.client.close()


@contextlib.asynccontextmanager
async def SearchName(table, name):
    db = await connect(table)
    try:
        yield next(db.fetch({'fullname?contains': name}))
    except:
        yield []
    finally:
        db.client.close()


@contextlib.asynccontextmanager
async def Search(table, query={}):
    db = await connect(table)
    try:
        yield next(db.fetch(query))
    finally:
        db.client.close()


@contextlib.asynccontextmanager
async def First(table, query={}):
    db = await connect(table)
    try:
        yield next(db.fetch(query))[0]
    except BaseException as e:
        yield
    finally:
        db.client.close()


@contextlib.asynccontextmanager
async def Last(table, query={}):
    db = await connect(table)
    try:
        yield next(db.fetch(query))[-1]
    except BaseException as e:
        raise ValueError(e)
    finally:
        db.client.close()


@contextlib.asynccontextmanager
async def GetOrCreate(table: str, data: Dict[ str, Any ]) -> Tuple[Union[Dict[str, Any]], Union[Dict[str, Any]]]:
    '''
    This function need the code kwarg to perform search in database before saving.
    :param table:
    :param data:
    :return:
    '''
    code = data.get('code', None)
    assert code != None, 'CODE could not be found'
    exist, created = None, None
    base = await connect(table)
    try:
        exist = next(base.fetch({'code': code}))[0]
    except:
        created = base.put(data)
    finally:
        yield exist, created
        base.client.close()







