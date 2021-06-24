#!/usr/bin/env python3
# Yonghang Wang

import sys
import argparse
import os


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
    parser.add_argument("-f", "--file", dest="tgtfile", help="file to check")
    parser.add_argument(
        "-r",
        "--rows",
        dest="rows",
        default=999,
        type=int,
        help="how many rows with nonascii char to be dumped",
    )
    parser.add_argument(
        "-a",
        "--all",
        dest="all",
        action="store_true",
        help="show lines without nonascii characters",
    )
    parser.add_argument(
        "-p",
        "--pipe",
        dest="pipe",
        action="store_true",
        default=False,
        help="input from pipe",
    )
    parser.add_argument(
        "-P",
        "--pipefile",
        dest="pipefile",
        action="store_true",
        default=False,
        help="treat each line from pipe as potential file to scan.",
    )
    parser.add_argument(
        "-L",
        "--followlink",
        dest="link",
        action="store_true",
        default=False,
        help="follow link",
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

    if not (args.tgtfile or args.pipe or args.pipefile):
        parser.print_help()
        sys.exit(0)

    def scan_stream(INPUT, pipefile=False):
        if not INPUT:
            print("")
            return
        n = 0
        found = 0
        for ln in INPUT:
            if found >= args.rows:
                break
            ln = ln.rstrip()
            n += 1
            nonasciis = [
                (ix, c, str(hex(ord(c)))) for ix, c in enumerate(ln) if ord(c) > 127
            ]
            if nonasciis or args.all:
                found += 1
                if args.tgtfile and found == 1:
                    print(" -> contains nonascii")
                if args.lineno:
                    if nonasciis:
                        print("  {}|{} => {}".format(n, ln, nonasciis))
                    else:
                        print("  {}|{}".format(n, ln))
                else:
                    if nonasciis:
                        print("  {} => {}".format(ln, nonasciis))
                    else:
                        print("  {}".format(ln))
            if pipefile and os.path.isfile(ln):
                with open(ln, "r") as fin:
                    print("# scanning {}".format(ln))
                    scan_stream(fin.readlines(), pipefile=False)

        if found == 0:
            print("")

    filename = None
    INPUT = None
    if args.pipe or args.pipefile:
        INPUT = sys.stdin
    if args.tgtfile:
        nonasciis = [
            (ix, c, str(hex(ord(c))))
            for ix, c in enumerate(args.tgtfile)
            if ord(c) > 127
        ]
        if nonasciis:
            print("  {} ({})".format(args.tgtfile, nonasciis), end="")
        else:
            print("  {}".format(args.tgtfile), end="")
        if os.path.isfile(args.tgtfile) and (
            not os.path.islink(args.tgtfile) or args.link
        ):
            with open(args.tgtfile, "r") as fin:
                INPUT = fin.readlines()
                filename = args.tgtfile
    scan_stream(INPUT, pipefile=args.pipefile)


if __name__ == "__main__":
    main()
