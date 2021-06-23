# -*- coding: utf-8 -*-
# TBlock - An anticapitalist ad-blocker that uses the hosts file
# Copyright (C) 2021 Twann <twann@ctemplar.com>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# Standard libraries
import os
import sqlite3
import random

# External libraries
from colorama import init

# Compatibility with Windows
# See: https://codeberg.org/tblock/tblock/pulls/17
if os.name == 'nt':
    # On POSIX, this breaks the colors
    init(convert=True)


class Font:
    BOLD = '\033[1m'
    DEFAULT = '\033[0m'
    UNDERLINE = '\033[4m'

    # The check mark appears weird on Windows, so replace it by 'v'
    if os.name == 'nt':
        CHECK_MARK = 'v'
    else:
        CHECK_MARK = '✓'


class Var:

    # The default IP address where to redirect blocked domains
    DEFAULT_IP = '127.0.0.1'

    # The list of all official mirrors of the remote filter repository that are available
    # Read more: https://tblock.codeberg.page/wiki/filters/remote-repository#mirrors
    REPO_MIRRORS = [
        'https://codeberg.org/tblock/repo/raw/branch/main/index.xml',
        'https://0xacab.org/twann/repo/-/raw/main/index.xml',
        'https://git.disroot.org/tblock/repo/raw/branch/main/index.xml',
        'https://tblock.codeberg.page/repo/index.xml'
    ]

    # Shuffle the mirror list to avoid too much traffic on only one of them
    random.shuffle(REPO_MIRRORS)


class Path:

    # The script is running on Termux
    if os.path.isdir('/data/data/com.termux/files/usr/lib/'):
        PREFIX = '/data/data/com.termux/files/usr/lib/tblock/'
        HOSTS = '/system/etc/hosts'
        TMP_DIR = '/data/data/com.termux/files/usr/tmp/tblock/'

    # The script is running on a POSIX platform
    elif os.name == 'posix':
        PREFIX = '/var/lib/tblock/'
        HOSTS = '/etc/hosts'
        TMP_DIR = '/tmp/tblock/'

    # The script is running on Windows
    elif os.name == 'nt':
        PREFIX = os.path.join(os.path.expandvars('%ALLUSERSPROFILE%'), 'TBlock')
        HOSTS = os.path.join(os.path.expandvars('%WINDIR%'), 'System32', 'drivers', 'etc', 'hosts')
        TMP_DIR = os.path.join(os.path.expandvars('%TMP%'), 'tblock')

    # If the script is running on an unsupported platform, raise an error
    else:
        raise OSError('TBlock is currently not supported on your operating system')

    # Other paths
    DATABASE = os.path.join(PREFIX, 'storage.sqlite')
    HOSTS_BACKUP = os.path.join(PREFIX, 'hosts')
    REPO_VERSION = os.path.join(PREFIX, 'repo')
    HOSTS_VERIFICATION = os.path.join(PREFIX, 'hosts_protection')
    DB_LOCK = os.path.join(PREFIX, '.db-lock')
    NEEDS_UPDATE = os.path.join(PREFIX, '.needs-update')


def setup_database(db_path: str) -> None:
    """Setup the SQLite3 database that is needed by TBlock in order to work
    Args:
        db_path (str): The path to the database to setup
    """
    with sqlite3.connect(db_path) as db:
        db.cursor().execute('''CREATE TABLE IF NOT EXISTS "rules" (
            "domain"	TEXT NOT NULL UNIQUE,
            "policy"	TEXT NOT NULL,
            "filter_id"	TEXT NOT NULL,
            "priority"	INTEGER NOT NULL,
            "ip"	TEXT,
            PRIMARY KEY("domain")
        );''')
        db.cursor().execute('''CREATE TABLE IF NOT EXISTS "filters" (
            "id"	TEXT NOT NULL UNIQUE,
            "source"	TEXT NOT NULL UNIQUE,
            "metadata"	TEXT NOT NULL,
            "subscribing"	INTEGER NOT NULL,
            "on_rfr"	INTEGER NOT NULL,
            "permissions"   TEXT,
            PRIMARY KEY("id")
        );''')
        db.commit()


# NOTE: These lines should be executed every time TBlock is launched

def check_dirs() -> None:
    """Check and create directories and files that doesn't exist
    """
    # Check if the hosts file exists. If it doesn't, raise an error
    if not os.path.isfile(Path.HOSTS):
        raise OSError('TBlock is currently not supported on your operating system')

    # Create directories if they do not exist
    for d in [Path.PREFIX, Path.TMP_DIR]:
        if not os.path.isdir(d):
            try:
                os.mkdir(d)
            except PermissionError:
                continue

    # Setup the database if it does not exist
    if not os.path.isfile(Path.DATABASE):
        try:
            setup_database(Path.DATABASE)
        except (PermissionError, sqlite3.OperationalError):
            pass


# Check if TBlock is protecting the machine or not
global PROTECTING_STATUS
if os.path.isfile(Path.HOSTS_BACKUP):
    PROTECTING_STATUS = True
else:
    PROTECTING_STATUS = False
