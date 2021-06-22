from bapy import icc

import bapy.data.frame
from bapy.data.frame import *
from bapy import *


def test_data_c():
    assert Stack(init=True) != A.init
    assert (A.init[0].file.exists and A.init[0].file.include) is True
    assert A.init[0].external and A.init[1].external is False
    assert (A.init[1].file.exists and A.init[1].file.include) is False
    assert (Stack(init=True)[1].file.exists and Stack(init=True)[1].file.include) is False

    assert len(A.c_1) > 2
    assert A.c_1[0].file.path == Path(bapy.data.frame.__file__)
    assert A.c_1[0].file.exists is True
    assert A.c_1[0].include is True
    assert A.c_1[0].cls == A.__name__
    assert classmethod.__name__ in A.c_1[0].decorator
    assert A.c_1[0].module is False
    assert A.c_1[0].qualname == A.c.__qualname__
    assert A.c_1[0].lines[A.c_1[0].lineno]['coro']['func'] is False
    assert A.c_1[0].args == dict()

    assert A.c_1[1].file.path == Path(bapy.data.frame.__file__)
    assert A.c_1[1].file.exists is True
    assert A.c_1[1].file.include is True
    assert A.c_1[1].function == N._MODULE
    assert A.c_1[1].args == dict()


def test_context():
    assert context.no_sync.caller == context.no_sync.stack[FRAME_INDEX]
    assert context.no_sync.stack[0].file.exists is True
    assert context.no_sync.stack[0].include is True
    lineno = context.no_sync.stack[0].lineno
    assert context.no_sync.stack[0].lines[lineno]['coro']['func'] is True
    assert context.no_sync.stack[0].function.decorators == list()
    assert context.no_sync.stack[0].function.name == asynccontext_call_async.__name__
    assert context.no_sync.stack[0].coro is True
    assert context.no_sync.stack[0].real == 0
    assert context.no_sync.stack[0].lines[lineno]['coro']['line'] is False
    assert context.no_sync.stack[FRAME_INDEX].file.exists is True
    assert context.no_sync.stack[FRAME_INDEX].include is True
    lineno = context.no_sync.stack[FRAME_INDEX].lineno
    assert context.no_sync.stack[FRAME_INDEX].lines[lineno]['coro']['func'] is True
    assert context.no_sync.stack[FRAME_INDEX].decorators == [asynccontextmanager.__name__]
    assert context.no_sync.stack[FRAME_INDEX].coro is True
    assert context.no_sync.stack[FRAME_INDEX].real == 0
    assert context.no_sync.stack[FRAME_INDEX].lines[lineno]['coro']['line'] is False


def test_thread():
    # icc(thread)
    assert thread[0].decorators == [staticmethod.__qualname__]
    assert thread[0].qualname == A.s.__qualname__
    assert thread[0].coro is False
    assert thread[FRAME_INDEX].real is None
    caller = thread()
    real = thread(real=True)
    assert caller == real.caller == real.real


# noinspection PyUnusedLocal
def test_completed():
    lineno = completed[0].lineno
    assert completed[0].lines[lineno]['coro']['func'] is True
    assert completed[0].decorators == [staticmethod.__qualname__]
    assert completed[0].qualname == A.d.__qualname__
    assert completed[0].coro is True
    assert completed[0].lines[lineno]['coro']['line'] is False
    icc(completed)
    caller = completed()  # 1
    assert caller.coro is True
    assert caller.path.has(asyncio.__name__)

    real = completed(real=True)
    index = completed.index(real)  # 6
    assert real.real.module is True
    assert completed[FRAME_INDEX].real is None
    caller = completed()
    real = completed(real=True)
    # icc(caller, real)
    # real.real.module is True
    # assert caller == real.caller == real.real


def test_foryield():
    pass
    # icc(foryield)
    # assert thread[0].function.qual == A.s.__qualname__
    # assert thread[0].info.ASYNC is False
    # assert thread[FRAME_INDEX].info.real is None
    # caller = thread()
    # real = thread(real=True)
    # icc(caller, real)
    # assert caller == real.caller == real.real


def test_prop_to_thread():
    pass
    # icc(prop_to_thread)
    # assert thread[0].function.qual == A.s.__qualname__
    # assert thread[0].info.ASYNC is False
    # assert thread[FRAME_INDEX].info.real is None
    # caller = thread()
    # real = thread(real=True)
    # icc(caller, real)
    # assert caller == real.caller == real.real


def test_task():
    pass
    # icc(task)
    # assert thread[0].function.qual == A.s.__qualname__
    # assert thread[0].info.ASYNC is False
    # assert thread[FRAME_INDEX].info.real is None
    # caller = thread()
    # real = thread(real=True)
    # icc(caller, real)
    # assert caller == real.caller == real.real


def test_ensure():
    pass
    # icc(ensure)
    # assert thread[0].function.qual == A.s.__qualname__
    # assert thread[0].info.ASYNC is False
    # assert thread[FRAME_INDEX].info.real is None
    # caller = thread()
    # real = thread(real=True)
    # icc(caller, real)
    # assert caller == real.caller == real.real


def test_gather():
    # gather = asyncio.run(asyncdef(gth=True), debug=False)

    pass
    # icc(gather)
    # assert thread[0].function.qual == A.s.__qualname__
    # assert thread[0].info.ASYNC is False
    # assert thread[FRAME_INDEX].info.real is None
    # caller = thread()
    # real = thread(real=True)
    # icc(caller, real)
    # assert caller == real.caller == real.real


test_data_c()
test_context()
test_thread()
test_completed()
test_foryield()
test_prop_to_thread()
test_task()
test_ensure()
test_gather()
