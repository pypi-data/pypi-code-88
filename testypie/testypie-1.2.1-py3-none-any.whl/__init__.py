import hashlib
import logging
import os
import sys
from typing import Dict
from urllib.parse import quote

import requests
import yaml
from clize import run
from flask import Flask, Response, request
from httplib2 import iri2uri
from werkzeug.datastructures import EnvironHeaders

app = Flask(__name__)


BASEDIR = "fixtures"


def url_to_filename(url):
    return quote(iri2uri(url), safe="") + ".yaml"


class literal(str):
    pass


def literal_presenter(dumper, data):
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")


yaml.add_representer(literal, literal_presenter)


class Cache:
    def __init__(self, basedir):
        self.basedir = basedir

    def __contains__(self, item):
        filename = os.path.join(self.basedir, url_to_filename(item))
        return os.path.exists(filename)

    def __setitem__(self, key, value):
        filename = os.path.join(self.basedir, url_to_filename(key))

        if not os.path.exists(os.path.dirname(filename)):
            os.makedirs(os.path.dirname(filename))

        with open(filename, "w") as cache_file:
            value["body"] = literal(value["body"])
            if "request_body" in value:
                value["request_body"] = literal(value["request_body"])

            yaml.dump(value, cache_file, default_flow_style=False)
            logging.info("Wrote to: {}", filename)

    def __getitem__(self, item):
        filename = os.path.join(self.basedir, url_to_filename(item))

        with open(filename) as cache_file:
            print(f"Writing to {filename}", file=sys.stderr)
            value = yaml.safe_load(cache_file)

        return value


def create_incoming_headers(upstream_response):
    server_headers = {}
    for wanted_header in {"Content-Type", "Location", "Server"}:
        if wanted_header in upstream_response.headers:
            server_headers[wanted_header] = upstream_response.headers[
                wanted_header
            ]
    return server_headers


def create_outgoing_headers(headers: EnvironHeaders):
    client_headers = {}
    for wanted_header in {
        "Accept",
        "Content-Type",
        "X-Amz-Date",
        "X-Amz-Security-Token",
        "User-Agent",
        "Content-Length",
        "Authorization",
    }:
        if wanted_header in headers:
            client_headers[wanted_header] = headers[wanted_header]
    return client_headers


CACHE = Cache(BASEDIR)
HTTP = requests.Session()


def get_response(
    url: str, headers: EnvironHeaders, method: str = "get", body: str = None
) -> Dict:

    cache_key = f"{method.upper()}-{url}"
    if body:
        cache_key += "-" + hashlib.md5(body.encode("utf-8")).hexdigest()

    if cache_key not in CACHE:
        # Use requests to fetch the upstream URL the client wants
        outgoing_headers = create_outgoing_headers(headers)

        upstream = HTTP.request(
            method,
            url,
            allow_redirects=False,
            headers=outgoing_headers,
            data=body,
        )

        response_headers = create_incoming_headers(upstream)
        response = dict(
            code=upstream.status_code,
            body=upstream.content.decode("utf-8"),
            headers=response_headers,
        )

        if body:
            response["request_body"] = body.encode("utf-8")

        CACHE[cache_key] = response

    return CACHE[cache_key]


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def proxy(_path: str) -> Response:
    response = get_response(
        request.url, request.headers, method=request.method
    )
    return Response(
        response=response["body"].encode("utf-8"),
        status=response["code"],
        headers=response["headers"],
    )


def run_app(host=None, port=None):
    app.run(host=host, port=port)


def cli():
    run(run_app)


if __name__ == "__main__":
    cli()
