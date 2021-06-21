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
import sqlite3
import os.path

# External libraries
from colorama import Fore, Style

# Local libraries
from . import run_help, run_converter_help, __version__
from .config import Path, PROTECTING_STATUS, Font
from .rules import get_all_rules
from .utils import check_root, prompt_user
from .hosts import update_hosts, restore_hosts
from .exceptions import SIGTERM


def enable_protection(force: bool = False) -> None:
    """Update the hosts file and enable protection if it is not active

    Args:
        force (bool, optional): Do not prompt user (False by default)
    """
    if not check_root():
        raise PermissionError(f'{Fore.RED}ERROR: you need to run as root to perform this operation{Style.RESET_ALL}')
    elif not force and not prompt_user('You are about to update the hosts file'):
        raise SIGTERM()
    else:
        print(':: Updating hosts file...')
        update_hosts(get_all_rules())


def disable_protection(force: bool = False) -> None:
    """Restore the default hosts file and disable the protection

    Args:
        force (bool, optional): Do not prompt user (False by default)
    """
    if not check_root():
        raise PermissionError(f'{Fore.RED}ERROR: you need to run as root to perform this operation{Style.RESET_ALL}')
    elif not force and not prompt_user('You are about to restore the default hosts file and disable the protection'):
        raise SIGTERM()
    else:
        print(':: Disabling protection...')
        restore_hosts()


def print_status() -> None:
    """Print the current status of the ad-blocker
    """

    if PROTECTING_STATUS:
        status = f'{Fore.GREEN}blocking{Style.RESET_ALL}'
    else:
        status = f'{Fore.RED}not blocking{Style.RESET_ALL}'

    try:
        with sqlite3.connect(Path.DATABASE) as db:
            total_rules = db.cursor().execute('SELECT COUNT() FROM rules;').fetchone()[0]
            allow = db.cursor().execute('SELECT COUNT() FROM rules WHERE policy="allow";').fetchone()[0]
            block = db.cursor().execute('SELECT COUNT() FROM rules WHERE policy="block";').fetchone()[0]
            redirect = db.cursor().execute('SELECT COUNT() FROM rules WHERE policy="redirect";').fetchone()[0]
            user = db.cursor().execute('SELECT COUNT() FROM rules WHERE priority=1;').fetchone()[0]
            total_filters = db.cursor().execute('SELECT COUNT() FROM filters WHERE subscribing=1;').fetchone()[0]
            custom = db.cursor().execute('SELECT COUNT() FROM filters WHERE on_rfr=0;').fetchone()[0]
            allow_redirect = db.cursor().execute(
                'SELECT COUNT() FROM filters WHERE permissions LIKE "%r%";').fetchone()[0]
            if os.path.isfile(Path.DB_LOCK):
                db_status = f'{Fore.YELLOW}locked{Style.RESET_ALL}'
            else:
                db_status = f'{Fore.GREEN}healthy{Style.RESET_ALL}'
    except (sqlite3.DatabaseError, sqlite3.OperationalError):
        total_rules = '-'
        allow = '-'
        block = '-'
        redirect = '-'
        user = '-'
        total_filters = '-'
        custom = '-'
        allow_redirect = '-'
        db_status = f'{Fore.RED}corrupted{Style.RESET_ALL}'

    if not allow_redirect:
        redirect_perm = f'{Fore.GREEN}0 filter(s) allowed{Style.RESET_ALL}'
    elif str(allow_redirect) != '-' and allow_redirect < 4:
        redirect_perm = f'{Fore.YELLOW}{allow_redirect} filter(s) allowed{Style.RESET_ALL}'
    else:
        redirect_perm = f'{Fore.RED}{allow_redirect} filter(s) allowed{Style.RESET_ALL}'

    if not PROTECTING_STATUS:
        hijack = f'{Fore.YELLOW}tblock is not active{Style.RESET_ALL}'
    else:
        try:
            with open(Path.HOSTS_VERIFICATION, 'rt') as h:
                verification_hosts = h.read()
        except FileNotFoundError:
            verification_hosts = ''
        with open(Path.HOSTS, 'rt') as h:
            hosts_real = h.read()
        if verification_hosts == hosts_real:
            hijack = f'{Fore.GREEN}no threat detected{Style.RESET_ALL}'
        else:
            hijack = f'{Fore.RED}threat(s) detected, run "tblock -H" to fix{Style.RESET_ALL}'

    try:
        with open(Path.REPO_VERSION, 'rt') as f:
            repo_version = f.read()
    except FileNotFoundError:
        repo_version = 0

    if os.path.isfile(Path.NEEDS_UPDATE):
        needs_update = f'{Fore.RED}needed{Style.RESET_ALL}'
    else:
        needs_update = f'{Fore.GREEN}not needed{Style.RESET_ALL}'

    if Path.PREFIX == '/data/data/com.termux/files/usr/lib/tblock/':
        _platform = 'android'
    else:
        _platform = sys.platform

    print(f'{Font.UNDERLINE}Status{Font.DEFAULT}')
    print(f'  TBlock       : version {__version__}')
    print(f'  Platform     : {_platform}')
    print(f'  Protection   : {status}')
    print(f'  Repository   : version {repo_version}')
    print(f'  Database     : {db_status}\n')
    print(f'{Font.UNDERLINE}Rules{Font.DEFAULT}')
    print(f'  Total        : {total_rules}')
    print(f'  User         : {user}')
    print(f'  Allowing     : {allow}')
    print(f'  Blocking     : {block}')
    print(f'  Redirecting  : {redirect}\n')
    print(f'{Font.UNDERLINE}Filters{Font.DEFAULT}')
    print(f'  Active       : {total_filters}')
    print(f'  Custom       : {custom}')
    print(f'  Full update  : {needs_update}\n')
    print(f'{Font.UNDERLINE}Security{Font.DEFAULT}')
    print(f'  Redirecting  : {redirect_perm}')
    print(f'  Hosts hijack : {hijack}')


def print_version_info(ad_blocker: bool) -> None:
    """Print the version of the program

    Args:
        ad_blocker (bool): If True, show info for tblock. If False, show info for tblockc
    """

    if ad_blocker:
        name = 'TBlock'
        desc = 'An anticapitalist ad-blocker that uses the hosts file'
    else:
        name = 'TBlockc'
        desc = 'TBlock\'s built-in filter converter'

    print(
        f'{name} version {__version__} - {desc}\n'
        'Copyright (C) 2021 Twann <twann@ctemplar.com>\n\n'
        'This program is free software: you can redistribute it and/or modify\n'
        'it under the terms of the GNU General Public License as published by\n'
        'the Free Software Foundation, either version 3 of the License, or\n'
        '(at your option) any later version.\n\n'
        'This program is distributed in the hope that it will be useful,\n'
        'but WITHOUT ANY WARRANTY; without even the implied warranty of\n'
        'MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\n'
        'GNU General Public License for more details.\n'
        'You should have received a copy of the GNU General Public License\n'
        'along with this program.  If not, see <https://www.gnu.org/licenses/>.'
    )


def print_help(ad_blocker: bool) -> None:
    """Print the help page of the program

    Args:
        ad_blocker (bool): If True, show info for tblock. If False, show info for tblockc
    """
    if ad_blocker:
        print(run_help)
    else:
        print(run_converter_help)
