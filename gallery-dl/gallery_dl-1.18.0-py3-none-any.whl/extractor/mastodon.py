# -*- coding: utf-8 -*-

# Copyright 2019-2021 Mike Fährmann
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

"""Extractors for mastodon instances"""

from .common import BaseExtractor, Message
from .. import text, exception
from ..cache import cache


class MastodonExtractor(BaseExtractor):
    """Base class for mastodon extractors"""
    basecategory = "mastodon"
    directory_fmt = ("mastodon", "{instance}", "{account[username]}")
    filename_fmt = "{category}_{id}_{media[id]}.{extension}"
    archive_fmt = "{media[id]}"
    cookiedomain = None

    def __init__(self, match):
        BaseExtractor.__init__(self, match)
        self.instance = self.root.partition("://")[2]
        self.item = match.group(match.lastindex)

    def items(self):
        for status in self.statuses():
            attachments = status["media_attachments"]
            if attachments:
                self.prepare(status)
                yield Message.Directory, status
                for media in attachments:
                    status["media"] = media
                    url = media["url"]
                    yield Message.Url, url, text.nameext_from_url(url, status)

    def statuses(self):
        """Return an iterable containing all relevant Status-objects"""
        return ()

    def prepare(self, status):
        """Prepare a status object"""
        del status["media_attachments"]
        status["instance"] = self.instance
        status["tags"] = [tag["name"] for tag in status["tags"]]
        status["date"] = text.parse_datetime(
            status["created_at"][:19], "%Y-%m-%dT%H:%M:%S")


INSTANCES = {
    "mastodon.social": {
        "root"         : "https://mastodon.social",
        "access-token" : "Y06R36SMvuXXN5_wiPKFAEFiQaMSQg0o_hGgc86Jj48",
        "client-id"    : "dBSHdpsnOUZgxOnjKSQrWEPakO3ctM7HmsyoOd4FcRo",
        "client-secret": "DdrODTHs_XoeOsNVXnILTMabtdpWrWOAtrmw91wU1zI",
    },
    "pawoo": {
        "root"         : "https://pawoo.net",
        "access-token" : "c12c9d275050bce0dc92169a28db09d7"
                         "0d62d0a75a8525953098c167eacd3668",
        "client-id"    : "978a25f843ec01e53d09be2c290cd75c"
                         "782bc3b7fdbd7ea4164b9f3c3780c8ff",
        "client-secret": "9208e3d4a7997032cf4f1b0e12e5df38"
                         "8428ef1fadb446dcfeb4f5ed6872d97b",
    },
    "baraag": {
        "root"         : "https://baraag.net",
        "access-token" : "53P1Mdigf4EJMH-RmeFOOSM9gdSDztmrAYFgabOKKE0",
        "client-id"    : "czxx2qilLElYHQ_sm-lO8yXuGwOHxLX9RYYaD0-nq1o",
        "client-secret": "haMaFdMBgK_-BIxufakmI2gFgkYjqmgXGEO2tB-R2xY",
    }
}

BASE_PATTERN = MastodonExtractor.update(INSTANCES)


class MastodonUserExtractor(MastodonExtractor):
    """Extractor for all images of an account/user"""
    subcategory = "user"
    pattern = BASE_PATTERN + r"/@([^/?#]+)(?:/media)?/?$"
    test = (
        ("https://mastodon.social/@jk", {
            "pattern": r"https://files.mastodon.social/media_attachments"
                       r"/files/(\d+/){3,}original/\w+",
            "range": "1-60",
            "count": 60,
        }),
        ("https://pawoo.net/@yoru_nine/", {
            "range": "1-60",
            "count": 60,
        }),
        ("https://baraag.net/@pumpkinnsfw"),
    )

    def statuses(self):
        api = MastodonAPI(self)
        username = self.item
        handle = "@{}@{}".format(username, self.instance)
        for account in api.account_search(handle, 1):
            if account["username"] == username:
                break
        else:
            raise exception.NotFoundError("account")
        return api.account_statuses(account["id"])


class MastodonStatusExtractor(MastodonExtractor):
    """Extractor for images from a status"""
    subcategory = "status"
    pattern = BASE_PATTERN + r"/@[^/?#]+/(\d+)"
    test = (
        ("https://mastodon.social/@jk/103794036899778366", {
            "count": 4,
        }),
        ("https://pawoo.net/@yoru_nine/105038878897832922", {
            "content": "b52e807f8ab548d6f896b09218ece01eba83987a",
        }),
        ("https://baraag.net/@pumpkinnsfw/104364170556898443", {
            "content": "67748c1b828c58ad60d0fe5729b59fb29c872244",
        }),
    )

    def statuses(self):
        return (MastodonAPI(self).status(self.item),)


class MastodonAPI():
    """Minimal interface for the Mastodon API

    https://github.com/tootsuite/mastodon
    https://github.com/tootsuite/documentation/blob/master/Using-the-API/API.md
    """

    def __init__(self, extractor):
        self.root = extractor.root
        self.extractor = extractor

        access_token = extractor.config("access-token")
        if access_token is None or access_token == "cache":
            access_token = _access_token_cache(extractor.instance)
        if not access_token:
            try:
                access_token = INSTANCES[extractor.category]["access-token"]
            except (KeyError, TypeError):
                raise exception.StopExtraction(
                    "Missing access token.\n"
                    "Run 'gallery-dl oauth:mastodon:%s' to obtain one.",
                    extractor.instance)

        self.headers = {"Authorization": "Bearer " + access_token}

    def account_search(self, query, limit=40):
        """Search for content"""
        endpoint = "/v1/accounts/search"
        params = {"q": query, "limit": limit}
        return self._call(endpoint, params).json()

    def account_statuses(self, account_id):
        """Get an account's statuses"""
        endpoint = "/v1/accounts/{}/statuses".format(account_id)
        params = {"only_media": "1"}
        return self._pagination(endpoint, params)

    def status(self, status_id):
        """Fetch a status"""
        endpoint = "/v1/statuses/" + status_id
        return self._call(endpoint).json()

    def _call(self, endpoint, params=None):
        if endpoint.startswith("http"):
            url = endpoint
        else:
            url = self.root + "/api" + endpoint

        while True:
            response = self.extractor.request(
                url, params=params, headers=self.headers, fatal=None)
            code = response.status_code

            if code < 400:
                return response
            if code == 404:
                raise exception.NotFoundError()
            if code == 429:
                self.extractor.wait(until=text.parse_datetime(
                    response.headers["x-ratelimit-reset"],
                    "%Y-%m-%dT%H:%M:%S.%fZ",
                ))
                continue
            raise exception.StopExtraction(response.json().get("error"))

    def _pagination(self, endpoint, params):
        url = endpoint
        while url:
            response = self._call(url, params)
            yield from response.json()

            url = response.links.get("next")
            if not url:
                return
            url = url["url"]


@cache(maxage=100*365*24*3600, keyarg=0)
def _access_token_cache(instance):
    return None
