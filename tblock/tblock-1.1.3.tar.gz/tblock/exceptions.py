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


class TBlockError(IOError):
    def __init__(self, *args):
        super(TBlockError, self).__init__(*args)


class SIGTERM(IOError):
    def __init__(self, *args):
        super(SIGTERM, self).__init__(*args)


class InvalidFilterSyntax(TBlockError):
    def __init__(self, *args):
        super(InvalidFilterSyntax, self).__init__(*args)


class FilterExistsError(TBlockError):
    def __init__(self, *args):
        super(FilterExistsError, self).__init__(*args)


class AlreadySubscribingError(TBlockError):
    def __init__(self, *args):
        super(AlreadySubscribingError, self).__init__(*args)


class NotSubscribingError(TBlockError):
    def __init__(self, *args):
        super(NotSubscribingError, self).__init__(*args)


class FilterNotExists(TBlockError):
    def __init__(self, *args):
        super(FilterNotExists, self).__init__(*args)


class FilterSourceExistsError(TBlockError):
    def __init__(self, *args):
        super(FilterSourceExistsError, self).__init__(*args)


class FilterNotCustomError(TBlockError):
    def __init__(self, *args):
        super(FilterNotCustomError, self).__init__(*args)


class NetworkError(TBlockError):
    def __init__(self, *args):
        super(NetworkError, self).__init__(*args)


class MissingArgumentError(TBlockError):
    def __init__(self, *args):
        super(MissingArgumentError, self).__init__(*args)


class InvalidLinkError(TBlockError):
    def __init__(self, *args):
        super(InvalidLinkError, self).__init__(*args)


class InvalidBindAddress(TBlockError):
    def __init__(self, *args):
        super(InvalidBindAddress, self).__init__(*args)


class RuleExistsError(TBlockError):
    def __init__(self, *args):
        super(RuleExistsError, self).__init__(*args)


class RuleNotExistsError(TBlockError):
    def __init__(self, *args):
        super(RuleNotExistsError, self).__init__(*args)


class InvalidRulePolicy(TBlockError):
    def __init__(self, *args):
        super(InvalidRulePolicy, self).__init__(*args)


class FilterReservedError(TBlockError):
    def __init__(self, *args):
        super(FilterReservedError, self).__init__(*args)
