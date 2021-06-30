# standard imports
import logging
import os
import re
import argparse

# local imports
from requirements_magic import VersionAuditer
from requirements_magic.check import split_requirement       
from requirements_magic.error import (
        ExistsError,
        VersionError,
        )


logging.basicConfig(level=logging.ERROR)
logg = logging.getLogger()

arg_description = """Merges requirements in all the specified files. 

The files are processed in the order arguments are given. Later dependency definitions will overwrite preceding ones.
"""

argparser = argparse.ArgumentParser(arg_description)
argparser.add_argument('-v', action='store_true', help='Be verbose')
argparser.add_argument('file', nargs='+', type=str, help='File to include in merge')
args = argparser.parse_args()

if args.v:
    logg.setLevel(logging.DEBUG)


def merge(requirements_files):

    auditer = VersionAuditer()

    for filepath in requirements_files:
        logg.debug('reading {}'.format(filepath))
        f = open(filepath, 'r')
        while True:
            l = f.readline()
            if l == '':
                break
            l = l.rstrip()
            (k, c, v) = split_requirement(l)
            if k == None:
                raise ValueError('invalid requirement line {}'.format(l))
            auditer.update(k, l)
        f.close()

    return auditer.all()


def main():
    s = '\n'.join(merge(args.file))
    print(s)


if __name__ == '__main__':
    main()
