import sqlite3
from dataclasses import dataclass
from typing import List

conn = sqlite3.connect("../todolist.sqlite3", check_same_thread=False)


@dataclass
class TODOItem:
    id: int
    title: str
    is_done: int = 0


def init():
    cur = conn.cursor()
    create = "CREATE TABLE IF NOT EXISTS todo (" \
             "id integer primary key autoincrement, " \
             "title varchar, " \
             "is_done integer default 0)"
    cur.execute(create)

    conn.commit()


def close():
    conn.close()


def parse_items(items: List[tuple]) -> List[TODOItem]:
    parsed_items = []
    for item in items:
        parsed_items.append(TODOItem(*item))
    return parsed_items


def get_all() -> List[TODOItem]:
    """Returns all items"""
    cur = conn.execute("SELECT * FROM todo")
    all_items = cur.fetchall()
    return parse_items(all_items)


def get_undone() -> List[TODOItem]:
    """Returns undone items"""
    cur = conn.execute("SELECT * FROM todo WHERE is_done = 0")
    undone = cur.fetchall()
    return parse_items(undone)


def get_done() -> List[TODOItem]:
    """Returns done items"""
    cur = conn.execute("SELECT * FROM todo WHERE is_done = 1")
    done = cur.fetchall()
    return parse_items(done)


def create_item(title: str):
    """Creates an item with title"""
    item = {
        "title": title
    }

    query = "INSERT INTO todo (title) VALUES (:title)"
    conn.execute(query, item)
    conn.commit()


def set_item_done(item_id: int, done: bool = True):
    """Sets item done with specific ID"""
    is_done = 1 if done else 0
    conn.execute(f"UPDATE todo set is_done={is_done} WHERE id={item_id}")
    conn.commit()


def edit_item(item_id: int, title: str):
    """Edits item title with ID"""
    conn.execute(f"UPDATE todo set title='{title}' WHERE id={item_id}")
    conn.commit()


def delete_item(item_id: int):
    """Deletes item with specific ID"""
    conn.execute(f"DELETE FROM todo WHERE id={item_id}")
    conn.commit()
