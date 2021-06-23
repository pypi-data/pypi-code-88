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

# External libraries
from colorama import Fore, Style

# Local libraries
from .hosts import update_hosts
from .config import Path, Font
from .utils import is_valid_ip, extract_domain, check_root, prompt_user, lock_database, unlock_database
from .exceptions import InvalidBindAddress, RuleExistsError, InvalidRulePolicy, \
    RuleNotExistsError, MissingArgumentError, SIGTERM


class Rule:

    def __init__(self, domain: str) -> None:
        """Rule object to use for user rules. This is to slow to be used for filter rules

        Args:
            domain (str): The domain or the URL of the domain to manage
        """
        self.domain = extract_domain(domain)

        # Fetch rule data from the database
        with sqlite3.connect(Path.DATABASE) as conn:
            data = conn.cursor().execute(
                'SELECT "policy", "priority", "filter_id", "ip" FROM "rules" WHERE domain=?;',
                (self.domain,)
            ).fetchall()
        self.exists = bool(data)
        self.policy = data[0][0] if data else None
        self.priority = data[0][1] if data else False
        self.filter_id = data[0][2] if data else None
        self.ip = data[0][3] if data else None

    def add(self, policy: str, ip: str = None) -> None:
        """Add rule to database

        Args:
            policy (str): The policy of the rule (allow/block/redirect)
            ip (str, optional): The IP where to redirect domain
        """
        print(f' [{Fore.YELLOW}|{Style.RESET_ALL}] Adding rule for {self.domain}', end='\r')

        if policy not in ['allow', 'block', 'redirect']:
            print(f' [{Fore.RED}x{Style.RESET_ALL}] Adding rule for {self.domain}')
            raise InvalidRulePolicy(f'invalid rule policy: "{policy}"')
        elif policy == 'redirect' and not ip:
            print(f' [{Fore.RED}x{Style.RESET_ALL}] Adding rule for {self.domain}')
            raise InvalidBindAddress('redirecting IP address cannot be NoneType')
        elif policy == 'redirect' and not is_valid_ip(ip):
            print(f' [{Fore.RED}x{Style.RESET_ALL}] Adding rule for {self.domain}')
            raise InvalidBindAddress('redirecting IP address cannot be NoneType')
        elif policy == self.policy and ip == self.ip and self.priority:
            print(f' [{Fore.GREEN}{Font.CHECK_MARK}{Style.RESET_ALL}] Adding rule for {self.domain}')
            raise RuleExistsError(f'exact same rule already exists for domain: "{self.domain}"')

        with sqlite3.connect(Path.DATABASE) as db:
            if self.exists:
                db.cursor().execute(
                    'UPDATE "rules" SET policy=?, priority=?, filter_id=?, ip=?  WHERE domain=?;',
                    (policy, True, '!user', ip, self.domain)
                )
            else:
                db.cursor().execute(
                    'INSERT INTO "rules" ("domain", "policy", "priority", "filter_id", "ip") VALUES (?, ?, ?, ?, ?);',
                    (self.domain, policy, True, '!user', ip)
                )
            db.commit()
        print(f' [{Fore.GREEN}{Font.CHECK_MARK}{Style.RESET_ALL}] Adding rule for {self.domain}')

    def delete(self) -> None:
        """Delete an user rule from database
        """
        print(f' [{Fore.YELLOW}|{Style.RESET_ALL}] Deleting rule for {self.domain}', end='\r')

        if not self.priority:
            print(f' [{Fore.RED}x{Style.RESET_ALL}] Deleting rule for {self.domain}')
            raise RuleNotExistsError(f'no rule found for domain "{self.domain}"')

        with sqlite3.connect(Path.DATABASE) as db:
            db.cursor().execute(
                'DELETE FROM "rules" WHERE domain=?;',
                (self.domain,)
            )
            db.commit()
        print(f' [{Fore.GREEN}{Font.CHECK_MARK}{Style.RESET_ALL}] Deleting rule for {self.domain}')


def get_all_rules(standard: bool = True, user: bool = True) -> dict:
    """Retrieve all active rules from the database

    Args:
        standard (bool, optional): Include rules set by filters
        user (bool, optional): Include user rules

    Returns:
        dict: All rules in the directory. The domain is the directory key
    """
    all_rules = {}
    with sqlite3.connect(Path.DATABASE) as db:
        if standard and user:
            data = db.cursor().execute(
                'SELECT "domain","policy","filter_id","priority","ip" FROM "rules";'
            ).fetchall()
        elif standard:
            data = db.cursor().execute(
                'SELECT "domain","policy","filter_id","priority","ip" FROM "rules" WHERE priority=0;'
            ).fetchall()
        elif user:
            data = db.cursor().execute(
                'SELECT "domain","policy","filter_id","priority","ip" FROM "rules" WHERE priority=1;'
            ).fetchall()
        else:
            data = []
    for row in data:
        all_rules[row[0]] = {}
        all_rules[row[0]]['policy'] = row[1]
        all_rules[row[0]]['filter_id'] = row[2]
        all_rules[row[0]]['priority'] = row[3]
        all_rules[row[0]]['ip'] = row[4]
    return all_rules


def add_rules(rules: list, force: bool = False) -> None:
    """Add rules for domains

    Args:
        rules (list): All rules in a list: [ [domain, policy, ip (if any)] ]
        force (bool, optional): Do not prompt user (False by default)
    """
    list_domains = []
    for r in rules:
        list_domains.append(extract_domain(r[0]))
    if not check_root():
        raise PermissionError(f'{Fore.RED}ERROR: you need to run as root to perform this operation{Style.RESET_ALL}')
    elif not rules:
        raise MissingArgumentError(
            f'{Fore.RED}ERROR: you need to specify at least one domain to manage{Style.RESET_ALL}'
        )
    elif not force and not prompt_user('You are about to add rules for the following domains:', list_domains):
        raise SIGTERM()
    print(':: Adding rules...')
    lock_database()
    for rule_data in rules:
        rule_obj = Rule(rule_data[0])
        try:
            if len(rule_data) == 2:
                rule_obj.add(rule_data[1])
            else:
                rule_obj.add(rule_data[1], rule_data[2])
        except RuleExistsError as err:
            print(f'{Fore.YELLOW}WARNING: {err}{Style.RESET_ALL}')
        except InvalidBindAddress as err:
            raise InvalidBindAddress(f'{Fore.RED}ERROR: {err}{Style.RESET_ALL}')
    update_hosts(get_all_rules())
    unlock_database()


def delete_rules(rules: list, force: bool = False) -> None:
    """Delete rules for domains

    Args:
        rules (list): All rules in a list: [domain1, domain2]
        force (bool, optional): Do not prompt user (False by default)
    """
    list_domains = []
    for r in rules:
        list_domains.append(extract_domain(r))
    if not check_root():
        raise PermissionError(f'{Fore.RED}ERROR: you need to run as root to perform this operation{Style.RESET_ALL}')
    elif not rules:
        raise MissingArgumentError(
            f'{Fore.RED}ERROR: you need to specify at least one domain to delete from rules{Style.RESET_ALL}'
        )
    elif not force and not prompt_user('You are about to add rules for the following domains:', list_domains):
        raise SIGTERM()
    print(':: Deleting rules...')
    lock_database()
    for rule_data in rules:
        rule_obj = Rule(rule_data)
        try:
            rule_obj.delete()
        except RuleNotExistsError as err:
            raise RuleNotExistsError(f'{Fore.RED}ERROR: {err}{Style.RESET_ALL}')
    update_hosts(get_all_rules())
    unlock_database()


def list_rules(standard_only: bool = False, user_only: bool = False) -> None:
    """List all active rules and their policy

    Args:
        standard_only (bool, optional): Only list standard rules
        user_only (bool, optional): Only list user rules
    """
    if not standard_only and not user_only:
        rules = get_all_rules()
    elif standard_only and not user_only:
        rules = get_all_rules(user=False)
    elif user_only and not standard_only:
        rules = get_all_rules(standard=False)
    else:
        rules = get_all_rules(False, False)

    for r in rules.keys():
        if rules[r]['policy'] == 'redirect':
            print(f'REDIRECT    {r}')
        elif rules[r]['policy'] == 'block':
            print(f'BLOCK       {r}')
        elif rules[r]['policy'] == 'allow':
            print(f'ALLOW       {r}')
