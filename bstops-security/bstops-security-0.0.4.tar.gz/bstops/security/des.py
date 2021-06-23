#!/usr/bin/env python

import base64
from Crypto.Cipher import DES as alog

base64.MAXBINSIZE = 1024

class DES:

    def __init__(self, key='Oxdbw8YV', padding='\0'):
        # key 只能 8 個字元
        self.key = key
        self.padding = padding

    def fill(self, value, padding, num=8):
        """填充字符"""
        if isinstance(value, str):
            value = value.encode('utf8')
        if isinstance(padding, str):
            padding = padding.encode('utf8')
        while len(value) % num != 0:
            value += padding
        return value

    def encrypt(self, msg):
        cryptor = alog.new(self.fill(self.key, self.padding), alog.MODE_ECB)
        code = cryptor.encrypt(self.fill(msg, self.padding))
        code = base64.encodebytes(code).decode('utf8').strip()
        return code

    def decrypt(self, code):
        cryptor = alog.new(self.fill(self.key, self.padding), alog.MODE_ECB)
        code = base64.decodebytes(code.encode('utf8'))
        msg = cryptor.decrypt(code).decode('utf8').replace(self.padding, '')
        return msg

    def pass_encrypt(self, user, pwd, split='の'):
        """
        用戶、密碼加密
        :param user(str): user
        :param pwd(str): password
        :return: key(str)
        """
        string = f'{user}{split}{pwd}'
        key = self.encrypt(string)
        return key.strip()

    def pass_decrypt(self, key, split='の'):
        """
        用戶、密碼解密
        :param key(str):
        :return: user(str), pwd(str)
        """
        string = self.decrypt(key)
        user, pwd = string.split(split)
        return user, pwd