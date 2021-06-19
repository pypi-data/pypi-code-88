#!/usr/bin/env python3
# Yonghang Wang

import sys
import argparse
import os
import json
import dicttoxml


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--infile", dest="infile", help="input file")
    parser.add_argument( "-X", "--debug", dest="debug", action="store_true", default=False, help="debug mode",)
    args = parser.parse_args()

    if args.infile:
        if not os.path.isfile(args.infile):
            print("# {} not exists.".format(args.infile))
        with open(args.infile, "r") as f:
            INPUT = f.read()
    else:
        INPUT = sys.stdin.read()

    try:
        js = json.loads(INPUT)
    except:
        print("# invalid JSON")
        if args.debug:
            print(INPUT)
        sys.exit(-1)

    print(dicttoxml.dicttoxml(js).decode())

if __name__ == "__main__":
    main()
