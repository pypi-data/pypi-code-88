from logzero import logger
import json
import requests
from http.server import BaseHTTPRequestHandler, HTTPServer
from os import path
import json

from urllib import request, parse


class FeishuSender:
    """
    https://open.feishu.cn/document/ukTMukTMukTM/uMDMxEjLzATMx4yMwETM
   https://getfeishu.cn/hc/zh-cn/articles/360024984973-在群聊中使用机器人
    """
    def __init__(self, app_id: str,secret_key):
        # 飞书机器人的密钥配置
        self._app_id = app_id
        self._secret_key = secret_key

        logger.info('FeishuSender|object init done')

    def _get_tenant_access_token(self):
        url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/"
        headers = {
            "Content-Type" : "application/json"
        }
        req_body = {
            "app_id": self._app_id,
            "app_secret": self._secret_key
        }

        data = bytes(json.dumps(req_body), encoding='utf8')
        req = request.Request(url=url, data=data, headers=headers, method='POST')
        try:
            response = request.urlopen(req)
        except Exception as e:
            print(e.read().decode())
            return ""

        rsp_body = response.read().decode('utf-8')
        rsp_dict = json.loads(rsp_body)
        code = rsp_dict.get("code", -1)
        if code != 0:
            print("get tenant_access_token error, code =", code)
            return ""
        return rsp_dict.get("tenant_access_token", "")

    def list_group(self):
        token = self._get_tenant_access_token()
        url ='https://open.feishu.cn/open-apis/chat/v4/list'
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token
        }
        req_body = {}

        data = bytes(json.dumps(req_body), encoding='utf8')
        req = request.Request(url=url, data=data, headers=headers, method='POST')
        try:
            response = request.urlopen(req)
        except Exception as e:
            print(e.read().decode())
            return

        rsp_body = response.read().decode('utf-8')
        print(rsp_body)
        rsp_dict = json.loads(rsp_body)
        code = rsp_dict.get("code", -1)
        if code != 0:
            return rsp_dict['data']
        pass

    def list_admin(self)->dict:
        """
        列出此机器人的管理员列表
        :return:
        """
        token = self._get_tenant_access_token()
        url ='https://open.feishu.cn/open-apis/user/v4/app_admin_user/list'
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token
        }
        req_body = {}

        data = bytes(json.dumps(req_body), encoding='utf8')
        req = request.Request(url=url, data=data, headers=headers, method='POST')
        try:
            response = request.urlopen(req)
        except Exception as e:
            print(e.read().decode())
            return

        rsp_body = response.read().decode('utf-8')
        print(rsp_body)
        rsp_dict = json.loads(rsp_body)
        code = rsp_dict.get("code", -1)
        if code != 0:
            return rsp_dict['data']
        pass


    def send_msg_by_robot(self, open_id, text)->None:
        """
        给单个用户或群组发送一个文本信息
        :param open_id:
        :param text:
        :return:
        """
        token = self._get_tenant_access_token()
        url = "https://open.feishu.cn/open-apis/message/v4/send/"

        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token
        }
        req_body = {
            "open_id": open_id,
            "msg_type": "text",
            "content": {
                "text": text
            }
        }

        data = bytes(json.dumps(req_body), encoding='utf8')
        req = request.Request(url=url, data=data, headers=headers, method='POST')
        try:
            response = request.urlopen(req)
        except Exception as e:
            print(e.read().decode())
            return

        rsp_body = response.read().decode('utf-8')
        rsp_dict = json.loads(rsp_body)
        code = rsp_dict.get("code", -1)
        if code != 0:
            print("send message error, code = ", code, ", msg =", rsp_dict.get("msg", ""))

    # def send_msg_by_webhook(self,webhook:str,title:str,text:str)->None:
    #     token = self._get_tenant_access_token()
    #     url = "https://open.feishu.cn/open-apis/bot/hook/​​{}".format(webhook)
    #     req_body = {
    #         "title": title,
    #         "text": text,
    #     }
    #     headers = {
    #         "Content-Type": "application/json",
    #         "Authorization": "Bearer " + token
    #     }
    #     print(url,req_body)
    #     res = requests.post(url, data=json.dumps(req_body), headers=headers)
    #     logger.info("send_msg_to_robot|消息已发送|{}|{}".format(req_body, res.text))
    #
    #     # request.post
    #     # data = bytes(json.dumps(req_body), encoding='gbk')
    #     # print(data)
    #     # req = request.Request(url=url, data=req_body, headers=headers, method='POST')
    #     # try:
    #     #     response = request.urlopen(req)
    #     # except Exception as e:
    #     #     print(e)
    #     #     return

