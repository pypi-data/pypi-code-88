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
import os.path

# External libraries
from colorama import Fore, Style

# Local libraries
from ..config import Font
from ..exceptions import InvalidFilterSyntax
from .parser import FilterParser


def get_syntax(file: str) -> None:
    """Get the syntax of a filter

    Args:
        file (str): The path to the filter
    """
    print(':: Detecting syntax...')
    try:
        f_parser = FilterParser(os.path.realpath(file))
    except InvalidFilterSyntax as err:
        raise InvalidFilterSyntax(f'{Fore.RED}ERROR: {err}{Style.RESET_ALL}')
    except FileNotFoundError as err:
        raise FileNotFoundError(f'{Fore.RED}ERROR: {err}{Style.RESET_ALL}')
    else:
        print(f' [{Fore.BLUE}i{Style.RESET_ALL}] Filter syntax is: {Font.UNDERLINE}{f_parser.syntax}{Font.DEFAULT}')


def convert_filter(input_file: str, output_file: str, output_syntax: str,
                   input_syntax: str = None, hosts_default_ip: str = '127.0.0.1', comments: bool = False,
                   allow: bool = True, block: bool = True, redirect: bool = True, force: bool = False) -> None:
    """Convert a filter into another syntax

    Args:
        input_file (str): The path to the filter to convert
        output_file (str): Where to write converted filter
        output_syntax (str): To which syntax the filter should be converted
        input_syntax (str, optional): The syntax of the filter (if not set, tblock will autodetect it)
        hosts_default_ip (str, optional): Specify a custom IP where to redirect blocked domains in hosts file format
        allow (bool, optional): Convert allowing rules when supported by syntax (default)
        block (bool, optional): Convert blocking rules when supported by syntax (default)
        redirect (bool, optional): Convert redirecting rules when supported by syntax (default)
        comments (bool, optional): Convert comments when supported by syntax (False by default)
        force (bool, optional): Do not prompt for anything (False by default)
    """
    try:
        f_parser = FilterParser(input_file, input_syntax)
    except InvalidFilterSyntax as err:
        raise InvalidFilterSyntax(f'{Fore.RED}ERROR: {err}{Style.RESET_ALL}')
    except FileNotFoundError as err:
        raise FileNotFoundError(f'{Fore.RED}ERROR: {err}{Style.RESET_ALL}')
    except IsADirectoryError as err:
        raise IsADirectoryError(f'{Fore.RED}ERROR: {err}{Style.RESET_ALL}')
    else:
        f_parser.convert(output_file, output_syntax, hosts_default_ip, allow, block, redirect, comments, force, True)
