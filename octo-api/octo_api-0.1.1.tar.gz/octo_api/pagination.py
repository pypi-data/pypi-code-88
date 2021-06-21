#!/usr/bin/env python3
#
#  pagination.py
"""
Class for handling paginated API responses.
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
import re
from typing import Any, Dict, Iterable, Iterator, List, MutableMapping, Optional, Type, TypeVar, Union, overload
from urllib.parse import parse_qs, urlparse

# 3rd party
from apeye.slumber_url import SlumberURL
from domdf_python_tools.doctools import prettify_docstrings
from typing_extensions import TypedDict

__all__ = ["OctoResponse", "PaginatedResponse"]

_T = TypeVar("_T")


class OctoResponse(TypedDict):
	"""
	:class:`~typing.TypedDict` representing the raw JSON data returned by
	the Octopus Energy API.
	"""  # noqa: D400

	#: The total number of responses.
	count: int
	#: The URL of the next page of results.
	next: str  # noqa: A003  # pylint: disable=redefined-builtin
	#: The URL of the previous page of results.
	previous: str
	#: The current page of results.
	results: List[Dict[str, Any]]


@prettify_docstrings
class PaginatedResponse(Iterable[_T]):
	"""
	Represents a multi-page response from a REST API.

	The items within the response can be iterated over or accessed by their indices.
	The total number of items can be accessed with :func:`len(response) <len>`.

	:param query_url: The initial query URL.
	:param query_params: The parameters to the query.
	:param obj_type: The object to convert the response data to.

	.. note::

		This class assumes the JSON response is in the format used by
		`Django REST framework <https://www.django-rest-framework.org/>`_.

		The response should be in the following format:

		.. code-block:: json

			{
				"count": 1023,
				"next": "https://api.example.org/accounts/?page=5",
				"previous": "https://api.example.org/accounts/?page=3",
				"results": []
			}

		See https://www.django-rest-framework.org/api-guide/pagination/ for more information.
	"""

	_next_page: Optional[int]
	_previous_page: Optional[int]
	_results: List[Dict[str, Any]]

	def __init__(
			self,
			query_url: SlumberURL,
			query_params: Optional[MutableMapping[str, Any]] = None,
			obj_type: Type = dict,
			):

		response: OctoResponse = query_url.get(**query_params)  # type: ignore

		if query_params is None:
			query_params = {}

		self.query_url: SlumberURL = query_url
		self.query_params: Dict[str, Any] = dict(query_params)
		self.obj_type = obj_type

		self._count: int = response["count"]

		self._results = response["results"]

		self._next_page = None
		self._previous_page = None
		self._parse_pages(response)

	def _parse_pages(self, response: OctoResponse):
		if response["next"] is not None:
			query = parse_qs(urlparse(response["next"]).query)
			page = query.get("page", [])
			if page:
				self._next_page = int(page[0])
			else:
				self._next_page = None
		else:
			self._next_page = None

		if response["previous"] is not None:
			query = parse_qs(urlparse(response["previous"]).query)
			page = query.get("page", [])
			if page:
				self._previous_page = int(page[0])
			else:
				self._previous_page = None
		else:
			self._previous_page = None

	def _get_next_page(self):
		# print(f"Getting {self._next_page}")
		response: OctoResponse = self.query_url.get(  # type: ignore
				page=self._next_page,
				**self.query_params,
				)

		self._results.extend(response["results"])
		self._parse_pages(response)
		return response["results"]

	def __iter__(self) -> Iterator[_T]:
		"""
		Iterate over items in the :class:`~.PaginatedResponse`.
		"""

		for res in self._results:
			yield self.obj_type(**res)

		while self._next_page:
			for res in self._get_next_page():
				yield self.obj_type(**res)

	def __eq__(self, other) -> bool:
		if isinstance(other, Iterable):
			for left, right in zip(self, other):
				if left != right:
					return False
			return True

		return NotImplemented

	def __len__(self) -> int:
		"""
		Returns the number of items in the :class:`~.PaginatedResponse`.
		"""

		return self._count

	@overload
	def __getitem__(self, item: int) -> _T: ...  # pragma: no cover

	@overload
	def __getitem__(self, item: slice) -> List[_T]: ...  # pragma: no cover

	def __getitem__(self, item: Union[int, slice]) -> Union[_T, List[_T]]:
		"""
		Returns the item or items in the :class:`~.PaginatedResponse`, as given by the index or slice.

		:param item:
		"""

		if isinstance(item, int):
			if item >= len(self):
				raise IndexError("index out of range")
			else:
				while item >= len(self._results):
					# print(item, len(self._results))
					self._get_next_page()

				return self.obj_type(**self._results[item])

		elif isinstance(item, slice):
			max_idx = item.stop + 1
			if max_idx >= len(self):
				max_idx = len(self)
			return [self[idx] for idx in range(item.start or 0, max_idx, item.step or 1)]

		else:
			return NotImplemented
