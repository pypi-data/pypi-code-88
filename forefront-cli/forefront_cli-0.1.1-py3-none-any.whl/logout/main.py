import click
from PyInquirer import prompt
from prompt_toolkit.validation import Validator, ValidationError
from halo import Halo
import json
from ..common import bcolors, get_user_token, set_user_token, get_project_id, set_project_id
from ..api import API, fetch_projects, create_project


@click.group()
def logout():
    pass


@logout.command()
def logout():
    """Log out of Forefront CLI"""
    api = API()

    if api.key is None or api.key == '':
        print(bcolors.OKBLUE +
              'You are already logged out.' + bcolors.ENDC)
        return

    set_user_token('')
    print(bcolors.OKBLUE + 'Logged out' + bcolors.ENDC)
