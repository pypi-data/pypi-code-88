from __future__ import print_function

import argparse
import sys

try:
    import future
except ImportError:
    pass
else:
    import codecs
    encoding = sys.stdin.encoding or 'utf-8'
    sys.stdin = codecs.getreader(encoding)(sys.stdin)
    sys.argv = [arg.decode(encoding) for arg in sys.argv]

from . import decode, encode

prog = 'python -m lesivka'
description = 'A simple command line interface for lesivka module.'

parser = argparse.ArgumentParser(prog=prog, description=description)
parser.add_argument("-d", "--decode", action="store_true")
parser.add_argument("-n", "--no-diacritics", action="store_true")
parser.add_argument("text", nargs="*")
options = parser.parse_args()

action = decode if options.decode else encode

if options.text:
    print(action(" ".join(options.text), no_diacritics=options.no_diacritics))
else:
    try:
        for line in sys.stdin:
            print(action(line, no_diacritics=options.no_diacritics), end="")
    except KeyboardInterrupt:
        pass
