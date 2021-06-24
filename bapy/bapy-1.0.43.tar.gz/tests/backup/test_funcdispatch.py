# coding=utf-8
import asyncio
from asyncio import as_completed
from asyncio import create_task
from asyncio import to_thread

from rclib import *


@funcdispatch
def sync():
    return True


@sync.register
async def _():
    return await to_thread(sync)


@funcdispatch
def func():
    return True


@func.register
async def _():
    return False


@funcdispatch
def func1(arg):
    return True, arg


@func1.register
async def _(arg):
    return False, arg


def funcdispatch_sync():
    return func()


async def funcdispatch_async():
    return await func()

module_sync_no_thread = sync()
module_sync_to_thread = asyncio.run(sync(), debug=False)
module_sync = func()
module_async = asyncio.run(func(), debug=False)
function_sync = funcdispatch_sync()
function_async = asyncio.run(funcdispatch_async(), debug=False)


def test_module_funcdispatch():
    assert module_sync is True
    assert module_async is False
    assert module_sync_no_thread == module_sync_to_thread


def test_function_funcdispatch():
    assert function_sync is True
    assert function_async is False


# def test_funcdispatch_sync(caplog):
#     assert func() is True
#     assert func1(True) == (True, True)
#     with caplog.at_level(verboselogs.SPAM, logger=logger.name):
#         msg = 'log_sync'
#         logger.setLevel(verboselogs.SPAM)
#         logger.spam(msg)
#         assert msg in caplog.text
#
#
# @pytest.mark.asyncio
# async def test_funcdispatch_async(caplog):
#     await to_thread(funcdispatch_sync)
#     assert await func() is False
#     assert await func1(False) == (False, False)
#     with caplog.at_level(verboselogs.SPAM, logger=logger.name):
#         msg = 'log_async'
#         logger.setLevel(verboselogs.SPAM)
#         await logger.spam(msg)
#         assert msg in caplog.text


def to_thread_sync():
    return True


async def to_thread_async():
    # noinspection PyUnusedLocal
    stack_context = 3

    await to_thread(to_thread_sync)

    result = list()
    for coro in as_completed([func(),
                              sync()]):
        r = await coro
        result.append(r)
    assert True in result
    assert False in result
    assert await asyncio.ensure_future(func()) is False
    assert await asyncio.gather(func()) == [False]

    task = create_task(func())
    assert isinstance(task, asyncio.Task)

asyncio.run(to_thread_async(), debug=False)
