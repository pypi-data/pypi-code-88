# -*- coding: utf-8 -*-
import urllib
import imghdr
import urllib.request
from urllib import request
from PIL import Image
import requests
import os
import base64
from Tool.joker_tool.base_tool import BaseTool


class ImgDispose(object):
    def __init__(self, *args, **kwargs):
        super.__init__(*args, **kwargs)

    def img_suffix(self, url):
        """
        检测图片的类型
        :param url:图片的url链接
        :return:
        """
        response = urllib.request.urlopen(url)
        file = response.read()
        suffix = imghdr.what('', file)
        return suffix

    def img_size(self, url):
        res = request.urlopen(url)
        img = Image.open(res)
        return img.size

    def save_img(self, url, name, suffix):
        """图片保存到本地"""
        img = requests.get(url)
        if not os.path.exists("img"):
            os.mkdir("img")
        img_path = "img\{}.{}".format(BaseTool().md5(name), suffix)
        with open(img_path, 'wb+') as f:
            f.write(img.content)
            f.close()
        return img_path

    def base64_to_img(self, base64_str):
        imgdata = base64.b64decode(base64_str)
        file = open('.jpg', 'wb')
        file.write(imgdata)
        file.close()
