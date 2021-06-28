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


"""Save a batch of data as returned by GetTweetsSearchAllDownloader.batches."""


__all__ = ["ApiResponseSaver"]


import datetime

import dateparser

from .engine import Session
from .includessaver import IncludesSaver
from .models import SearchTerm
from .tweetsaver import TweetSaver
from ..exceptions import MonthlyQuotaExceededError


class ApiResponseSaver(IncludesSaver, TweetSaver):
    """Save a batch of data as returned by GetTweetsSearchAllDownloader.batches."""

    def __init__(self, shutdown):
        """Initialise an ApiResponseSaver instance."""
        super().__init__(shutdown)
        self.count = 0

    def save_batch_of_tweets(self, batch, search_term=None):
        """
        Save the data in `batch` to the database.

        Expects `batch` to be a data dictionary returned from one of the
        tweets endpoints.
        """
        earliest_tweet_created_at = datetime.datetime.now(datetime.timezone.utc)

        with Session() as session:
            with session.begin():
                if search_term:
                    search_term = (
                        session.query(SearchTerm)
                        .filter(SearchTerm.search_term == search_term)
                        .first()
                    ) or session.add(SearchTerm(search_term=search_term))

            if "data" in batch:
                if "includes" in batch["data"]:
                    self._save_includes(batch["data"]["includes"], session)
                for tweet in batch["data"]:
                    if self.shutdown.is_set():
                        break
                    self._save_tweet(tweet, session, search_term)
                    self.count += 1
                    earliest_tweet_created_at = min(
                        earliest_tweet_created_at, dateparser.parse(tweet["created_at"])
                    )
            else:
                if "title" in batch and batch["title"] == "UsageCapExceeded":
                    raise MonthlyQuotaExceededError()
        return earliest_tweet_created_at

    def save_batch_of_users(self, batch):
        """
        Save the data in `batch` to the database.

        Expects `batch` to be a data dictionary returned from one of the
        user endpoints
        """
        with Session() as session:
            if "data" in batch:
                if "includes" in batch["data"]:
                    self._save_includes(batch["data"]["includes"], session)
                for user in batch["data"]:
                    if self.shutdown.is_set():
                        break
                    self._save_user(user, session)
