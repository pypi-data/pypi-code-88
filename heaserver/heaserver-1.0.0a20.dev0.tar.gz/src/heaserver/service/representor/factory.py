"""
A factory for getting a representor object from the heaserver.service.representor package for a provided mimetype. A
representor formats WeSTL documents into one of various output formats, and it may provide for parsing data represented
in the format into name-value pair (NVP) JSON. Supported mimetypes are application/vnd.wstl+json (WeSTL),
application/json (name-value pair JSON), and application/vnd.collection+json (Collection+JSON).
"""
from . import wstljson, nvpjson, cj, xwwwformurlencoded, representor
from accept_types import get_best_match
from typing import Optional, Mapping, Type


# Priority-ordered mapping of mime types to representor implementation. The priority ordering is used by
# get_from_accepts_header() to select a representor when multiple candidate mime types are found in the Accepts header.
# Python dicts have guaranteed insertion order since version 3.7.
_mime_type_to_representor: Mapping[str, Type[representor.Representor]] = {
    cj.MIME_TYPE: cj.CJ,
    wstljson.MIME_TYPE: wstljson.WeSTLJSON,
    nvpjson.MIME_TYPE: nvpjson.NVPJSON,
    xwwwformurlencoded.MIME_TYPE: xwwwformurlencoded.XWWWFormURLEncoded
}


DEFAULT_REPRESENTOR: Type[representor.Representor] = next(iter(_mime_type_to_representor.values()))


def from_accepts_header(accepts: Optional[str]) -> representor.Representor:
    """
    Selects a representor from the contents of a HTTP Accepts header.

    :param accepts: an Accepts header string.
    :return: An object that implements the representor interface, described in the heaserver.service.representor
    package documentation. It will return a representor for Collection+JSON if the provided mimetype is None or unknown.
    """
    if not accepts:
        return DEFAULT_REPRESENTOR()
    result = get_best_match(accepts.lower(), _mime_type_to_representor.keys())
    return _mime_type_to_representor.get(result, DEFAULT_REPRESENTOR)()


def from_content_type_header(content_type: Optional[str]) -> representor.Representor:
    """
    Selects a representor from the contents of a HTTP Content-Type header.

    :param content_type: the Content-Type header string.
    :return: An object that implements the representor interface, described in the heaserver.service.representor
    package documentation. It will return a representor for Collection+JSON if the provided mimetype is None or unknown.
    """
    if not content_type:
        return DEFAULT_REPRESENTOR()
    return _mime_type_to_representor.get(content_type.split(';')[0].strip().lower(), DEFAULT_REPRESENTOR)()
