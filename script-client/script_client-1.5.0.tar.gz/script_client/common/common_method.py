'''
common method
'''

import os
import sys
import json
import socket
import shutil
import importlib
from importlib import reload
from loguru import logger
from script_client.const import config,fm
from script_client.common.my_requests import MyRequests



def find_script():
    l=[]
    if os.path.exists(os.sep.join([config.work_path,'test_script'])):
        for root, dirs, files in os.walk(os.sep.join([config.work_path,'test_script'])):
            for file in files:
                if os.path.splitext(file)[1] == '.py':
                    l.append(os.path.splitext(file)[0])
        return l
    else:
        return False

def save_script(f_path,f_text):
    try:
        with open(f_path, 'w', encoding='utf-8') as f:
            f.write(f_text)
        return True
    except Exception as e:
        return e

def upload_script(f_path,files):
    try:
        for meta in files:
            with open(f_path, 'wb+') as f:
                f.write(meta['body'])
        return True
    except Exception as e:
        return e

def del_script(f_path):
    try:
        pass
        return True
    except Exception as e:
        return e

def import_and_regist():
    # import
    l = find_script()
    if l != False :
        for i in l:
            importlib.import_module(f"test_script.{i}")
    # regist
    ret = regist_app()
    if ret == True:
        logger.info(f"注册映射关系完成")
        return True
    return False

def reload_script():
    l = (find_script())
    # print(sys.modules.keys())
    fm.empty_map()
    for i in l:
        module = sys.modules['test_script.'+i]
        reload(module)
        # print(f"reload了{i}")
    regist_app()


def get_tree():
    tree = [
        {
            "title": "test_script",
            'spread': 'true',
            # "children": [
            #     {
            #         "title": "西安",
            #     },
            #     {
            #         "title": "延安",
            #     }
            # ]
        }
    ]
    children = []
    l = find_script()
    if l != False:
        for i in l:
            children.append({'title': i})
    tree[0]['children'] = children
    return tree


def is_none(kwargs):
    '''
    0、空、None、False 外都算 True
    :param kwargs:
    :return:
    '''
    ll = []
    for k, v in kwargs.items():
        ll.append(v)
    if all(ll):
        return False
    return True


def del_path(path):
    '''
    删文件夹，以及文件夹内的文件
    :param path:
    :return:
    '''
    try:
        shutil.rmtree(path)
    except Exception as e:
        logger.error(f"清空 {path} 出错 ：{e}")


def del_all_file(path):
    '''
    删目录下所有文件，包括子目录内
    :param path:
    :return:
    '''
    for i in os.listdir(path):
        path_file = os.sep.join([path, i])
        if os.path.isfile(path_file):
            os.remove(path_file)
        else:
            del_all_file(path_file)


def robot_send_message(msg_type='text', message=''):
    try:
        if config.robot_url != '':
            mr = MyRequests(timeout=config.http_request_timeout)
            url = config.robot_url
            json = {
                "msg_type": msg_type,
                "content": {
                    "text": message
                }
            }
            rep = mr.run(method='post', url=url, json=json)
            if isinstance(rep, str) or rep.status_code != 200 or rep.json()['StatusMessage'] != 'success':
                return False
            return True
    except Exception as e:
        logger.error(f"{e}")
        return False


def regist_app():
    try:
        data = {
            'is_quanliang': 0,  # 0重启服务全量更新  非0追加
            'registry': []
        }
        for k, v in fm.get_map().items():
            t_d = {
                'scriptclient_name': config.client_name,
                'app_code': '',
                'ip': config.local_ip,
                'port': str(config.local_port),
                'path': []
            }
            t_d['app_code'] = k
            for kk, vv in v.items():
                t_l = []
                for vvv in vv:
                    for kkkk, vvvv in vvv.items():
                        t_j = {'name':vvvv['name'],'value':kkkk.__name__}
                        t_l.append(t_j)
                tt_d = {'moniter_path': kk, 'function': t_l}
                t_d['path'].append(tt_d)
            data['registry'].append(t_d)
        url = config.regist_server_url
        mr = MyRequests(config.http_request_timeout)
        # logger.info(data)
        rep = mr.run(url=url, method='post', json=data)
        if isinstance(rep, str) or rep.status_code != 200:
            msg = f"注册失败 接口返回 = {rep}"
            logger.error(msg)
            return msg
        else:
            # logger.info(f"注册成功--{data}")
            return True
    except Exception as e:
        logger.error(f'注册失败:{e}')
        return f'注册失败:{e}'


def str_to_dict(str):
    str_t = str.replace(r'\r\n', '')
    str_e = str_t.replace("'", '"')
    return json.loads(str_e)

def replace_str(s):
    s = s.replace('\r\n', '')
    s = s.replace('\n', '')
    return s


def get_local_ip():
    local_ip = ""
    try:
        socket_objs = [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]
        ip_from_ip_port = [(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close()) for s in socket_objs][0][1]
        ip_from_host_name = [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if
                             not ip.startswith("127.")][:1]
        local_ip = [l for l in (ip_from_ip_port, ip_from_host_name) if l][0]
    except (Exception) as e:
        print("get_local_ip found exception : %s" % e)
    return local_ip if ("" != local_ip and None != local_ip) else socket.gethostbyname(socket.gethostname())



if "__main__" == __name__:
    # del_path(r'D:\1\2 python code\script_client\test_script\1')
    pass
