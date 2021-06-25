# -*-coding:utf-8 -*-

import requests
import json
import os
from logger import logger


def ding_talk_alert(msg, alert_to, level='P0', keyword=None, access_token=None):
    if not keyword:
        keyword = os.environ.get('DING_TALK_KEYWORD')
    if not access_token:
        access_token = os.environ.get('DING_TALK_TOKEN')
    user_dict = json.loads(os.environ.get('USER_PHONE_DICT'))
    data = {
        "msgtype": "markdown",
        "markdown": {
            "title": f"{keyword}",
            "text": f"# 【{keyword}】\n## 【告警级别】：{level}\n## 【内容】：{msg}\n## 【责任人】：@{user_dict.get(alert_to)}"
        },
        # "text": {
        #     "content": f"【{keyword}】：\n【告警级别】：{level}\n【内容】：{msg}\n【责任人】：{alert_to}"
        # },
        "at": {
            "atMobiles": [user_dict.get(alert_to)],
            "isAtAll": False,
        }
    }
    r = requests.request('POST', 'https://oapi.dingtalk.com/robot/send',
                         headers={'Content-Type': 'application/json'},
                         params={'access_token': access_token},
                         data=json.dumps(data)
                         )
    logger.info(f"send msg:{msg}, return:{r.text}")
