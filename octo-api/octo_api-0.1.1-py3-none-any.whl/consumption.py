#!/usr/bin/env python3
#
#  consumption.py
"""
Class to represent consumption data.
"""
#
#  Copyright © 2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#  DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
#  OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
#  OR OTHER DEALINGS IN THE SOFTWARE.
#

# stdlib
from datetime import datetime

# 3rd party
import attr
from attr_utils.serialise import serde
from domdf_python_tools.doctools import prettify_docstrings

# this package
from octo_api.utils import add_repr, from_iso_zulu

__all__ = ["Consumption"]


@serde
@add_repr
@prettify_docstrings
@attr.s(slots=True, frozen=True, repr=False)
class Consumption:
	"""
	Represents the consumption for a given period of time.
	"""

	#: The consumption.
	consumption: float = attr.ib()

	#: The start of the time period.
	interval_start: datetime = attr.ib(converter=from_iso_zulu)

	#: The end of the time period.
	interval_end: datetime = attr.ib(converter=from_iso_zulu)
