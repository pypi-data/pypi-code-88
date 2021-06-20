# This file is part of pybib2web, a translator of BibTeX to HTML.
# https://gitlab.com/sosy-lab/software/pybib2web
#
# SPDX-FileCopyrightText: 2021 Dirk Beyer <https://www.sosy-lab.org>
#
# SPDX-License-Identifier: Apache-2.0

"""Module for parsing config.yml"""

import yaml
from datetime import datetime
from typing import Optional
from . import util


class Config:
    def __init__(self, config_dict):
        self._authors_to_index = [
            util.get_shortform(a) for a in config_dict.pop("authors_to_be_indexed", [])
        ]

        self._tail = config_dict.pop("tail", "")

        if config_dict:
            raise ValueError(f"Unused configuration option(s): {config_dict.keys()}")

    def index_author(self, author):
        return (
            not self._authors_to_index
            or util.get_shortform(author) in self._authors_to_index
        )

    @property
    def tail(self):
        return self._tail.format(timestamp=self._get_timestamp())

    def _get_timestamp(self):
        return datetime.now().strftime(r"%a %b %d %H:%M:%S %Y")


def parse(config_file: Optional[str]) -> Config:
    if config_file is None:
        return Config({})

    with open(config_file) as inp:
        return Config(yaml.safe_load(inp))
