#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import httpx
import random


def get_proxy():
    url = f'http://ip.ipjldl.com/index.php/api/entry?method=proxyServer.generate_api_url&packid=0&fa=0&fetch_key=&groupid=0&qty=1&time=1&pro=&city=&port=1&format=txt&ss=1&css=&ipport=1&dt=1&specialTxt=3&specialJson=&usertype=2'
    try:
        resp = httpx.get(url)
        while ':' not in resp.text:
            time.sleep(random.randint(1, 3))
            resp = httpx.get(url)
        else:
            print(f'获取到代理IP:' + resp.text)
            return resp.text
    except Exception as e:
        print(e)
