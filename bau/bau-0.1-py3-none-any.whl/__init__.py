from contextlib import contextmanager
import sqlite3
import hashlib
import json
import os
import subprocess
from types import SimpleNamespace
import sys

from .util import error, info, sha256sum
from .rule import rule, Rule
from . import c, pkgconfig, util

class Output:
    VERSION = 2
    def __init__(self, dir):
        # all rules, used to purge unused rules from the database
        self.rules = set()

        self.dir = dir
        os.makedirs(dir, exist_ok=True)
        con = sqlite3.connect(os.path.join(dir, ".build.db"))
        (version0,) = next(con.execute("pragma user_version"))

        if version0 < self.VERSION:
            info(f"[init] db migration {version0} -> {self.VERSION}")
        elif version0 > self.VERSION:
            error("bau database version not supported - please upgrade")
            sys.exit(10)

        version = version0
        if version == 0:
            with con:
                con.execute("""
                  create table if not exists rules
                    ( hash blob primary key
                    , result blob )""")
                con.execute("""
                  create table if not exists files
                    ( path text
                    , rule blob
                    , hash blob
                    , unique(path, rule) on conflict replace )""")
                con.execute("""
                  create index if not exists idx_files on files
                    ( rule )""")
                # globals and idx_globals used to be created here, but they are
                # not needed anymore, so there is no point in creating them
            version = 1

        if version == 1:
            with con:
                con.execute("drop table if exists globals;")
                con.execute("drop index if exists idx_globals;")
            version = 2

        if version0 < self.VERSION:
            con.execute(f"pragma user_version = {self.VERSION}")

        self.con = con

    def get(self, rule):
        self.rules.add(rule.hash)

        cur = self.con.execute("select result from rules where hash = ?",
                (rule.hash,))
        try:
            (result,) = next(cur)
        except StopIteration:
            return

        try:
            result = json.loads(result)
        except json.JSONDecodeError:
            return None

        # check file dependencies
        cur = self.con.execute("select path, hash from files where rule = ?",
                (rule.hash,))

        for path, h in cur:
            if sha256sum(path) != h:
                return None

        return SimpleNamespace(result=result)

    def put(self, rule, result):
        with self.con as con:
            con.execute("""
            insert into rules (hash, result) 
                values (?, ?)
                on conflict (hash)
                do update set result = excluded.result""",
                (rule.hash, json.dumps(result)))

    def cleanup(self):
        query = ", ".join('?' for r in self.rules)
        params = tuple(self.rules)

        with self.con as con:
            con.execute(f"delete from rules where hash not in ({query})", params)
            con.execute(f"delete from files where rule not in ({query})", params)

@contextmanager
def build(path):
    out = Output(path)
    try:
        yield out
    except subprocess.CalledProcessError:
        sys.exit(1)

    # only cleanup old rules if we complete successfully
    out.cleanup()

def bau(path, script='build.py'):
    sub = subprocess.Popen(
        [sys.executable, os.path.join(path, script)],
        encoding='utf-8',
        stdout=subprocess.PIPE,
        cwd=path)
    silent = True
    for line in sub.stdout:
        if silent:
            silent = False
            info('>>>', path)
        print(line, end='')
    if not silent:
        info('<<<')
