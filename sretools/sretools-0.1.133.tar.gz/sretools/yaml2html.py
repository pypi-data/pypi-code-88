#!/usr/bin/env python3
# Yonghang Wang

import sys
import argparse
import os
import json
import yaml
from sretools import JsonConverter


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
        "-a",
        "--table_attributes",
        dest="attributes",
        default="border-collapse:collapse;",
        help="table attributes",
    )
    parser.add_argument(
        "-C", "--colors", dest="colors", help="colors to be used for background"
    )
    parser.add_argument(
        "-I",
        "--keys-included",
        dest="keys_included",
        action="append",
        help="include these keys only",
    )
    parser.add_argument(
        "-E",
        "--keys-excluded",
        dest="keys_excluded",
        action="append",
        help="exclude these keys",
    )
    parser.add_argument(
        "-k",
        "--keywords_order",
        dest="keyorder",
        help="use this ordered keywords to help sort dict.",
    )
    parser.add_argument(
        "-v",
        "--dictsortbyvalue",
        dest="dtbyval",
        action="store_true",
        default=False,
        help="with -s, sort dict by value.",
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
        yl = yaml.safe_load(INPUT)
    except:
        print("not invalid YAML")
        if args.debug:
            print(INPUT)
        sys.exit(-1)

    print(
        JsonConverter(
            jsstr=yl,
            tblattr=args.attributes,
            sort=args.sorted,
            sort_by_val=args.dtbyval,
            sortkeywords=args.keyorder,
            keys_included=args.keys_included,
            keys_excluded=args.keys_excluded,
            colors=args.colors,
        ).json2html()
    )


if __name__ == "__main__":
    main()
