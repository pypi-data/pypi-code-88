#!/usr/bin/python3
# @Time    : 2021-06-21
# @Author  : Kevin Kong (kfx2007@163.com)

import unittest
from unittest import TestCase, TestSuite
from dingtalk.dingtalk import DingTalk


class TestMessage(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.appkey = "dingtjjs1pr7nlgmtoxc"
        cls.appsecret = "8a6Ltc8_w-BNpqVOXg3dUH_1PHxxgmWnuf6Gt1ZcQqaMR3fYDDD6rs3Jnmzxr9uy"
        cls.agentid = 1218698174
        cls.dingtalk = DingTalk(cls.appkey, cls.appsecret, cls.agentid)

    def test_send_notication(self):
        res = self.dingtalk.message.send_notification(
            {"msgtype": "text", "text": {"content": "请提交日报。"}}, to_all_user=True)
        self.assertTrue

if __name__ == "__main__":
    unittest.main()
