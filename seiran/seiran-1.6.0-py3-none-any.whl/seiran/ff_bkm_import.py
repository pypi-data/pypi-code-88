"""
Import bookmarks from Firefox and derivatives: Pale Moon, IceCat,
Basilisk, Nightly, etc. This is not extremely well-tested. Use at your
own risk!
"""

import sqlite3, datetime, os
from collections import OrderedDict
import json


def formList(bookmark_tup: tuple) -> list:
    """
    Convert a tuple of bookmark data into a format Seiran can use.

    Parameters
    ----------
    bookmark_tup : tuple
        Raw bookmark data from the imported database.

    Returns
    -------
    list of tuple
        The title, URL, and date for the bookmark.
    """
    title, url, date_raw = bookmark_tup
    date_cut = int(date_raw) / 1000000
    date = datetime.datetime.fromtimestamp(date_cut).strftime("%Y-%m-%dT%H:%M:%S.%f%z")
    conv_list = [title, url, date]
    return conv_list


def flattenJson(imported_json: dict) -> list:
    """
    Flatten out the nested dictionary from a Firefox JSON import.

    Parameters
    ----------
    imported_json : dict
        The JSON input to flatten.

    Returns
    -------
    list of dict
        The JSON flatted out into a format usable by Seiran.
    """
    out = []

    def flatten(dic: dict) -> None:
        """
        Recursively flatten children of a dictionary list.

        Parameters
        ----------
        dic : dict
            The dictionary to flatten.
        """
        try:
            flatten(dic["children"])
        except KeyError:
            out.append(dic)
        except TypeError:
            for i in dic:
                flatten(i)

    flatten(imported_json)
    return out


def import_ffjson(json_path: str) -> list:
    """
    Import JSON data from a Firefox-type bookmark backup.

    Parameters
    ----------
    json_path : str
        Path to the JSON backup file.

    Returns
    -------
    list of tuple
        Processed bookmarks.
    """
    try:
        with open(json_path, "r", encoding="utf-8") as fin:
            j = json.load(fin)
    except FileNotFoundError:
        print("File {jsonf} not found.".format(jsonf=json_path))
        return False
    except json.decoder.JSONDecodeError:
        print(
            "Couldn't load {location} as JSON. It may be invalid.".format(
                location=json_path
            )
        )
        return False
    print("Preparing Firefox JSON bookmarks...")
    flattened = flattenJson(j)
    output = [
        formList((bookmark["title"], bookmark["uri"], str(bookmark["dateAdded"])))
        for bookmark in flattened
        if "title" in bookmark.keys() and "uri" in bookmark.keys()
    ]
    return output


def importDatabase() -> list:
    """
    Import a database from a Firefox-type browser profile.

    Returns
    -------
    list
        The bookmark data converted to Seiran's internal format.
    """
    # Get the full path of your Firefox profile.
    firefox = input(
        "Please enter the path to the Firefox profile directory OR the Firefox bookmarks JSON file from which you wish to import. > "
    )
    # Try JSON first.
    if firefox[-5:].lower() == ".json":
        try:
            jmarks = import_ffjson(firefox)
            if not jmarks:
                return False
            print(
                "{l} bookmarks loaded from {firefox}.".format(
                    l=len(jmarks), firefox=firefox
                )
            )
            return jmarks
        except json.decoder.JSONDecodeError:
            print(
                "Couldn't load {location} as JSON. It may be invalid.".format(
                    location=firefox
                )
            )
            return False
        except FileNotFoundError:
            print("File {jsonf} not found.".format(jsonf=firefox))
            return False
    # If it's not JSON, it's a directory with a SQLite database.

    # For whatever reason, Android profiles are set up completely
    # differently.
    mobile = input(
        "Is this from a mobile version of Firefox? If you're unsure, it probably is not. (y/n) > "
    )
    if mobile.lower() == "y":
        mobile = True
        database = os.path.join(firefox, "browser.db")
    else:
        mobile = False
        database = os.path.join(firefox, "places.sqlite")

    if not os.path.exists(database):
        print("File {dbf} not found.".format(dbf=database))
        return False
    try:
        conn = sqlite3.connect(database)
    except sqlite3.OperationalError:
        print(
            "Couldn't find a profile database of that type in {location}. You may be looking in the wrong directory, or it may be a different platform's database.".format(
                location=firefox
            )
        )
        return False
    cursor = conn.cursor()

    if not mobile:
        sql = "select id,title from moz_bookmarks where type=2;"
        cursor.execute(sql)
        folders = cursor.fetchall()

        bookmarks = OrderedDict()

        # Get folders first

        for id in folders:
            bookmarks[id[1]] = cursor.execute(
                "select b.title, a.url, b.dateAdded from moz_places a, moz_bookmarks b where a.id=b.fk and b.parent='%s';"
                % (id[0])
            ).fetchall()

        tup_list = []
        for i in bookmarks.items():
            tup_list.append(i)

        fmarks = []

        for i in tup_list:
            folderName = i[0]
            if folderName == "":
                folderName == "Blank"
            for item in i:
                if i[1]:
                    bms = i[1]
                    for bookmark in bms:
                        bookmark_list = formList(bookmark)
                        bookmark_list.append(folderName)
                        fmarks.append(bookmark_list)
                else:
                    pass

        # Now the individual, non-foldered bookmarks.
        bookmarks = OrderedDict()

        sql = "select id,title from moz_bookmarks where type=1;"
        cursor.execute(sql)
        single_bookmarks = cursor.fetchall()

        single_bookmarks = single_bookmarks[0:20]

        for id in single_bookmarks:
            bookmarks[id[1]] = cursor.execute(
                "select b.title, a.url, b.dateAdded from moz_places a, moz_bookmarks b where a.id=b.fk;"
            ).fetchall()

        tup_list = [item for item in bookmarks.items()][0][1]

        for i in tup_list:
            bookmark_list = formList(i)
            bookmark_list.append("")
            fmarks.append(bookmark_list)
    else:

        # Android browsers don't have folders and the database is set
        # up much more straightforwardly.

        fmarks = []

        sql = "select title,url,created from bookmarks;"

        bookmarks = cursor.execute(sql).fetchall()

        for i in bookmarks:
            bookmark_list = formList(i)
            bookmark_list.append("")
            fmarks.append(bookmark_list)

    conn.close()
    print(
        "{l} bookmarks loaded from {firefox}.".format(l=len(fmarks), firefox=database)
    )

    return fmarks
