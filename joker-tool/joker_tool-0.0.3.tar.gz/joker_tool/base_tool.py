# -*- coding: utf-8 -*-
import hashlib
import time
from functools import wraps
from functools import lru_cache
from concurrent import futures
from urllib.parse import unquote
from func_timeout import func_set_timeout
import func_timeout

executor = futures.ThreadPoolExecutor(1)


def timeit_wrapper(func):
    """
    函数执行耗时
    :param func:
    :return:
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func_return_val = func(*args, **kwargs)
        end = time.perf_counter()
        print('函数 {1:<4} 耗时: {2:<8}'.format(func.__module__, func.__name__, end - start))
        return func_return_val

    return wrapper


def timeout(seconds):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kw):
            future = executor.submit(func, *args, **kw)
            return future.result(timeout=seconds)

        return wrapper

    return decorator


class BaseTool(object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def md5(self, name):
        m = hashlib.md5()
        m.update(name.encode("utf8"))
        return m.hexdigest()

    def url_decode(self, url_suffix):
        """
        url_suffix: 拼接在url 后面的参数? 后的 字符转形式
        return: 返回decode解码后的 字典形式的字符串
        """
        str_text = unquote(url_suffix, 'utf-8')
        payload_dict = {}
        for payload in str_text.split("&"):
            payload_list = payload.split("=", 1)
            payload_dict[payload_list[0]] = payload_list[1]
        return payload_dict

    def pmgressbar(self):
        scale = 50
        print("执行开始，祈祷不报错".center(scale // 2, "-"))
        start = time.perf_counter()
        for i in range(scale + 1):
            a = "#" * i
            b = "·" * (scale - i)
            c = (i / scale) * 100
            dur = time.perf_counter() - start
            print("\r{:^3.0f}% [{}{}] 耗时:{:.2f}s".format(c, a, b, dur), end="")
            time.sleep(0.1)
        print("\n" + "执行结束，万幸".center(scale // 2, "-"))


# @timeout(3)
@func_set_timeout(3)  # 设定函数超执行时间_
def task():
    print('hello world')
    time.sleep(2)
    return '执行成功_未超时'


@lru_cache()
def time_item():
    time.sleep(3)
    return 3


if __name__ == '__main__':
    # payload = 'Account=17200272387&UType=201&ProvinceID=01&AreaCode=&CityNo=&Captcha=pqyw&RandomFlag=0&Password=xWF0hFlIRsfEJXyRLhhepQ%3D%3D'
    #
    # BaseTool().url_decode(payload)
    try:
        print(task())
    # 若调用函数超时自动走异常(可在异常中写超时逻辑处理)
    except:
        print('执行函数超时')
