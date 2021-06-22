#!/usr/bin/python3
# @Time    : 2021-06-21
# @Author  : Kevin Kong (kfx2007@163.com)

from .core import Core, URL


class Message(Core):

    def send_notification(self, msg, **kwargs):
        """
        send work notification.

        :param agentid: agentid
        :param useridlist: user id list
        :param dept_id_list: id of departments
        :param to_all_user: whether send to all users.
        :param msg: json object.
        :return task_id: async task id.
        """
        url = f"{URL}/topapi/message/corpconversation/asyncsend_v2"
        data = {'agent_id': self._agentid, 'msg': msg}
        data.update(kwargs)
        res = self._post(url, data)
        return res['task_id']
