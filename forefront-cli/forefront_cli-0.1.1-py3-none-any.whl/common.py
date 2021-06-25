import os
import json
import requests
import time
from pathlib import Path


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def set_user_token(token):
    path = os.path.join(Path.home(), '.forefront', 'creds')
    with open(path, 'w') as file:
        file.write(token)
        file.close()


def get_user_token():
    with open(os.path.join(Path.home(), '.forefront', 'creds'), 'r') as file:
        token = file.read().strip()
    return token


def set_project_id(project):
    with open(os.path.expanduser('~/.forefront/config'), 'w+') as file:
        file.write(f"project_id={project}")
        file.close()


def get_project_id():
    with open(os.path.expanduser('~/.forefront/config'), 'r') as file:
        project_id = file.read().strip().split('=')[1]
    return project_id
