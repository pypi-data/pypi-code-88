#!/usr/bin/env python3
# Yonghang Wang

import os
import sys
import argparse
import re
import getpass
import pexpect
import string


class LE:
    def __init__(self, command, usedefaults=True, timeout=10, consts=None, rules=None):
        self.command = command or "echo"
        self.usedefaults = usedefaults
        self.timeout = timeout
        self.consts = consts or dict()
        self.rules = rules or list()
        self.debug = False
        if self.usedefaults:
            self.rules.append(("[\$#]", "%IGNORE"))
            self.rules.append(("%WHENEOF", "%BREAK"))
            self.rules.append(("%WHENTIMEOUT", "%NONE"))

    def add_const(self, const=None, value=None):
        if not (const and value):
            return
        self.consts[str(const)] = str(value)

    def add_rule(self, pattern, response):
        if not (pattern and response):
            return
        self.rules.append((str(pattern), str(response)))

    def set_debug(self, state=True):
        self.debug = state

    def spawn(self):
        for k, v in self.consts.items():
            if v == "INPUT":
                v = input("% " + k + " : ")
                self.consts[k] = v
            elif v == "PASSWORD":
                v = getpass.getpass("% " + k + " : ")
                self.consts[k] = v
        patterns = list()
        responses = list()
        for p, r in self.rules:
            if p == "%WHENEOF":
                p = pexpect.EOF
            elif p == "%WHENTIMEOUT":
                p = pexpect.TIMEOUT
            if r == "%NONE":
                r = None
            if r:
                m = re.search(r"\{\{(.*?)\}\}", r)
                while m and m.group(1) in self.consts:
                    k = m.group(1)
                    r = re.sub("\{\{" + k + "\}\}", self.consts[k], r)
                    m = re.search(r"\{\{(.*?)\}\}", r)
            patterns.append(p)
            responses.append(r)
        self.child = pexpect.spawn(self.command, timeout=self.timeout)
        cnt = 0
        rcnt = -999
        respawn = False
        while True:
            r = self.child.expect(patterns)
            cnt += 1
            if respawn and rcnt + 1 != cnt:
                respawn = False
            if self.debug:
                print("# Matched : {} (r={})".format(patterns[r], r))
            # timeout
            if patterns[r] == pexpect.TIMEOUT:
                self.print_content()
                print()
                break
            # EOF
            if patterns[r] == pexpect.EOF:
                self.print_content()
                print()
                if respawn:
                    if rcnt + 1 == cnt:
                        self.child.close()
                        self.child = pexpect.spawn(self.command, timeout=self.timeout)
                        continue
                print()
                break
            rsp = responses[r]
            if not rsp:
                break
            actlst = re.split(r";", rsp)
            if self.debug:
                print("# actlst = {}".format(actlst))
            self.print_content()
            gobreak = False
            for rsp in actlst:
                if rsp.upper() == "%IGNORE":
                    continue
                if rsp.upper() == "%BREAK":
                    gobreak = True
                    break
                if re.search(r"%CMD=(\S+)", rsp.upper()):
                    command = re.sub(r"%(CMD|cmd)=", "", rsp, count=1)
                    if self.debug:
                        print("# runcmd : {}".format(command))
                    os.system(command)
                if rsp.upper() == "%RESPAWN":
                    if self.debug:
                        print("# set respawn flag")
                    respawn = True
                    rcnt = cnt
                    continue
                if self.debug:
                    print("# sendline : {}".format(rsp))
                self.child.sendline(rsp)
            if gobreak:
                break
        self.child.interact()

    def print_content(self):
        if not self.child:
            return
        content = self.child.before.decode()
        if self.child.after:
            try:
                content += self.child.after.decode()
            except:
                pass
        printable = set(string.printable)
        if re.search(r"\S+", content):
            lines = content.splitlines()
            output = "\n".join(
                ("".join((x for x in ln if x in printable)) for ln in lines)
            )
            print(output, end="")

    def __repr__(self):
        output = "LE {\n"
        output += "  command : {}\n".format(self.command)
        for k, v in self.consts.items():
            output += "  const  {} : {}\n".format(str(k), str(v))
        for i in self.rules:
            output += "  rule    : {}\n".format(str(i))
        output += "}\n"
        return output


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--command", dest="command", help="command to spawn")
    parser.add_argument("--const", dest="consts", action="append", help="const->value")
    parser.add_argument(
        "--rule", dest="rules", action="append", help="pattern->response"
    )
    parser.add_argument(
        "--timeout", dest="timeout", type=int, default=60, help="timeout"
    )
    parser.add_argument("--debug", dest="debug", action="store_true", help="debug mode")
    args = parser.parse_args()
    if args.debug:
        print("# command = ", args.command)
        print("# consts  = ", args.consts)
        print("# rules   = ", args.rules)
    if not args.command:
        print("# no command specified.")
        parser.print_help()
        sys.exit(0)
    le = LE(command=args.command, timeout=args.timeout)
    le.set_debug(args.debug)
    for c in args.consts or []:
        m = re.search(r"(.+?)->(.+)", c)
        if m:
            le.add_const(m.group(1), m.group(2))
    for r in args.rules or []:
        m = re.search(r"(.+?)->(.+)", r)
        if m:
            le.add_rule(m.group(1), m.group(2))
    if args.debug:
        print("# LE = ", str(le))
    le.spawn()


if __name__ == "__main__":
    main()
