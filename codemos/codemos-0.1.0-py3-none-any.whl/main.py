import os

import requests
from urllib.parse import urlencode
from dotenv import load_dotenv

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from starlette.responses import RedirectResponse

GITHUB_AUTHORIZE_URL = 'https://github.com/login/oauth/authorize'
GITHUB_ACCESS_TOKEN_URL = 'https://github.com/login/oauth/access_token'

load_dotenv()
app = FastAPI()
templates = Jinja2Templates(directory='templates')

@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    print('index')
    return templates.TemplateResponse('index.html', {'request': request})

@app.get('/auth')
async def auth():
    print('auth')
    params = {
        'client_id': os.getenv('GH_CLIENT_ID'),
        'redirect_uri': os.getenv('GH_REDIRECT_URI'),
        'scope': 'read:user', # write:repo_hook?
        'state': 'unguessable random string'
    }
    return RedirectResponse(url='%s?%s' % (GITHUB_AUTHORIZE_URL, urlencode(params)))

@app.get('/login')
async def login(request: Request, code: str = '', state: str = '',
                error: str = '', error_description: str = ''):
    if error:
        print("error %{error}: %{error_description}")
        return RedirectResponse(app.url_path_for('index'))

    USER_INFO_API_ENDPOINT = 'https://api.github.com/user'
    headers = {
        'Accept': 'application/json',
        'Authorization': 'token %s' % get_token(code)
    }

    response = requests.get(USER_INFO_API_ENDPOINT, headers=headers).json()
    return templates.TemplateResponse('index.html', {'request': request, 'name': response['name']})

def get_token(code: str) -> str:
    params = {
        'client_id': os.getenv('GH_CLIENT_ID'),
        'client_secret': os.getenv('GH_CLIENT_SECRET'),
        'code': code,
        'redirect_uri': os.getenv('GH_REDIRECT_URI')
    }
    headers = {
        'Accept': 'application/json'
    }
    response = requests.post(GITHUB_ACCESS_TOKEN_URL, headers=headers, data=params).json()
    # {'access_token': '...', 'token_type': 'bearer', 'scope': 'read:user'}

    return response['access_token']
