__author__ = "Ilya Baldin"
__version__ = "0.1"
__maintainer__ = "Ilya Baldin"

import hashlib, base64
from Crypto.PublicKey import RSA
import requests
import urllib3.exceptions

"""set of helper functions to interface with a SAFE server"""

SAFE_HTTP_POST_SUCCESS = 200
SAFE_RESULT_FIELD = "result"
SAFE_MESSAGE_FIELD = "message"
SAFE_SUCCESS = "succeed"

def hash_key(keyName):
    """ create a safe-compatible hash string of a public key file."""

    try:
        f = open(keyName, 'rb')
    except IOError:
        raise SafeException(f"Unable to read key file {keyName}")

    with f:
        try:
            r = RSA.importKey(f.read(), passphrase='')
        except:
            raise SafeException(f"Unable to parse key file: {keyName}")

        s = hashlib.sha256()
        s.update(r.exportKey(format='DER'))
        encoded = base64.urlsafe_b64encode(s.digest())

        return encoded.decode('utf-8')


def post_to_safe(*, headUrl, endpoint, principal, listOfParams):
    """ post a call to SAFE """
    params = {"principal": principal, "methodParams": listOfParams}
    #print(f"Parameters for {headUrl}{endpoint} are {params}")
    try:
        resp = requests.post(headUrl + endpoint, json=params)
    except Exception as e:
        raise SafeException(f"Connection error")

    if resp.status_code != SAFE_HTTP_POST_SUCCESS:
        raise SafeException(f"Unable to post due to error: {resp.status_code}")

    json = resp.json()
    if json[SAFE_RESULT_FIELD] != SAFE_SUCCESS:
        raise SafeException(f"POST failed due to error: {json[SAFE_MESSAGE_FIELD]}")
    return json[SAFE_MESSAGE_FIELD]

def post_raw_id_set(*, headUrl, principal):
    """ post a raw ID set of the principal """
    return post_to_safe(headUrl=headUrl, endpoint='postRawIdSet', principal=principal,
                      listOfParams=[principal])

def post_per_flow_rule(*, headUrl, principal, flowId):
    """ post a single per-workflow rule """
    return post_to_safe(headUrl=headUrl, endpoint='postPerFlowRule', principal=principal,
                      listOfParams=[flowId])

def post_two_flow_data_owner_policy(*, headUrl, principal, dataset, wf1, wf2):
    """ post a ruleset for two workflows associated with the dataset """
    return post_to_safe(headUrl=headUrl, endpoint='postTwoFlowDataOwnerPolicy', principal=principal,
                      listOfParams=[dataset, wf1, wf2])

class SafeException(Exception):
    """ SAFE-related exception. Behaves like Exception """
    pass