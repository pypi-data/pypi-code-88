#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:LeisureMan
# email:LeisureMam@gmail.com
# datetime:2021-06-21 14:02
# software: PyCharm
import os
import platform
import subprocess
import time

import requests

from protocol_helper.setting import PPPOE_NAME, PPPOE_USER, PPPOE_PASS

SYSTEM = platform.system()


class PPPOEService:
    """
    拨号服务
    """

    @staticmethod
    def status():
        """
        宽带状态
        Returns:

        """
        return subprocess.getoutput("pppoe-status")

    @staticmethod
    def testing_network() -> bool:
        """
        测试网络
        Returns:

        """
        try:
            resp = requests.get("https://api.ip.sb/ip", timeout = 10).text
            print(f"验证网络成功:{resp}")
            return True
        except (requests.exceptions.ConnectTimeout, requests.exceptions.ConnectionError):
            print("验证网络失败,....")
            return False

    def redial(self, number = 5):
        """
        重新拨号
        Args:
            number:尝试次数

        Returns:

        """
        if SYSTEM in ['Windows']:
            for index in range(number):
                print(f"拨号尝试:{index + 1}/{number}")
                # 卸载拨号
                os.system(f'@Rasdial {PPPOE_NAME} /DISCONNECT')
                print(f'@Rasdial {PPPOE_NAME} /DISCONNECT')
                os.system(f'@Rasdial {PPPOE_NAME} {PPPOE_USER} {PPPOE_PASS}')
                time.sleep(5)
                if self.testing_network():
                    break

        elif SYSTEM in ['Linux']:
            for index in range(number):
                print(f"拨号尝试:{index}/{number}")
                ip_front = subprocess.getoutput("pppoe-status |grep inet|awk '{print $2}'")
                print('拨号前IP:', ip_front or self.status())
                subprocess.getoutput('systemctl restart network')
                ip_back = subprocess.getoutput("pppoe-status |grep inet|awk '{print $2}'")
                print('拨号后IP:', ip_back or self.status())
                if ip_back is None:
                    continue
                print("拨号成功,测试是否能够上网...")
                if self.testing_network():
                    break
        else:
            raise Exception(f"Does not support changing the operating system:{SYSTEM}")
