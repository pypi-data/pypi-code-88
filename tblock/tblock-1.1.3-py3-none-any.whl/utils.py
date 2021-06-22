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
import sys
import os
import re
import time
import datetime
import random

# External libraries
import requests
from colorama import Fore, Style

# Local libraries
from .config import Path
from .exceptions import InvalidLinkError


# This is meant to see which process is locking the database and to avoid others to unlock it
DB_PID = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f') + str(random.randint(0, 100))


def check_root() -> bool:
    """Check if the user is the superuser.

    Returns:
        bool: True if the user is the superuser
    """
    # Just try to open the hosts file to edit it, to check if it gets restricted by the system
    try:
        with open(Path.HOSTS, 'at') as dummy_check:
            dummy_check.close()
    except PermissionError:
        return False
    else:
        return True


def lock_database() -> None:
    """Lock the database
    """
    if os.path.isfile(Path.DB_LOCK):
        print(
            f'{Fore.YELLOW}WARNING: database locked, wait for another instance of tblock to finish.\n'
            f'You can also delete "{Path.DB_LOCK}" if you are sure this is the only instance running.{Style.RESET_ALL}'
        )
    try:
        while os.path.isfile(Path.DB_LOCK):
            time.sleep(1)
        else:
            try:
                with open(Path.DB_LOCK, 'wt') as f:
                    f.write(str(DB_PID))
            except PermissionError:
                pass
    except KeyboardInterrupt:
        sys.exit(1)


def unlock_database() -> None:
    """Unlock the database
    """
    try:
        with open(Path.DB_LOCK, 'rt') as f:
            if f.read() == str(DB_PID):
                f.close()
                os.remove(Path.DB_LOCK)
    except (FileNotFoundError, PermissionError):
        pass


def is_url(url: str) -> bool:
    """Check whether a string is a valid URL or not

    Args:
        url (str): Tĥe string to check

    Returns:
        bool: True if URL seems valid
    """
    return 'http://' in url or 'https://' in url


def prompt_user(message: str, list_of_elements: list = None) -> bool:
    """Prompt the user before executing an action

    Args:
        message (str): The message to display
        list_of_elements (list, optional): A list of elements to display
    """
    output_string = ''
    line_count = 0
    if list_of_elements:
        for item in list_of_elements:
            if line_count + len(f' {item}') >= 62:
                output_string += f'\n  {item}'
                line_count = len(f' {item}')
            else:
                output_string += f' {item}'
                line_count += len(f' {item}')
    print(f':: {message}')
    if output_string:
        print(f'\n {output_string}\n')
    try:
        answer = input(':: Are you sure to continue ? [y/n] ')
    except KeyboardInterrupt:
        return False
    else:
        return answer.lower() == 'y'


def is_valid_ip(ip: str) -> bool:
    """Check whether an IP address is valid or not

    Args:
        ip (str): Tĥe IP address to check

    Returns:
        bool: True if IP address seems valid
    """
    if 7 <= len(ip) <= 15:
        if len(re.findall(r"\.", ip)) == 3:
            return True
        else:
            return False
    else:
        return False


def download_file(url: str, output_path: str) -> None:
    """Get the content of an online file and export it into a local file

    Args:
        url (str): The URL of the online file
        output_path (str): Where to export file content
    """
    online_file = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
    if online_file.status_code != 200:
        raise InvalidLinkError()
    with open(os.path.relpath(output_path), 'wb') as f:
        f.write(online_file.content)


def extract_domain(url: str) -> str:
    """Extract the domain from an URL

    Args:
        url (str): The URL

    Returns:
        str: The domain
    """
    if re.match(re.compile('.*://'), url):
        url = url.split('://')[1]
    return url.split('/')[0].split(':')[0].split('#')[0].split('?')[0]
