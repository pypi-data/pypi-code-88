#!/usr/bin/python3
# @Time    : 2021-06-18
# @Author  : Kevin Kong (kfx2007@163.com)

from .core import Core
from .contact import Department, Role, User
from .message import Message


class DingTalk(object):

    def __init__(self,  appkey, appsecret, corpid=None, agentid=None, suitticket=None):
        """
        init dingtalk client

        params:
        corpid: Corpration Id
        appkey: app key
        appsecret: app secret
        suitticket: suit ticket from dingtalk when using third party app.
        """
        self._corpid = corpid
        self._appkey = appkey
        self._appsecret = appsecret
        self._suitticket = suitticket
        self._agentid = agentid

    core = Core()
    department = Department()
    role = Role()
    user = User()
    message = Message()

    # def _get_enterprise_access_token(self):
    #     """
    #     getting enterprise access token.
    #     url =
