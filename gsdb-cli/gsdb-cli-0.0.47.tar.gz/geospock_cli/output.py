# Copyright (c) 2014-2021 GeoSpock Ltd.

import requests
import click
import json
from http.client import responses
from .exceptions import CLIError


def output_response(response: requests.Response, expect_json):
    if response.status_code == 401:
        raise CLIError(responses[401] + " - {response_text}"
                       .format(response_text="Authentication failed"))
    if response.status_code == 404 and "<center>nginx</center>" in response.text:
        raise CLIError("This command is not available in the current GeoSpock DB deployment")
    elif response.status_code >= 300:
        message = response.text
        try:
            message = response.json()["message"]
        except json.JSONDecodeError:
            pass
        raise CLIError("{response_code} - {response_text}"
                       .format(response_code=responses[response.status_code], response_text=message))
    if expect_json:
        click.echo(json.dumps(response.json(), indent=2))
    else:
        standard_output = {"response": responses[response.status_code]}
        click.echo(json.dumps(standard_output, indent=2))
