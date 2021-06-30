from ctypes import *
from l0n0lnet.buildcpp import try_create_lib, get_lib_path

_close_funcs = []   # 程序退出时会顺序执行列表中所有函数


def add_quit_func(func):
    """
    向退出函数列表加入函数

    程序接收到sigint 或者所有运行的 tcp, udp, 延时函数都退出后会顺序执行close_funcs列表中所有的函数。\n
    本函数可以将自定义的退出函数加入到close_funcs列表中
    """
    _close_funcs.append(func)


@CFUNCTYPE(None)
def _on_quit():
    """
    给c++的退出回调（不要主动调用该函数)
    """
    for func in _close_funcs:
        func()


def _load_cpp_lib():
    # 构建库
    try_create_lib()

    # 加载库
    se = cdll.LoadLibrary(get_lib_path())

    # 初始化库
    se.init()

    # 初始化一些函数元数据
    se.quit.restype = None

    se.set_on_quit(_on_quit)

    return se


def run():
    """
    用来启动程序，会卡线程
    """
    se.run()


def run_nowait():
    """
    用来启动程序，不卡线程
    """
    se.run_nowait()


se = _load_cpp_lib()
