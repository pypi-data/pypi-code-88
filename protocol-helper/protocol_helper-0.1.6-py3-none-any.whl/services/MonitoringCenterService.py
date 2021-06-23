#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:LeisureMan
# email:LeisureMam@gmail.com
# datetime:2021-06-10 16:45
# software: PyCharm
from abc import ABC

from protocol_helper.setting import SURVEILLANCE_SYSTEM_DOMAIN, SURVEILLANCE_SYSTEM_TOKEN
from protocol_helper.utils.RequestBase import RequestBase


class MonitoringCenterService(RequestBase, ABC):

    def __init__(self):

        self.url = SURVEILLANCE_SYSTEM_DOMAIN
        self.token = SURVEILLANCE_SYSTEM_TOKEN

        if self.token is None:
            self._headers = {}
        else:
            self._headers = {
                    'Authorization': f'Token {self.token}'
            }
        self.HEADERS = self._headers

    def support_service(self):
        """
        数据获取支持的格式
        Returns:

        """
        return self.get(f"{self.url}/api/collection").json()

    def collection(self, mode, server_type, url):
        """

        Args:
            mode:        参考 support_service 返回数据体
            server_type: 服务类型
            url:

        Returns:

        """
        data = {
                'mode':        mode,
                'server_type': server_type,
                'url':         url
        }
        return self.post(f"{self.url}/api/collection", data = data).json()

    def available_agents(self):
        """
        获取一条随机可使用的代理IP
        Returns:

        """

        return self.get(f"{self.url}/api/agent/").json()

    def agent_status_notify(self, server_name, status):
        """
        通知代理可用状态
        Args:
            server_name:  服务器名称
            status:       状态

        Returns:

        """
        data = {
                'status':      status,
                'server_name': server_name,
        }
        return self.post(f"{self.url}/api/agent/", data = data).json()

    def get_proxy_configuration(self, server_name):
        """
        获取代理服务器信息
        Args:
            server_name:

        Returns:

        """

        return self.get(f"{self.url}/api/agent/{server_name}/").json()

    def agent_lock(self, server_name, lock = 0):
        """
        设置代理服务器加锁
        Args:
            server_name:
            lock:   0=>加锁  1=>解锁

        Returns:

        """
        data = {
                'status': lock
        }
        return self.post(f"{self.url}/api/agent/{server_name}/", data = data).json()

    def get_equipment_pool(self, equipment_type):
        """
        获取代理池cookie
        Args:
            equipment_type:参考后台服务类型

        Returns:

        """
        return self.get(f"{self.url}/api/equipment-pool/{equipment_type}").json()

    def set_equipment_pool(self, equipment_type, _hash, status):
        """
        cookies状态设置
        Args:
            equipment_type:参考后台服务类型
            _hash: 回去cookie之后会返回一个hash
            status:200=>占用中 500=>失效  50=>可用

        Returns:

        """
        data = {
                'hash':   hash,
                'status': status
        }
        return self.post(f"{self.url}/api/equipment-pool/{equipment_type}", data = data).json()

    def get_weibo_s(self, uid):
        """
        微博国际版s加密
        Args:
            uid:微博uid


        Returns:

        """
        data = {
                'uid': uid,
        }
        return self.get(f"{self.url}/api/wb/get-s/", params = data).json()

    def get_weibo_registered_equipment(self):
        """

        Returns:

        """
        return self.get(f"{self.url}/api/wb/registered-equipment").json()

    def get_dy_sign(self,url,uid):
        return self.post(f"{self.url}/api/dy/signature", data = {
            'url': url,
            'uid': uid
        },headers={})

    def get_oss_authorization(self):
        """
        获取oss授权
        Returns:

        """
        return self.get(f'{self.url}/api/oss/get-authorization/').json()

    def upload_software_version(self, project_id, data):
        """
        上传软件版本
        Args:
            project_id:
            data:
        Returns:

        """
        return self.post(f'{self.url}/api/software/add-record/{project_id}/', data).json()

    def get_dial_status(self, server_name):
        """
        获取服务器拨号许可
        Args:
            server_name:

        Returns:

        """
        return self.get(f'{self.url}/api/agent/{server_name}/').json()

    def get_proxy_detail(self, server_name):
        """
        通过名称获取服务器代理信息
        Args:
            server_name: 服务器名称 ->dd2

        Returns:

        """
        return self.get(f'{self.url}/api/agent/{server_name}/').json()

    def report(self, service_name, status):
        """
        上传服务器当前状态
        Args:
            service_name: 服务器名称
            status: 当前状态

        Returns:

        """
        data = {
                "status":      status,
                "server_name": service_name,
        }
        return self.post(f'{self.url}/api/agent/', data = data).json()

    def get_project_detail(self, project_id) -> dict:
        """
        获取项目详情
        Returns:

        """
        return self.get(f'{self.url}/api/project/{project_id}/').json()
