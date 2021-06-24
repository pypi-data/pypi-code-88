#!/usr/bin/env python3
# Yonghang Wang

import os
import sys
import argparse
import re
import json
import readline
import string
from datetime import datetime
from time import sleep
from texttable import Texttable
from sretools import SimpleTable

args = None
db = dict()


def initdb():
    global args
    global db
    args.db = os.path.expanduser(args.db)
    if not os.path.isdir(os.path.dirname(args.db)):
        os.mkdir(os.path.dirname(args.db))
    if not os.path.isfile(args.db):
        with open(args.db, "w") as f:
            f.write(json.dumps(db, indent=2, sort_keys=True))
    else:
        with open(args.db, "r") as f:
            db = json.loads(f.read())
    return db


def closedb():
    global args
    global db
    with open(args.db, "w") as f:
        f.write(json.dumps(db, indent=2, sort_keys=True))


def show_incident_list():
    global args
    global db
    rows = list()
    for inum, inc in db.items():
        rows.append(
            [
                str(inc.get("incident_number")),
                inc.get("create_time"),
                inc.get("brief"),
                str(len(inc.get("updates"))),
            ]
        )
    table = SimpleTable(
        header=["incident#", "create_time", "brief", "#updt"], data=rows
    )
    print(table)


def delete_incident():
    global args
    global db
    if args.incident not in db:
        print("# cannot find {}".format(args.incident))
        sys.exit(-1)
    del db[args.incident]
    closedb()


def show_incident():
    global args
    global db
    if args.incident not in db:
        print("# cannot find {}".format(args.incident))
        sys.exit(-1)
    # print(json.dumps(db[args.incident],indent=2,sort_keys=True))
    cout = ""
    mout = ""
    wout = "<html>\n<header>\n"
    wout += "<tt>\n"
    i = db[args.incident]
    mout += "## {}\n".format(i["brief"])
    mout += "### {} \n".format(i["incident_number"])
    mout += "| __meta__ | __value__ |\n"
    mout += "| ---- | ---- |\n"
    cout += "# ({}) {}\n\n".format(i["incident_number"], i["brief"])
    wout += "<title>{} Postmortem</title>\n".format(i["incident_number"])
    wout += "<h2>{} - {}</h2>\n".format(i["incident_number"], i["brief"])
    wout += "</header>\n"
    wout += "<table>\n"
    mout += "|{}|{}|\n".format("CreateTime", i["create_time"])
    cout += "Create_time :\n    {}\n".format(i["create_time"])
    wout += "<tr><td><b>CreateTime</b></td><td>{}</td></tr>\n".format(i["create_time"])
    for keym in [
        "OncallOps",
        "Status",
        "Impact",
        "RootCause",
        "DurationOfProblem",
        "ServiceImpacted",
        "%Impacted",
        "UserImpact",
        "RevenueImpact",
        "HowToRepeat",
        "Resolution",
        "References",
        "LessonLearned",
        "ActionItem",
        "KeywordsForSearch",
    ]:
        if keym in i and i[keym]:
            cout += "{} : \n".format(keym)
            cout += "    {}\n".format(i[keym])
            wout += "<tr><td><b>{}</b></td><td>{}</td></tr>\n".format(keym, i[keym])
            mout += "| {} | {} |\n".format(keym, i[keym])
        else:
            if args.post:
                i[keym] = input("# {}=".format(keym))
                cout += "{} : \n".format(keym)
                cout += "    {}\n".format(i[keym])
                wout += "<tr><td><b>{}</b></td><td>{}</td></tr>\n".format(keym, i[keym])
                mout += "| {} | {} |\n".format(keym, i[keym])
                closedb()
    wout += "</table>\n"
    if args.json:
        print(json.dumps(i, indent=2, sort_keys=True))
        return
    cout += "\n\n# timeline   : \n"
    wout += "<h2>Timeline    :</h2>\n"
    mout += "\n\n"
    mout += "### {} \n".format("Timeline :")
    mout += "| __datetime__ | __brief__ | __detail__ | \n"
    mout += "| ---- | ---- | ---- | \n"
    # wout += "<table style=\"border-collapse: collapse;border: 1px;\">\n"
    wout += '<table border=1 style="border-collapse: collapse;">\n'
    wout += '<tr style="background-color:#F3F3F3"><th>update_time</th><th>brief</th><th>detail</th></tr>\n'
    table = Texttable()
    table.set_header_align(["l", "l", "l"])
    table.set_cols_align(["l", "l", "l"])
    table.set_chars([" ", " ", " ", "-"])
    maxw = 0
    for x in [u.get("xcontent", "") for u in i.get("updates", dict())]:
        for l in x.splitlines():
            if len(l) > maxw:
                maxw = len(l)
    table.set_cols_width([12, 25, maxw + 1])
    rows = list()
    rows.append(["update_time", "brief", "detail"])
    for u in sorted(i.get("updates", []), key=lambda x: x["create_time"], reverse=True):
        rows.append([u["create_time"][:-3], u["update_content"], u.get("xcontent", "")])
        mout += "| {} | {} | <pre>{}</pre> | \n".format(
            u["create_time"][:-3],
            u["update_content"],
            re.sub(
                r"([\\\`\*\_\{\}\[\]\(\)#+-.!|])",
                r"\\\1",
                u.get("xcontent", "").replace("\n", "</br>").replace("~", "\$HOME"),
            ),
        )
        wout += "<tr>\n"
        for val in [u["create_time"][:-3], u["update_content"], u.get("xcontent", "")]:
            wout += "<td>{}</td>\n".format(
                val.replace("\n", "</br>").replace(" ", "&nbsp;")
            )
        wout += "</tr>\n"

    mout += "\n\n"
    table.add_rows(rows)
    stbl = table.draw()
    stbl = "\n".join([re.sub(r"\s+$", "", ln) for ln in stbl.splitlines()])
    cout += stbl + "\n"
    wout += "</table>\n"
    wout += "</html>\n"
    if args.export:
        if args.expand:
            incdir = (
                args.incident
                + "."
                + "".join(
                    c
                    for c in re.sub(r"\s+", ".", i["brief"])
                    if c in set(string.ascii_letters + string.digits + "_-.")
                )
            )
        else:
            incdir = args.incident
        if not os.path.exists(incdir):
            os.mkdir(incdir)
        with open("{}/{}.html".format(incdir, args.incident), "w") as f:
            f.write(wout)
        with open("{}/{}.txt".format(incdir, args.incident), "w") as f:
            f.write(cout)
        with open("{}/{}.md".format(incdir, args.incident), "w") as f:
            f.write(mout)
        with open("{}/{}.json".format(incdir, args.incident), "w") as f:
            f.write(json.dumps(db[args.incident], indent=2, sort_keys=True))
        sys.exit(0)
    if args.html:
        print(wout)
    elif args.markdown:
        print(mout)
    else:
        print(cout)


def add_new_incident():
    global args
    global db
    now = datetime.now()
    snow = "c" + now.strftime("%Y%m%d%H%M%S")
    create_time = now.strftime("%Y-%m-%d %H:%M:%S")
    while snow in db:
        sleep(1)
        now = datetime.now()
        snow = "c" + now.strftime("%Y%m%d%H%M%S")
        create_time = now.strftime("%Y-%m-%d %H:%M:%S")
    incident = dict()
    incident["incident_number"] = snow
    incident["create_time"] = create_time
    incident["brief"] = args.new
    incident["updates"] = list()
    db[snow] = incident
    print("# incident {} added.".format(snow))
    closedb()
    return snow


def update_incident():
    global args
    global db
    if args.incident not in db:
        print("# cannot find {}".format(args.incident))
        sys.exit(-1)
    updt = dict()
    now = datetime.now()
    update_time = now.strftime("%Y-%m-%d %H:%M:%S")
    updt["create_time"] = update_time
    updt["update_content"] = args.update
    updt["xcontent"] = args.attach
    if args.attach == "vi":
        tmpfile = "/tmp/.incident.{}.{}".format(
            args.incident, now.strftime("%Y%m%d%H%M%S")
        )
        os.system("vi {}".format(tmpfile))
        with open(tmpfile, "r") as f:
            updt["xcontent"] = f.read()
        os.unlink(tmpfile)
    if os.path.isfile(args.attach):
        with open(args.attach, "r") as f:
            updt["xcontent"] = f.read()
    db[args.incident]["updates"].append(updt)
    closedb()


def main():
    global args
    global db
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        "--dbfile",
        dest="db",
        default="~/.sretools/incidents.json",
        action="store_true",
        help="db file",
    )
    parser.add_argument(
        "-R",
        "--report",
        dest="report",
        default=False,
        action="store_true",
        help="run report",
    )
    parser.add_argument("-i", "--incident", dest="incident", help="incident number")
    parser.add_argument(
        "-n", "--new_incident", dest="new", help="new incident. value used for brief"
    )
    parser.add_argument(
        "-u", "--update_incident", dest="update", help="update incident with progress"
    )
    parser.add_argument(
        "-x",
        "--delete_incident",
        dest="delete",
        action="store_true",
        default=False,
        help="delete incident",
    )
    parser.add_argument(
        "-a",
        "--attachment",
        dest="attach",
        default="",
        help="detail info from file or vi.",
    )
    parser.add_argument(
        "-J",
        "--json",
        dest="json",
        action="store_true",
        default=False,
        help="dump incident postmortem in JSON format",
    )
    parser.add_argument(
        "-p",
        "--postmortem",
        dest="post",
        action="store_true",
        default=False,
        help="google SRE postmortem format",
    )
    parser.add_argument(
        "-w",
        "--html",
        dest="html",
        action="store_true",
        default=False,
        help="dump report in HTML format",
    )
    parser.add_argument(
        "-m",
        "--markdown",
        dest="markdown",
        default=False,
        action="store_true",
        help="dump report in Markdown format",
    )
    parser.add_argument(
        "-F",
        "--export",
        dest="export",
        action="store_true",
        default=False,
        help="export json/html/markdown file as well. use with -p.",
    )
    parser.add_argument(
        "-e",
        "--noexpanddirname",
        dest="expand",
        action="store_false",
        default=True,
        help="with -F. only use cid for dirname when specified.",
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
    if args.new:
        args.new = re.sub(r"\\n", "\n", args.new)
    if args.update:
        args.update = re.sub(r"\\n", "\n", args.update)
    if args.attach:
        args.attach = re.sub(r"\\n", "\n", args.attach)
    if not (args.incident or args.new or args.report):
        parser.print_help()
        sys.exit(0)
    db = initdb()
    if args.report:
        if not args.incident:
            show_incident_list()
        else:
            show_incident()
        sys.exit(0)
    if args.delete:
        delete_incident()
        closedb()
    if args.new:
        add_new_incident()
        closedb()
    if args.incident and args.update:
        update_incident()
        closedb()


if __name__ == "__main__":
    main()
