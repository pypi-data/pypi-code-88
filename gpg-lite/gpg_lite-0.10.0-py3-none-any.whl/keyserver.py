import re
from typing import (
    Optional,
    Tuple,
    Iterator,
    IO,
    ContextManager,
)
from urllib.error import HTTPError
from urllib.parse import unquote, quote
import urllib.request

from .model import KeyInfo, Uid


def parse_search_keyserver(source: IO[bytes]) -> Iterator[KeyInfo]:
    """Extract key information (fingerprint, user ID) from the string returned
    by a search request made via the OpenPGP HTTP Keyserver Protocol. See
    https://tools.ietf.org/html/draft-shaw-openpgp-hkp-00 for details.

    Example of keyserver response to key index search:
    info:1:1
    pub:AA1020B5F0F873830B9AF245AA2BB155CF133521:1:4096:1593675716::
    uid:Alice Smith <alice.smith@example.com>:1593675716::
    """
    try:
        b_line = next(source).rstrip(b"\r\n")
    except StopIteration:
        return
    if not b_line.startswith(b"info:"):
        raise ValueError(
            "Unknown response format from gpg, starting with\n"
            + b_line.decode("utf-8", "replace")
        )
    for b_line in source:
        line = b_line.decode("utf-8", "replace").rstrip("\r\n")
        if not line:
            continue
        try:
            (
                hdr_key,
                fingerprint,
                algorithm,
                key_length,
                creation_date,
                expiration_date,
                _,
            ) = line.split(":")
        except ValueError as e:
            raise ValueError(f"Wrong format for search_key: {line}") from e
        try:
            hdr_uid, uid, _, _, _ = (
                next(source).decode("utf-8", "replace").rstrip("\n").split(":")
            )
        except StopIteration as e:
            raise ValueError("Unexpected end of source. Expected 'uid:' line") from e
        if hdr_key != "pub":
            raise ValueError(
                f"Unknown response format from gpg: "
                f"expected 'pub:', got '{hdr_key}'"
            )
        if hdr_uid != "uid":
            raise ValueError(
                f"Unknown response format from gpg: "
                f"expected 'uid:', got '{hdr_uid}'"
            )

        yield KeyInfo(
            uid=Uid.from_str(unquote(uid)),
            fingerprint=fingerprint,
            key_algorithm=int(algorithm),
            creation_date=creation_date,
            expiration_date=expiration_date or None,
            key_length=int(key_length),
        )


def normalize_fingerprint(fp: str):
    valid_len = (8, 16, 32, 40)
    s = re.sub(r"^0[xX]", "", re.sub(r"\s", "", fp))
    if len(s) not in valid_len:
        raise ValueError(f"Invalid fingerprint length. Allowed lengths {valid_len}")
    try:
        int(s, 16)
    except ValueError as e:
        raise ValueError(
            "Fingerprint contains invalid characters. Allowed characters: 0-9A-Fa-f"
        ) from e
    return f"0x{s}"


def search_keyserver(
    search_term: str, keyserver: str, url_opener=urllib.request.urlopen
) -> Iterator[KeyInfo]:
    """Search for a key on a keyserver supporting the OpenPGP HTTP Keyserver
    Protocol, e.g. an SKS keyserver.

    :param search_term: search term. This can be either a key fingerprint,
        key ID or part of the key user ID (e.g. email address).
    :param keyserver: URL of keyserver where to search for keys.
    :param url_opener: function/wrapper through which to make the http request.
    :return: key information summary.
    :raises HTTPError: raises error if the request to the keyserver fails
        for a reason different than 404 (requested resource not found but
        connection to keyserver could be made).
    """
    try:
        queries = {normalize_fingerprint(search_term), search_term}
    except ValueError:
        queries = {search_term}
    for query in queries:
        try:
            with query_keyserver(
                keyserver=keyserver, query=query, op="index", url_opener=url_opener
            ) as response:
                yield from parse_search_keyserver(response)
        except HTTPError as e:
            if e.code != 404:
                raise e


def download_key(fingerprint: str, keyserver: str, **kwargs) -> ContextManager:
    """Download key from keyserver to a user's local keyring. Keys can only
    be retrieved via their fingerprint, or key ID. It is recommended to use
    full fingerprints (40 chars hexadecimal string) to avoid key collisions.

    :param fingerprint: fingerprint (40 chars) or key ID (8, 16 or 32 chars) of
        the key to download.
    :param keyserver: URL of keyserver from where to download keys.
    :param kwargs:
    :return: urlopen context manager containing the downloaded PGP key.
    """
    return query_keyserver(
        keyserver=keyserver,
        query=normalize_fingerprint(fingerprint),
        op="get",
        exact="on",
        **kwargs,
    )


def query_keyserver(
    keyserver: str, query: str, op: str, url_opener=urllib.request.urlopen, **parameters
) -> ContextManager:
    """Send a request to a keyserver supporting the OpenPGP HTTP Keyserver
    Protocol, e.g. to download a key or retrieve information about a key.

    :param keyserver: URL of keyserver to query.
    :param query: search/query term, e.g. a normalized fingerprint or email
        address.
    :param op: operation type to perfrom, e.g. "index" to list keys or "get"
        to download keys.
    :param url_opener: function/wrapper through which to make the http request.
    :param parameters: optional arguments to pass to
    :return: urlopen context manager containing the data returned by the query
        made to the keyserver.
    """
    url = build_host(keyserver)
    query_url = f"{url}/pks/lookup?search={quote(query)}&op={op}&options=mr" + "".join(
        f"?{key}={val}" for key, val in parameters.items()
    )
    return url_opener(query_url)


def split_host(url: str) -> Tuple[Optional[str], str, Optional[str]]:
    match = re.fullmatch(r"(https?://|hkp://)?([^:]+)(:[0-9]+)?", url)
    if not match:
        raise ValueError(f"Invalid URL: {url}")
    scheme, host, port = match.groups()
    return scheme, host, port


def build_host(url: str) -> str:
    scheme, host, port = split_host(url)
    if scheme not in {"http://", "https://"}:
        if port in {":80", ":8080", ":11371"}:
            scheme = "http://"
        else:
            scheme = "https://"
    if port is None:
        if scheme == "https://":
            port = ":443"
        else:
            port = ":80"
    return scheme + host + port


default_opener = urllib.request.build_opener(
    urllib.request.HTTPSHandler(debuglevel=0)
).open


def post(url, data, url_opener=default_opener):
    request = urllib.request.Request(
        url,
        data,
        method="POST",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    with url_opener(request) as response:
        response_text = response.read()
        return response_text
