#!/usr/bin/env python3
# Yonghang Wang

import sys
import argparse
import os
import json
import traceback
from sretools import SimpleTable


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--infile", dest="infile", help="input file")
    parser.add_argument("-H", "--header", dest="header", help="optional header")
    parser.add_argument("-X", "--debug", dest="debug", action="store_true", default=False, help="debug mode",)
    args = parser.parse_args()

    if args.infile:
        if not os.path.isfile(args.infile):
            print("# {} not exists.".format(args.infile))
        with open(args.infile, "r") as f:
            INPUT = f.read()
    else:
        INPUT = sys.stdin.read()

    header = list()
    if args.header :
        header = [ h for h in args.header.split(",") if h]

    data = list()
    try:
        js = json.loads(INPUT)
        if type(js) is list and all([type(i) is list for i in js]) :
            for row in js :
                r=list()
                for col in row :
                    r.append(str(col))
                data.append(r)
        elif type(js) is list and all([type(i) is dict for i in js]) :
            # now each row is a dict
            if not header :
                loaded=set()
                for row in js :
                    for k in row.keys() :
                        if k not in loaded :
                            header.append(k)
                            loaded.add(k)
            for row in js :
                r=list()
                for h in header :
                    r.append(row.get(h,""))
                data.append(r)
        else :
            print("# not supported format.")
            print(json.dumps(js,indent=2))
            return -1 
    except:
        traceback.print_exc()
        if args.debug:
            print(INPUT)
        return -1 

    #print("header = ",header)
    #print("data = ",data)
    #data=None, header=None, cols=None, maxwidth=-1, noheader=False,tree=False
    noheader = True
    if header :
        noheader = False
    print(SimpleTable(data=data,header=header,noheader=noheader))

if __name__ == "__main__":
    main()
