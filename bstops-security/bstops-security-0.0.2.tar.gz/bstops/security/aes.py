#!/usr/bin/env python

import base64
from Crypto.Cipher import AES
# key 只能 16,24,32 個字元
key = 'fKzQ7wkUvdbTprh5KDf_H9B8sSF'
padding = '\0'


def fill(value, num=16, padding=padding):
    """
    填充字符
    """
    if isinstance(value, str):
        value = value.encode('utf8')
    if isinstance(padding, str):
        padding = padding.encode('utf8')
    while len(value) % num != 0:
        value += padding
    return value


def encrypt(msg):
    cryptor = AES.new(fill(key), AES.MODE_ECB)
    code = cryptor.encrypt(fill(msg))
    code = base64.encodebytes(code).decode('utf8').strip()
    return code


def decrypt(code):
    cryptor = AES.new(fill(key), AES.MODE_ECB)
    code = base64.decodebytes(code.encode('utf8'))
    msg = cryptor.decrypt(code).decode('utf8').replace(padding, '')
    return msg


def pass_encrypt(user, pwd, split='の'):
    """
    用戶、密碼加密
    :param user(str): user
    :param pwd(str): password
    :return: key(str)
    """
    string = f'{user}{split}{pwd}'
    key = encrypt(string)
    return key.strip()


def pass_decrypt(key, split='の'):
    """
    用戶、密碼解密
    :param key(str):
    :return: user(str), pwd(str)
    """
    string = decrypt(key)
    user, pwd = string.split(split)
    return user, pwd