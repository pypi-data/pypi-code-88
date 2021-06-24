#作者： tony
#作者： tony
import os, sys


def __init__(self, args):
    self.aa = args
    print(args)
    #return self

def show(self):
    print("test123")

Test = type('test', (object,), dict(__init__=__init__,show=show))  # 创建Hello class


