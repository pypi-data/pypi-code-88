import json
from datetime import datetime, timedelta

import requests
from yucebio_config import Config
from yucebio_notifier.backend.base import BaseNotifier

class DingAPI(BaseNotifier):
    """dingding message api

    {HTTP method} https://api.dingtalk.com/{version}/{resource}?{query-parameters}
    """
    baseURI = 'https://oapi.dingtalk.com/'


    def __init__(self, corpid, corpsecret, agentid):
        """init value"""
        self.corpid = corpid
        self.corpsecret = corpsecret
        self.agentid = agentid

        self.access_token = ""
        self.expires_in = datetime.now()

    @classmethod
    def getAPI(cls, env=None):
        if not env:
            env = cls.config("dingding")

        for k in ['corpid', 'corpsecret', 'agent_id']:
            if k not in env or not env[k]:
                raise KeyError("缺失必要的配置内容[%s]" % k)

        return cls(env['corpid'], env['corpsecret'], env['agent_id'])

    def gettoken(self):
        """internal, get and refresh access_token"""
        if self.access_token and datetime.now() < self.expires_in:
            return self.access_token

        url = self.baseURI + "gettoken"
        payload = {'corpid': self.corpid, 'corpsecret': self.corpsecret}
        ret = requests.get(url, params=payload)
        try:
            ret = ret.json()
            self.access_token = ret["access_token"]
            self.expires_in = datetime.now() + timedelta(seconds=ret['expires_in'] - 15)
        except Exception:
            raise RuntimeError("get dingding access_token failed!!!")
        return self.access_token

    def get_userid_by_phone(self, phone: str):
        """根据手机号获取userid
        
        POST https://oapi.dingtalk.com/topapi/v2/user/getbymobile
        {
            access_token
            mobile
        }
        """
        raise RuntimeError("no permmission!!!")

    def get_userinfo(self, userid: str):
        """获取指定用户的用户信息
        POST https://oapi.dingtalk.com/topapi/v2/user/get
        {
            access_token
            userid
        }

        Response:
        {
            errcode: 0 | 非0
            errmsg: 'msg' | any
            result: {...}
            request_id: "..."
        }
        """
        self.gettoken()
        rsp =requests.post(f"{self.baseURI}topapi/v2/user/get", data={
            "access_token": self.access_token,
            "userid": str(userid)
        })
        data = rsp.json()
        if data.get('errcode') != 0:
            raise RuntimeError(f"get userinfo failed: {data['errmsg']}")

        return data['result']

    def _assemble_msg(self, title: str, markdown: str = None) -> dict:
        if not title:
            raise RuntimeError("请提供消息内容")

        if not markdown:
            return {"msgtype": "text", "text": {"content": title}}
        return {
            "msgtype": "markdown",
            "markdown": {
                "title": title,
                "text": markdown 
            }
        }

    def send_message(self, user: str, title: str, markdown: str = None):
        """发送工作通知

        Args:
            user (str): 接受消息的钉钉员工userId，或 逗号分隔的多个员工userId
            title (str): 钉钉消息主题 或 一句话消息内容
            markdown (str, optional): markdown格式的详细消息内容

        Returns:
            str: 本次消息发送的请求ID，使用者需要使用该请求ID确认消息是否发送成功

        工作通知消息是以某个微应用的名义推送到员工的工作通知消息，例如生日祝福、入职提醒等
        refer to: https://developers.dingtalk.com/document/app/asynchronous-sending-of-enterprise-session-messages

        注：该接口是异步发送消息，接口返回成功并不表示用户一定会收到消息，需要通过获取工作通知消息的发送结果接口查询是否给用户发送成功

        POST api
        {
            access_token
            agent_id
            userid_list     指定接收消息员工的id
            dept_id_list    指定接收消息的部门
            to_all_user     是否发送给全体员工
            msg             JSON Object格式的消息内容
        }
        """
        msg = self._assemble_msg(title, markdown=markdown)

        payload = {
            "access_token": self.gettoken(),
            "agent_id": self.agentid,
            "userid_list": user,
            "to_all_user": "false",
            "msg": json.dumps(msg)
        }
        rsp = requests.post(f"{self.baseURI}topapi/message/corpconversation/asyncsend_v2", data = payload)
        return self._process_response(rsp)


    def _process_response(self, response: requests.Response):
        d = response.json()
        if d['errcode'] != 0:
            raise RuntimeError(d['errmsg'])
        return d.get('request_id', 'success')

class RobotAPI(DingAPI):

    def send_message(self, user: str, title: str, markdown: str = None):
        """send message to robot

        Args:
            user (str): 接受消息的钉钉群ID
            title (str): 消息主题 或 一句话消息内容
            markdown (str, optional): 消息正文. Defaults to None.

        Returns:
            str: 本次消息发送的请求ID，使用者需要使用该请求ID确认消息是否发送成功
        """
        url = "https://oapi.dingtalk.com/robot/send"
        msg = self._assemble_msg(title, markdown=markdown)
        payload = {"access_token": user}
        rsp = requests.post(url, params=payload, json=msg)
        return self._process_response(rsp)
