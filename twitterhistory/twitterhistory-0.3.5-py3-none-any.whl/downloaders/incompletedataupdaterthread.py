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


"""Worker threads wrapping an IncompleteDataUpdater."""


__all__ = ["IncompleteDataUpdaterThread"]


import datetime
import math
import time

from ..exceptions import (
    MonthlyQuotaExceededError,
    TemporaryApiResponseError,
)
from .basedownloaderthread import BaseDownloaderThread


class IncompleteDataUpdaterThread(BaseDownloaderThread):
    """Wraps an IncompleteDataUpdater to run in a separate thread."""

    def __init__(self, api_key_managers, in_queue):
        """
        Initialize a IncompleteDataUpdaterThread.

        Args:
            api_key_managers: instance of an ApiKeyManager
            todo_deque: collections.deque that serves (search_term, TimeSpan)
                        tuples that need to be downloaded
            done_queue: queue.Queue into which to put (search_term, TimeSpan)
                        tuples that have been downloaded

        """
        super().__init__(api_key_managers=api_key_managers)
        self._in_queue = in_queue

    def run(self):
        """Download data for incomplete records."""
        while not self.shutdown.is_set():
            data_downloader = self._Downloader(
                self._in_queue,
                self._api_key_managers,
                self.shutdown
            )

            try:
                for batch in data_downloader.batches:
                    self.save_batch(batch)

                    if self.shutdown.is_set():
                        break

            except TemporaryApiResponseError as exception:
                # wait until we’re allowed again
                wait_seconds = (
                    exception.reset_time - datetime.datetime.now(datetime.timezone.utc)
                ).total_seconds()
                for _ in range(math.ceil(wait_seconds)):
                    time.sleep(1)
                    if self.shutdown.is_set():
                        break
                else:
                    continue

            except MonthlyQuotaExceededError as exception:
                # TODO: report error properly,
                # for now, re-raise exception to escalate to parent thread
                raise exception from None
