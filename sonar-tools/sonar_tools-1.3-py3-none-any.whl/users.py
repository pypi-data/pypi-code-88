#
# sonar-tools
# Copyright (C) 2019-2021 Olivier Korach
# mailto:olivier.korach AT gmail DOT com
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
'''

    Abstraction of the SonarQube "user" concept

'''
import json
import datetime as dt
import pytz
import sonarqube.env as env
import sonarqube.sqobject as sq

import sonarqube.audit_severities as sev
import sonarqube.audit_types as typ
import sonarqube.audit_problem as pb
import sonarqube.user_tokens as tok

SQ_DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S%z'
SQ_DATE_FORMAT = "%Y-%m-%d"
SQ_TIME_FORMAT = "%H:%M:%S"


class User(sq.SqObject):
    API_ROOT = 'users'
    API_CREATE = API_ROOT + '/create'
    API_SEARCH = API_ROOT + '/search'
    API_DEACTIVATE = API_ROOT + '/deactivate'

    def __init__(self, login, name, endpoint=None, **kwargs):
        super().__init__(key=login, env=endpoint)
        self.login = login
        self.name = name
        self.local = kwargs.get('local', False)
        self.password = kwargs.get('password', None)
        self.email = kwargs.get('email', None)
        self.scmAccounts = kwargs.get('scmAccounts', None)
        self.groups = kwargs.get('groups', None)
        self.externalIdentity = kwargs.get('externalIdentity', None)
        self.externalProvider = kwargs.get('externalProvider', None)
        self.avatar = kwargs.get('avatar', None)
        self.tokenCount = kwargs.get('tokenCount', None)
        self.tokens_list = None

    def __str__(self):
        return self.login

    def deactivate(self):
        env.post(User.API_DEACTIVATE, {'name': self.name, 'login': self.login}, self.env)
        return True

    def tokens(self):
        if self.tokens_list is None:
            self.tokens_list = tok.search(self.login, self.env)
        return self.tokens_list


def search(q=None, endpoint=None, p=None, ps=500):
    users_list = {}
    resp = env.get(User.API_SEARCH, {'q': q, 'p': p, 'ps': ps}, endpoint)
    data = json.loads(resp.text)
    nb_pages = (data['paging']['total'] + ps - 1) // ps
    for u in data['users']:
        users_list[u['login']] = User(endpoint=endpoint, **u)
    if p is not None:
        return users_list
    p = 2
    while p <= nb_pages:
        resp = env.get(User.API_SEARCH, {'q': q, 'p': p, 'ps': ps}, endpoint)
        data = json.loads(resp.text)
        nb_pages = (data['paging']['total'] + ps - 1) // ps
        for u in data['users']:
            users_list[u['login']] = User(endpoint=endpoint, **u)
        p += 1
    return users_list


def create(name, login=None, endpoint=None):
    resp = env.post(User.API_CREATE, {'name': name, 'login': login}, endpoint)
    data = json.loads(resp.text)
    return User(data['login'], data['name'], endpoint, **data)


def audit(audit_settings, endpoint=None):
    today = dt.datetime.today().replace(tzinfo=pytz.UTC)
    max_days = audit_settings['audit.tokens.maxAge']
    problems = []
    for l, u in search(endpoint=endpoint).items():
        for t in u.tokens():
            if abs((today - t.createdAt).days) <= max_days:
                continue
            problems.append(pb.Problem(
                typ.Type.SECURITY, sev.Severity.HIGH,
                "Token '{}' of user '{}' is {} days old and should be revoked".format(
                    str(t), str(u), abs((today - t.createdAt).days)), concerned_object=t))
    return problems
