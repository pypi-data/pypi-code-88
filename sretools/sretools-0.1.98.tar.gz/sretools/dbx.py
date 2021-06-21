#!/usr/bin/env python3
# Yonghang Wang

import sys
import argparse
import os
import re
import jaydebeapi
import socket
import psutil
import traceback
import json
import time
import getpass
import yaml

# from multiprocessing import Process as Task
from threading import Thread as Task
from sretools import SimpleTable


class DBX:
    def __init__(self, jar, driver, url, user, password):
        self.__jar = jar
        self.__driver = driver
        self.__url = url
        self.__user = user
        self.__password = password
        self.__conn = None
        self.__cursor = None

    def close(self):
        try:
            self.__cursor.close()
            self.__conn.close()
        except:
            pass

    def get_connection(self):
        if not (self.__conn and self.__cursor):
            if (
                not self.__password
                or re.match(r"ignore", self.__password, re.IGNORECASE)
                or re.search(r"password=", self.__url)
            ):
                auth = None
            else:
                auth = [self.__user, self.__password.encode()]
            self.__conn = jaydebeapi.connect(
                self.__driver, self.__url, auth, jars=self.__jar
            )
            self.__cursor = self.__conn.cursor()

    def run_sql(self, sql):
        result = dict()
        try:
            self.__cursor.execute(sql)
            rchg = self.__cursor.rowcount
            result["sql"] = sql
            result["rows_impacted"] = rchg
            if rchg == -1:
                data = list()
                for row in self.__cursor.fetchall():
                    data.append([str(c) if c is not None else "" for c in row])
                hdr = [d[0] for d in self.__cursor.description]
                result["header"] = hdr
                result["data"] = data
        # except (Exception, jaydebeapi.DatabaseError) :
        except:
            result = {"error": traceback.format_exc().splitlines()[-1], "sql": sql}
        return json.dumps(result)

    def run_sp(self, sp, args=list()):
        pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-J", "--jar", dest="jar", help="jdbc driver jar file")
    parser.add_argument(
        "-P", "--plugin", dest="plugin", help="plugin file for user defined commands"
    )
    parser.add_argument(
        "-u", "--user", dest="user", help="user. default as current unix user."
    )
    parser.add_argument(
        "-p", "--password", dest="password", help='password. ENV["dbx_mypwd"]'
    )
    parser.add_argument("-D", "--driver", dest="driver", help="jdbc driver name")
    parser.add_argument("-U", "--url", dest="url", help="jdbc url or connection string")
    parser.add_argument(
        "-C",
        "--connect",
        dest="connect",
        action="store_true",
        default=False,
        help="force connect as server",
    )
    parser.add_argument("-Q", "--sql", dest="sql", help="sql statement to run")
    parser.add_argument(
        "-w",
        "--maxwidth",
        dest="maxwidth",
        type=int,
        default=-1,
        help="maxwidth of column",
    )
    parser.add_argument(
        "-F", "--outformat", dest="format", default="", help="json,yaml,csv,html"
    )
    parser.add_argument(
        "-v",
        "--pivot",
        dest="pivot",
        action="store_true",
        default=False,
        help="pivot the view",
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

    ppid = os.getppid()
    found = False
    p = ppid
    for d in ["~/.cache", "~/.cache/sretools"]:
        fulld = os.path.expanduser(d)
        if not os.path.exists(fulld):
            os.mkdir(fulld)
    while p not in [0, 1]:
        if os.path.exists(os.path.expanduser("~/.cache/sretools/.dbx.{}".format(p))):
            found = True
            break
        else:
            np = psutil.Process(ppid).ppid()
            if p == np:
                break
            else:
                p = np

    global CMDDT
    if args.plugin and os.path.isfile(args.plugin):
        with open(args.plugin, "r") as f:
            CMDDT = yaml.safe_load(f.read())
    else:
        CMDDT = dict()

    if not found or args.connect:
        addr = os.path.expanduser("~/.cache/sretools/.dbx.{}".format(ppid))
        if os.path.exists(addr):
            if args.debug:
                print("# ready to remove old server process")
            fdummy = addr + ".pid"
            for p in psutil.process_iter():
                try:
                    if fdummy in str(p.open_files()):
                        p.kill()
                except:
                    pass
            os.unlink(addr)
            if os.path.exists(fdummy):
                os.unlink(fdummy)
    else:
        # client only
        addr = os.path.expanduser("~/.cache/sretools/.dbx.{}".format(p))

    def get_sql_command(sqlorpath):
        global CMDDT
        if args.debug:
            print("# sqlorpath = ", sqlorpath)
            print("# CMDDT = ", CMDDT)
        cmddt = CMDDT
        if not cmddt or not sqlorpath:
            return sqlorpath
        if not re.search(r"^\s*\\", sqlorpath):
            return sqlorpath
        s = re.sub(r"^\s*\\", "", sqlorpath)
        p = cmddt
        for c in re.split(r"\.", s.strip()):
            if c in p:
                p = p[c]
            else:
                return sqlorpath
        return p

    def clientrun():
        rsql = get_sql_command(args.sql)
        try:
            if args.debug:
                print("# DBXClient {}".format(addr))
            s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            if args.connect and rsql:
                attempt = 10
                while attempt > 0:
                    if args.debug:
                        print("attempt = {}".format(attempt))
                    try:
                        time.sleep(1)
                        s.connect(addr)
                        break
                    except:
                        attempt -= 1
                if attempt == 0:
                    print("# cannot establish connections.")
                    return -1
            else:
                try:
                    s.connect(addr)
                except:
                    print("# cannot establish connections.")
                    return -1
            s.send(rsql.encode())
            if args.debug:
                print("# Client sent : {}".format(rsql))
            rsp = s.recv(1024 * 1024).decode()
            if args.debug:
                print("# Client got :", rsp)
            try:
                obj = json.loads(rsp)
                if "error" in obj:
                    print(obj.get("error", ""))
                    return -1
            except:
                obj = dict()
            if (
                not re.match(r"^\s*\\q\s*$", args.sql)
                and "header" in obj
                and "data" in obj
            ):
                if args.format == "json":
                    t = SimpleTable(header=obj["header"], data=obj["data"])
                    print(t.get_json(), end="")
                elif args.format == "yaml":
                    t = SimpleTable(header=obj["header"], data=obj["data"])
                    print(t.get_yaml(), end="")
                elif args.format == "csv":
                    t = SimpleTable(header=obj["header"], data=obj["data"])
                    print(t.get_csv(), end="")
                elif args.format == "html":
                    t = SimpleTable(header=obj["header"], data=obj["data"])
                    print(t.get_html(), end="")
                else:
                    t = SimpleTable(
                        header=obj["header"], data=obj["data"], maxwidth=args.maxwidth
                    )
                    if args.pivot:
                        print(t.repr_pivot(), end="")
                    else:
                        print(t, end="")
            rw = obj.get("rows_impacted", 0)
            if rw >= 0 and not re.match(r"^\s*\\q\s*$", args.sql):
                print("# {} row(s) impacted.".format(rw))
        except:
            print(traceback.format_exc().splitlines()[-1])

    # server
    if args.connect:
        if not args.user:
            args.user = getpass.getuser()
        if not args.password:
            args.password = os.environ.get("dbx_password", None)
            if not args.password and not re.search(r"password=", args.url):
                args.password = getpass.getpass(
                    prompt="# password for {} :".format("args.user")
                )
        if (
            not args.password
            or (not re.search(r"\S+", args.password))
            or re.match(r"ignore", args.password, re.IGNORECASE)
        ):
            args.password = ""
        if not all([args.jar, args.driver, args.url]):
            print("# Must specify jdbc driver jar(-J), driver(-D) and URL(-U).")
            return -1
        pid = os.fork()
        # keep attachment to pid file
        fdummy = open(addr + ".pid", "w")
        # child
        if pid == 0:
            print("# DBXServer {}@{}".format(os.getpid(), addr))
            args.driver = os.path.expanduser(args.driver)
            dbx = DBX(
                driver=args.driver,
                url=args.url,
                jar=args.jar,
                user=args.user,
                password=args.password,
            )
            dbx.get_connection()
            s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            s.settimeout(600)
            s.bind(addr)
            s.listen(1)

            def sqlworker(netconn, osql):
                try:
                    sql = get_sql_command(osql)
                    result = dbx.run_sql(sql)
                    if args.debug:
                        print("# Sqlworker: sql={}, result={}".format(sql, result))
                    netconn.send(result.encode())
                except:
                    print(traceback.format_exc().splitlines()[-1])

            while True:
                try:
                    netconn, cltaddr = s.accept()
                    sql = netconn.recv(32768).decode()
                    if args.debug:
                        print("# Eventloop: sql = [{}]".format(sql))
                    if re.match(r"^\s*\\q\s*$", sql):
                        break
                    wk = Task(target=sqlworker, args=(netconn, sql))
                    wk.start()
                except:
                    msg = traceback.format_exc()
                    print(msg.splitlines()[-1:])
                    if re.search("timeout", msg, re.IGNORECASE):
                        break
            if os.path.exists(addr):
                os.unlink(addr)
        # parent
        elif pid > 0:
            if args.sql:
                clientrun()
            return 0
        else:
            print("# Error forking new process ...")
            return -1
    # client
    else:
        if not args.sql:
            s = ""
            for ln in sys.stdin:
                if not ln or re.search(r"^\s*#", ln) or re.search(r"^\-\-", ln):
                    continue
                s += " " + ln.rstrip()
            args.sql = s.strip()
        clientrun()


if __name__ == "__main__":
    main()
