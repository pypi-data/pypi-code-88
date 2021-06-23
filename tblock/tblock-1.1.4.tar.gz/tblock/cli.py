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
import re
import sqlite3

# External libraries
from colorama import Fore, Style

# Local libraries
from .tools import enable_protection, disable_protection, print_status, print_version_info, print_help
from .config import check_dirs
from .repo import sync_remote_repo
from .rules import add_rules, list_rules, delete_rules
from .converter import convert_filter, get_syntax
from .utils import check_root, unlock_database
from .filters import subscribe_to_filters, show_filters, update_filters, update_all_filters, unsubscribe_from_filters, \
    list_filters, change_filters_permissions, change_filter_id, search_filters
from .exceptions import FilterNotExists, MissingArgumentError, FilterSourceExistsError, NotSubscribingError, \
    RuleNotExistsError, InvalidBindAddress, SIGTERM, InvalidFilterSyntax, NetworkError, FilterNotCustomError, \
    FilterExistsError


tblock_args = [
    '-h', '--help',
    '-s', '--status',
    '-v', '--version',
    '-a', '--allow',
    '-b', '--block',
    '-r', '--redirect',
    '-d', '--delete-rule',
    '-l', '--list-rules',
    '-S', '--subscribe',
    '-C', '--add-custom',
    '-R', '--remove',
    '-U', '--update',
    '-Q', '--search',
    '-M', '--mod',
    '-X', '--change-id',
    '-I', '--info',
    '-L', '--list',
    '-Y', '--sync',
    '-H', '--update-hosts',
    '-D', '--restore'
]

tblock_opts = [
    '-f', '--force',
    '-t', '--standard',
    '-u', '--user',
    '-y', '--with-sync',
    '-c', '--custom',
    '-k', '--subscribing',
    '-n', '--unsubscribing',
    '-w', '--on-remote-repo',
]


tblockc_opts = [
    '-h', '--help',
    '-f', '--force',
    '-v', '--version',
    '-c', '--comments',
    '-o', '--output',
    '-i', '--input-syntax',
    '-s', '--syntax',
    '-g', '--get-syntax',
    '-0', '--zero'
]


class TBlockArguments:

    def __init__(self, args: list) -> None:
        """Arguments object

        Args:
            args (list): A list of all arguments
        """
        self.action = None
        self.options = {
            'force': False,
            'standard': False,
            'user': False,
            'custom': False,
            'with-sync': False,
            'subscribing': False,
            'unsubscribing': False,
            'on-remote-repo': False
        }
        self.values = []

        for argument in args:

            if re.match(re.compile(r'--'), argument):
                # Is an argument
                if argument in tblock_args:
                    self.action = argument.split('--')[1]

                # Is an option
                elif argument in tblock_opts:
                    self.options[argument.split('--')[1]] = True

                # Other
                else:
                    print(f'{Fore.RED}ERROR: invalid argument "{argument}"{Style.RESET_ALL}')
                    sys.exit(1)

            elif re.match(re.compile(r'-'), argument):
                # Is an argument
                if argument in tblock_args:
                    self.action = tblock_args[tblock_args.index(argument) + 1].split('--')[1]

                # Is an option
                elif argument in tblock_opts:
                    self.options[tblock_opts[tblock_opts.index(argument) + 1].split('--')[1]] = True

                # Contains an argument
                elif argument[0:2] in tblock_args:
                    self.action = tblock_args[tblock_args.index(argument[0:2]) + 1].split('--')[1]
                    for option in argument[2:]:
                        if f'-{option}' in tblock_opts:
                            self.options[tblock_opts[tblock_opts.index(f'-{option}') + 1].split('--')[1]] = True
                        else:
                            print(f'{Fore.RED}ERROR: invalid option "{option}"{Style.RESET_ALL}')
                            sys.exit(1)

                # Contains an option
                elif argument[0:2] in tblock_opts:
                    self.options[tblock_opts[tblock_opts.index(argument[0:2]) + 1].split('--')[1]] = True
                    for option in argument[2:]:
                        if f'-{option}' in tblock_opts:
                            self.options[tblock_opts[tblock_opts.index(f'-{option}') + 1].split('--')[1]] = True
                        else:
                            print(f'{Fore.RED}ERROR: invalid option "{option}"{Style.RESET_ALL}')
                            sys.exit(1)

                # Other
                else:
                    print(f'{Fore.RED}ERROR: invalid argument "{argument}"{Style.RESET_ALL}')
                    sys.exit(1)

            else:
                self.values.append(argument)

        if not self.action:
            print(f'{Fore.RED}ERROR: one argument is required{Style.RESET_ALL}\nTo show the help page, run "tblock -h"')
            sys.exit(1)


class TBlockcArguments:

    def __init__(self, args: list) -> None:
        """Arguments object

        Args:
            args (list): A list of all arguments
        """
        self.options = {
            'help': [bool, False],
            'force': [bool, False],
            'version': [bool, False],
            'comments': [bool, False],
            'output': [str, None],
            'syntax': [str, None],
            'input-syntax': [str, None],
            'get-syntax': [bool, False],
            'zero': [bool, False]
        }

        self.filter_path = None

        for argument in args:

            if re.match(re.compile(r'--'), argument):
                # Is an option
                if argument in tblockc_opts:
                    if self.options[argument.split('--')[1]][0] is bool:
                        self.options[argument.split('--')[1]][1] = True
                    elif self.options[argument.split('--')[1]][0] is str:
                        try:
                            self.options[argument.split('--')[1]][1] = args[args.index(argument) + 1]
                            args.pop(args.index(argument) + 1)
                        except IndexError:
                            print(f'{Fore.RED}ERROR: option "{argument}" requires a value{Style.RESET_ALL}')
                            sys.exit(1)

                # Other
                else:
                    print(f'{Fore.RED}ERROR: invalid option "{argument}"{Style.RESET_ALL}')
                    sys.exit(1)

            elif re.match(re.compile(r'-'), argument):
                # Is an option
                if argument in tblockc_opts:
                    if self.options[tblockc_opts[tblockc_opts.index(argument) + 1].split('--')[1]][0] is bool:
                        self.options[tblockc_opts[tblockc_opts.index(argument) + 1].split('--')[1]][1] = True
                    elif self.options[tblockc_opts[tblockc_opts.index(argument) + 1].split('--')[1]][0] is str:
                        try:
                            self.options[tblockc_opts[tblockc_opts.index(argument) + 1].split('--')[1]][1] = \
                                args[args.index(argument) + 1]
                            args.pop(args.index(argument) + 1)
                        except IndexError:
                            print(f'{Fore.RED}ERROR: option "{argument[0:2]}" requires a value{Style.RESET_ALL}')
                            sys.exit(1)

                # Contains an option
                elif argument[0:2] in tblockc_opts:

                    if self.options[tblockc_opts[tblockc_opts.index(argument[0:2]) + 1].split('--')[1]][0] is bool:
                        self.options[tblockc_opts[tblockc_opts.index(argument[0:2]) + 1].split('--')[1]][1] = True
                    else:
                        print(f'{Fore.RED}ERROR: option "{argument[0:2]}" requires a value{Style.RESET_ALL}')
                        sys.exit(1)

                    for option in argument[2:]:
                        if f'-{option}' in tblockc_opts:

                            if self.options[tblockc_opts[tblockc_opts.index(f'-{option}') + 1].split('--')[1]][0] \
                                    is bool:
                                self.options[tblockc_opts[tblockc_opts.index(f'-{option}') + 1].split('--')[1]][1] \
                                    = True

                            elif self.options[tblockc_opts[tblockc_opts.index(f'-{option}') + 1].split('--')[1]][0] \
                                    is str and len(argument[2:]) - 1 == argument[2:].index(option):
                                try:
                                    self.options[tblockc_opts[tblockc_opts.index(f'-{option}') + 1].split('--')[1]][1] \
                                        = args[args.index(argument) + 1]
                                    args.pop(args.index(argument) + 1)
                                except IndexError:
                                    print(
                                        f'{Fore.RED}ERROR: option "{option}" requires a value{Style.RESET_ALL}'
                                    )
                                    sys.exit(1)
                            else:
                                print(f'{Fore.RED}ERROR: option "{option}" requires a value{Style.RESET_ALL}')
                                sys.exit(1)

                        else:
                            print(f'{Fore.RED}ERROR: invalid option "{option}"{Style.RESET_ALL}')
                            sys.exit(1)
                # Other
                else:
                    print(f'{Fore.RED}ERROR: invalid option "{argument}"{Style.RESET_ALL}')
                    sys.exit(1)
            else:
                self.filter_path = argument


def parse_args_tblock() -> None:
    """Parse arguments and run the ad-blocker
    """
    parser = TBlockArguments(sys.argv[1:])

    if parser.action == 'help':
        print_help(True)

    elif parser.action == 'status':
        print_status()

    elif parser.action == 'version':
        print_version_info(True)

    elif parser.action == 'allow':
        data = []
        for rule in parser.values:
            data.append([rule, 'allow'])
        add_rules(data, parser.options['force'])

    elif parser.action == 'block':
        data = []
        for rule in parser.values:
            data.append([rule, 'block'])
        add_rules(data, parser.options['force'])

    elif parser.action == 'redirect':
        data = []
        for rule in parser.values[:len(parser.values) - 1]:
            data.append([rule, 'redirect', parser.values[len(parser.values) - 1]])
        add_rules(data, parser.options['force'])

    elif parser.action == 'delete-rule':
        delete_rules(parser.values, parser.options['force'])

    elif parser.action == 'list-rules':
        list_rules(parser.options['standard'], parser.options['user'])

    elif parser.action == 'subscribe':
        data = []
        for filter_id in parser.values:
            data.append([filter_id, 'b'])
        if parser.options['with-sync']:
            sync_remote_repo(parser.options['force'])
            print()
        subscribe_to_filters(data, parser.options['force'])

    elif parser.action == 'add-custom':
        data = []
        for filter_id in parser.values:
            data.append([filter_id, 'b', parser.values[parser.values.index(filter_id) + 1]])
            parser.values.pop(parser.values.index(filter_id) + 1)
        if parser.options['with-sync']:
            sync_remote_repo(parser.options['force'])
            print()
        subscribe_to_filters(data, parser.options['force'])

    elif parser.action == 'remove':
        if parser.options['with-sync']:
            sync_remote_repo(parser.options['force'])
            print()
        unsubscribe_from_filters(parser.values, parser.options['force'])

    elif parser.action == 'update':
        if parser.options['with-sync']:
            sync_remote_repo(parser.options['force'])
            print()
        if parser.values:
            update_filters(parser.values, parser.options['force'])
        else:
            update_all_filters(parser.options['force'])

    elif parser.action == 'search':
        for query in parser.values:
            search_filters(query, parser.options['on-remote-repo'], parser.options['custom'],
                           parser.options['subscribing'], parser.options['unsubscribing'])

    elif parser.action == 'mod':
        data = []
        try:
            permissions = parser.values[0]
            for filter_id in parser.values[1:]:
                data.append([filter_id, permissions])
            if parser.options['with-sync']:
                sync_remote_repo(parser.options['force'])
                print()
            change_filters_permissions(data, parser.options['force'])
        except IndexError:
            if not check_root():
                raise PermissionError(
                    f'{Fore.RED}ERROR: you need to run as root to perform this operation{Style.RESET_ALL}')
            else:
                raise MissingArgumentError(
                    f'{Fore.RED}ERROR: please specify the new policy and the filter to change{Style.RESET_ALL}'
                )

    elif parser.action == 'change-id':
        # This verification should stay here, as only two values are required and not a list
        if not check_root():
            raise PermissionError(
                f'{Fore.RED}ERROR: you need to run as root to perform this operation{Style.RESET_ALL}')
        if len(parser.values) > 2:
            raise IOError(f'{Fore.RED}ERROR: too much arguments are given for changing filter ID{Style.RESET_ALL}')
        if parser.options['with-sync']:
            sync_remote_repo(parser.options['force'])
            print()
        try:
            change_filter_id(parser.values[0], parser.values[1])
        except IndexError:
            raise MissingArgumentError(
                f'{Fore.RED}ERROR: you need to specify the filter to rename as well as its new ID{Style.RESET_ALL}'
            )

    elif parser.action == 'info':
        show_filters(parser.values)

    elif parser.action == 'list':
        list_filters(parser.options['on-remote-repo'], parser.options['custom'],
                     parser.options['subscribing'], parser.options['unsubscribing'])

    elif parser.action == 'sync':
        sync_remote_repo(parser.options['force'])

    elif parser.action == 'update-hosts':
        enable_protection(parser.options['force'])

    elif parser.action == 'restore':
        disable_protection(parser.options['force'])

    else:
        pass    # This should never happen


def parse_args_tblockc() -> None:
    """Parse arguments and run the converter
    """
    parser = TBlockcArguments(sys.argv[1:])

    if parser.options['help'][1]:
        print_help(False)

    elif parser.options['version'][1]:
        print_version_info(False)

    else:

        if not parser.filter_path:
            print(f'{Fore.RED}ERROR: please specify at least one file{Style.RESET_ALL}\n'
                  f'To show the help page, run "tblockc -h"')
            sys.exit(1)

        elif parser.options['get-syntax'][1]:
            get_syntax(parser.filter_path)

        else:
            if not parser.options['output'][1]:
                print(f'{Fore.RED}ERROR: you must specify the output filter{Style.RESET_ALL}')
                sys.exit(1)

            elif not parser.options['syntax'][1]:
                print(f'{Fore.RED}ERROR: you must specify the output syntax{Style.RESET_ALL}')
                sys.exit(1)

            else:
                default_ip = '0.0.0.0' if parser.options['zero'][1] else '127.0.0.1'

                convert_filter(
                    input_file=parser.filter_path,
                    output_file=parser.options['output'][1],
                    output_syntax=parser.options['syntax'][1],
                    hosts_default_ip=default_ip,
                    input_syntax=parser.options['input-syntax'][1],
                    comments=parser.options['comments'][1],
                    force=parser.options['force'][1]
                )


def run() -> None:
    check_dirs()
    try:
        parse_args_tblock()
    except (PermissionError, FilterSourceExistsError, MissingArgumentError, FilterNotExists, NotSubscribingError,
            RuleNotExistsError, InvalidBindAddress, InvalidFilterSyntax, FileNotFoundError, NetworkError,
            FilterExistsError, FilterNotCustomError, IsADirectoryError) as err:
        print(str(err).replace('[Errno 2] N', 'n').replace('[Errno 21] I', 'i'))
        unlock_database()
        sys.exit(1)
    except sqlite3.OperationalError:
        print(f'{Fore.RED}ERROR: database error: please run "tblock -Yf" as superuser '
              f'to resolve this problem{Style.RESET_ALL}')
        sys.exit(1)
    except sqlite3.DatabaseError:
        print(f'{Fore.RED}ERROR: database may be locked or corrupted: please run "tblock -Yf" as superuser')
    except (SIGTERM, KeyboardInterrupt):
        unlock_database()
        sys.exit(1)
    else:
        unlock_database()


def run_converter() -> None:
    try:
        parse_args_tblockc()
    except (PermissionError, FilterSourceExistsError, MissingArgumentError, FilterNotExists, NotSubscribingError,
            RuleNotExistsError, InvalidBindAddress, InvalidFilterSyntax, FileNotFoundError, IsADirectoryError) as err:
        print(str(err).replace('[Errno 2] N', 'n').replace('[Errno 21] I', 'i'))
        sys.exit(1)
    except (SIGTERM, KeyboardInterrupt):
        exit(1)
