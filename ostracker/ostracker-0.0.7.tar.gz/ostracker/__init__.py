import os
import json
import time
import logging
import calendar
import datetime
import urllib.parse
import urllib.error
import urllib.request


LOGGER = logging.getLogger("ostracker")
TRACKER_URL = os.environ.get("TRACKER_URL", "https://ostracker.xyz")


def _poll_update(account, handle):
    params = urllib.parse.urlencode({
        "player": account,
        "start": handle["created_at"],
        "mode": handle["mode"],
    })
    req = urllib.request.Request(
        f"{TRACKER_URL}/api/v1/hiscores?{params}",
        headers={
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0",
        },
    )
    expires = datetime.datetime.utcfromtimestamp(handle["expires_at"])

    while datetime.datetime.utcnow() < expires:
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.load(resp)
            if data["hiscores"]:
                return data
            time.sleep(0.5)
        except Exception as err:
            LOGGER.debug("tracker error=%s", err)


def __update(account, mode, upsert):
    params = urllib.parse.urlencode({
        "player": account,
        "upsert": upsert,
        "mode": mode,
    })
    req = urllib.request.Request(
        f"{TRACKER_URL}/api/v1/hiscores?{params}",
        method="PUT",
        headers={
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as err:
        if err.code != 409:
            raise
        # Conflicts with a pending update -> use that as a handle
        return json.load(err)


def _update(account, mode, upsert):
    return _poll_update(account, __update(account, mode, upsert))


def _scores(account, mode, dt):
    params = {
        "player": account,
        "mode": mode,
    }

    if dt is not None:
        start_at = datetime.datetime.utcnow() + dt
        params["start"] = calendar.timegm(start_at.utctimetuple())

    q_str = urllib.parse.urlencode(params)
    req = urllib.request.Request(
        f"{TRACKER_URL}/api/v1/hiscores?{q_str}",
        headers={
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0",
        },
    )
    with urllib.request.urlopen(req, timeout=300) as resp:
        return json.load(resp)


def update(account, upsert=True):
    return _update(account, "main", upsert)


def update_leagues(account, upsert=True):
    return _update(account, "leagues", upsert)


def scores(account, dt=None):
    return _scores(account, "main", dt)


def scores_leagues(account, dt=None):
    return _scores(account, "leagues", dt)
