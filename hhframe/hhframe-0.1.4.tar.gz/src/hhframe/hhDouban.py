
# -*- codeing = utf-8 -*-
# @File：hhDouban.py
# @Ver：1.0.0
# @Author：立树
# @Time：2021/6/11 17:01
# @IDE：PyCharm

import re
import execjs
from .hhAjax import hhGet

class hhDouban(object):

    def __init__(self):
        pass

    def search(self,opt={}):
        # 配置
        hhOpt = {
            "search": "",
            "decrypt": ""
        }
        hhOpt.update(opt)

        # 参数判断
        if hhOpt["search"]=="" or hhOpt["decrypt"]=="":
            print("hhframe.hhDouban Error - 请补全参数（search、decrypt）")
            return {}

        try:
            # 发起请求
            page = hhGet(f"https://search.douban.com/movie/subject_search?search_text={hhOpt['search']}&cat=1002")

            # 获取加密数据
            encrypt = re.search('window.__DATA__ = "([^"]+)"',page).group(1)
            # print(encrypt)

            # 提取解密 js
            with open(hhOpt["decrypt"], "r", encoding="UTF-8", errors="ignore") as f:
                decrypt_js = f.read()
                # print(decrypt_js)

            # 解密数据
            ctx = execjs.compile(decrypt_js)
            ret = ctx.call("decrypt",encrypt)
            return ret["payload"]
        except Exception as err:
            print(f"hhframe.hhDouban Error - {err}")
            return {}
