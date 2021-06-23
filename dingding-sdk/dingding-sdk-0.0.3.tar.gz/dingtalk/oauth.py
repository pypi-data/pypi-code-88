#!/usr/bin/python3
# @Time    : 2021-06-22
# @Author  : Kevin Kong (kfx2007@163.com)

from .core import Core, URL
import time
import requests
from dingtalk.exceptions import DingTalkException
import logging
from hmac import HMAC
from hashlib import sha256
from base64 import b64encode

_logger = logging.getLogger(__name__)


class Oauth(Core):

    def get_userinfo(self, code):
        """
        get user info via qrcode.

        :param code: authorized code.

        :return userinofo: object.
        """

        url = f"{URL}/topapi/v2/user/getuserinfo"
        data = {'code': code}
        res = self._post(url, data)
        return res['result']

    def get_app_manager(self, code):
        """
        get app manager info.

        :param code: authorized code.

        :return userinfo and corpinfo: {'user_info':{},'corp_info':{}}
        """
        url = f"{URL}/sso/getuserinfo"
        data = {'code': code}
        res = self._post(url, data)
        return res['user_info'], res['corp_info']


class AppOauth(object):

    def __init__(self, appid, appsecret):
        """
        setting scan loging app id & secret

        :param appid: appid
        :param appsecret: appsecret

        :return result：None
        """
        self.appid = appid
        self.appsecret = appsecret

    def _sign_request(self, appsecret, timestamp):
        """
        compute signature for third app request.
        """
        signstring = f"{timestamp}\n{self._suitticket}"
        return b64encode(HMAC(appsecret, signstring, sha256).digest())

    def get_userinfo_by_code(self, code):
        """
        get user's info by code.

        :param code: authorized code.

        :return tmp_auth_code: temp auth code
        """
        url = f"{URL}/sns/getuserinfo_bycode"
        timestamp = int(time.time())
        data = {
            "accessKey": self.appid,
            "timestamp": timestamp,
            "signature": self._sign_request(self.appsecret, timestamp),
            "tmp_auth_code": code
        }
        try:
            res = requests.post(url, json=data).json()
            return res['user_info']
        except DingTalkException(res):
            _logger.error(f"[DingTallk] get userinfo by code error:{res}")
