#!/usr/bin/env python3
# Yonghang Wang

import sys
import argparse
import os
import re
import jaydebeapi
from sretools import SimpleTable


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-J", "--jar", dest="jar", help="jdbc driver jar file")
    parser.add_argument("-D", "--driver", dest="driver", help="jdbc driver name")
    parser.add_argument("-U", "--url", dest="url", help="jdbc url or connection string")
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
        "-F", "--outformat", dest="format", default="", help="json,yaml,csv"
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

    if not args.jar:
        print("must specify jdbc driver jar(-J).")
        sys.exit(-1)

    if not args.driver:
        print("must specify jdbc driver name(-D).")
        sys.exit(-1)

    if not args.url:
        print("must specify connection string(-U).")
        sys.exit(-1)

    if not args.sql:
        print("must specify SQL statement(-Q).")
        sys.exit(-1)

    conn = jaydebeapi.connect(args.driver, args.url, jars=args.jar)
    cur = conn.cursor()
    cur.execute(args.sql)
    rchg = cur.rowcount
    if rchg == -1:
        try:
            data = cur.fetchall()
            hdr = [d[0] for d in cur.description]
            if args.debug:
                print("# header :", hdr)
                print("# data :", data)
            if args.pivot:
                print(SimpleTable(data=data, header=hdr).repr_pivot(), end="")
            else:
                if args.format == "json":
                    print(SimpleTable(data=data, header=hdr).get_json(), end="")
                elif args.format == "yaml":
                    print(SimpleTable(data=data, header=hdr).get_yaml(), end="")
                elif args.format == "csv":
                    print(SimpleTable(data=data, header=hdr).get_csv(), end="")
                else:
                    print(
                        SimpleTable(data=data, header=hdr, maxwidth=args.maxwidth),
                        end="",
                    )
        except:
            pass
        finally:
            cur.close()
    else:
        print("# {} rows impacted.".format(rchg))
    conn.close()


# postgresql
# sretools-jdbc-call  -J "/usr/share/java/postgresql.jar" -D "org.postgresql.Driver" -U "jdbc:postgresql://localhost:5432/sample?user=postgres&password=postgres" -Q "select id, count(*)cnt from t1 group by id"
# id cnt
# ------
# 1  1
# 2  1

# /jdbc_call.py -J ~/jdbc/db2jcc4.jar -D com.ibm.db2.jcc.DB2Driver  -U "jdbc:db2://localhost:50000/sample:user=db2inst1;password=db2inst1;" -Q "select viewschema,viewname,varchar(text) as text from syscat.views fetch first 1 rows only with ur"
# VIEWSCHEMA VIEWNAME          TEXT
# -------------------------------------------------------------------------------------------------------
# SYSIBM     CHECK_CONSTRAINTS CREATE OR REPLACE VIEW SYSIBM.CHECK_CONSTRAINTS
#                              (CONSTRAINT_CATALOG, CONSTRAINT_SCHEMA, CONSTRAINT_NAME, CHECK_CLAUSE)
#                              AS SELECT
#                              CAST(CURRENT SERVER AS VARCHAR(128)), TBCREATOR,
#                              CAST(NAME AS VARCHAR(128)), TEXT
#                              FROM SYSIBM.SYSCHECKS
#                              WHERE TYPE='C'
#                              UNION ALL
#                              SELECT CAST(CURRENT SERVER AS VARCHAR(128)), TBCREATOR,
#                              CAST(CONCAT(RTRIM(CONCAT(CHAR(CTIME), CHAR(FID) ) ),
#                              RTRIM(CHAR(COLNO)) ) AS VARCHAR(128) ),
#                              CAST(CONCAT(CONCAT('CHECK (', C.NAME), ' IS NOT NULL)') AS CLOB(64K) )
#                              FROM SYSIBM.SYSCOLUMNS C, SYSIBM.SYSTABLES T
#                              WHERE C.TBCREATOR = T.CREATOR AND C.TBNAME = T.NAME AND TYPE IN('U', 'T')
#                              AND NULLS ='N'
#

if __name__ == "__main__":
    main()
