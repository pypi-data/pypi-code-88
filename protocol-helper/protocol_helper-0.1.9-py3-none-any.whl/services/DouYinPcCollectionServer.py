#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author:  Boge
# @software: pycharm
# @file: DouYinPcCollectionServer.py
# @time: 2021/6/15 9:50
from protocol_helper.utils.RequestBase import RequestBase
from abc import ABC
import re
from protocol_helper.services.MonitoringCenterService import MonitoringCenterService
from bs4 import BeautifulSoup
from protocol_helper.Exceptions import *
from lxml import etree


class DouYinPcCollectionServer(MonitoringCenterService, ABC):
    def __init__(self):
        super(DouYinPcCollectionServer, self).__init__()

    """直播"""
    URL_STATUS_LIVE = 'live'
    """用户"""
    URL_STATUS_USER = 'user'
    """视频"""
    URL_STATUS_VIDEO = 'video'
    """未定义"""
    URL_STATUS_ERROR = 'error'

    URL_STATUS_LABEL = {
        URL_STATUS_LIVE: '分享',
        URL_STATUS_USER: '主页分享',
        URL_STATUS_VIDEO: '视频分享',
        URL_STATUS_ERROR: '未定义'
    }
    HEADERS = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) 2AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/90.0.4430.93 Safari/537.36",
    }
    TIMEOUT = 30
    URL_TYPE_STATUS = None

    def get_user_void(self, _url, typer = None, mode = None, judge_type = None):
        """

        Args:
            _url:
            typer:

        Returns:

        """

        if typer is None:
            response = self.get(_url)
            url = response.url
            if url.find("404?from_url") != -1:
                return "不是主页或者是视频链接"
        else:
            url = _url
        # 如果是视频链接则走下面这个方法
        if url.find(mode) == -1 and judge_type:
            return "链接类型错误"
        if url.find("video") != -1:
            data = self.url_to_id(_url)
            if isinstance(data, str):
                return data
            return data['response']
        elif url.find("user") != -1:
            # 如果是主页链接去sec_uid
            if "sec_uid" not in url:
                return "主页链接错误"
            sec = self.get_user(url, sec_uid = url)
            if isinstance(sec, str):
                return sec
            uid = url.split("?")[0].split("/")[-1]
            sec_uid = re.findall(r'sec_uid=(.*?)&', url)[0]
            # 走接口计算加密
            signature = self.get_dy_sign(url, uid)
            sign = signature.json()['data'] if signature.json().get("data", "") != "" and signature.json().get("url",
                                                                                                               "") != "" else ""
            if not sign:
                raise DefaultException(f'请求加密接口错误{uid} 链接：{_url}')
            url = f"https://www.iesdouyin.com/web/api/v2/aweme/post/?sec_uid={sec_uid}&count=21&max_cursor=0&aid=1128&_signature={sign}"
            response = self.get(url)
            return {
                'video': response,
                'user': sec
            }
        else:
            return "不支持此类型"

    def get_user(self, url, sec_uid = None):
        try:
            if sec_uid == None:
                response = self.get(url)
                if response.status_code == 200:
                    url_id = re.findall(r'&sec_uid=(.*?)&', response.url)[0]
                else:
                    url_id = ""
            else:
                url_id = re.findall(r'&sec_uid=(.*?)&', sec_uid)
                if len(url_id) == 0:
                    url_id = re.findall(r'\?sec_uid=(.*?)&', sec_uid)
                if len(url_id) != 0:
                    url_id = url_id[0]
                if len(url_id) == 0:
                    return "主页链接错误"
            response = self.get("https://www.iesdouyin.com/web/api/v2/user/info/?sec_uid={}".format(url_id))
            return response
        except Exception as _error:
            return {'code': 107, 'msg': '取用户ID错误', 'response': str(response.text)}

    def url_to_id(self, url):
        """

        Args:
            url:

        Returns:

        """
        resp = self.get(url)
        status = "error"

        if resp.url.find('share/live') > -1:
            status = "live"

        if resp.url.find('share/user') > -1:
            status = "user"
            return {"code": 0, "id": re.findall(r'/(\d+)', resp.url)[0], "type": status, "item_list": [],
                    "sec_uid": resp.url.split("sec_uid=")[-1].split("&")[0]}

        if resp.url.find('share/video') > -1:
            status = "video"
            # if "视频找不到了，看看其他精彩作品吧！" in resp.text:
            #     status = URL_STATUS_VIDEO_DEL
        if resp.url.find('webcast') > -1:
            status = "webcast"

        id_ = re.findall(r'/(\d+)', resp.url)[0]
        info = self.get(f'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={id_}')
        if info.json().get("item_list", None) in [[], None]:
            return "视频链接错误"
        item_list = info.json()["item_list"]
        return {"code": 0, "id": id_, "type": status, "user": item_list, 'response': info}

    def judge_url_type(self, url, flag = None):
        if url.find("www.iesdouyin.com") != -1:
            return True
        return None

    def get_dy_user(self, url, flag = False):
        """

        :param url: 主页链接
        :param flag: 如果只视频链接只获取视频链接信息，则传入Ture，否则就会去获取。
        :return: 返回response对象
        """
        typer = self.judge_url_type(url)
        try:
            return self.get_user_void(url, typer, self.URL_STATUS_USER, flag)
        except Exception as _error:
            return f"未知错误，信息：{_error}"

    def get_dy_video(self, url, flag = False):
        """
        获取视频链信息方法
        :param url: 视频链接
        :param flag: 如果只视频链接只获取视频链接信息，则传入Ture，否则就会去获取。
        :return:返回response对象
        """
        typer = self.judge_url_type(url)
        try:
            return self.get_user_void(url, typer, self.URL_STATUS_VIDEO, flag)
        except Exception as _error:
            return f"未知错误，信息：{_error}"

    def get_url_type(self, url):
        data = self.url_to_id(url)
        if isinstance(data, dict):
            return data['type']
        else:
            return data

    def request_processing(self, url):
        """
        判断是否为作品链接
        :param url: 作品链接
        :return:
        """
        type = url.split('/')[3]
        if type == "video":
            response = self.get(url)
            return response.text
        else:
            return "不是作品链接"

    def collect_work_information(self, url):
        """
        采集作品信息
        :param url: 作品链接
        :return:
        """
        interim_list = []  # 临时 interim
        storage_list = []  # 存储 storage
        response = self.request_processing(url)
        html_response = etree.HTML(response)
        title = html_response.xpath('//h1[@class="_0101d0dac9513f32356fa89903cf7f4e-scss"]//text()')[0]  # 视频标题
        release_date = html_response.xpath('//div[@class="_1c5fdff0b83f80174147ddcadc9f7141-scss"]/span/text()')[
            0]  # 发布时间
        name = html_response.xpath('//div[@class="_976c31c5a089c1b1b6d8809f82aa9a7a-scss"]/a//span/text()')[0]  # 作者名称
        interim_list.append(
            html_response.xpath('//div[@class="_976c31c5a089c1b1b6d8809f82aa9a7a-scss"]/p//span/text()')[1])  # 粉丝
        interim_list.append(
            html_response.xpath('//div[@class="_976c31c5a089c1b1b6d8809f82aa9a7a-scss"]/p//span/text()')[3])  # 总获赞
        interim_list.append(
            html_response.xpath('//span[@class="_63f39b0bbf80afa98948f5dc199307f7-scss"]/text()')[0])  # 视频点赞喜欢数
        interim_list.append(
            html_response.xpath('//span[@class="_63f39b0bbf80afa98948f5dc199307f7-scss"]/text()')[1])  # 视频评论数
        for num in interim_list:
            if num[-1] == 'w':
                num = round(float(num[:-1]), 1) * 10000  # 转换一下单位3w=30000
                storage_list.append(num)
            else:
                storage_list.append(num)

        data = {
            'nickname': name,
            'fans': storage_list[0],
            'great': storage_list[1],
            'title': title,
            'like_num': storage_list[2],
            'comment_num': storage_list[3],
            'date': release_date,
        }

        return data
