# coding: utf-8

# Copyright 2021 IBM All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import requests
import urllib3
from ibm_cloud_sdk_core.authenticators import BearerTokenAuthenticator
from http import HTTPStatus

def get_iamtoken(url, username, password):
    fqdn = urllib3.util.parse_url(url).netloc
    domain = '.'.join(fqdn.split('.')[1:])
    token_url = 'https://cp-console.{}/idprovider/v1/auth/identitytoken'.format(domain)
    data = {
        'grant_type': 'password',
        'username': username,
        'password': password,
        'scope': 'openid'
    }
    return requests.post(token_url, data, verify=False)

def get_accesstoken(url, username, iamtoken):
    url = '{}/v1/preauth/validateAuth'.format(url)
    headers = {
        'Content-type': 'application/json',
        'username': username,
        'iam-token': iamtoken
    }
    return requests.get(url, headers=headers, verify=False)

def get_bearer_authenticator(url, username, password):
    iamtoken = get_iamtoken(url,username,password).json()['access_token']
    access_token = get_accesstoken(url,username, iamtoken).json()['accessToken']
    return BearerTokenAuthenticator(bearer_token=access_token)

def get_access_token(url, username, password):
    response = get_iamtoken(url,username,password)
    #service is not available when iamintegration=false so fall back to old way of generating code
    if response.status_code==HTTPStatus.SERVICE_UNAVAILABLE:
        url = '{}/v1/preauth/validateAuth'.format(url)
        headers = {'Content-type': 'application/json'}
        data = {
            'grant_type': 'password',
            'username': username,
            'password': password
        }
        return requests.get(url, headers=headers, auth= (username,password),verify=False).json()['accessToken']
        
    else:
        return get_accesstoken(url,username, response.json()['access_token']).json()['accessToken']
        