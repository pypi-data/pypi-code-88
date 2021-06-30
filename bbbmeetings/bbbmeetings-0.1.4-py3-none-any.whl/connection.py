#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime
from typing import NewType, Optional, Tuple, Iterable, List
import hashlib
import requests
import xmltodict

from bbbmeetings.types import *
import bbbmeetings as classes

def generate_checksum(call_name: str, query_string: str, secret: Secret) -> str:
    """
    Generate Checksum for the request header (passed as value for `?checksum=`)
    """
    m = hashlib.sha1()
    m.update(call_name.encode('utf-8'))
    m.update(query_string.encode('utf-8'))
    m.update(secret.encode('utf-8'))
    return m.hexdigest()


def send_request(bbb_url: Url, secret: Secret, call_name: str, query_string: str = "") -> Optional[CheckedResponse]:
    """
    Requests a certain call and query from the BBB-API. Returns None if anything fails or a checked OrderedDict otherwise
    """
    bbb_url = bbb_url.rstrip("/")
    checksum = generate_checksum(call_name, query_string, secret)
    url = "{}/bigbluebutton/api/{}?checksum={}".format(bbb_url, call_name, checksum)

    try:
        r = requests.get(url, timeout=3)
        if r.ok:
            d = xmltodict.parse(r.text)
            checked = clean_and_check_dict(d)
            return checked
        else:
            print(f"Request to Server failed with {r.status_code}")
            return None
    except requests.exceptions.Timeout as e:
        print(f"Request to Server timed out")
        # Offline Server!
        return None
    except:
        # Offline Server!
        return None


def clean_and_check_dict(d: UnparsedResponse) -> Optional[CheckedResponse]:
    """
    Checks if the response was a SUCCESS and returns the unpacked OrderedDict, None otherwise
    """
    if not "response" in d.keys():
        return None
    elif d["response"]["returncode"].upper() != "SUCCESS":
        return None
    return d["response"]


def get_meetings(bbb_url: Url, secret: Secret) -> List['Meeting']:
    checked_dict = send_request(bbb_url, secret, "getMeetings")
    if checked_dict is None:
        return []
    elif not "meetings" in checked_dict or checked_dict["meetings"] is None:
        return []
    else:
        meetings = []
        for d in checked_dict["meetings"].values():
            if isinstance(d, list):
                for x in d:
                    meetings.append(classes.Meeting.from_dict(x))
            else:
                meetings.append(classes.Meeting.from_dict(d))
        return meetings