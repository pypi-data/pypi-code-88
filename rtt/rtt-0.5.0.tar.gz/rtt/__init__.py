from functools import cache
from tabulate import tabulate
from argparse import ArgumentParser
from datetime import datetime, timedelta
from os.path import expanduser, exists, join
from subprocess import check_call
from json import dumps, loads
from sqlite3 import connect


def get_default_config():
    return dict(
        utc_reset_hour=3,
        tasks=dict(setup_rtt="Setup your rtt config (~/.rtt/config.json)"),
    )


def get_args():
    root_parser = ArgumentParser()
    sub_parsers = root_parser.add_subparsers(dest="cmd", required=True)
    sub_parsers.add_parser("status")
    record_parser = sub_parsers.add_parser("complete")
    record_parser.add_argument("task")
    return root_parser.parse_args()


@cache
def get_rtt_path():
    path = expanduser("~/.rtt")
    check_call(["mkdir", "-p", path])
    return path


@cache
def get_config():
    path = join(get_rtt_path(), "config.json")
    if not exists(path):
        with open(path, "w") as f:
            f.write(dumps(get_default_config(), indent=4))
    with open(path) as f:
        return loads(f.read())


@cache
def get_log():
    path = join(get_rtt_path(), "log.db")
    return connect(path)


def get_tasks():
    return get_config()["tasks"]


def get_utc_reset_hour():
    return get_config()["utc_reset_hour"]


def get_description(name):
    tasks = get_tasks()
    if name not in tasks:
        raise RuntimeError(f"Task: {name} doesn't exist in the config.")
    return tasks[name]


def setup_log():
    con = get_log()
    cur = con.cursor()
    cur.execute(
        f"""
        CREATE TABLE IF NOT EXISTS completed_task (
            name TEXT,
            description TEXT NOT NULL,
            completed_at TIMESTAMP NOT NULL
        );
    """
    )
    cur.execute(
        f"""
        CREATE INDEX IF NOT EXISTS completed_task_ix
            ON completed_task (name, completed_at);
    """
    )
    con.commit()


def get_last_reset():
    reset_hour = get_utc_reset_hour()
    utc_now = datetime.utcnow()
    utc_reset = utc_now.replace(hour=reset_hour, minute=0)
    if utc_reset > utc_now:
        utc_reset -= timedelta(days=1)
    return utc_reset


def is_task_completed(name):
    row = (
        get_log()
        .cursor()
        .execute(
            f"""
        SELECT 1 FROM completed_task
        WHERE name = ?
        AND completed_at > ?
    """,
            (name, get_last_reset()),
        )
        .fetchone()
    )
    return row is not None


def complete_task(name):
    if is_task_completed(name):
        return

    con = get_log()
    con.cursor().execute(
        f"""
        INSERT INTO completed_task VALUES (
            ?, ?, ?
        )
    """,
        (name, get_description(name), datetime.utcnow()),
    )
    con.commit()


def print_task_statuses():
    tbl = list()
    for name, description in get_tasks().items():
        tbl.append([name, description, "Complete" if is_task_completed(name) else ""])
    tbl.sort(key=lambda x: x[0])
    print(tabulate(tbl, headers=["Task", "Description", "Status"]))


def cli():
    setup_log()
    args = get_args()
    if args.cmd == "status":
        print_task_statuses()
    elif args.cmd == "complete":
        complete_task(args.task)
