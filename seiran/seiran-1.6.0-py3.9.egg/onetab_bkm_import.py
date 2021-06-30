"""
Import bookmarks from the OneTab addon.
This is not extremely well-tested. Use at your own risk!
"""

import sqlite3, datetime, os, sys


def importFromTxt() -> list:
    """
    Import bookmarks from a plain-text list of titles and URLs.

    Returns
    -------
    list of tuple
        The bookmark data converted to Seiran's internal format.
    """
    onetab_file = input("Enter the path to the .txt exported from OneTab. > ")
    try:
        with open(onetab_file, "r", encoding="utf-8") as f:
            onetab_raw = f.read().splitlines()
    except FileNotFoundError:
        print("File {otf} not found.".format(otf=onetab_file))
        return False
    onetab = []
    for entry in onetab_raw:
        if entry.strip():
            entry_pieces = entry.split(" | ", 1)
            try:
                url, title = entry_pieces
            except ValueError:
                (title,) = entry_pieces
                (url,) = entry_pieces
            # OneTab exports don't include the time data for some
            # reason, so we'll just set the date to the import time.
            date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f%z")
            category = "OneTab"
            bookmark = (title, url, date, category)
            onetab.append(bookmark)
    print(
        "{l} bookmarks loaded from {database}.".format(
            l=len(onetab), database=onetab_file
        )
    )
    return onetab
