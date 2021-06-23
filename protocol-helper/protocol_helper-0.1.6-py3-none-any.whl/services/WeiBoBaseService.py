#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:LeisureMan
# email:LeisureMam@gmail.com
# datetime:2021/6/11 23:04
# software: PyCharm
import re

from protocol_helper.Exceptions import CollectedDataError, DefaultException

ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def rsplit(s, count):
    _f = lambda x: x > 0 and x or 0
    return [s[_f(i - count):i] for i in range(len(s), 0, -count)]


def id2mid(id):
    result = ''
    for i in rsplit(id, 7):
        str62 = base62_encode(int(i))
        result = str62.zfill(4) + result
    return result.lstrip('0')


def mid2id(mid):
    result = ''
    for i in rsplit(mid, 4):
        str10 = str(base62_decode(i)).zfill(7)
        result = str10 + result
    return result.lstrip('0')


def filter_weibo_url(url):
    """
    过滤微博网址
    """
    try:
        data = url.split('?')
        url = data[0]
        # 替换空格换行
        url = re.sub('[\r\n\f]{2,}', '\n', url)
        return url
    except Exception as error:
        print('过滤网址失败', error)
        return url


def base62_encode(num, alphabet = ALPHABET):
    """Encode a number in Base X
    `num`: The number to encode
    `alphabet`: The alphabet to use for encoding
    """
    if num == 0:
        return alphabet[0]
    arr = []
    base = len(alphabet)
    while num:
        rem = num % base
        num = num // base
        arr.append(alphabet[rem])
    arr.reverse()
    return ''.join(arr)


def base62_decode(string, alphabet = ALPHABET):
    """Decode a Base X encoded string into the number
    Arguments:
    - `string`: The encoded string
    - `alphabet`: The alphabet to use for encoding
    """
    base = len(alphabet)
    strlen = len(string)
    num = 0

    idx = 0
    for char in string:
        power = (strlen - (idx + 1))
        num += alphabet.index(char) * (base ** power)
        idx += 1
    return num


class WeiBoBaseService(object):

    def url_to_mid(self, url):
        """
        微博博文网址获取mid
        Args:
            url:

        Returns:

        """
        # 过滤微博网址
        urls = self.filter_weibo_url(url).split('/')
        if len(urls) <= 0:
            mid = url
        else:
            if urls[-1] == '':
                urls.pop(-1)
            mid = urls[len(urls) - 1]
        # 如果是英文的需要进制转换
        if mid.isdigit() in [False]:
            mid = mid2id(mid)
        return mid, urls

    @staticmethod
    def filter_weibo_url(url):
        """
        过滤微博网址
        """
        try:
            data = url.split('?')
            url = data[0]
            # 替换空格换行
            url = re.sub('[\r\n\f]{2,}', '\n', url)
            return url
        except Exception as error:
            print('过滤网址失败', error)
            return url

    @staticmethod
    def cst_to_str(cstTime):
        """
        格式化时间
        :param cstTime:
        :return:
        """
        # print(cstTime)

        # time_str = 'Fri Jul 31 10:30:59 +0800 2020'
        month_map = {
                'jan': 1,
                'feb': 2,
                'mar': 3,
                'apr': 4,
                'may': 5,
                'jun': 6,
                'jul': 7,
                'aug': 8,
                'sep': 9,
                'oct': 10,
                'nov': 11,
                'dec': 12
        }
        time_list = cstTime.split(' ')
        year = time_list[-1]
        month = time_list[1]
        day = time_list[2]
        hour, mina, sec = time_list[3].split(":")
        _time = '{}-{}-{} {}:{}:{}'.format(year, month_map.get(month.lower()), day, hour, mina, sec)
        return _time

    @staticmethod
    def check_url(array, url):
        """
        :param array:
        :param url:
        :return:
        """
        try:
            # 手机格式

            if url.find('status') > 0 or url.find('detail') > 0:

                if url.find(str(array['mblogid'])) > 0:
                    return array
                if url.find(str(array['mid'])) > 0:
                    return array
            # 如果是视频地址
            elif url.find('tv') > 0:
                if url.find(str(array['mblogid'])) > 0:
                    return array
                if url.find(str(array['mid'])) > 0:
                    return array
            # 其他地址
            else:
                if url.find(str(array['mid'])) > 0:
                    return array
                if url.find(str(array['mblogid'])) > 0:
                    return array
            return False
        except Exception as _error:
            raise Exception(_error)

    @staticmethod
    def id2mid(article_id):
        """
        4479896300333392 to Ixwt01oJi
        Args:
            article_id:

        Returns:

        """
        return id2mid(article_id)

    @staticmethod
    def mid2id(article_id):
        """
        Iyfcpyr8d to 4481615818207449
        Returns:

        """
        return mid2id(article_id)

    def cleaning_url(self, url):
        """
        清洗url额外参数
        Args:
            url:

        Returns:

        """
        try:
            data = url.split('?')
            url = data[0]
            # 替换空格换行
            url = re.sub('[\r\n\f]{2,}', '\n', url)
            return url
        except Exception as error:
            print('过滤网址失败', error)
            return url

    def weibo_url_to_mid(self, url):
        """
        微博url 转换 mid

        Args:
            url:

        Returns:

        """
        url = self.cleaning_url(url)
        array = url.split('/')
        if len(array) <= 0:
            mid = url
        else:
            if array[-1] == '':
                array.pop(-1)
            mid = array[len(array) - 1]
            # 如果是数字的需要进制转换
        if mid.isdigit() in [True]:
            url = url.replace(mid, self.id2mid(mid))
            url = url.replace('m.weibo.cn', 'weibo.com')
        else:
            if "#" in mid:
                mid = mid.split("#")[0]
            mid = self.mid2id(mid)
        if len(mid) < 16:
            raise DefaultException(f'计算mid错误,请检查网站 {url}')
        return mid

    @staticmethod
    def __filter_video_information(status):
        """
        视频信息
        Args:
            status:

        Returns:

        """
        page_info = status['page_info']
        media_info = page_info['media_info']
        if media_info.get('h5_url', None) is None:
            return {
                    'page_id':     page_info.get('page_id', ''),
                    'object_type': page_info['object_type'],
                    'content1':    page_info['content1'],
                    'content2':    page_info['content2'],
                    'page_pic':    page_info['page_pic'],
                    'media_info':  {
                            'video_url': media_info['stream_url']
                    }
            }

        return {
                'page_id':     page_info.get('page_id', ''),
                'object_type': page_info['object_type'],
                'content1':    page_info['content1'],
                'content2':    page_info['content2'],
                'page_pic':    page_info['page_pic'],
                'media_info':  {
                        'name':                media_info['name'],
                        'video_url':           media_info['h5_url'],
                        'next_title':          media_info['next_title'],
                        'media_id':            media_info['media_id'],
                        'online_users':        media_info['online_users'],
                        'online_users_number': media_info['online_users_number'],  # 播放次数
                }
        }

    def article_cleaning(self, data, url, urls):
        """
        微博博文数据处理
        Args:
            data:
            url:
            urls:

        Returns:

        """
        try:
            status, response = data['data'], data['data']
        except KeyError:
            status, response = data, data

        if status.get("mblogid", None) is None:
            judge_mid = [x for x in urls if x != "" if not str(x).isalnum()]
            status['mblogid'] = judge_mid[-1]
        # 封装需要返回的数据
        pic_urls = [f'https://wx4.sinaimg.cn/mw690/{pic}' for pic in status.get('pic_ids', [])]
        # 是否有消息
        if response.get('tip_close_disable', None) == 1:
            tip_msg = response['tip_msg']
        else:
            tip_msg = None

        header_text = response.get('header_text', None)
        if header_text is None:
            if len(response.get("datas", [])) > 0:
                header_text = response['datas'][0]['data'].get("actionName", None)

        if status['isLongText'] and status.get('longText', None) is not None:
            content = status['longText'].get('longTextContent', None)
            if content is None:
                content = status['longText']['content']
        else:
            content = status['text']

        user = {
                'id':             status['user']['id'],
                'screen_name':    status['user']['screen_name'],
                'name':           status['user']['screen_name'],
                'followers':      status['user']['followers_count'],
                'friends_count':  status['user'].get('friends_count', 0),
                'statuses_count': status['user']['statuses_count'],
                'avatar':         status['user']['avatar_hd']
        }

        if 'mblogid' in status.keys():
            bid = status['mblogid']
        else:
            bid = status['bid']
        data = {
                'mid':             status['id'],
                'text':            content,
                'url':             f"{user['id']}/{bid}",
                'mblogid':         bid,
                'reposts_count':   status['reposts_count'],
                'comment_count':   status['comments_count'],
                'attitudes_count': status['attitudes_count'],
                'user':            user,
                'long_text':       content,
                'pic_urls':        pic_urls,
                'is_app':          True,
                'tip_msg':         tip_msg,
                'header_text':     header_text,
                'created_at':      self.cst_to_str(status['created_at'])
        }
        try:
            data['pid'] = status['pid']
        except KeyError:
            pass

        # 获取视频信息
        if 'page_info' in status.keys():
            data.update({'video': self.__filter_video_information(status)})

        try:
            # 转发信息
            retweeted_status = status.get('retweeted_status', None)
            if retweeted_status is not None:
                if retweeted_status.get('user', None) is None:
                    data['retweeted_status'] = {
                            'messages': retweeted_status['text']
                    }
                else:
                    if retweeted_status['isLongText'] and retweeted_status.get('longText', None) is not None:
                        content = retweeted_status['longText'].get('longTextContent', None)
                        if content is None:
                            content = retweeted_status['longText']['content']
                    else:
                        content = retweeted_status['text']
                    name = retweeted_status.get('user', {}).get('name', None) or retweeted_status['user']['screen_name']
                    friends_count = retweeted_status['user'].get('friends_count', None) or retweeted_status['user'][
                        'follow_count']
                    retweeted_user = {
                            'id':             retweeted_status['user']['id'],
                            'screen_name':    retweeted_status['user']['screen_name'],
                            'name':           name,
                            'followers':      retweeted_status['user']['followers_count'],
                            'friends_count':  friends_count,
                            'statuses_count': retweeted_status['user']['statuses_count'],
                    }
                    if 'mblogid' in retweeted_status.keys():
                        bid = retweeted_status['mblogid']
                    else:
                        bid = retweeted_status['bid']

                    data['retweeted_status'] = {
                            'mid':             retweeted_status['id'],
                            'text':            content,
                            'url':             f"{retweeted_user['id']}/{bid}",
                            'mblogid':         bid,
                            'reposts_count':   retweeted_status['reposts_count'],
                            'comment_count':   retweeted_status['comments_count'],
                            'attitudes_count': retweeted_status['attitudes_count'],
                            'user':            retweeted_user,
                            'long_text':       content,
                            'created_at':      self.cst_to_str(retweeted_status['created_at'])
                    }

                    # 获取视频信息
                    if 'page_info' in retweeted_status.keys():
                        data.update({'video': self.__filter_video_information(retweeted_status)})

        except KeyError as key:
            raise Exception(f'获取转发信息失败:{key}')

        # 判断如果是一个数组且url是mid
        if len(urls) == 1 and len(url) == 16:
            return data
        _result = self.check_url(data, url)
        if _result in [False]:
            raise CollectedDataError('内部URl对比失败')
        return _result

    def fans_app_cleaning(self, data):
        """
        微博分数数据清理
        Args:
            data:

        Returns:

        """
        userInfo = data

        """
            -1普通用户;
            0名人,
            1政府,
            2企业,
            3媒体,
            4校园,
            5网站,
            6应用,
            7团体（机构）,
            8待审企业,
            200初级达人,
            220中高级达人,
            400已故V用户。

            -1 0 3 5 6  200 220

        """
        verified_type = {
                -1:  '普通用户',
                1:   "蓝V",
                0:   '黄V',
                3:   '蓝V',
                4:   '蓝V',
                2:   '蓝V',
                7:   '蓝V',
                220: '中高级达人',
                200: '初级达人',
                5:   '网站',
                6:   '应用',
                10:  '普通用户'
        }

        gender_label = {
                'm': "男",
                'f': "女",
                'n': "未知"
        }

        verified_type_ext = userInfo.get('verified_type_ext', 0)

        if userInfo['verified_type'] == 0 and verified_type_ext == 1:
            verified_type_label = '金V'
        else:
            verified_type_label = verified_type[userInfo['verified_type']]

        if userInfo.get('status', None) is not None:
            status_id = userInfo['status']['id']
        else:
            status_id = userInfo.get('status_id', None)

        description = userInfo.get("description", "暂无简介")
        if description == "":
            description = "暂无简介"

        user = {
                'id':                  userInfo['id'],
                'screen_name':         userInfo.get('screen_name', None),
                'name':                userInfo.get('name', None),
                'followers_count':     userInfo.get('followers_count', 0),
                'friends_count':       userInfo.get('friends_count', 0),
                'statuses_count':      userInfo.get('statuses_count', 0),
                'domain':              userInfo.get('domain', None),
                'avatar_hd':           userInfo.get('avatar_hd', None),
                'province':            userInfo.get('province', None),
                'city':                userInfo.get('city', None),
                'verified_type_ext':   verified_type_ext,
                'verified_reason':     userInfo['verified_reason'],
                'description':         description,
                'created_at':          self.cst_to_str(userInfo.get('created_at', None)),  # 账号注册时间
                'status_id':           status_id,  # 最近一条微博的
                'verified':            userInfo['verified'],
                'verified_type':       userInfo['verified_type'],
                'verified_type_label': verified_type_label,
                'gender':              userInfo['gender'],
                'number':              userInfo.get('mbrank', 0),
                'verified_detail':     userInfo.get('verified_detail', []),  # 认证详情
        }
        return user

    def comment_details_cleaning(self, data):
        """
        评论详情数据清理
        Args:
            data:

        Returns:

        """
        status = data['status']
        root_comment = data['rootComment']
        user = {
                'id':             root_comment['user']['id'],
                'screen_name':    root_comment['user']['screen_name'],
                'name':           root_comment['user']['screen_name'],
                'followers':      root_comment['user']['followers_count'],
                'friends_count':  root_comment['user'].get('friends_count', 0),
                'statuses_count': root_comment['user']['statuses_count'],
                'avatar':         root_comment['user']['avatar_hd']
        }
        url = f'https://weibo.com/{status["user"]["id"]}/{status["id"]}'
        mid, urls = self.url_to_mid(url)
        return {
                'text':         root_comment['text'],
                'mid':          root_comment['id'],
                'floor_number': root_comment['floor_number'],  # 楼层数
                'like_counts':  root_comment['like_counts'],  # 点赞数
                'comment_time': self.cst_to_str(root_comment['created_at']),
                'user':         user,
                'article':      self.article_cleaning(status, url, urls)
        }

    def profile_statuses_cleaning(self, data):
        """
        微博主页数据获取 返回可见的博文列表
        Args:
            data:

        Returns:

        """
        params = [

        ]
        for card in data['cards']:
            # card_type=>9 是博文  其他的类型可能是广告置顶或者其他没有具体分析
            if card['card_type'] != 9:
                continue
            blog = card['mblog']
            url = f"https://weibo.com/{blog['user']['id']}/{blog['id']}"
            mid, urls = self.url_to_mid(url)
            params.append(self.article_cleaning(blog, url, urls))
        return params
