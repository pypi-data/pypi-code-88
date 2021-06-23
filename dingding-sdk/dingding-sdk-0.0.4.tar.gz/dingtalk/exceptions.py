#!/usr/bin/python3
# @Time    : 2021-06-18
# @Author  : Kevin Kong (kfx2007@163.com)


class DingTalkException(Exception):

    def __init__(self, errcode=None, sub_code=None, sub_msg=None, errmsg=None, request_id=None):
        self.errcode = errcode
        self.sub_code = sub_code
        self.sub_msg = sub_msg
        self.errmsg = errmsg
        self.request_id = request_id

    def __str__(self):
        return f"errcode: {self.errcode}, errmsg:{self.errmsg}, request_id:{self.request_id} submsg:{self.sub_msg or ''}"
