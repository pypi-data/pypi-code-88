import requests
import google.auth.transport.requests
import google.oauth2.id_token

def gfunction_post(fn_url, params):
    auth_req = google.auth.transport.requests.Request()
    id_token = google.oauth2.id_token.fetch_id_token(auth_req, fn_url)
    response = requests.post(fn_url, headers={'Authorization': f'Bearer {id_token}'}, json=params)
    return response