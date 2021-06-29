
import time
from loguru import logger
from script_client.const import fm



def register(app='',path='',name='',timeout=0):
    '''
    注册为回调函数
    :param app: app_code
    :param path: path
    :param timeout: timeout 本期没做无效
    :return:
    '''
    def deco(func):
        fm.add_map(app=app.strip(),path=path.strip(),func=func,
                   name=name,timeout=timeout)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return deco



def print_run_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        var = func(*args, **kwargs)
        t2 = time.time()
        t = '%.6f' % (t2 - t1)
        logger.info(f"函数 {func.__name__} 运行消耗了 {t} 秒")
        return var
    return wrapper