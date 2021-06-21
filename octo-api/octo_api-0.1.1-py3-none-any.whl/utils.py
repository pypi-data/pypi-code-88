#!/usr/bin/env python3
#
#  utils.py
"""
Utility functions.
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
import sys
import textwrap
from typing import Any, Dict, NamedTuple, Optional, Type, Union

# 3rd party
import attr
import prettyprinter  # type: ignore
from domdf_python_tools.doctools import prettify_docstrings
from domdf_python_tools.stringlist import StringList
from enum_tools import StrEnum

__all__ = [
		"from_iso_zulu",
		"RateType",
		"Region",
		"MeterPointDetails",
		"add_repr",
		]

# stdlib
from datetime import datetime, timedelta, timezone

if sys.version_info[:2] < (3, 7):
	# 3rd party
	from backports.datetime_fromisoformat import MonkeyPatch  # nodep
	MonkeyPatch.patch_fromisoformat()

# def format_datetime(dt: datetime) -> str:
# 	"""
# 	Format a :class:`datetime.datetime` object to a string in
# 	:wikipedia:`ISO 8601` format.
#
# 	:param dt:
# 	"""
#
# 	return dt.strftime("%Y-%m-%dT:")


def from_iso_zulu(the_datetime: Union[str, datetime, None]) -> Optional[datetime]:
	"""
	Constructs a :class:`datetime.datetime` object from an
	`ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_ format string.

	This function understands the character ``Z`` as meaning Zulu time (GMT/UTC).

	:param the_datetime:
	"""  # noqa: D400

	if the_datetime is None:
		return the_datetime
	elif isinstance(the_datetime, datetime):
		return the_datetime
	else:
		return datetime.fromisoformat(  # type: ignore
				the_datetime.replace('Z', "+00:00"),
				)


class RateType(StrEnum):
	"""
	Enumeration of different rate types.
	"""

	StandingCharge = "standing-charges"
	StandardUnitRate = "standard-unit-rates"
	DayUnitRate = "day-unit-rates"
	NightUnitRate = "night-unit-rates"


class Region(StrEnum):
	"""
	Enumeration of different electricity supply regions.

	The different regions can be seen on the following map:

	.. image:: pes_boundaries.png
		:width: 300
		:alt: Electricity Regions
	"""

	Eastern = "_A"  # Eastern Electricity
	EastMidlands = "_B"  # East Midlands Electricity
	London = "_C"  # London Electricity
	Merseyside = "_D"  # Merseyside and North Wales Electricity Board
	NorthWales = "_D"  # Merseyside and North Wales Electricity Board
	Midlands = "_E"  # Midlands Electricity
	NorthEastern = "_F"  # North Eastern Electricity Board
	NorthWestern = "_G"  # North Western Electricity Board
	Southern = "_H"  # Southern Electric
	SouthEastern = "_J"  # South Eastern Electricity Board
	SouthWales = "_K"  # South Wales Electricity
	SouthWestern = "_L"  # South Western Electricity
	Yorkshire = "_M"  # Yorkshire Electricity
	SouthScotland = "_N"  # South of Scotland Electricity Board
	NorthScotland = "_P"  # North of Scotland Hydro Board


@prettify_docstrings
class MeterPointDetails(NamedTuple):
	"""
	Information about a meter point.

	:param mpan: The meter point access number.
	:param gsp: The grid supply point/region that the meter point is located in.
	:param profile_class: The profile class of the meter point.

	* **Profile Class 1** -- Domestic Unrestricted Customers
	* **Profile Class 2** -- Domestic Economy 7 Customers
	* **Profile Class 3** -- Non-Domestic Unrestricted Customers
	* **Profile Class 4** -- Non-Domestic Economy 7 Customers
	* **Profile Class 5** -- Non-Domestic Maximum Demand (MD) Customers with a Peak Load Factor (LF) of less than 20%
	* **Profile Class 6** -- Non-Domestic Maximum Demand Customers with a Peak Load Factor between 20% and 30%
	* **Profile Class 7** -- Non-Domestic Maximum Demand Customers with a Peak Load Factor between 30% and 40%
	* **Profile Class 8** -- Non-Domestic Maximum Demand Customers with a Peak Load Factor over 40%

	Information from https://www.elexon.co.uk/knowledgebase/profile-classes/

	.. seealso:: `Load Profiles and their use in Electricity Settlement <https://www.elexon.co.uk/documents/training-guidance/bsc-guidance-notes/load-profiles/>`_ by Elexon
	"""

	mpan: str
	gsp: Region
	profile_class: int

	@classmethod
	def _from_dict(cls, octopus_dict: Dict[str, Any]) -> "MeterPointDetails":
		return MeterPointDetails(
				mpan=str(octopus_dict["mpan"]),
				gsp=Region(octopus_dict["gsp"]),
				profile_class=int(octopus_dict["profile_class"]),
				)


#: The British Summer Time timezone (UTC+1).
bst = timezone(timedelta(seconds=3600))

#: The Greenwich Mean Time timezone (aka UTC).
gmt = timezone.utc

utc = gmt


def add_repr(cls: Type) -> Type:
	"""
	Add a pretty-printed ``__repr__`` function to the decorated attrs class.

	:param cls:

	.. seealso:: :func:`attr_utils.pprinter.pretty_repr`.
	"""

	if attr.has(cls):

		def __repr__(self) -> str:
			buf = StringList()
			buf.indent_type = "    "
			buf.append(f"{self.__class__.__module__}.{self.__class__.__qualname__}(")

			with buf.with_indent_size(1):
				for attrib in attr.fields(self.__class__):
					value = getattr(self, attrib.name)

					if isinstance(value, datetime):
						buf.append(f"{attrib.name}={value.isoformat()!r},")

					elif isinstance(value, str):
						lines = textwrap.wrap(value, width=80 - len(attrib.name) - 1)
						buf.append(f"{attrib.name}={lines.pop(0)!r}")

						for line in lines:
							buf.append(' ' * len(attrib.name) + ' ' + repr(line))

						buf[-1] = f"{buf[-1][len(buf.indent_type) * buf.indent_size:]},"
					elif value is None:
						buf.append(f"{attrib.name}=None,")
					else:
						buf.append(f"{attrib.name}={prettyprinter.pformat(value)},")

			buf.append(')')
			return str(buf)

		__repr__.__doc__ = f"Return a string representation of the :class:`~.{cls.__name__}`."

		cls.__repr__ = __repr__  # type: ignore
		cls.__repr__.__qualname__ = f"{cls.__name__}.__repr__"
		cls.__repr__.__module__ = cls.__module__

	return cls
