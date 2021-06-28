
# -*- codeing = utf-8 -*-
# @File：hhAjax.py
# @Ver：1.0.0
# @Author：立树
# @Time：2021/5/26 13:38
# @IDE：PyCharm

# 测试网站：http://httpbin.org

import urllib.request,urllib.error,urllib.parse

def hhGet(url,decode="utf-8"):
    # 请求数据
    html = ""
    request = urllib.request.Request(
        url = urllib.request.quote(url,safe=";/?:@&=+$,",encoding="utf-8"),
        method = "GET",
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"
        }
    )
    # 发起请求
    try:
        response = urllib.request.urlopen(request,timeout=30)
        html = response.read().decode(decode,"ignore")
    except urllib.error.URLError as err:
        if hasattr(err,"code"):
            print(err.code)
        if hasattr(err,"reason"):
            print(err.reason)
    return html


def hhPost(url,data={},decode="utf-8"):
    # 请求数据
    html = ""
    request = urllib.request.Request(
        url,
        data=bytes(urllib.parse.urlencode(data),encoding="utf-8"),
        method="POST",
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"
        }
    )

    # 发起请求
    try:
        response = urllib.request.urlopen(request)
        # 对获取到的网页源码进行 utf-8 解码
        html = response.read().decode(decode,"ignore")
    except urllib.error.URLError as err:
        if hasattr(err,"code"):
            print(err.code)
        if hasattr(err,"reason"):
            print(err.reason)
    return html
