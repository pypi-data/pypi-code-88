#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Seiran
#
# Copyright 2015-2020 Matthew "garrick" Ellison.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

name = "seiran"
author = "gargargarrick"
__author__ = "gargargarrick"
__version__ = "1.6.0"
__copyright__ = "Copyright 2015-2019 Matthew Ellison"
__license__ = "GPL"
__maintainer__ = "gargargarrick"
__status__ = "Development"

import datetime, os, sys, argparse, json
import sqlite3
from appdirs import *
import requests
from bs4 import BeautifulSoup
import seiran.ff_bkm_import
import seiran.onetab_bkm_import


def initBookmarks(c: sqlite3.Cursor) -> None:
    """
    Check if a bookmarks database already exists.

    Parameters
    ----------
    c : sqlite3.Cursor
        Cursor of the bookmarks database.
    """
    try:
        c.execute(
            """CREATE TABLE bookmarks
            (title text,url text NOT NULL,date text,folder text,PRIMARY KEY(url))"""
        )
        print("Database created.")
    except sqlite3.OperationalError:
        pass


def addBKM(
    c: sqlite3.Cursor, conn: sqlite3.Connection, title: str, url: str, folder: str
) -> None:
    """
    Add a new bookmark to the database.

    Parameters
    ----------
    c : sqlite3.Cursor
        Cursor of the bookmarks database.
    conn : sqlite3.Connection
        Connection to the bookmarks database.
    title : str
        The name of the new bookmark.
    url : str
        The new bookmark's Uniform Resource Locator. Must be unique.
    folder : str
        A category or folder for the new bookmark.
    """
    if not title:
        title = input("Title? > ")
    if not url:
        url = input("URL? > ")
    if not title:
        title = url

    # I don't want to connect to the net to validate bookmarks (that's
    # what browsers are for) so this only looking the first few
    # characters and does absolutely no other checking or processing.
    # Checking is done to make opening bookmarks in the browser a bit
    # easier; feel free to take that part out if you don't want or need
    # this feature. I would recommend leaving in checking for empty
    # URLs, though.

    while not url or url[0:4] != "http":
        print(
            "Sorry, that is empty or doesn't seem to be a URL. (Make sure your URL uses the HTTP or HTTPS protocol.)"
        )
        url = input("URL? > ")
    # Add the current date
    date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f%z")
    if not folder:
        folder = input("Folder/Category? (can be left blank) > ")
        if not folder:
            folder = "None"
    bkm = (
        title,
        url,
        date,
        folder,
    )

    # Frankly, I don't know how necessary SQL injection countermeasures
    # are for this specific program (what, are you going to inject your
    # OWN database?) but it always pays to be careful in my opinion.

    try:
        c.execute("INSERT INTO bookmarks VALUES (?,?,?,?)", bkm)
        print("Inserted.")
        conn.commit()
    # I don't want users to end up with databases full of duplicated
    # bookmarks by mistake, so URLs must be unique.
    except sqlite3.IntegrityError:
        print("Already exists.")
    except sqlite3.OperationalError:
        print("Operational error")


def delBKM(c: sqlite3.Cursor, conn: sqlite3.Connection, url: str) -> None:
    """
    Remove a bookmark from the database.

    Parameters
    ----------
    c : sqlite3.Cursor
        Cursor of the bookmarks database.
    conn : sqlite3.Connection
        Connection to the bookmarks database.
    url : str
        The U.R.L. of the bookmark to be deleted.
    """
    if not url:
        url = input("URL to delete? (Deleted bookmarks cannot be recovered!) > ")
    sq_url = (url,)
    c.execute("SELECT url FROM bookmarks WHERE url=?", sq_url)
    conn.commit()
    if len(c.fetchall()) >= 1:
        try:
            c.execute("DELETE FROM bookmarks WHERE url=?", sq_url)
            conn.commit()
            print("DELETED!")
        except:
            # Yeah, I got nothing.
            print("Unable to delete for unknown reasons.")
    else:
        print("No bookmark of {url} exists.".format(url=url))


def listBKMs(c: sqlite3.Cursor) -> None:
    """
    List all bookmarks in the database.

    Spaces are included at the ends of lines such that the output can be
    interpreted as Markdown.

    Parameters
    ----------
    c : sqlite3.Cursor
        Cursor of the bookmarks database.
    """
    c.execute("SELECT * from bookmarks")
    print("# Seiran Bookmarks")
    template = (
        "\nTitle: {title}  \n  URL: {url}  \n  Date: {date}  \n  Folder: {folder}"
    )
    for title, url, date, folder in c.fetchall():
        print(template.format(title=title, url=url, date=date, folder=folder))


def oneSearch(c: sqlite3.Cursor, search_term: str, column: str) -> None:
    """
    Search a single field in the bookmark database.

    Parameters
    ----------
    c : sqlite3.Cursor
        Cursor of the bookmarks database.
    search_term : str
        The phrase for which to search.
    column : str
        The field to search. Can be title, url, folder, or date.
    """
    sq_search_term = "%{search_term}%".format(search_term=search_term)
    t = (sq_search_term,)
    if column == "title":
        c.execute("SELECT * from bookmarks WHERE title LIKE ?", t)
    elif column == "url":
        c.execute("SELECT * from bookmarks WHERE url LIKE ?", t)
    elif column == "folder":
        c.execute("SELECT * from bookmarks WHERE folder LIKE ?", t)
    elif column == "date":
        c.execute("SELECT * from bookmarks WHERE date LIKE ?", t)
    result_list = c.fetchall()
    if not result_list:
        print("No results.")
    else:
        print(
            "\n# Seiran - Results for {column}: {search_term}".format(
                search_term=search_term, column=column
            )
        )
        template = (
            "\nTitle: {title}  \n  URL: {url}  \n  Date: {date}  \n  Folder: {folder}"
        )
        for title, url, date, folder in result_list:
            print(template.format(title=title, url=url, date=date, folder=folder))


def searchAll(c: sqlite3.Cursor, search_term: str) -> None:
    """
    Search all fields in the bookmark database.

    Parameters
    ----------
    c : sqlite3.Cursor
        Cursor of the bookmarks database.
    search_term : str
        The phrase for which to search.
    """
    sq_search_term = "%{search_term}%".format(search_term=search_term)
    t = (
        sq_search_term,
        sq_search_term,
        sq_search_term,
        sq_search_term,
    )
    results = []
    c.execute(
        "SELECT DISTINCT * from bookmarks WHERE title LIKE ? OR url LIKE ? OR folder LIKE ? OR date LIKE ?",
        t,
    )
    result_list = c.fetchall()
    for i in result_list:
        results.append(i)
    if results == []:
        print("No results.")
    else:
        print("\n# Seiran - {search_term}".format(search_term=search_term))
        template = (
            "\nTitle: {title}  \n  URL: {url}  \n  Date: {date}  \n  Folder: {folder}"
        )
        for title, url, date, folder in results:
            print(template.format(title=title, url=url, date=date, folder=folder))


def editBKM(
    c: sqlite3.Cursor, conn: sqlite3.Connection, url: str, field: str, new: str
) -> None:
    """
    Edit an existing bookmark.

    Parameters
    ----------
    c : sqlite3.Cursor
        Cursor of the bookmarks database.
    conn : sqlite3.Connection
        Connection to the bookmarks database.
    url : str
        The U.R.L. of the target bookmark.
    field : str
        The field to be edited. Can be title or folder.
    new : str
        The new value for the edited field.
    """
    if not url:
        url = input("Which URL do you want to edit? > ")
    sq_url = (url,)
    c.execute("SELECT * from bookmarks WHERE url = ?", sq_url)
    # error handling goes here
    you_found_it = False
    for title, url, date, folder in c:
        print("\nCurrent bookmark data:")
        print(
            "\nTitle: {title}\n  URL: {url}\n  Date: {date}\n  Folder: {folder}".format(
                title=title, url=url, date=date, folder=folder
            )
        )
        you_found_it = True
    if not you_found_it:
        print("Sorry, that doesn't seem to be a URL in the database. Try again.")
        return False
    if not field:
        field = input("Which field do you wish to edit? (title/category/none)> ")
    if field == "folder":
        field = "category"
    if field not in {"title", "category"}:
        return
    if not new:
        new = input("What should the new {field} be? > ".format(field=field))
        new = str(new)
    newBKM = (new, url)
    if field == "title":
        c.execute("UPDATE bookmarks SET title=? WHERE url=?", newBKM)
        conn.commit()
    elif field == "category":
        c.execute("UPDATE bookmarks SET folder=? WHERE url=?", newBKM)
        conn.commit()
    else:
        return
    print("\nUpdated bookmark.")
    c.execute("SELECT * from bookmarks WHERE url = ?", sq_url)
    for title, url, date, folder in c:
        print(
            "\nTitle: {title}\n  URL: {url}\n  Date: {date}\n  Folder: {folder}".format(
                title=title, url=url, date=date, folder=folder
            )
        )


def getFirefoxBookmarks(c: sqlite3.Cursor, conn: sqlite3.Connection) -> None:
    """
    Import bookmarks from Mozilla-based browsers.

    This is an experimental feature and may cause errors. Please back up
    your bookmark database before use.

    Parameters
    ----------
    c : sqlite3.Cursor
        Cursor of the bookmarks database.
    conn : sqlite3.Connection
        Connection to the bookmarks database.
    """
    # Grab the Firefox bookmarks.
    fmarks = seiran.ff_bkm_import.importDatabase()
    if not fmarks:
        return False
    # Add them to Seiran's database.
    for i in fmarks:
        try:
            bkm = (
                i[0],
                i[1],
                str(i[2]),
                i[3],
            )
        except IndexError:
            bkm = (
                i[0],
                i[1],
                str(i[2]),
                "Firefox",
            )
        try:
            c.execute("INSERT INTO bookmarks VALUES (?,?,?,?)", bkm)
            conn.commit()
        except sqlite3.IntegrityError:
            print("Duplicate found. Ignoring {i}.".format(i=i[1]))
        except sqlite3.OperationalError:
            print("Operational error")
    print("Import complete!")
    return


def getOneTabBookmarks(c: sqlite3.Cursor, conn: sqlite3.Connection) -> None:
    """
    Import bookmarks from a OneTab text export.

    This is an experimental feature and may cause errors. Please back up
    your bookmark database before use.

    Parameters
    ----------
    c : sqlite3.Cursor
        Cursor of the bookmarks database.
    conn : sqlite3.Connection
        Connection to the bookmarks database.
    """
    omarks = seiran.onetab_bkm_import.importFromTxt()
    if not omarks:
        return False
    for i in omarks:
        bkm = (
            i[0],
            i[1],
            str(i[2]),
            i[3],
        )
        try:
            c.execute("INSERT INTO bookmarks VALUES (?,?,?,?)", bkm)
            conn.commit()
        except sqlite3.IntegrityError:
            print("Duplicate found. Ignoring {i}.".format(i=i[1]))
        except sqlite3.OperationalError:
            print("Operational error")
    print("Import complete!")
    return


def getSeiranBookmarks(c: sqlite3.Cursor, conn: sqlite3.Connection) -> None:
    """
    Import bookmarks from an existing Seiran database.

    This is an experimental feature and may cause errors. Please back up
    your bookmark database before use.

    Parameters
    ----------
    c : sqlite3.Cursor
        Cursor of the bookmarks database.
    conn : sqlite3.Connection
        Connection to the bookmarks database.
    """
    print("Warning! This is not well-tested and may ruin everything.")
    print("Back up your database before use!")
    seiran_file = input("Enter the path to the Seiran database you want to copy. > ")
    if seiran_file.lower() == "q":
        print("Import cancelled.")
        return
    sconn = sqlite3.connect(seiran_file)
    sc = sconn.cursor()
    attach_main = "ATTACH DATABASE ? as x"
    main_db_path = installToConfig()
    main_db = (main_db_path,)
    c.execute(attach_main, main_db)
    attach_branch = "ATTACH DATABASE ? as y"
    branch_db = (seiran_file,)
    c.execute(attach_branch, branch_db)
    c.execute("INSERT OR IGNORE INTO x.bookmarks SELECT * FROM y.bookmarks;")
    conn.commit()
    print("Import complete!")
    return


def exportBookmarks(c: sqlite3.Cursor, fformat: str) -> None:
    """
    Export bookmark database to a file in the user data directory.

    Parameters
    ----------
    c : sqlite3.Cursor
        Cursor of the bookmarks database.
    fformat : str
        The target output format. Can be txt, html, or json.
    """
    c.execute("SELECT * from bookmarks")
    bookmarks = []
    if fformat == "txt":
        ## Using the same format as [list]
        template = (
            "Title: {title}  \n  URL: {url}  \n  Date: {date}  \n  Folder: {folder}\n"
        )
    elif fformat == "html":
        template = (
            "<p><a href={url}>{title}</a> ({folder}) [<time='{date}'>{date}</a>]</p>"
        )
    if not fformat == "json":
        for title, url, date, folder in c.fetchall():
            if not title or title == "None":
                title = url
            bookmarks.append(
                template.format(title=title, url=url, date=date, folder=folder)
            )
    else:
        for title, url, date, folder in c.fetchall():
            if not title or title == "None":
                title = url
            bkm_d = {"title": title, "url": url, "date": date, "category": folder}
            bookmarks.append(bkm_d)
    save_path = user_data_dir(name, author)
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    file_name = "seiran_bookmarks_export_{date}.{fformat}".format(
        date=datetime.datetime.now().strftime("%Y-%m-%d"), fformat=fformat
    )
    bookmarks_out = os.path.join(save_path, file_name)
    if fformat == "txt":
        bookmarks_write = "\n".join(bookmarks)
    elif fformat == "html":
        front_matter = [
            "<!DOCTYPE HTML>",
            "<html>",
            "<head>",
            "<title>Seiran Bookmarks</title>",
            """<meta charset="utf-8">""",
            "</head>",
            "<body>",
            "<h1>Seiran Bookmarks</h1>",
        ]

        end_matter = ["</body>", "</html>"]
        bookmarks_write = "\n".join(front_matter + bookmarks + end_matter)
    elif fformat == "json":
        bookmarks_write = {"seirandb": bookmarks}
        with open(bookmarks_out, "w", encoding="utf-8") as fout:
            json.dump(bookmarks_write, fout)
            print("Exported to {bookmarks_out}".format(bookmarks_out=bookmarks_out))
        return
    with open(bookmarks_out, "w", encoding="utf-8") as f_out:
        f_out.write(bookmarks_write)
    print("Exported to {bookmarks_out}.".format(bookmarks_out=bookmarks_out))
    return


def cleanBKMs(c: sqlite3.Cursor, conn: sqlite3.Connection) -> None:
    """
    Perform basic housekeeping features on the bookmarks database.

    It checks for bookmarks without titles, then adds their U.R.L. as a
    title. It also lists bookmarks that have the same title, which may
    indicate duplicates.

    Parameters
    ----------
    c : sqlite3.Cursor
        Cursor of the bookmarks database.
    conn : sqlite3.Connection
        Connection to the bookmarks database.
    """
    c.execute("SELECT * from bookmarks")
    for i in c.fetchall():
        # Check for empty titles
        if not i or i[0] == "None":
            print(
                "Bookmark {url} doesn't have a title. Adding URL as title.".format(
                    url=i[1]
                )
            )
            new_title = i[1]
            newBKM = (
                new_title,
                i[1],
            )
            c.execute("UPDATE bookmarks SET title=? WHERE url=?", newBKM)
            conn.commit()
    # And this one checks for ones that might be duplicates.
    print("# Seiran Cleanup")
    c.execute("SELECT title, COUNT(*) c FROM bookmarks GROUP BY title HAVING c > 1;")
    result_list = c.fetchall()
    if not result_list:
        print("No results.")
    else:
        template = """\n{count} bookmarks have the title "{title}":\n"""
        for i in result_list:
            print(template.format(title=i[0], count=i[1]))
            t = (i[0],)
            c.execute("SELECT url from bookmarks where title is ?", t)
            url_list = c.fetchall()
            for ordinal, u in enumerate(url_list, start=1):
                print("{ordinal}. {url}".format(ordinal=str(ordinal), url=u[0]))
    return


def getJsonBookmarks(c: sqlite3.Cursor, conn: sqlite3.Connection) -> None:
    """
    Import bookmarks from a Seiran JSON export.

    Parameters
    ----------
    c : sqlite3.Cursor
        Cursor of the bookmarks database.
    conn : sqlite3.Connection
        Connection to the bookmarks database.
    """
    json_input = input("Enter the path to the .json exported from Seiran. > ")
    try:
        with open(json_input, "r", encoding="utf-8") as fin:
            j = json.load(fin)
    except FileNotFoundError:
        print("File {jsonf} not found.".format(jsonf=json_input))
        return False
    except json.decoder.JSONDecodeError:
        print(
            "Couldn't load {location} as JSON. It may be invalid.".format(
                location=json_input
            )
        )
        return False
    try:
        jmarks = j["seirandb"]
    except KeyError:
        print("Unable to extract bookmarks. This file was not exported from Seiran.")
        return False
    for bkmd in jmarks:
        bkm = tuple(bkmd.values())
        try:
            c.execute("INSERT INTO bookmarks VALUES (?,?,?,?)", bkm)
            conn.commit()
        except sqlite3.IntegrityError:
            print("Duplicate found. Ignoring {i}.".format(i=i[1]))
        except sqlite3.OperationalError:
            print("Operational error")
    print("Import complete!")
    return


def installToConfig() -> str:
    """
    Create a Seiran folder in the user's data directory, and get the
    path to the bookmarks database within.

    Returns
    -------
    str
        The path to the active bookmarks.db file.
    """
    config_path = user_data_dir(name, author)
    if not os.path.exists(config_path):
        os.makedirs(config_path)
    bookmarks_file = os.path.join(config_path, "bookmarks.db")
    return bookmarks_file


def main() -> None:
    """
    Set up the database and parse arguments.
    """
    bookmarks_file = installToConfig()
    conn = sqlite3.connect(bookmarks_file)
    c = conn.cursor()
    initBookmarks(c)
    print(
        "{name} by {author}, v.{version}.".format(
            name=name, author=__author__, version=__version__
        )
    )

    parser = argparse.ArgumentParser(prog="seiran")
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    parser_help = subparsers.add_parser("help", help="List commands")
    parser_add = subparsers.add_parser("add", help="Create a new bookmark.")
    parser_del = subparsers.add_parser("del", help="Remove a bookmark.")
    parser_list = subparsers.add_parser(
        "list", help="Display all bookmarks in the database."
    )
    parser_search = subparsers.add_parser("search", help="Find specific bookmark(s).")
    parser_edit = subparsers.add_parser("edit", help="Change a bookmark's metadata.")
    parser_import = subparsers.add_parser(
        "import", help="Add bookmarks from another system to the database."
    )
    parser_export = subparsers.add_parser(
        "export", help="Save all bookmarks to a formatted file."
    )
    parser_clean = subparsers.add_parser("clean", help="Tidy up bookmark metadata.")
    parser_copyright = subparsers.add_parser(
        "copyright", help="Show legal information."
    )

    parser_add.add_argument(
        "-t",
        "--title",
        help="A bookmark's name. Usually appears in <h1> or <title> tags on the page.",
    )
    parser_add.add_argument(
        "-u", "--url", help="A bookmark's Universal Resource Locator. Must be unique."
    )
    parser_edit.add_argument(
        "-u", "--url", help="A bookmark's Universal Resource Locator. Must be unique."
    )
    parser_del.add_argument(
        "-u",
        "--url",
        help="The Universal Resource Locator of the bookmark you want to delete.",
    )
    parser_add.add_argument(
        "-c",
        "--category",
        help="A bookmark's category. This is inspired by Firefox's folders, but you can put almost anything here.",
    )
    parser_search.add_argument(
        "-f",
        "--field",
        help="The column you want to search. Available arguments are title, url, category, date, or all.",
    )
    parser_edit.add_argument(
        "-f",
        "--field",
        help="The column you want to edit. Available arguments are title or category.",
    )
    parser_search.add_argument("-q", "--query", help="The term you want to search for.")
    parser_edit.add_argument(
        "-n", "--new", help="The new value you want an edited field to have."
    )
    parser_import.add_argument(
        "-i",
        "--importformat",
        help="The system you want to import bookmarks from. Available arguments are firefox, onetab, seiran, or json.",
    )
    parser_export.add_argument(
        "-x",
        "--exportformat",
        help="The format you want to export your bookmarks to. Available options are txt or html.",
    )
    choice = parser.parse_args()

    if choice.command == "add":
        addBKM(c, conn, choice.title, choice.url, choice.category)
    elif choice.command == "del":
        delBKM(c, conn, choice.url)
    elif choice.command == "list":
        print("Listing all bookmarks...")
        listBKMs(c)
        return
    elif choice.command == "search":
        field = choice.field
        if not field:
            field = input("  Which field? (title/url/category/date/all) > ")
        search_term = choice.query
        if not search_term:
            search_term = input("  Search term? (case insensitive) > ")
        if field.lower() == "title":
            oneSearch(c, search_term, "title")
        elif field.lower() == "url":
            oneSearch(c, search_term, "url")
            return
        elif field.lower() == "category":
            oneSearch(c, search_term, "folder")
            return
        elif field.lower() == "date":
            oneSearch(c, search_term, "date")
        else:
            searchAll(c, search_term)
            return
    elif choice.command == "edit":
        editBKM(c, conn, choice.url, choice.field, choice.new)
    elif choice.command == "import":
        # This has a big enough possibility to mess things up that I'm
        # not adding an argument to do it automatically. You must accept
        # manually to avoid accidents.
        ic = input(
            "Are you sure you want to import bookmarks? It might take a while. Back up your database first! (y/N) > "
        )
        if ic.lower() == "y" or ic.lower() == "yes":
            importer_c = choice.importformat
            if not importer_c:
                importer_c = input(
                    "Import from Firefox-type browser, OneTab export, another Seiran database, or JSON? (firefox/onetab/seiran/json) > "
                )
            if importer_c == "firefox":
                getFirefoxBookmarks(c, conn)
                return
            elif importer_c == "onetab":
                getOneTabBookmarks(c, conn)
                return
            elif importer_c == "seiran":
                getSeiranBookmarks(c, conn)
                return
            elif importer_c == "json":
                getJsonBookmarks(c, conn)
        else:
            print("OK, nothing will be copied.")
    elif choice.command == "export":
        ex_form = choice.exportformat
        if not ex_form:
            ex_form = input("Which format? (html,txt,json) > ")
        if ex_form.lower() in {"html", "txt", "json"}:
            exportBookmarks(c, ex_form)
            return
        else:
            print("Unrecognized format. Export cancelled.")
            return
    elif choice.command == "clean":
        cleanBKMs(c, conn)
        return
    elif choice.command == "copyright":
        print(
            "Copyright 2015-2021 Matthew 'gargargarrick' Ellison. Released under the GNU GPL version 3. See LICENSE for full details."
        )
    elif choice.command == "help":
        print(
            "Available arguments: add [a bookmark], del[ete a bookmark], list [all bookmarks], search [bookmarks], edit [a bookmark], import [bookmarks from other system], export [bookmarks to other formats], clean [bookmark metadata], copyright, help"
        )
    else:
        conn.close()


if __name__ == "__main__":
    main()
