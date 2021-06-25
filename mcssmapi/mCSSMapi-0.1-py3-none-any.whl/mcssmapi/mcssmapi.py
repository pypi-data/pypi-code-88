"""
Class for access to Cisco Smart Account Licensing API 

Required:
requests

Version: 0.1

"""

import requests
import json

from requests.models import HTTPError

class Licensing(object):
    def __init__(self, client_id, client_secret, disable_warnings=False, timeout=5):
        """
        Class to manage CSSM via the REST API
        :param client_id: Smart Account API Client ID
        :param client_secret: Smart Account API Client Secret Key
        :param disable_warnings: Disable SSL warnings
        :param timeout: Request timeout value
        """
        self.client_id = client_id
        self.client_secret = client_secret

        self.url_login = 'https://cloudsso.cisco.com/as/token.oauth2'
        self.login_headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
            }
        self.login_body = f'grant_type=client_credentials&client_id={self.client_id}&client_secret={self.client_secret}'
        self.session = requests.session()
        self.disable_warnings = disable_warnings
        self.timeout = timeout
        
        self.oAuthToken = ''
        self.session.headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + self.oAuthToken,
                'Cache-Control': 'no-cache'
            }
        

        if self.disable_warnings:
            requests.packages.urllib3.disable_warnings()

    def bearer_update(self):
        """
        Method to update login token
        """
        result = {
            'success': False,
            'response': '',
            'error': ''
        }
        resp = requests.request('POST',self.url_login,data=self.login_body,headers=self.login_headers)
        j_resp = resp.json()
        result['response'] = j_resp
        if resp.status_code == 200:
            self.oAuthToken = j_resp['access_token']
            self.session.headers.update({'Authorization': 'Bearer ' + self.oAuthToken})
            result['success'] = True
            result['error'] = False

        else:
            result['success'] = False
            result['error'] = resp.status_code
        # print(json.dumps(result,indent=2))
        return result

    def send_json_request_cssm(self, url, body, method='POST'):
        """
        Method to send json request to CSSM
        :param url: URL of CSSM request
        :param body: Body of CSSM request
        :param method: POST or GET request method (optional)(default: POST)
        """
        result = {
            'success': False,
            'response': '',
            'error': ''
        }
        # print(url)
        # print(self.session.headers)
        # print(body)
        json_body = json.dumps(body)
        # resp = self.session.post(url,data=json_body)
        resp = self.session.request(method,url,json=json_body)
        result['response'] = resp.json()
        if resp.status_code == 200:
            result['success'] = True
            result['error'] = False
        else:
            result['success'] = False
            result['error'] = resp.status_code
        # print(result)
        return result

    def reserve_license(self, sadomain, va, reservationcode, licenses):
        """
        Reserce SLR license
        :param sadomain: Smart Account name
        :param va: Virtual Account name
        :param reservationcode: Reservation code from device
        :param licenses: list of licenses in specific format. Examle:
            [
                {
                    "quantity" : 1,
                    "entitlementTag" : "regid.2018-05.com.cisco.C9200L-DNA-E-48,1.0_e213fd3f-18f9-4940-a21c-617b92efdaae"
                },
                {
                    "quantity" : 1,
                    "entitlementTag" : "regid.2018-05.com.cisco.C9200L-NW-E-48,1.0_52d2a0bd-de8a-480f-b70b-1d57e7738aec"
                },
            ]
        """
        url = f"https://swapi.cisco.com/services/api/smart-accounts-and-licensing/v2/accounts/{sadomain}/virtual-accounts/{va}/reserve-licenses"
        payloadlicenses = []
        for license in licenses:
            lic = {
            'entitlementTag': license['entitlementTag'],
            'quantity': license['quantity'],
            'precedence': 'LONGEST_TERM_FIRST'
            }
            payloadlicenses.append(lic)
        
        payload = {
            'reservationRequests': [
                {
                'licenses': payloadlicenses,
                'reservationCode': reservationcode,
                'reservationType': 'SPECIFIC'
                }
            ]
        }
        res = self.send_json_request_cssm(url,payload)
        # if res['success']:
        #     reserved_licenses = res['response']
        # else:
        #     reserved_licenses = False
        return res

    def smart_license_usage(self, sadomain, limit=50, offset=0,*va):
        """
        Get Smart license usage
        :param sadomain: Smart Account domain name
        :param limit: limit licenses per connection (as pagination)
        :param offset: offset from which license usage is getting (as start page)
        :param *va: Virtual Account names
        """
        url = f"https://swapi.cisco.com//services/api/smart-accounts-and-licensing/v1/accounts/{sadomain}/licenses"
        virtualaccounts = []
        for account in va:
            virtualaccounts.append(account)
        payload = {
                'virtualAccounts': virtualaccounts,
                'limit': limit,
                'offset': offset
                }

        res = self.send_json_request_cssm(url,payload)
        
        # if res['success']:
        #     usage = res['response']
        # else:
        #     usage = False
        return res