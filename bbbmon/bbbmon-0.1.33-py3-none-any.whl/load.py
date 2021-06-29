#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import re
import requests
from typing import Optional
from bbbmon.printing import eprint


LOAD_PATTERN = re.compile(r"(?!\d+\.\d+[\./])\d+\.\d+")

def read_load(read_load_from: Optional[str]) -> Optional[float]:
    """
    Read the load either from a file or a url depending on the input. Return None if anything fails.
    This matches all floats in the given file/url and returns the average
    """
    if read_load_from is None:
        return None

    text = ""
    if read_load_from.lower().startswith(("http")):
        try:
            r = requests.get(read_load_from, timeout=3)
            text = r.text
        except:
            eprint("Error: Ignored load - Couldn't read load from {}: Response was: {}".format(read_load_from, r))
            return None
    else:
        if os.path.isfile(read_load_from):
            with open(read_load_from, "r", encoding="utf-8") as f:
                text = f.read()
        else:
            eprint("Error: Ignored load - Couldn't read load from {}: Not a file or not readable".format(read_load_from))
            return None

    text = text.strip()

    if text == "":
        eprint("Error: Ignored load - Couldn't read load from {}: The file was empty".format(read_load_from))
        return None

    matches = re.findall(LOAD_PATTERN, text)

    if matches is None:
        eprint("Error: Ignored load - Couldn't read load from {}: No float values found".format(read_load_from))
        return None
    elif len(matches) == 0:
        eprint("Error: Ignored load - Couldn't read load from {}: No float values found".format(read_load_from))
        return None
    else:
        return sum([float(m) for m in matches]) / float(len(matches))