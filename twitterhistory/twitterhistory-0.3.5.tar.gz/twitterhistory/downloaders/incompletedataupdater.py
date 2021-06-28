#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#   Copyright (C) 2020 Christoph Fink, University of Helsinki
#
#   This program is free software; you can redistribute it and/or
#   modify it under the terms of the GNU General Public License
#   as published by the Free Software Foundation; either version 3
#   of the License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, see <http://www.gnu.org/licenses/>.


"""Base class for workers that update incomplete records (of tweets and users, e.g.)."""


__all__ = ["IncompleteDataUpdater"]


from .basedownloader import BaseDownloader


class IncompleteDataUpdater(BaseDownloader):
    """Re-download data for incomplete records."""

    def __init__(self, in_queue, api_key_managers, shutdown):
        """Initialize an IncompleteDataUpdater."""
        super().__init__(api_key_managers)
        self._in_queue = in_queue
        self.shutdown = shutdown
