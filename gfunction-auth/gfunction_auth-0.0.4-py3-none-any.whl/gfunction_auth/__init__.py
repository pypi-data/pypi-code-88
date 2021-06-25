import requests
import google.auth.transport.requests
import google.oauth2.id_token

def _authorize(fn_url):
    auth_req = google.auth.transport.requests.Request()
    return google.oauth2.id_token.fetch_id_token(auth_req, fn_url)

def gfunction_post(fn_url, params):
    id_token = _authorize(fn_url)
    response = requests.post(fn_url, headers={'Authorization': f'Bearer {id_token}'}, json=params)
    return response

def gfunction_get(fn_url):
    id_token = _authorize(fn_url)
    response = requests.post(fn_url, headers={'Authorization': f'Bearer {id_token}'}, json=params)
    return response