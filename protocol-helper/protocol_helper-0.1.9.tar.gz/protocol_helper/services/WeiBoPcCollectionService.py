#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:LeisureMan
# email:LeisureMam@gmail.com
# datetime:2021-06-11 17:42
# software: PyCharm
import json
import random
import re
from abc import ABC
from bs4 import BeautifulSoup
from protocol_helper.Exceptions import *
from protocol_helper.services.WeiBoBaseService import WeiBoBaseService
from protocol_helper.services.BaseService import BaseService
from protocol_helper.utils.RequestBase import RequestBase
import requests


def helper(function):
    def clothes(func):
        def wear(*args, **kwargs):
            cls = args[0]
            if function == 'login_guest':
                if cls._headers.get('Cookie', None) is None:
                    cls.get_cookies_tourist()
            return func(*args, **kwargs)

        return wear

    return clothes


class WeiBoPcCollectionService(RequestBase, BaseService, WeiBoBaseService, ABC):
    HEADERS = {
            'x-requested-with': 'XMLHttpRequest',
            'user-agent':       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                'Chrome/90.0.4430.72 Safari/537.36 ',
            'accept':           'application/json, text/plain, */*',
    }

    def __init__(self):
        super(WeiBoPcCollectionService, self).__init__()

        # pc 游客权限使用
        self._headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/90.0.4430.72 Safari/537.36 ',
        }

        self.requests = requests.Session()

    def get_random_cookies(self):
        """
        随机返回一条cookies
        Returns:

        """
        resp = self.eoms.get_equipment_pool('WeiBoH5PCAFaZHU')
        if resp.get('status_code', None) != 0:
            raise DefaultException(resp.get('messages', resp))
        self.COOKIES = resp['data']['cookie']
        return resp['data']

    def set_cookies(self, value):
        """
        设置全局cookies
        Args:
            value:

        Returns:

        """
        self.COOKIES = value

    def get_topic(self, title):
        """
        微博话题
        支持格式 #吴一凡# 吴一凡

        Returns:

        """
        params = {"containerid": f"100103type=1&q={title}&t=0", "page": "1", "count": "20"}
        return self.get('https://weibo.com/ajax/search/all', params = params).json()

    def get_article(self, mid):
        """
        微博博文
        Args:
            mid: 微博文章mid

        Returns:

        """
        params = {'id': mid}
        return self.get('https://weibo.com/ajax/statuses/show', params = params).json()

    def get_fans(self, uid = None, custom = None):
        """
        微博主页

        uid 与  custom 不能同时为空

        Args:
            uid:   uid
            custom:custom

        Returns:

        """
        params = {}
        if uid is not None:
            params.update({'uid': uid})
        if custom is not None:
            params.update({'custom': custom})
        return self.get('https://weibo.com/ajax/profile/info', params = params).json()

    def get_user_article(self, uid, page = 1):
        """
        获取用户博文
        :param uid:     微博uid
        :param page:   获取页数
        :return:
        """
        params = {}
        if uid is not None:
            params.update({'uid': uid})
        if page is not None:
            params.update({'page': page})
        return self.get(f"https://weibo.com/ajax/statuses/mymblog", params = params).json()

    def get_tid_tourist(self):
        """
        获取访客信息
        Returns:

        """
        tid_url = "https://passport.weibo.com/visitor/genvisitor"
        data = {
                "cb": "gen_callback",
                "fp": {
                        "os":         "3",
                        "browser":    "Chrome69,0,3497,100",
                        "fonts":      "undefined",
                        "screenInfo": "1920*1080*24",
                        "plugins":    "Portable Document Format::internal-pdf-viewer::Chrome PDF "
                                      "Plugin|::mhjfbmdgcfjbbpaeojofohoefgiehjai::Chrome PDF "
                                      "Viewer|::internal-nacl-plugin::Native Client "
                }
        }
        resp = self.requests.post(url = tid_url, data = data, headers = self._headers, timeout = self.TIMEOUT)

        if resp.status_code != 200:
            raise RequestException(resp)
        content = re.findall(r'&& gen_callback\((.*?)\);', resp.text)
        if len(content) <= 0:
            return DefaultException("获取注册访客信息失败")
        data = json.loads(content[0])
        return data.get('data').get('tid')

    def get_cookies_tourist(self):
        """
        获取游客注册信息
        Returns:

        """
        tid = self.get_tid_tourist()

        cookies = {
                "tid": tid + "__095"
        }
        url = "https://passport.weibo.com/visitor/visitor"

        params = {
                "a":     "incarnate",
                "t":     tid,
                "w":     "2",
                "c":     "095",
                "gc":    "",
                "cb":    "cross_domain",
                "from":  "weibo",
                "_rand": f"0.{random.random()}"
        }
        resp = self.requests.get(url, params = params, cookies = cookies, headers = self._headers,
                                 timeout = self.TIMEOUT)
        if resp.status_code != 200:
            return None

        content = re.findall(r'&& cross_domain\((.*?)\);', resp.text)
        if len(content) <= 0:
            return DefaultException("注册访客信息失败")
        data = json.loads(content[0])
        if data.get('retcode', None) != 20000000:
            raise DefaultException(data.get('msg', resp.text))

        cookies = 'SUB={};SUBP={}'.format(data['data']['sub'], data['data']['subp'])
        self._headers.update({'Cookie': cookies})
        print("注册游客cookies 成功", cookies)

    @helper("login_guest")
    def get_fans_tourist(self, url):
        """
        游客权限获取用户信息
        Args:
            url:

        Returns:

        """
        if url.find('m.weibo.com') > 0:
            url = url.replace('m.weibo.com', 'weibo.com')

        if url.find('m.weibo.cn') > 0:
            url = url.replace('m.weibo.cn', 'weibo.com')
        if url.find('/follow') > 0:
            url = url[:url.find('/follow')]

        resp = self.requests.get(url, headers = self._headers, timeout = 30)
        if resp.status_code != 200:
            raise RequestException(resp)
        # 起始位置
        _bs4 = BeautifulSoup(resp.content, 'lxml')
        if _bs4.text.find('出错情况返回登录页') > 0:
            raise DefaultException('Cookies可能错误')

        if _bs4.text.find('该页面不存在') > 0:
            raise DefaultException('该页面不存在')

        user_array = re.findall(r"CONFIG\['(onick|oid)'\]='(.*?)';", resp.text)

        if user_array in [None] or len(user_array) != 2:
            raise DefaultException('获取UID失败')
        counts = re.findall(r'<strong class=\\"W_f[\d]+\\">([\d]+)<', resp.text) or re.findall(
                r'<strong class=\\"\\">([\d]+)<', resp.text)
        if counts in [None] or len(counts) != 3:
            raise DefaultException('获取UID失败')

        if counts in [[]]:
            raise DefaultException('匹配数量失败')

        if user_array[0][1].isdigit() not in [True]:
            raise DefaultException('识别错误')
        response = re.sub(r'(\s|\\r\\n|\\t|\\)', '', resp.text)
        verified_array = re.findall(r'<emtitle="(.*?)"class="(\w+)".*username', response)
        avatar = re.findall(r'photo_wrap"><imgsrc="(.*?)"', response)
        if len(avatar) > 0:
            avatar = avatar[0]
        else:
            avatar = 'null'
        if verified_array:
            verified_data = {
                    'W_icon_co2icon_pf_approve_co': '蓝V', 'W_iconicon_pf_approve_co': '蓝V',
                    'W_iconicon_pf_approve_gold':   '金V', 'W_iconicon_pf_approve': '黄V'
            }
            verified_title = verified_array[0][0]
            verified_type = verified_data.get(verified_array[0][1], '未知')
        else:
            verified_type, verified_title = None, None

        content = re.findall(r'pf_intro"title="(.*?)"', response)
        if len(content) > 0:
            content = content[0]
        else:
            content = '暂无简介'
        user = {
                'uid':             str(user_array[0][1]),
                'nick_name':       user_array[1][1],
                'name':            user_array[1][1],
                'followers_count': counts[1],
                'friends_count':   counts[0],
                'statuses_count':  counts[2],
                'verified_title':  verified_title,
                'verified_type':   verified_type,
                'avatar':          avatar,
                'content':         content
        }

        return user

    @helper("login_guest")
    def get_article_tourist(self, url):
        """
        pc 游客状态访问 获取博文数据
        Args:
            url:

        Returns:

        """
        # PC 识别 正则提取麻烦使用 h5端获取数据
        headers = {
                'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, '
                              'like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
                'accept':     'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,'
                              'image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Cookie':     self._headers.get('Cookie', '')
        }

        resp = self.requests.get(url, headers = headers, timeout = self.TIMEOUT)

        if resp.text.find('update-desc-r">打开微博客户端，查看全文</p>') >= 0:
            raise WeiBoH5SideRestrictions(resp, "打开微博客户端，查看全文")

        if resp.text.find('微博不存在或暂无查看权限!') >= 0:
            raise WeiBoUrlError(resp, "微博不存在或暂无查看权限")

        mid = re.findall(r'"mid": "(.*?)"', resp.text)
        if len(mid) > 2 or len(mid) <= 0:
            raise DefaultException("数据格式错误")

        # 通过 h5获取数据
        headers = {
                'X-Requested-With': 'XMLHttpRequest',
                'Accept':           'application/json',
                'Cookie':           self._headers.get('Cookie', ''),
        }
        # Mid 需要是英文的 不是 18位数字需要转换
        mid = self.id2mid(mid[0])
        resp = self.requests.get(f'https://m.weibo.cn/statuses/show?id={mid}', headers = headers,
                                 timeout = self.TIMEOUT)

        if resp.status_code != 200:
            raise RequestException(resp)

        return json.loads(resp.text)

    @helper("login_guest")
    def get_likes_tourist(self, url):
        headers = {
                # 'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, '
                #               'like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
                # 'accept':     'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,'
                #               'image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Cookie': self._headers.get('Cookie', '')
        }
        _res = self.requests.get(url, headers = headers, timeout = self.TIMEOUT)
        if _res.status_code != 200:
            return '访问code错误：{0}'.format(_res.status_code)

        if _res.text.find('博文涉及营销推广正在审核中，暂时无法传播') >= 0:
            return '博文涉及营销推广正在审核中，暂时无法传播'
        if _res.text.find('由于用户设置，你无法回复评论。') >= 0:
            return '由于用户设置，你无法回复评论。'
        if _res.text.find('以下为博主精选评论') >= 0:
            return '以下为博主精选评论'

        return _res.text

    @staticmethod
    def _unit_conversion(unit) -> int:
        """
        单位转换
        Args:
            unit:

        Returns:

        """
        if unit == '万':
            return 10000

        if unit == "亿":
            return 100000000

        return 1

    @helper("login_guest")
    def get_super_tourist(self, url):
        """

        Args:
            url:

        Returns:

        """
        resp = self.requests.get(url, headers = self._headers, timeout = 30)
        if resp.status_code != 200:
            raise RequestException(resp)
        # 起始位置
        page_id = re.findall(r"\$CONFIG\['page_id'\]='(.*?)'", resp.text)
        nick_name = re.findall(r"\$CONFIG\['onick'\]='(.*?)'", resp.text)
        title_value = re.findall(r"\$CONFIG\['title_value'\]='(.*?)'", resp.text)
        counts = re.findall(r'<strong class=\\"W_f14\\">(.*?)<', resp.text)
        if len(counts) <= 0:
            raise DefaultException('匹配数量失败')
        # 阅读数
        read_count = float(counts[0].replace(counts[0][-1], ''))
        # 文章数量
        article_count = float(counts[1].replace(counts[1][-1], ''))
        # 粉丝数量
        fans_count = float(counts[2].replace(counts[2][-1], ''))
        return {
                'page_id':       page_id[0],
                'nick_name':     nick_name[0],
                'title_value':   title_value[0],
                'read_count':    int(read_count * self._unit_conversion(counts[0][-1])),
                'article_count': int(article_count * self._unit_conversion(counts[1][-1])),
                'fans_count':    int(fans_count * self._unit_conversion(counts[2][-1]))
        }
