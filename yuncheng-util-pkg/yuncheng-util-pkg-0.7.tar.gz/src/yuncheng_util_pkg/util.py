import requests
import json
import os

def get_for_request(url,session=None):
    '''
    发送get请求
    :param url:
    :param session:
    :return:
    '''
    result = "error"
    if session is None:
        result = requests.get(url)
    else:
        result = session.get(url)
    if result.status_code != 200:
        return "error"
    else:
        return json.loads(result.text)
def post_for_request(url,requestbody,session=None):
    '''
    发送post请求
    :param url:
    :param requestbody:
    :param session:
    :return:
    '''
    result = "error"
    if session is None:
        result = requests.post(url,json=requestbody)
    else:
        result = session.post(url,json=requestbody)
    if result.status_code != 200:
        return "error"
    else:
        return json.loads(result.text)

def make_dirs(path):
    '''
    创建文件夹，
    :param path:
    :return:
    '''
    if os.path.isdir(path) and os.path.exists(path) is False:
        os.makedirs(path)
