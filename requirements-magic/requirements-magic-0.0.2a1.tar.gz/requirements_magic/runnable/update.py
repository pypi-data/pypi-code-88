# standard imports
import sys
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


arg_description = """Updates versions for packages defined in original_file with versions in upstream_files.

The files are processed in the order arguments are given, and if two files define the same package the latter file will overwrite the version(s) of the former.
"""

argparser = argparse.ArgumentParser(description=arg_description)
argparser.add_argument('-v', action='store_true', help='Be verbose')
argparser.add_argument('original_file', type=str, help='file to update versions for')
argparser.add_argument('upstream_files', nargs='+', type=str, help='version source files, separated by space')
args = argparser.parse_args(sys.argv[1:])

if args.v:
    logg.setLevel(logging.DEBUG)


def merge(requirements_files):

    initial = True

    auditer = VersionAuditer()
    #requirements = {}

    for filepath in requirements_files:
        logg.debug('reading {}'.format(filepath))
        f = open(filepath, 'r')
        while True:
            l = f.readline()
            if l == '':
                break
            l = l.rstrip()
            (k, c, v) = split_requirement(l)
            if initial:
                auditer.add(k, l)
            else:
                auditer.update(k, l, on_exist='update_if_exist')
        f.close()
        initial = False

    return auditer.all()


def main():
    files = [args.original_file] + args.upstream_files
    s = '\n'.join(merge(files))
    print(s)


if __name__ == '__main__':
    main()
