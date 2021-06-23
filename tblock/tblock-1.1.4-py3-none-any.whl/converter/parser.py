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
import re

# External libraries
from colorama import Fore, Style

# Local libraries
from ..exceptions import InvalidFilterSyntax, SIGTERM
from ..utils import prompt_user
from ..config import Font


class Syntax:
    """The class containing all supported filter formats
    """
    adblockplus = 'adblockplus'
    hosts = 'hosts'
    tblock = 'tblock'
    list = 'list'
    dnsmasq = 'dnsmasq'
    opera = 'opera'


def is_comment(line: str, syntax: str) -> bool:
    """Check if a line is a comment

    Args:
        line (str): The line to check
        syntax (str): The syntax to use for check

    Returns:
        bool: True if line is a comment
    """
    if hasattr(Syntax, syntax):
        if syntax == Syntax.adblockplus:
            return line[0:1] == '!'
        else:
            return line[0:1] == '#'
    else:
        raise InvalidFilterSyntax(f'"{syntax}" is not a valid syntax')


class FilterParser:

    def __init__(self, filter_path: str, syntax: str = None) -> None:
        """
        Filter to parse
        Args:
            filter_path (str): The path to the filter
            syntax (str, optional): The syntax of the filter (if not set, tblock will autodetect it)
        """
        self.filter_path = os.path.realpath(filter_path)

        # Prevent files that are not UTF-8 encoded to be opened as filters
        try:
            with open(self.filter_path, 'rt', encoding='utf-8') as f:
                self.list = f.readlines()
        except UnicodeDecodeError:
            raise InvalidFilterSyntax(f'cannot read file "{self.filter_path}" since its encoding is not supported')

        self.total_lines = len(self.list)

        if syntax:
            self.syntax = syntax
        else:
            try:
                self.syntax = self.detect_syntax()
            except ZeroDivisionError:
                self.syntax = ''

    def detect_syntax(self) -> str:
        """Detect the syntax of a filter

        Returns:
            str: The syntax. See the Syntax object for more information.
        """
        rules = []

        # Remove blank lines from test
        for rule in self.list:
            if rule != '\n':
                rules.append(rule.split("\n")[0])

        # Count the number of lines that are not empty
        rules_count = len(rules)

        # Convert that list into a string, in order to use regex to find patterns in it
        rules = str(rules)

        # Check the syntax of the filter using regex and calculating the percentage of rules that match a syntax
        if re.findall(re.compile(r'(\[adblock plus)', re.IGNORECASE), rules):
            return Syntax.adblockplus
        elif re.findall(re.compile(r'(@BEGIN_RULES|@END_RULES)'), rules):
            return Syntax.tblock
        elif len(re.findall(re.compile(r'(\|\|[.a-z\-]*[$^]|![ A-z]*[.]*:|!)'), rules)) * 100 / rules_count >= 50:
            return Syntax.adblockplus
        elif len(re.findall(re.compile(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}[ \t]|::1[ \t]'), rules)) \
                * 100 / rules_count >= 50:
            return Syntax.hosts
        elif len(re.findall(re.compile(r'(server=/|domain=/)'), rules)) * 100 / rules_count >= 50:
            return Syntax.dnsmasq
        elif len(re.findall(re.compile(r'(http://)'), rules)) * 100 / rules_count >= 50:
            return Syntax.opera
        elif len(re.findall(re.compile(r'([0-9a-z]*\.[.a-z]*)'), rules)) * 100 / rules_count >= 50:
            return Syntax.list
        else:
            return ''

    def get_filter_content(self, allow: bool = True, block: bool = True,
                           redirect: bool = True, comments: bool = False) -> list:
        """Get all rules from a filter

        Args:
            allow (bool, optional): Return allowing rules when supported by syntax (default)
            block (bool, optional): Return blocking rules when supported by syntax(default)
            redirect (bool, optional): Return redirecting rules when supported by syntax (default)
            comments (bool, optional): Return comments when supported by syntax (False by default)
        """

        # Prevent unsupported syntax to be opened
        if not hasattr(Syntax, self.syntax):
            raise InvalidFilterSyntax(f'"{self.syntax}" is not a valid syntax')
        filter_data = []

        # Variables for specific filter formats
        tblock_begin = None
        tblock_policy = None
        opera_policy = None

        count = 0
        load_character = '|'

        print(f' [{Fore.BLUE}i{Style.RESET_ALL}] Filter syntax is: {Font.UNDERLINE}{self.syntax}{Font.DEFAULT}')

        for rule in self.list:
            if not count + 1 == self.total_lines:
                print(f' [{Fore.YELLOW}{load_character}{Style.RESET_ALL}] Parsing filter '
                      f'({count + 1}/{self.total_lines})', end='\r')
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
                print(f' [{Fore.GREEN}{Font.CHECK_MARK}{Style.RESET_ALL}] Parsing filter '
                      f'({count + 1}/{self.total_lines})')

            # Skip all blank lines
            if rule != "\n":
                if not is_comment(rule, self.syntax):

                    if self.syntax == Syntax.adblockplus:
                        if not re.findall(re.compile(r'([$/&%?:*()=,;#\"+_])'), rule):
                            if '^' in rule:
                                if rule[0:2] == '||' and block:
                                    filter_data.append(
                                        ['rule', rule.split("\n")[0].split('||')[1].split('^')[0], 'block']
                                    )
                                elif rule[0:4] == '@@||' and allow:
                                    filter_data.append(
                                        ['rule', rule.split("\n")[0].split('||')[1].split('^')[0], 'allow']
                                    )

                    elif self.syntax == Syntax.hosts:
                        if re.match(re.compile(r'(127\.0\.[01]\.[0-9]{1,3}[ \t]|0\.0\.0\.0[ \t]|::1[ \t])'), rule):
                            for k in rule.split('\n')[0].split('#')[0].split(' '):
                                for r in k.split('\t'):
                                    if not re.findall(re.compile(r'[$/&%?:*()=,;#\"+\t_]'), r):
                                        if not re.findall(
                                                re.compile(r'(127\.0\.[01]\.[0-9]{1,3}|0\.0\.0\.0)'), r
                                        ) and r and block:
                                            filter_data.append(
                                                ['rule', r, 'block']
                                            )
                        else:
                            if not re.findall(re.compile(r'([$/&%?:*()=,;#\"+_])'), rule):
                                ip = rule.split(' ')[0].split('\t')[0]
                                rule = rule.split('\n')[0].split(' ')[len(rule.split(' ')) - 1].replace(' ', '')
                                rule = rule.split('\t')[1] if '\t' in rule else rule
                                if rule and redirect:
                                    filter_data.append(
                                        ['rule', rule, 'redirect', ip]
                                    )

                    elif self.syntax == Syntax.list:
                        if not re.findall(re.compile(r'([$/&%?:*()=,;#\"+_])'), rule) and block:
                            filter_data.append(['rule', rule.split("\n")[0], 'block'])

                    elif self.syntax == Syntax.dnsmasq:
                        if re.match(re.compile(r'(server=/|domain=/)'), rule):
                            if not re.findall(re.compile(r'([$&%?:*(),;#\"+_])'), rule) and block:
                                filter_data.append(
                                    ['rule', rule.split("\n")[0].split('=/')[1].split('/')[0], 'block']
                                )

                    elif self.syntax == Syntax.tblock:
                        if tblock_begin == 'rules':
                            if rule.split('\n')[0] == '@END_RULES':
                                tblock_begin = None
                            elif rule[0:1] == '!':
                                if rule.split('\n')[0] == '!allow':
                                    tblock_policy = 'allow'
                                elif rule.split('\n')[0] == '!block':
                                    tblock_policy = 'block'
                                elif rule[0:10] == '!redirect ':
                                    tblock_policy = 'redirect ' + rule.split('!redirect ')[1].split('\n')[0]
                            else:
                                if not re.findall(re.compile(r'([$/&%?:*()=,;#\"+_])'), rule):
                                    if 'redirect' in tblock_policy and redirect:
                                        filter_data.append([
                                            'rule', rule.split("\n")[0], 'redirect',
                                            tblock_policy.split('redirect ')[1]
                                        ])
                                    elif tblock_policy == 'block' and block or tblock_policy == 'allow' and allow:
                                        filter_data.append(['rule', rule.split("\n")[0], tblock_policy])
                        elif tblock_begin is None:
                            if rule.split('\n')[0] == '@BEGIN_RULES':
                                tblock_begin = 'rules'

                    elif self.syntax == Syntax.opera:
                        if rule.split('\n')[0] == '[include]':
                            opera_policy = 'allow'
                        elif rule.split('\n')[0] == '[exclude]':
                            opera_policy = 'block'
                        if re.match(r'^http://[a-z0-9]*\.[a-z0-9.]*/\*', rule.split('\n')[0]):
                            if opera_policy == 'allow':
                                filter_data.append(['rule', rule.split("http://")[1].split('/*')[0], 'allow'])
                            elif opera_policy == 'block':
                                filter_data.append(['rule', rule.split("http://")[1].split('/*')[0], 'block'])

                elif comments:
                    if self.syntax == Syntax.adblockplus:
                        filter_data.append(['comment', rule.split('!')[1].replace('\n', '')])
                    else:
                        filter_data.append(['comment', rule.split('#')[1].replace('\n', '')])
            count += 1
        print(f' [{Fore.BLUE}i{Style.RESET_ALL}] Skipped {self.total_lines - len(filter_data)} '
              f'invalid rule(s) or blank line(s)')
        return filter_data

    def convert(self, output_file: str, output_syntax: str, hosts_default_ip: str = '127.0.0.1', allow: bool = True,
                block: bool = True, redirect: bool = True, comments: bool = False, force: bool = False,
                verbosity: bool = False) -> None:
        """Convert a filter into another syntax

        Args:
            output_file (str): Where to write converted filter
            output_syntax (str): To which syntax the filter should be converted
            hosts_default_ip (str, optional): Specify a custom IP where to redirect blocked domains in hosts file format
            allow (bool, optional): Convert allowing rules when supported by syntax (default)
            block (bool, optional): Convert blocking rules when supported by syntax (default)
            redirect (bool, optional): Convert redirecting rules when supported by syntax (default)
            comments (bool, optional): Convert comments when supported by syntax (False by default)
            force (bool, optional): Do not prompt for anything (False by default)
            verbosity (bool, optional): Enable verbosity
        """

        # If output file already exists that the force option is not set, and that the user answers
        # no to the confirm prompt, exit the script
        if os.path.isfile(os.path.realpath(output_file)) and \
                not force and not prompt_user(f'You are about to overwrite the file "{output_file}"'):
            raise SIGTERM()

        print(':: Converting filter...')

        if verbosity:
            print(f'{Font.BOLD}==> Converting into: {output_syntax}{Font.DEFAULT}')

        # Check if the syntax is supported, raise an exception if not
        if not hasattr(Syntax, output_syntax):
            raise InvalidFilterSyntax(f'"{output_syntax}" is not a valid syntax')

        # Set the first line for most filter formats
        if output_syntax == Syntax.adblockplus:
            output_content = '[Adblock Plus 3.1]\n\n! Converted by tblockc (https://tblock.codeberg.page/)\n\n'
        elif output_syntax == Syntax.tblock:
            output_content = '# Converted by tblockc (https://tblock.codeberg.page/)\n\n@BEGIN_RULES\n\n'
        elif not output_syntax == Syntax.list:
            output_content = '# Converted by tblockc (https://tblock.codeberg.page/)\n\n'
        else:
            output_content = ''

        # Variables for specific filter formats
        tblock_syntax = None
        opera_policy = None
        count = 1
        load_character = '|'

        for rule in self.get_filter_content(allow, block, redirect, comments):

            if count < self.total_lines:
                print(f' [{Fore.YELLOW}{load_character}{Style.RESET_ALL}] Converting rules '
                      f'({count}/{self.total_lines})', end='\r')
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
                print(f' [{Fore.GREEN}{Font.CHECK_MARK}{Style.RESET_ALL}] Converting rules '
                      f'({count}/{self.total_lines})')

            if rule[0] == 'comment' and comments:
                if output_syntax == Syntax.adblockplus:
                    output_content += f'!{rule[1]}\n'
                elif not output_syntax == Syntax.list:
                    output_content += f'#{rule[1]}\n'
            elif rule[0] == 'rule':

                if rule[2] == 'allow' and allow:
                    if output_syntax == Syntax.adblockplus:
                        output_content += f'@@||{rule[1]}^\n'
                    elif output_syntax == Syntax.tblock:
                        if tblock_syntax != 'allow':
                            tblock_syntax = 'allow'
                            output_content += f'\n!allow\n{rule[1]}\n'
                        else:
                            output_content += f'{rule[1]}\n'
                    elif output_syntax == Syntax.opera:
                        if opera_policy != 'allow':
                            opera_policy = 'allow'
                            output_content += f'[include]\nhttp://{rule[1]}/*\n'
                            output_content += f'http://*.{rule[1]}/*\n'
                        else:
                            output_content += f'http://{rule[1]}/*\n'
                            output_content += f'http://*.{rule[1]}/*\n'

                elif rule[2] == 'block' and block:
                    if output_syntax == Syntax.adblockplus:
                        output_content += f'||{rule[1]}^\n'
                    elif output_syntax == Syntax.dnsmasq:
                        output_content += f'server=/{rule[1]}/\n'
                    elif output_syntax == Syntax.hosts:
                        output_content += f'{hosts_default_ip}    {rule[1]}\n'
                    elif output_syntax == Syntax.list:
                        output_content += f'{rule[1]}\n'
                    elif output_syntax == Syntax.tblock:
                        if tblock_syntax != 'block':
                            tblock_syntax = 'block'
                            output_content += f'\n!block\n{rule[1]}\n'
                        else:
                            output_content += f'{rule[1]}\n'
                    elif output_syntax == Syntax.opera:
                        if opera_policy != 'block':
                            opera_policy = 'block'
                            output_content += f'[exclude]\nhttp://{rule[1]}/*\n'
                            output_content += f'http://*.{rule[1]}/*\n'
                        else:
                            output_content += f'http://{rule[1]}/*\n'
                            output_content += f'http://*.{rule[1]}/*\n'

                elif rule[2] == 'redirect' and redirect:
                    if output_syntax == Syntax.hosts:
                        output_content += f'{rule[3]}    {rule[1]}\n'
                    elif output_syntax == Syntax.tblock:
                        if tblock_syntax != f'redirect {rule[3]}':
                            tblock_syntax = f'redirect {rule[3]}'
                            output_content += f'\n!redirect {rule[3]}\n{rule[1]}\n'
                        else:
                            output_content += f'{rule[1]}\n'

            count += 1
        if output_syntax == Syntax.tblock:
            output_content += '\n@END_RULES\n'
        with open(os.path.realpath(output_file), 'wt') as f:
            f.write(output_content)
        print(f' [{Fore.GREEN}{Font.CHECK_MARK}{Style.RESET_ALL}] Filter successfully converted')
