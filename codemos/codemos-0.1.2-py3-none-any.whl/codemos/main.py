from os import environ
from sys import argv, exit
import os.path as op
import shutil

import requests
from uvicorn import run as uvicorn_run
from appdirs import user_config_dir
from urllib.parse import urlencode
from dotenv import dotenv_values

from starlette.responses import RedirectResponse
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.logger import logger

PROJECT_NAME = 'codemos'
PROJECT_DIR = op.dirname(op.dirname(op.abspath(__file__)))
DEFAULT_CONFIG_FILE = op.join(PROJECT_DIR, 'env.dist')

GITHUB_AUTHORIZE_URL = 'https://github.com/login/oauth/authorize'
GITHUB_ACCESS_TOKEN_URL = 'https://github.com/login/oauth/access_token'

config = {
    **dotenv_values(DEFAULT_CONFIG_FILE), # load default config
    **dotenv_values(user_config_dir(PROJECT_NAME)),  # override with user config
    **dotenv_values(op.join(PROJECT_DIR, 'env')),  # override with local config
    **environ  # override with environment variables
}

print('Config:')
for key, value in config.items():
    print('- %s: %s' % (key, value))

app = FastAPI()
# templates = Jinja2Templates(directory='templates')
app.mount('/static', StaticFiles(directory='static'), name='static')

@app.get('/', response_class=HTMLResponse)
def index(request: Request):
    return RedirectResponse(url='/static/index.html')

@app.get('/gh_auth')
def gh_auth(code: str) -> str:
    params = {
        'client_id': config['GH_CLIENT_ID'],
        'client_secret': config['GH_CLIENT_SECRET'],
        'code': code,
        'redirect_uri': config['GH_REDIRECT_URI']
    }
    headers = {
        'Accept': 'application/json'
    }
    # response: {'access_token': '...', 'token_type': 'bearer', 'scope': 'read:user'}
    return requests.post(GITHUB_ACCESS_TOKEN_URL, headers=headers, data=params).json()

@app.get('/gh_user')
def gh_user(token: str) -> str:
    USER_INFO_API_ENDPOINT = 'https://api.github.com/user'
    headers = {
        'Accept': 'application/json',
        'Authorization': 'token %s' % token
    }

    return requests.get(USER_INFO_API_ENDPOINT, headers=headers).json()['name']

def run():
    if len(argv) == 2 and argv[1] == 'init' and not op.isfile(user_config_dir(PROJECT_NAME)):
        shutil.copyfile(DEFAULT_CONFIG_FILE , user_config_dir(PROJECT_NAME))
        exit(0)

    uvicorn_run('codemos.main:app', host=config['UVICORN_HOST'], port=int(config['UVICORN_PORT']), log_level=config['UVICORN_LOG_LEVEL'])

if __name__ == '__main__':
    run()
