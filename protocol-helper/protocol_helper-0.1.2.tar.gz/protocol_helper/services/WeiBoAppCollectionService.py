#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:LeisureMan
# email:LeisureMam@gmail.com
# datetime:2021-06-11 16:34
# software: PyCharm
from abc import ABC

from protocol_helper.Exceptions import RequestException, NeedToLogin, DefaultException
from protocol_helper.services.BaseService import BaseService
from protocol_helper.services.WeiBoBaseService import WeiBoBaseService
from protocol_helper.utils.RequestBase import RequestBase


def helper(function):
    def clothes(func):
        def wear(*args, **kwargs):
            cls = args[0]
            print(args, kwargs)
            if function == 'detect_login':  # 自动登录游客协议
                if not cls.is_login:
                    resp = cls.guest_login()
                    print(f"自动登录:{resp}")
            return func(*args, **kwargs)

        return wear

    return clothes


class WeiBoAppCollectionService(RequestBase, BaseService, WeiBoBaseService, ABC):

    def __init__(self):
        super(WeiBoAppCollectionService, self).__init__()

        # 默认访问
        self.uid = None
        self.gsid = None
        self.aid = None
        self.s = None
        self.comment_s = None

        # 登录账号
        self.logged_uid = None
        self.logged_gsid = None
        self.logged_aid = None
        self.logged_s = None
        self.logged_comment_s = None

        # 登录账号
        self.tourist_uid = None
        self.tourist_gsid = None
        self.tourist_aid = None
        self.tourist_s = None
        self.tourist_comment_s = None

        self.ua = "BLA-AL00_6.0.1_WeiboIntlAndroid_3660"
        self.is_login = False

    def guest_login(self):
        """

        Returns:

        """

        # 获取设备
        try:
            resp = self.eoms.get_weibo_registered_equipment()
        except RequestException as error:
            raise error
        except Exception as error:
            raise error
        headers = {
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Host':         'api.weibo.cn',
                'User-Agent':   'okhttp/3.12.1'
        }
        # 注册设备可用
        data = resp['data']['equipment']
        resp = self.post('https://api.weibo.cn/2/guest/login', data = data, headers = headers)
        if resp.status_code != 200:
            raise RequestException(resp)
        data = resp.json()
        if data.get('errmsg', None):
            return data.get('errmsg', None)
        self.tourist_uid = data['uid']
        self.tourist_gsid = data['gsid']
        self.tourist_aid = data['aid']
        data = self.eoms.get_weibo_s(self.tourist_uid)
        if data.get('status_code', None) != 0:
            return "获取 s 加密错误"
        self.tourist_s = data['data']['s']
        self.tourist_comment_s = data['data']['comment_s']
        return "success"

    def __set_token(self, custom_login):
        """
        切换 token
        Args:
            custom_login:

        Returns:

        """
        if custom_login:
            if self.logged_uid is None:
                self.get_random_cookies()
            self.uid = self.logged_uid
            self.gsid = self.logged_gsid
            self.aid = self.logged_aid
            self.s = self.logged_s
            self.comment_s = self.logged_comment_s
        else:
            self.uid = self.tourist_uid
            self.gsid = self.tourist_gsid
            self.aid = self.tourist_aid
            self.s = self.tourist_s
            self.comment_s = self.tourist_comment_s

    @helper("detect_login")
    def get_topics(self, title, custom_login = False):
        """
        获取话题数据
        Args:
            title:话题内容
            custom_login: 是否使用自定义登录
        Returns:

        """
        self.__set_token(custom_login)
        params = {
                "v_f":         "2",
                "s":           self.s,
                "source":      "4215535043",
                "wm":          "2468_1001",
                "gsid":        self.gsid,
                "count":       "20",
                "containerid": f"231522type%3D1%26q%3D{title}",
                "from":        "1299295010",
                "i":           "4366450",
                "c":           "weicoabroad",
                "ua":          self.ua,
                "lang":        "zh_CN",
                "page":        "1",
                "aid":         self.aid,
                "v_p":         "72"
        }

        return self.get('https://api.weibo.cn/2/cardlist', params = params).json()

    def get_random_cookies(self):
        """

        Returns:

        """
        resp = self.eoms.get_equipment_pool('WeiBoAPP')
        if resp.get('status_code', None) != 0:
            raise DefaultException(resp.get('messages', resp))
        data = resp['data']
        self.logged_uid = data['uid']
        self.logged_gsid = data['gsid']
        self.logged_aid = data['aid']
        self.logged_s = data['s']
        self.logged_comment_s = data['comment_s']

    @helper("detect_login")
    def get_article(self, mid, custom_login = False):
        """
        获取文章数据
        Args:
            mid: 只支持 4646504838991322
            custom_login: 是否使用自定义登录
        Returns:

        """
        self.__set_token(custom_login)
        params = {
                "s":             self.s,
                "source":        "4215535043",
                "c":             "weicoabroad",
                "id":            mid,
                "wm":            "2468_1001",
                "gsid":          self.gsid,
                "isGetLongText": "1",
                "ua":            self.ua,
                "lang":          "zh_CN",
                "from":          "1299295010",
                "aid":           self.aid
        }
        data = self.get('https://api.weibo.cn/2/statuses/show', params = params).json()
        if data.get('errmsg', "").find('login user in official client/website!') >= 0:
            raise NeedToLogin(data.get('errmsg', data))

        if data.get('errmsg', None) is not None:
            raise DefaultException(data.get('errmsg', data))

        return data

    @helper("detect_login")
    def get_comment_mid(self, rid, custom_login = False):
        """
        获取评论id数据
        Args:
            rid:评论id
            custom_login:是否使用自定义登录
        Returns:

        """
        self.__set_token(custom_login)
        params = {
                "s":                self.comment_s,
                "source":           "4215535043",
                "wm":               "2468_1001",
                "gsid":             self.gsid,
                "count":            "20",
                "from":             "1081095010",
                "fetch_level":      "1",
                "is_reload":        "1",
                "c":                "weicoabroad",
                "id":               rid,
                "ua":               self.ua,
                "lang":             "zh_CN",
                "is_show_bulletin": "2",
                "aid":              self.aid,
                "flow":             "0",
                "v_p":              "72",
                "max_id":           "0"
        }
        return self.get('https://api.weibo.cn/2/comments/build_comments', params = params).json()

    @helper("detect_login")
    def get_fans(self, uid = None, screen_name = None, custom_login = False):
        """
        获取粉丝数据 两者只能存在一个
        Args:
            uid:
            screen_name:
            custom_login: 是否使用自定义登录

        Returns:

        """
        self.__set_token(custom_login)
        params = {
                "s":           self.s,
                "screen_name": screen_name,
                "source":      "4215535043",
                "c":           "weicoabroad",
                "wm":          "2468_1001",
                "gsid":        self.gsid,
                "ua":          self.ua,
                "lang":        "zh_CN",
                "uid":         uid,
                "from":        "1299295010",
                "aid":         self.aid,
        }
        return self.get('https://api.weibo.cn/2/users/show', params = params).json()

    @helper("detect_login")
    def get_user_profile_statuses(self, uid, page = 1, custom_login = False):
        """
        获取主页博文
        Args:
            uid:
            page:
            custom_login:

        Returns:

        """
        self.__set_token(custom_login)
        params = {
                "need_new_pop":    "0",
                "v_f":             "2",
                "s":               self.s,
                "source":          "4215535043",
                "wm":              "2468_1001",
                "gsid":            self.gsid,
                "fid":             f"107603{uid}_-_WEIBO_SECOND_PROFILE_WEIBO",
                "need_head_cards": "0",
                "count":           "20",
                "containerid":     f"107603{uid}_-_WEIBO_SECOND_PROFILE_WEIBO",
                "from":            "1299295010",
                "c":               "weicoabroad",
                "ua":              self.ua,
                "lang":            "zh_CN",
                "uid":             uid,
                "page":            page,
                "aid":             self.aid,
                "v_p":             "82"
        }
        resp = self.get('https://api.weibo.cn/2/profile/statuses', params = params)
        return resp.json()

    @helper("detect_login")
    def get_topic_id(self, topic_id, custom_login = False):
        """
        获取超话数据
        Args:
            topic_id:
            custom_login:

        Returns:

        """
        self.__set_token(custom_login)
        params = {
                "since_id":    "0",
                "s":           self.s,
                "source":      "4215535043",
                "c":           "weicoabroad",
                "wm":          "2468_1001",
                "gsid":        self.gsid,
                "ua":          self.ua,
                "lang":        "zh_CN",
                "count":       "20",
                "containerid": topic_id,
                "from":        "1299295010",
                "aid":         self.aid,
                "v_p":         "72"
        }
        resp = self.get('https://api.weibo.cn/2/page', params = params)
        return resp.json()
