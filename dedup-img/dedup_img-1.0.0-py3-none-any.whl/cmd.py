import os
import sys
from getopt import getopt
from .dedup_utils import filter_images


def exc(_method, _root):
    filter_images(_method, _root)


def main():
    try:
        method = 'PHash'
        root = None
        opts, args = getopt(sys.argv[1:], 'PADWd:')
        for i, v in opts:
            if i == "-P":
                method = 'PHash'
            elif i == '-A':
                method = 'AHash'
            elif i == '-D':
                method = 'DHash'
            elif i == '-W':
                method = 'WHash'
            elif i == '-d':
                root = v
        if root is None:
            raise Exception('image dir can not be null')
        if not os.path.exists(root):
            raise Exception('image dir is not exist')
        if not os.path.isdir(root):
            raise Exception('the input image dir is not a dir')
        exc(method, root)
    except Exception as e:
        print(e)
