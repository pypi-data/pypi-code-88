#!/usr/bin/env python3
# Yonghang Wang

import sys
import argparse
import os
import re
import csv
import copy
from wcwidth import wcswidth
from collections import defaultdict
from itertools import zip_longest
from sretools import SimpleTable


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-n",
        "--lineno",
        dest="lineno",
        default=False,
        action="store_true",
        help="show line no.",
    )
    parser.add_argument("-H", "--header", dest="header", help="header columns")
    parser.add_argument("-f", "--infile", dest="infile", help="input file")
    parser.add_argument(
        "-C",
        "--dump-column",
        dest="dumpcols",
        help="only print columns indentified by index numbers.",
    )
    parser.add_argument(
        "-s", "--sortby", dest="sortby", help="column id starts with 0."
    )
    parser.add_argument(
        "-d",
        "--delimiter",
        dest="delimiter",
        default=",",
        help="char to seperate columns",
    )
    parser.add_argument(
        "-q",
        "--quotechar",
        dest="quotechar",
        default='"',
        help="char to seperate columns",
    )
    parser.add_argument(
        "-w",
        "--maxwidth",
        dest="maxwidth",
        type=int,
        default=-1,
        help="max col width when print in console, min==20",
    )
    parser.add_argument(
        "-v",
        "--pivot",
        dest="pivot",
        action="store_true",
        default=False,
        help="pivot wide tables.",
    )
    parser.add_argument(
        "-F", "--format", dest="format", help="other than console table, json,yaml,html"
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

    header = list()
    data = list()
    if args.lineno:
        header.append("#")
    headered = False
    if args.header:
        header += re.split(args.delimiter, args.header)
        headered = True
    if not args.infile:
        INPUT = sys.stdin
    else:
        INPUT = open(args.infile, "r", newline="")
    # with open(args.infile,"r",newline='') as f :
    if True:
        cr = csv.reader(INPUT, delimiter=args.delimiter, quotechar=args.quotechar)
        if not headered:
            header += next(cr)
            headered = True
        for r in cr:
            data.append(r)
    INPUT.close()

    if args.sortby:

        def fsort(x):
            v = list()
            for i in re.split(r",", args.sortby):
                v0 = x[int(i)] or ""
                if re.match(r"^\d+(\.\d*)*$", v0):
                    v.append(float(v0))
                else:
                    v.append(0)
                v.append(v0)
            return v

        data = sorted(data, key=fsort)
    if args.pivot:
        print(SimpleTable(header=header, data=data, cols=args.dumpcols).repr_pivot())
    else:
        t = SimpleTable(
            header=header, data=data, cols=args.dumpcols, maxwidth=args.maxwidth
        )
        if args.format == "json":
            print(t.get_json(), end="")
        elif args.format == "yaml":
            print(t.get_yaml(), end="")
        elif args.format == "html":
            print(t.get_html(), end="")
        else:
            print(t, end="")


if __name__ == "__main__":
    main()
