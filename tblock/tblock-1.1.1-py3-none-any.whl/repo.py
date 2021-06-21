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
import json
import os.path
import sqlite3
from xml.etree import ElementTree

# External libraries
import requests
import urllib3
from colorama import Fore, Style

# Local libraries
from .filters import Filter, get_all_from_rfr
from .config import Path, Var, Font
from .utils import download_file, check_root, lock_database, unlock_database
from .exceptions import InvalidLinkError, NetworkError, SIGTERM


def sync_remote_repo(force: bool = False) -> None:
    """Sync the remote filter repository

    Args:
        force (bool, optional): Force update the remote repository (disabled by default)
    """
    if not check_root():
        raise PermissionError(f'{Fore.RED}ERROR: you need to run as root to perform this operation{Style.RESET_ALL}')

    print(':: Updating remote repository...')
    lock_database()

    # Download index
    tmp_index = os.path.join(Path.TMP_DIR, 'remote-repo.xml.tmp')
    for mirror in Var.REPO_MIRRORS:
        print(f' [{Fore.YELLOW}|{Style.RESET_ALL}] Get mirror: {mirror}', end='\r')
        try:
            download_file(mirror, tmp_index)
        except (requests.exceptions.ConnectionError, urllib3.exceptions.MaxRetryError, ConnectionRefusedError,
                urllib3.exceptions.NewConnectionError, InvalidLinkError):
            print(f' [{Fore.RED}x{Style.RESET_ALL}] Get mirror: {mirror}')
            if Var.REPO_MIRRORS.index(mirror) == len(Var.REPO_MIRRORS) - 1:
                raise NetworkError(f'{Fore.RED}ERROR: cannot download any remote repository mirror{Style.RESET_ALL}')
        else:
            print(f' [{Fore.GREEN}{Font.CHECK_MARK}{Style.RESET_ALL}] Get mirror: {mirror}')
            break

    # Check if the repository is an XML file, and if it is a valid repository
    print(f' [{Fore.YELLOW}|{Style.RESET_ALL}] Checking repository validity', end='\r')
    try:
        data = ElementTree.parse(tmp_index).getroot()
    except ElementTree.ParseError:
        print(f' [{Fore.RED}x{Style.RESET_ALL}] Checking repository validity')
        print(f' [{Fore.RED}x{Style.RESET_ALL}] Failed to update remote repository')
        raise SIGTERM()
    else:
        if data.tag == 'repository':
            print(f' [{Fore.GREEN}{Font.CHECK_MARK}{Style.RESET_ALL}] Checking repository validity')
        else:
            print(f' [{Fore.RED}x{Style.RESET_ALL}] Checking repository validity')
            print(f' [{Fore.RED}x{Style.RESET_ALL}] Failed to update remote repository')
            raise SIGTERM()

    # Check repository version
    if os.path.isfile(Path.REPO_VERSION):
        with open(Path.REPO_VERSION, 'rt') as f:
            current_version = int(f.read())
    else:
        current_version = 0
    if len(str(current_version)) >= 6 and int(str(current_version)[0:6]) >= int(data.attrib['version']) and not force:
        print(f' [{Fore.GREEN}{Font.CHECK_MARK}{Style.RESET_ALL}] Remote repository is up-to-date')
    else:

        # Upgrade the repository
        print(f' [{Fore.BLUE}i{Style.RESET_ALL}] Upgrading repository version {data.attrib["version"]} '
              f'over {str(current_version)}')
        all_filters = []
        count = 1
        db = sqlite3.connect(Path.DATABASE)
        for _filter in data:
            all_filters.append(_filter.attrib['id'])
        len_filters = len(all_filters)
        load_character = '|'
        warns = []

        for _filter in data:

            if count < len_filters:
                print(f' [{Fore.YELLOW}{load_character}{Style.RESET_ALL}] Updating filter index '
                      f'({count}/{len_filters})', end='\r')
                # Show process
                if load_character == '|' and not count % 2:
                    load_character = '/'
                elif load_character == '/' and not count % 2:
                    load_character = '-'
                elif load_character == '-' and not count % 2:
                    load_character = '\\'
                elif load_character == '\\' and not count % 2:
                    load_character = '|'
            else:
                print(
                    f' [{Fore.GREEN}{Font.CHECK_MARK}{Style.RESET_ALL}] Updating filter index ({count}/{len_filters})'
                )

            metadata = {
                "title": None,
                "description": None,
                "homepage": None,
                "license": None,
                "syntax": None
            }
            new_filter = Filter(_filter.attrib['id'])

            if new_filter.exists and new_filter.on_rfr:
                source = new_filter.source
            else:
                source = None

            for attr in _filter:

                if attr.tag == 'title':
                    metadata['title'] = attr.text
                elif attr.tag == 'desc':
                    metadata['description'] = attr.text
                elif attr.tag == 'homepage':
                    metadata['homepage'] = attr.text
                elif attr.tag == 'license':
                    metadata['license'] = attr.text
                elif attr.tag == 'syntax':
                    metadata['syntax'] = attr.text
                elif attr.tag == 'source':
                    source = attr.text
            if new_filter.exists and new_filter.on_rfr:
                db.cursor().execute(
                    'UPDATE "filters" SET source=?, metadata=? WHERE id=?;',
                    (source, json.dumps(metadata), new_filter.id)
                )
            elif not new_filter.exists:
                db.cursor().execute(
                    'INSERT INTO "filters" ("id", "source", "metadata", "on_rfr", "subscribing") '
                    'VALUES (?, ?, ?, ?, ?)',
                    (new_filter.id, source, json.dumps(metadata), True, False)
                )
            elif new_filter.exists and not new_filter.on_rfr:
                warns.append(new_filter.id)
            else:
                pass

            count += 1
        db.commit()

        # Check for all filters that were removed from the remote repository
        all_filters_in_db = get_all_from_rfr()
        for filter_id in all_filters_in_db:
            if filter_id not in all_filters:
                new_filter = Filter(filter_id)
                if new_filter.subscribing:
                    # Transform the filter into a custom filter if the user is subscribing to it
                    db.cursor().execute(
                        'UPDATE "filters" SET source=?, metadata=?, on_rfr=? WHERE id=?;',
                        (new_filter.source, json.dumps(new_filter.metadata), False, new_filter.id)
                    )
                else:
                    # Delete the filter if the user is not subscribing to it
                    db.cursor().execute(
                        'DELETE FROM "filters" WHERE "id"=?',
                        (new_filter.id,)
                    )

        db.commit()
        db.close()
        os.remove(tmp_index)

        # Write new version in the repo version file
        with open(os.path.realpath(Path.REPO_VERSION), 'wt') as f:
            f.write(data.attrib["version"])
        print(f' [{Fore.GREEN}{Font.CHECK_MARK}{Style.RESET_ALL}] Remote repository updated successfully')

        if warns:
            for warn in warns:
                print(f'{Fore.YELLOW}WARNING: the filter "{warn}" could not be updated as a '
                      f'custom filter takes its ID{Style.RESET_ALL}')

    unlock_database()
