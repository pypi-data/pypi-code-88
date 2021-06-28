
import os
import sys
import requests
import json
import pyotp

class Login:

    def get_login_headers(self, ydata):
        headers = ydata['headers']
        headers['Referer'] = ydata['url'] + "/user/login"
        headers['Origin'] = ydata['url']
        headers['Host'] = ydata['url'].split('//')[1]
        return headers

    def login(self, url, secret, username, password, headers):
        url = url + '/auth/verify-user'
        totp = pyotp.TOTP(secret).now()
        post_payload = {
            'args': '{"type":"oath","username":"'+username+'","password":"'+password+'","captcha":"","oath":"'+totp+'","remember":false}'
        }
        re = requests.post(url, data=post_payload, headers=headers)
        if re.json()['code']==0:
            return re.cookies.get_dict()['_sid']
        else:
            print(re.json()['message'], ': login err!')
            sys.exit()
