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
import sqlite3
import os.path
import json
import re

# External libraries
from colorama import Fore, Style
import requests
import urllib3

# Local libraries
from .rules import get_all_rules
from .converter.parser import FilterParser
from .config import Path, Font
from .utils import check_root, prompt_user, is_url, download_file, lock_database, unlock_database
from .hosts import update_hosts
from .exceptions import FilterExistsError, FilterSourceExistsError, AlreadySubscribingError, InvalidLinkError, \
    FilterNotExists, NotSubscribingError, SIGTERM, NetworkError, MissingArgumentError, FilterReservedError, \
    InvalidFilterSyntax, FilterNotCustomError


class FilterPermissions:

    def __init__(self, pattern: str = None) -> None:
        """Filter permission object (which rule policies a filter is allowed to use)

        Args:
            pattern (str, optional): The pattern that contains permissions
        """

        # By default, is a permission pattern is empty, the only policy allowed will be blocked
        # Therefore, it is impossible to restrict a filter to add all types of rule policies. The only way to do that is
        # to unsubscribe to the filter. There would be no reason to keep a filter as 'subscribed' if that filter was
        # not allowed to set any rules; it would simply slow down TBlock, since it would still need to download the
        # source of the filter.
        if not pattern:
            self.block = True
            self.allow = False
            self.redirect = False

        else:
            if re.match(re.compile(r'.*b', re.IGNORECASE), pattern):
                self.block = True
            else:
                self.block = False
            if re.match(re.compile(r'.*a', re.IGNORECASE), pattern):
                self.allow = True
            else:
                self.allow = False
            if re.match(re.compile(r'.*r', re.IGNORECASE), pattern):
                self.redirect = True
            else:
                self.redirect = False

        # Cleanly redefine permission pattern to avoid multiple 'a', 'b' or 'r', or uppercase letters
        self.pattern = ''
        self.pattern += 'a' if self.allow else ''
        self.pattern += 'b' if self.block else ''
        self.pattern += 'r' if self.redirect else ''


class Filter:

    def __init__(self, filter_id: str) -> None:
        """Filter object

        Args:
            filter_id (str): The ID of the filter
        """

        if filter_id == '!user':
            raise FilterReservedError('the filter ID "!user" is reserved by TBlock and cannot be used')
        self.id = filter_id

        # Fetch filter data from the database
        with sqlite3.connect(Path.DATABASE) as conn:
            data = conn.cursor().execute(
                'SELECT "source", "metadata", "subscribing", "on_rfr", "permissions" FROM "filters" WHERE id=?;',
                (self.id,)
            ).fetchall()
        self.exists = bool(data)
        self.source = data[0][0] if data else None
        self.metadata = json.loads(data[0][1]) if data else {}
        self.subscribing = bool(data[0][2]) if data else False
        self.on_rfr = bool(data[0][3]) if data else False
        self.permissions = FilterPermissions(data[0][4]) if data else None

    def subscribe(self, permissions: FilterPermissions, source: str = None) -> None:
        """Mark a filter as subscribed in the database

        Args:
            permissions (FilterPermissions): Permissions of the filter
            source (str, optional): If the filter is a custom filter, specify its source
        """
        self.permissions = permissions
        print(f'{Font.BOLD}==> Subscribing to filter: {self.id}{Font.DEFAULT}')

        if source:
            if self.exists:
                raise FilterExistsError(f'the filter "{self.id}" already exists')
            else:
                if source in get_all_sources():
                    raise FilterSourceExistsError(f'the source "{source}" is already the source of another filter')
                else:
                    self.source = source if is_url(source) else os.path.realpath(source)
                    self.update(verbosity=False, subscribing_operation=True)
                    print(f' [{Fore.YELLOW}|{Style.RESET_ALL}] Marking filter as subscribed in database', end='\r')
                    with sqlite3.connect(Path.DATABASE) as conn:
                        conn.cursor().execute(
                            'INSERT INTO "filters" ("id", "source", "metadata", "subscribing", "on_rfr", "permissions")'
                            'VALUES (?, ?, ?, ?, ?, ?);',
                            (self.id, self.source, json.dumps(self.metadata), True, False, self.permissions.pattern)
                        )
                        conn.commit()
                    self.exists = True
                    self.subscribing = True
                    print(f' [{Fore.GREEN}{Font.CHECK_MARK}{Style.RESET_ALL}] Marking filter as subscribed in database')

        else:
            if not self.exists:
                raise FilterNotExists(f'the filter "{self.id}" does not exist or is not available')
            else:
                if self.subscribing:
                    raise AlreadySubscribingError(f'you are already subscribing to filter: "{self.id}"')
                else:
                    self.update(verbosity=False, subscribing_operation=True)
                    print(f' [{Fore.YELLOW}|{Style.RESET_ALL}] Marking filter as subscribed in database', end='\r')
                    with sqlite3.connect(Path.DATABASE) as conn:
                        conn.cursor().execute(
                            'UPDATE "filters" SET subscribing=?, permissions=? WHERE id=?;',
                            (True, permissions.pattern, self.id)
                        )
                        conn.commit()
                    self.subscribing = True
                    print(f' [{Fore.GREEN}{Font.CHECK_MARK}{Style.RESET_ALL}] Marking filter as subscribed in database')

    def change_permissions(self, permissions: FilterPermissions) -> None:
        """Change the permissions of a filter

        Args:
            permissions (FilterPermissions): New permissions of the filter
        """
        if not self.exists:
            raise FilterNotExists(f'the filter "{self.id}" does not exist or is not available')
        elif not self.subscribing:
            raise NotSubscribingError(f'you are not subscribing to filter "{self.id}"')
        print(f'{Font.BOLD}==> Changing permissions of filter: {self.id}{Font.DEFAULT}')
        print(f' [{Fore.YELLOW}|{Style.RESET_ALL}] Writing new permissions in database', end='\r')
        with sqlite3.connect(Path.DATABASE) as conn:
            conn.cursor().execute(
                'UPDATE "filters" SET permissions=? WHERE id=?;',
                (permissions.pattern, self.id)
            )
            conn.commit()
        self.permissions = permissions
        print(f' [{Fore.GREEN}{Font.CHECK_MARK}{Style.RESET_ALL}] Writing new permissions in database')

    def unsubscribe(self) -> None:
        """Unsubscribe from a filter. If the filter is available on the remote filter repository, it will simply be
           marked as "unsubscribed", but if it is a custom filter, it will be removed from the database.
        """
        if not self.exists:
            raise FilterNotExists(f'the filter "{self.id}" does not exist or is not available')
        elif not self.subscribing:
            raise NotSubscribingError(f'you are not subscribing to filter "{self.id}"')
        print(f'{Font.BOLD}==> Unsubscribing from filter: {self.id}{Font.DEFAULT}')
        with sqlite3.connect(Path.DATABASE) as conn:

            # Simply mark as "unsubscribed" if filter is available on the remote repository
            if self.on_rfr:
                print(f' [{Fore.YELLOW}|{Style.RESET_ALL}] Marking filter as subscribed in database', end='\r')
                conn.cursor().execute(
                    'UPDATE "filters" SET subscribing=?, permissions=? WHERE id=?;',
                    (False, None, self.id)
                )
                self.subscribing = False
                print(f' [{Fore.GREEN}{Font.CHECK_MARK}{Style.RESET_ALL}] Marking filter as subscribed in database')

            # Remove filter from the database if it is a custom filter
            else:
                print(f' [{Fore.YELLOW}|{Style.RESET_ALL}] Removing custom filter from database', end='\r')
                conn.cursor().execute(
                    'DELETE FROM "filters" WHERE id=?;',
                    (self.id,)
                )
                self.exists = False
                self.subscribing = False
                print(f' [{Fore.GREEN}{Font.CHECK_MARK}{Style.RESET_ALL}] Removing custom filter from database')
            conn.commit()

    def delete_all_rules(self) -> None:
        print(f' [{Fore.YELLOW}|{Style.RESET_ALL}] Removing all filter rules from database', end='\r')
        with sqlite3.connect(Path.DATABASE) as conn:
            conn.cursor().execute(
                'DELETE FROM "rules" WHERE filter_id=?;',
                (self.id,)
            )
            conn.commit()
        print(f' [{Fore.GREEN}{Font.CHECK_MARK}{Style.RESET_ALL}] Removing all filter rules from database')

    def change_id(self, new_id: str) -> None:
        """Change the ID of a custom filter

        Args:
            new_id (str): The new filter ID to use
        """
        if not self.exists:
            raise FilterNotExists(f'the filter "{self.id}" does not exist or is not available')
        elif self.on_rfr:
            raise FilterNotCustomError(f'the filter "{self.id}" is not a custom filter')
        print(f'{Font.BOLD}==> Changing filter ID: {self.id}{Font.DEFAULT}')
        self.delete_all_rules()
        with sqlite3.connect(Path.DATABASE) as conn:
            conn.cursor().execute(
                'UPDATE "filters" SET id=? WHERE id=?;',
                (new_id, self.id)
            )
        self.update(False)

    def update(self, verbosity: bool = True, subscribing_operation: bool = False) -> None:
        """Update rules from a filter

        Args:
            verbosity (bool, optional): Display info about what is happening (default)
            subscribing_operation (bool, optional): The subscribing operation is in progress
        """
        if not self.exists and not subscribing_operation:
            raise FilterNotExists(f'the filter "{self.id}" does not exist or is not available')
        elif not self.subscribing and not subscribing_operation:
            raise NotSubscribingError(f'you are not subscribing to filter "{self.id}"')
        if verbosity:
            print(f'{Font.BOLD}==> Updating filter: {self.id}{Font.DEFAULT}')

        # Download the filter is it is online
        print(f' [{Fore.YELLOW}|{Style.RESET_ALL}] Get: {self.source}', end='\r')
        if is_url(self.source):
            tmp_filter = os.path.join(Path.TMP_DIR, self.id + '.tmp')
            try:
                download_file(self.source, tmp_filter)
            except (requests.exceptions.ConnectionError, urllib3.exceptions.MaxRetryError, ConnectionRefusedError,
                    urllib3.exceptions.NewConnectionError, InvalidLinkError):
                print(f' [{Fore.RED}x{Style.RESET_ALL}] Get: {self.source}')
                raise NetworkError(f'{Fore.RED}ERROR: cannot download: {self.source}{Style.RESET_ALL}')
        else:
            # This sequence is just meant to show an error message in the terminal before exiting
            tmp_filter = self.source
            try:
                with open(tmp_filter, 'rt') as f:
                    f.close()
            except FileNotFoundError:
                print(f' [{Fore.RED}x{Style.RESET_ALL}] Get: {self.source}')
                raise FileNotFoundError(f'cannot find file: {self.source}')
            else:
                print(f' [{Fore.YELLOW}|{Style.RESET_ALL}] Get: {self.source}', end='\r')
        print(f' [{Fore.GREEN}{Font.CHECK_MARK}{Style.RESET_ALL}] Get: {self.source}')

        # Check if the filter has a specified syntax
        try:
            rules = FilterParser(tmp_filter, syntax=self.metadata['syntax'])
        except KeyError:
            rules = FilterParser(tmp_filter)

        self.delete_all_rules()

        # Get all rules from the filter and from the database
        all_rules = rules.get_filter_content(
            self.permissions.allow, self.permissions.block, self.permissions.redirect, False
        )
        all_rules_in_db = get_all_rules()

        # Remove the filter only if it has been downloaded in a temporary location
        if self.source != tmp_filter:
            os.remove(tmp_filter)

        count = 1
        all_rules_count = len(all_rules)
        db = sqlite3.connect(Path.DATABASE)
        cursor = db.cursor()
        load_character = '|'

        # Start to add rules in the database
        for rule in all_rules:

            if count < all_rules_count:
                print(f' [{Fore.YELLOW}{load_character}{Style.RESET_ALL}] Adding new rules to database '
                      f'({count}/{all_rules_count})', end='\r')
                # Show process
                if load_character == '|' and not count % 500:
                    load_character = '/'
                elif load_character == '/' and not count % 500:
                    load_character = '-'
                elif load_character == '-' and not count % 500:
                    load_character = '\\'
                elif load_character == '\\' and not count % 500:
                    load_character = '|'
            else:
                print(f' [{Fore.GREEN}{Font.CHECK_MARK}{Style.RESET_ALL}] Adding new rules to database '
                      f'({count}/{all_rules_count})')

            if rule[0] == 'rule':

                if rule[1] in all_rules_in_db.keys() and all_rules_in_db[rule[1]]['priority']:
                    continue

                elif rule[2] == 'allow' and self.permissions.allow or rule[2] == 'block' and self.permissions.block:

                    # Avoid allowing or redirecting rules to be overwritten by blocking rules
                    # See: https://codeberg.org/tblock/tblock/issues/4
                    if rule[1] in all_rules_in_db.keys():
                        if rule[2] == 'block' and all_rules_in_db[rule[1]]['policy'] in ['redirect', 'allow']:
                            continue
                        cursor.execute(
                            'UPDATE "rules" SET policy=?, filter_id=?, priority=? WHERE domain=?;',
                            (rule[2], self.id, False, rule[1])
                        )
                    else:
                        cursor.execute(
                            'INSERT INTO "rules" ("domain", "policy", "filter_id", "priority") VALUES (?, ?, ?, ?)',
                            (rule[1], rule[2], self.id, False)
                        )
                        all_rules_in_db[rule[1]] = {
                            'policy': rule[2],
                            'filter_id': self.id,
                            'priority': False,
                            'ip': None
                        }

                elif rule[2] == 'redirect' and self.permissions.redirect:

                    # Avoid allowing rules to be overwritten by redirecting rules
                    # See: https://codeberg.org/tblock/tblock/issues/4
                    if rule[1] in all_rules_in_db.keys():
                        if all_rules_in_db[rule[1]]['policy'] == 'allow':
                            continue
                        cursor.execute(
                            'UPDATE "rules" SET policy=?, filter_id=?, priority=?, ip=? WHERE domain=?;',
                            (rule[2], self.id, False, rule[3], rule[1])
                        )
                    else:
                        cursor.execute(
                            'INSERT INTO "rules" ("domain", "policy", "filter_id", "priority", "ip") '
                            'VALUES (?, ?, ?, ?, ?)',
                            (rule[1], rule[2], self.id, False, rule[3])
                        )
                        all_rules_in_db[rule[1]] = {
                            'policy': rule[2],
                            'filter_id': self.id,
                            'priority': False,
                            'ip': rule[3]
                        }
            else:
                continue

            count += 1
        db.commit()
        db.close()
        print(f' [{Fore.GREEN}{Font.CHECK_MARK}{Style.RESET_ALL}] Filter successfully updated')

    def show(self) -> None:
        """Show information about a filter
        """
        if not self.exists:
            raise FilterNotExists(f'the filter "{self.id}" does not exist or is not available')

        # If subscribing to filter, get the number of rules that are set by it
        if self.subscribing:
            with sqlite3.connect(Path.DATABASE) as db:
                total_rules = len(
                    db.cursor().execute(
                        'SELECT "domain" FROM "rules" WHERE filter_id=?;',
                        (self.id,)
                    ).fetchall()
                )
        else:
            total_rules = None

        print(f'Filter ID     : {self.id}')

        if self.on_rfr:
            print(f'Title         : {self.metadata["title"]}')
            print(f'Homepage      : {self.metadata["homepage"]}')
            print(f'License       : {self.metadata["license"]}')
            print(f'Syntax        : {self.metadata["syntax"]}')
            print('Type          : available on online repository')

        else:
            print('Type          : custom filter')

        print(f'Source        : {self.source}')

        if self.subscribing:
            print('Subscribing   : yes')
            print(f'Permissions   : {self.permissions.pattern}')
            print(f'Total rules   : {total_rules}')
        else:
            print('Subscribing   : no')

        # This must be the last thing displayed, as it can be long and break the visual rendering of other information
        if self.on_rfr:
            print(f'Description   : {self.metadata["description"]}')


def get_all_sources() -> list:
    """Get a list of all filter sources from the database

    Returns:
        list: A list of all sources
    """
    with sqlite3.connect(Path.DATABASE) as conn:
        data = conn.execute('SELECT "source" FROM "filters";').fetchall()
    for row in data:
        data[data.index(row)] = row[0]
    return data


def get_all_custom() -> list:
    """Get a list of all custom filter IDs

    Returns:
        list: A list of all IDs
    """
    with sqlite3.connect(Path.DATABASE) as conn:
        data = conn.execute('SELECT "id" FROM "filters" WHERE on_rfr=0;').fetchall()
    for row in data:
        data[data.index(row)] = row[0]
    return data


def get_all_id(subscribing: bool = True, not_subscribing: bool = True) -> list:
    """Get a list of all filter IDs from the database

    Args:
        subscribing (bool, optional): Also return subscribed filters (default)
        not_subscribing (bool, optional): Also return not subscribed filters (default)

    Returns:
        list: A list of all IDs
    """
    with sqlite3.connect(Path.DATABASE) as conn:
        if subscribing and not_subscribing:
            data = conn.execute('SELECT "id" FROM "filters";').fetchall()
        elif subscribing:
            data = conn.execute('SELECT "id" FROM "filters" WHERE subscribing=1;').fetchall()
        elif not_subscribing:
            data = conn.execute('SELECT "id" FROM "filters" WHERE subscribing=0;').fetchall()
        else:
            data = []
    for row in data:
        data[data.index(row)] = row[0]
    return data


def get_all_from_rfr(subscribing: bool = True, not_subscribing: bool = True) -> list:
    """Get a list of all filter IDs available on the remote repository

    Returns:
        list: A list of all IDs
    """
    with sqlite3.connect(Path.DATABASE) as conn:
        if subscribing and not_subscribing:
            data = conn.execute('SELECT "id" FROM "filters" WHERE on_rfr=1;').fetchall()
        elif subscribing:
            data = conn.execute('SELECT "id" FROM "filters" WHERE on_rfr=1 AND subscribing=1;').fetchall()
        elif not_subscribing:
            data = conn.execute('SELECT "id" FROM "filters" WHERE on_rfr=1 AND subscribing=0;').fetchall()
        else:
            data = []
    for row in data:
        data[data.index(row)] = row[0]
    return data


def subscribe_to_filters(filters: list, force: bool = False) -> None:
    """Subscribe to a list of filters

    Args:
        filters (list): All filters ID in a list: [ [id, permissions, custom_source (if any)] ]
        force (bool, optional): Do not prompt user before subscribing to filters (False by default)
    """
    list_id = []
    for filter_id in filters:
        if not Filter(filter_id[0]).exists and len(filter_id) < 3:
            raise FilterNotExists(f'{Fore.RED}ERROR: filter does not exist: {filter_id[0]}{Style.RESET_ALL}')
        list_id.append(filter_id[0])
    if not check_root():
        raise PermissionError(f'{Fore.RED}ERROR: you need to run as root to perform this operation{Style.RESET_ALL}')
    elif not filters:
        raise MissingArgumentError(f'{Fore.RED}ERROR: you need to specify at least one filter{Style.RESET_ALL}')
    elif not force and not prompt_user('You are about to subscribe to the following filters:', list_id):
        raise SIGTERM()
    print(':: Subscribing to filters...')
    lock_database()
    try:
        for filter_data in filters:
            filter_obj = Filter(filter_data[0])
            try:
                if len(filter_data) == 1:
                    filter_obj.subscribe(FilterPermissions())
                elif len(filter_data) == 2:
                    filter_obj.subscribe(FilterPermissions(filter_data[1]))
                else:
                    filter_obj.subscribe(FilterPermissions(filter_data[1]), filter_data[2])
            except AlreadySubscribingError as err:
                print(f'{Fore.YELLOW}WARNING: {err}{Style.RESET_ALL}')
            except (FilterSourceExistsError, FilterExistsError) as err:
                raise FilterSourceExistsError(f'{Fore.RED}ERROR: {err}{Style.RESET_ALL}')
            except InvalidFilterSyntax as err:
                raise InvalidFilterSyntax(f'{Fore.RED}ERROR: {err}{Style.RESET_ALL}')
            except FileNotFoundError as err:
                raise FileNotFoundError(f'{Fore.RED}ERROR: {err}{Style.RESET_ALL}')
            except IsADirectoryError as err:
                raise IsADirectoryError(f'{Fore.RED}ERROR: {err}{Style.RESET_ALL}')
        update_hosts(get_all_rules())
        unlock_database()
    except PermissionError:
        raise PermissionError(f'{Fore.RED}ERROR: permission error{Style.RESET_ALL}')


def change_filters_permissions(filters: list, force: bool = False) -> None:
    """Subscribe to a list of filters

    Args:
        filters (list): All filters ID in a list: [ [id, permissions] ]
        force (bool, optional): Do not prompt user (False by default)
    """
    list_id = []
    for filter_id in filters:
        if not Filter(filter_id[0]).subscribing:
            raise NotSubscribingError(f'{Fore.RED}ERROR: not subscribing to filter: {filter_id[0]}{Style.RESET_ALL}')
        list_id.append(filter_id[0])
    if not check_root():
        raise PermissionError(f'{Fore.RED}ERROR: you need to run as root to perform this operation{Style.RESET_ALL}')
    elif not filters:
        raise MissingArgumentError(f'{Fore.RED}ERROR: you need to specify at least one filter{Style.RESET_ALL}')
    elif not force and not prompt_user('You are about to change the permissions of the following filters:', list_id):
        raise SIGTERM()
    print(':: Changing filters permissions...')
    lock_database()
    try:
        for filter_data in filters:
            filter_obj = Filter(filter_data[0])
            try:
                filter_obj.change_permissions(FilterPermissions(filter_data[1]))
            except NotSubscribingError as err:
                print(f'{Fore.YELLOW}WARNING: {err}{Style.RESET_ALL}')
            try:
                filter_obj.update(False)
            except InvalidFilterSyntax as err:
                raise InvalidFilterSyntax(f'{Fore.RED}ERROR: {err}{Style.RESET_ALL}')
            except FileNotFoundError as err:
                raise FileNotFoundError(f'{Fore.RED}ERROR: {err}{Style.RESET_ALL}')
            except IsADirectoryError as err:
                raise IsADirectoryError(f'{Fore.RED}ERROR: {err}{Style.RESET_ALL}')
        update_hosts(get_all_rules())
        unlock_database()
    except PermissionError:
        raise PermissionError(f'{Fore.RED}ERROR: permission error{Style.RESET_ALL}')


def unsubscribe_from_filters(filters: list, force: bool = False) -> None:
    """Subscribe from a list of filters

    Args:
        filters (list): All filters ID in a list: [id_1, id_2]
        force (bool, optional): Do not prompt user (False by default)
    """
    list_id = []
    for filter_id in filters:
        if not Filter(filter_id).subscribing:
            raise NotSubscribingError(f'{Fore.RED}ERROR: not subscribing to filter: {filter_id}{Style.RESET_ALL}')
        list_id.append(filter_id)
    if not check_root():
        raise PermissionError(f'{Fore.RED}ERROR: you need to run as root to perform this operation{Style.RESET_ALL}')
    elif not filters:
        raise MissingArgumentError(f'{Fore.RED}ERROR: you need to specify at least one filter{Style.RESET_ALL}')
    elif not force and not prompt_user('You are about to unsubscribe from the following filters:', list_id):
        raise SIGTERM()
    print(':: Unsubscribing from filters...')
    lock_database()
    try:
        for filter_id in filters:
            filter_obj = Filter(filter_id)
            filter_obj.unsubscribe()
            filter_obj.delete_all_rules()
        update_hosts(get_all_rules())
        unlock_database()
    except PermissionError:
        raise PermissionError(f'{Fore.RED}ERROR: permission error{Style.RESET_ALL}')
    try:
        open(Path.NEEDS_UPDATE, 'wt').close()
    except PermissionError:
        pass


def update_filters(filters: list, force: bool = False, subscribing_operation: bool = False) -> None:
    """Update rules from a list of filters

    Args:
        filters (list): All filters ID in a list: [id_1, id_2]
        force (bool, optional): Do not prompt user (False by default)
        subscribing_operation (bool, optional): The subscribing operation is in progress
    """
    list_id = []
    for filter_id in filters:
        if not Filter(filter_id).subscribing and not subscribing_operation:
            raise NotSubscribingError(f'{Fore.RED}ERROR: not subscribing to filter: {filter_id}{Style.RESET_ALL}')
        list_id.append(filter_id)
    if not check_root():
        raise PermissionError(f'{Fore.RED}ERROR: you need to run as root to perform this operation{Style.RESET_ALL}')
    elif not filters:
        MissingArgumentError(f'{Fore.RED}ERROR: you need to specify at least one filter{Style.RESET_ALL}')
    elif not force and not prompt_user('You are about to update the rules from the following filters:', list_id):
        raise SIGTERM()
    print(':: Updating filters...')
    lock_database()
    try:
        for filter_id in filters:
            filter_obj = Filter(filter_id)
            try:
                filter_obj.update()
            except InvalidFilterSyntax as err:
                raise InvalidFilterSyntax(f'{Fore.RED}ERROR: {err}{Style.RESET_ALL}')
            except FileNotFoundError as err:
                raise FileNotFoundError(f'{Fore.RED}ERROR: {err}{Style.RESET_ALL}')
            except IsADirectoryError as err:
                raise IsADirectoryError(f'{Fore.RED}ERROR: {err}{Style.RESET_ALL}')
        update_hosts(get_all_rules())
        unlock_database()
    except PermissionError:
        raise PermissionError(f'{Fore.RED}ERROR: permission error{Style.RESET_ALL}')


def change_filter_id(filter_id: str, new_id: str, force: bool = False) -> None:
    """Change the ID of a custom filter

    Args:
        filter_id (str): The filter to rename
        new_id (str): The new ID to use
        force (bool, optional): Do not prompt user (False by default)
    """
    if not Filter(filter_id).subscribing:
        raise NotSubscribingError(f'{Fore.RED}ERROR: not subscribing to filter: {filter_id}{Style.RESET_ALL}')
    if not check_root():
        raise PermissionError(f'{Fore.RED}ERROR: you need to run as root to perform this operation{Style.RESET_ALL}')
    if Filter(new_id).exists:
        raise FilterExistsError(
            f'{Fore.RED}ERROR: the filter ID "{new_id}" is already taken by another filter{Style.RESET_ALL}'
        )
    elif not force and not prompt_user(f'You are about to change the ID of the filter "{filter_id}" to:', [new_id]):
        raise SIGTERM()
    print(':: Changing filter ID...')
    lock_database()
    try:
        filter_obj = Filter(filter_id)
        filter_obj.change_id(new_id)
        update_hosts(get_all_rules())
        unlock_database()
    except FilterNotCustomError as err:
        raise FilterNotCustomError(f'{Fore.RED}ERROR: {err}{Style.RESET_ALL}')
    except PermissionError:
        raise PermissionError(f'{Fore.RED}ERROR: permission error{Style.RESET_ALL}')


def update_all_filters(force: bool = False) -> None:
    """Update rules from all filters that the user is subscribing to

    Args:
        force (bool, optional): Do not prompt user (False by default)
    """
    update_filters(get_all_id(subscribing=True, not_subscribing=False), force)
    try:
        os.remove(Path.NEEDS_UPDATE)
    except (FileNotFoundError, PermissionError):
        pass


def show_filters(filters: list) -> None:
    """Show information about a list of filters

    Args:
        filters (list): All filters ID in a list: [id_1, id_2]
    """
    if not filters:
        raise MissingArgumentError(f'{Fore.RED}ERROR: please specify at least one filter{Style.RESET_ALL}')
    for filter_id in filters:
        if not Filter(filter_id).exists:
            raise FilterNotExists(f'{Fore.RED}ERROR: filter does not exist: {filter_id}{Style.RESET_ALL}')
    for filter_id in filters:
        filter_obj = Filter(filter_id)
        print('----------------------------------------------')
        filter_obj.show()
    print('----------------------------------------------')


def list_filters(online_only: bool = False, custom_only: bool = False,
                 subscribing_only: bool = True, not_subscribing_only: bool = False) -> None:
    """List all filters with some criteria

    Args:
        online_only (bool, optional): List only filters that are available on the remote repository
        custom_only (bool, optional): List only custom filters
        subscribing_only (bool, optional): List only filters that the user is subscribing to
        not_subscribing_only (bool, optional): List only filters that the user is not subscribing to
    """

    if subscribing_only and not_subscribing_only:
        subscribing = False
        not_subscribing = False
    elif subscribing_only and not not_subscribing_only:
        subscribing = True
        not_subscribing = False
    elif not_subscribing_only and not subscribing_only:
        subscribing = False
        not_subscribing = True
    else:
        subscribing = True
        not_subscribing = True

    if online_only and custom_only:
        pass
    elif online_only and not custom_only:
        for filter_id in get_all_from_rfr(subscribing, not_subscribing):
            print(filter_id)
    elif custom_only and not online_only:
        for filter_id in get_all_custom():
            print(filter_id)
    else:
        for filter_id in get_all_id(subscribing, not_subscribing):
            print(filter_id)


def search_filters(query: str, online_only: bool = False, custom_only: bool = False,
                   subscribing_only: bool = False, not_subscribing_only: bool = False) -> None:
    """Search a query in the filters list and their metadata

    Args:
        query (str): The query to search
        online_only (bool, optional): Show only results from filters that are available on the remote repository
        custom_only (bool, optional): Show only results from custom filters
        subscribing_only (bool, optional): Show only results from filters that the user is subscribing to
        not_subscribing_only (bool, optional): Show only results from filters that the user is not subscribing to
    """
    regex_query = re.compile(query, re.IGNORECASE)
    if subscribing_only and not_subscribing_only:
        subscribing = False
        not_subscribing = False
    elif subscribing_only and not not_subscribing_only:
        subscribing = True
        not_subscribing = False
    elif not_subscribing_only and not subscribing_only:
        subscribing = False
        not_subscribing = True
    else:
        subscribing = True
        not_subscribing = True

    if online_only and custom_only:
        filters_list = []
    elif online_only and not custom_only:
        filters_list = get_all_from_rfr(subscribing, not_subscribing)
    elif custom_only and not online_only:
        filters_list = get_all_custom()
    else:
        filters_list = get_all_id(subscribing, not_subscribing)

    for filter_id in filters_list:
        filter_match = Filter(filter_id)
        if re.findall(regex_query, filter_match.id):
            print(filter_id)
        elif filter_match.on_rfr and re.findall(regex_query, filter_match.metadata['title']):
            print(filter_id)
        elif filter_match.on_rfr and re.findall(regex_query, filter_match.metadata['description']):
            print(filter_id)
        else:
            pass
