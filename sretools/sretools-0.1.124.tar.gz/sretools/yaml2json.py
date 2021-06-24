#!/usr/bin/env python3
# Yonghang Wang

import sys
import argparse
import os
import json
import yaml


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--infile", dest="infile", help="input file")
    parser.add_argument(
        "-s",
        "--sorted",
        dest="sorted",
        action="store_true",
        default=False,
        help="sort keys",
    )
    parser.add_argument(
        "-X",
        "--debug",
        dest="debug",
        action="store_true",
        default=False,
        help="debug mode",
    )
    args = parser.parse_args()

    if args.infile:
        if not os.path.isfile(args.infile):
            print("{} not exists.")
        with open(args.infile, "r") as f:
            INPUT = f.read()
    else:
        INPUT = sys.stdin.read()

    try:
        yl = yaml.load(INPUT)
    except:
        print("not invalid YAML")
        if args.debug:
            print(INPUT)
        sys.exit(-1)

    print(json.dumps(yl, sort_keys=args.sorted, indent=2))


if __name__ == "__main__":
    main()
