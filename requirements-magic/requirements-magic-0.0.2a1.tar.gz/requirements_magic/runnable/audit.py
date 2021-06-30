# standard imports
import sys
import logging
import os
import re
import argparse

# local imports
from requirements_magic import VersionAuditer
from requirements_magic.error import (
        ExistsError,
        VersionError,
        )

logging.basicConfig(level=logging.ERROR)
logg = logging.getLogger()

arg_description = """Check if requirements in file match the dependency constraints of another
"""

argparser = argparse.ArgumentParser(arg_description)
argparser.add_argument('-v', action='store_true', help='Be verbose')
argparser.add_argument('master', type=str, help='File containing correct constraints')
argparser.add_argument('subject', type=str, help='File to check constraints for')
args = argparser.parse_args()

if args.v:
    logg.setLevel(logging.DEBUG)


def check(subject, master):

    auditer = VersionAuditer()

    versions = {}

    f = open(master, 'r')
    while True:
        l = f.readline().rstrip()
        if l == '':
            break
        (m, v) = l.split('==')
        #versions[m.lower()] = version.parse(v)
        try:
            auditer.add(m, v)
        except ExistsError:
            raise AttributeError('module {} is defined more than once in {}'.format(m, master))
    f.close()


    re_versionline = r'^(.+)([=\~\>\<]=)(\d.+)$'
    f = open(subject, 'r')
    while True:
        l = f.readline().rstrip()
        if len(l) == 0:
            break

        match = re.match(re_versionline, l)

        modulename = match[1].replace('_', '-').lower()
        logg.debug('found modulename {}'.format(modulename))

        if modulename[:4] == 'cic-':
            logg.info('skipping cic internal version {} => {}'.format(modulename, match[3]))
            continue

        auditer.check(modulename, match[3], match[2])


def main():
    try:
        return check(args.subject, args.master)
    except KeyError as e:
        sys.stderr.write('ERROR: dependency not found in subject: {}\n'.format(e))
        sys.exit(1)
    except VersionError as e:
        sys.stderr.write('ERROR: {}\n'.format(e))
        sys.exit(1)


if __name__ == '__main__':
    main()
