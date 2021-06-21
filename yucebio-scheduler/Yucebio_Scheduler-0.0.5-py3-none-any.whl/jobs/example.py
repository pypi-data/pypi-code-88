import os
from sys import prefix
from icecream import ic
import datetime

def format_prefix():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S ')

ic.configureOutput(prefix=format_prefix)

def example_job1():
    ic("start")
    ic(os.path.abspath(os.curdir))


