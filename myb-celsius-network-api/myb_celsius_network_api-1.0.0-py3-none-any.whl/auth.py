import json, hmac, hashlib, time, requests, base64
from requests.auth import AuthBase

# Create custom authentication for Exchange
class CelsiusNetworkAuth(AuthBase):
    def __init__(self, celsius_partner_token, user_api_key):
        self.celsius_partner_token = celsius_partner_token
        self.user_api_key = user_api_key

    def __call__(self, request):
        request.headers.update({
            'X-Cel-Partner-Token': self.celsius_partner_token,
            'X-Cel-Api-Key': self.user_api_key,
            'Content-Type': 'application/json'
        })
        return request
