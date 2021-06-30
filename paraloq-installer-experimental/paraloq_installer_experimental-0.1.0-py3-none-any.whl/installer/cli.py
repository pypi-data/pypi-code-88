import click
import requests
import json
import os
import datetime

from paraloq.installer import session
from paraloq.installer.prompt import ParaloqConfig


def _login(verbose: bool = True):

    paraloq_file = ParaloqConfig.from_disc()
    now = datetime.datetime.now().timestamp()
    valid_token = (float(paraloq_file.cached_bearer.get("expires_at", 0)) - now) > 0

    if not valid_token:
        session.Session.connect(stay_connected=False)
        paraloq_file.cached_bearer["bearer"] = session.Session._BEARER_
        paraloq_file.cached_bearer["expires_at"] = str(
            session.Session._SESSION_["expires_at"].timestamp()
        )
        paraloq_file.commit()

        if verbose:
            click.echo("Login successful")

    elif verbose:
        click.echo("You are already logged in")


def _logout(verbose: bool = True):

    paraloq_file = ParaloqConfig.from_disc()
    paraloq_file.cached_bearer = {}
    paraloq_file.commit()
    if verbose:
        click.echo("Logout successful")


@click.group("paraloq")
def paraloq():
    pass


@paraloq.command()
def login():
    _login(verbose=True)


@paraloq.command()
def logout():
    _logout(verbose=True)


@paraloq.command(
    context_settings=dict(
        ignore_unknown_options=True,
    )
)
@click.argument("name")
@click.argument("pip_args", nargs=-1, type=click.UNPROCESSED)
def install(name, pip_args):
    """Install paraloq modules from the paraloq package repository. PIP_ARGS will be forwarded to
    pip install"""
    # Login if necessary
    _login(verbose=False)
    # Prepare the arguments that will be forwarded to pip istall
    pip_args = " ".join(pip_args)

    paraloq_file = ParaloqConfig.from_disc()
    paraloq_file.api_url = "http://127.0.0.1:8000"

    token_response = requests.get(
        url=paraloq_file.api_url + "/v1/codeartifact/get-authentication-token",
        headers={
            "Authorization": "Bearer " + paraloq_file.cached_bearer["bearer"],
            "Content-Type": "application/json",
        },
    )

    token_response = json.loads(token_response.text)
    token = token_response["authorizationToken"]
    hive_account = token_response["hiveAccount"]
    repo_url = f"https://aws:{token}@paraloq-{hive_account}" \
               f".d.codeartifact.eu-central-1.amazonaws.com/pypi/paraloq/simple/"
    os.system(f"pip config set global.index-url {repo_url}")

    try:
        os.system(f"pip install paraloq-{name} {pip_args}")
    finally:
        os.system("pip config unset global.index-url")
