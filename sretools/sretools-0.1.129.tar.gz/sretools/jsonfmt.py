#!/usr/bin/env python3
# Yonghang Wang

import sys
import argparse
import os
import json
from sretools import jsonize


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--infile", dest="infile", help="input file")
    parser.add_argument("-r", "--recursive", dest="recursive", action="store_true", default=False, help="detect and format JSON content recursively",)
    parser.add_argument("-X", "--debug", dest="debug", action="store_true", default=False, help="debug mode",)
    args = parser.parse_args()

    if args.infile:
        if not os.path.isfile(args.infile):
            print("{} not exists.")
        with open(args.infile, "r") as f:
            INPUT = f.read()
    else:
        INPUT = sys.stdin.read()

    try:
        js = json.loads(INPUT)
    except:
        print("invalid JSON")
        if args.debug:
            print(INPUT)
        sys.exit(-1)

    if args.recursive :
        js = jsonize(js)
    print(json.dumps(js,indent=2,sort_keys=True))


if __name__ == "__main__":
    main()
