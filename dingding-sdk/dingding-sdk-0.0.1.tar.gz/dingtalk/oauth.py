#!/usr/bin/python3
# @Time    : 2021-06-22
# @Author  : Kevin Kong (kfx2007@163.com)

from .core import Core, URL


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

    def get_app_manager(self,code):
        """
        get app manager info.

        :param code: authorized code.

        :return userinfo and corpinfo: {'user_info':{},'corp_info':{}}
        """
        url = f"{URL}/sso/getuserinfo"
        data ={'code': code}
        res = self._post(url,data)
        return res['user_info'], res['corp_info']
