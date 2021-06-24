from yarl import URL
import json
from aiohttp.web import Request
from typing import Union, Mapping, Any, Dict, List
import abc


class Representor(abc.ABC):
    """
    Abstract base class for formatting WeSTL documents into a response body and parsing an HTTP request body into a
    name-value pair JSON dict.
    """
    MIME_TYPE: str = ''

    @abc.abstractmethod
    async def formats(self, request: Request, wstl_obj: Union[List[Dict[str, Any]], Dict[str, Any]], dumps=json.dumps) -> bytes:
        """
        Formats a run-time WeSTL document into a response body.

        :param request: the HTTP request.
        :param wstl_obj: dict with run-time WeSTL JSON, or a list of run-time WeSTL JSON dicts.
        :param dumps: any callable that accepts dict with JSON and outputs str. Cannot be None.
        :return: a bytes containing the formatted data.
        """
        pass

    @abc.abstractmethod
    async def parse(self, request: Request) -> Mapping[str, Any]:
        """
        Parses an HTTP request body into a name-value pair dict-like object.

        :param request: the HTTP request. Cannot be None.
        :return: a name-value pair dict-like object.
        """
        pass

