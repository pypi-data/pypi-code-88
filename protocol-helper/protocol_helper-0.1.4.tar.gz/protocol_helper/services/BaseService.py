#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:LeisureMan
# email:LeisureMam@gmail.com
# datetime:2021-06-15 12:27
# software: PyCharm
from protocol_helper.services.MonitoringCenterService import MonitoringCenterService


class BaseService(object):

    def __init__(self):
        self.eoms = MonitoringCenterService()
