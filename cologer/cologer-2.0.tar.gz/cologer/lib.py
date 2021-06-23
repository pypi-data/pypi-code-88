import os
import sys
from datetime import datetime


def get_time(): return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_cur_info():
    try:
        raise Exception
    except Exception:
        trace = sys.exc_info()[2].tb_frame
        while trace.f_back:
            trace = trace.f_back
        return (trace.f_code.co_filename, trace.f_lineno)


def get_filename(): return 'file:{}'.format(get_cur_info()[0])


def get_lineno(): return 'lineno:{}'.format(get_cur_info()[1])
