from tpexe.login.login import Login
from tpexe.conf.conf import GetConfig

import math
import json
import os
import sys
import requests

# CSV_PATH = 'teleport.csv'
CONF_PATH = './config.yaml'


class Alloc(object):

    def __init__(self, csv):
        self.csv = csv
        if os.path.exists(self.csv):
            self.f = open(self.csv, 'r', encoding='utf8')
        else:
            print('teleport.csv: no such file or dir!')
            sys.exit()

    def get_new_host_list(self):
        """
            获取需要将权限授给用户的服务器列表
        """
        new_host_list = []
        data = self.f.read().split()
        for row in data:
            new_host_list.append(row.split(',')[0])
        return new_host_list

    def get_opt_headers(self, conf_data):
        server_url = conf_data['url']
        user_list = conf_data['user_list']
        permission_user = conf_data['permission_user']
        referer_url = server_url + "/user/auth/" + permission_user
        headers = conf_data['headers']
        host_group = conf_data['host_group']
        headers['Referer'] = referer_url
        headers['Origin'] = server_url
        headers['Host'] = server_url.split('//')[1]
        return headers

    def host_list(self, headers, page_index, host_group, server_url):
        """
             获取授权页面下部分该用户未拥有权限的所有服务器，
        """
        args = {
            'args': '{"filter":{"host_group":' + host_group + ',"host_sys_type":0,"search":""},"order":{"k":"host_id","v":true},"limit":{"page_index":' + page_index + ',"per_page":100}}'
        }
        url = server_url + '/host/list'
        ret = requests.post(url, data=args, headers=headers)
        try:
            if json.loads(ret.text)["code"] != 0:
                print("Get host list error！")
                sys.exit()
            else:
                return json.loads(ret.text)["data"]
        except json.JSONDecodeError:
            print(ret.text)

    def alloc_host_user(self, headers, user_list, host_list_data, permission_user, server_url):
        """
            将获取的需要授权的服务器以及服务器验证信息列表host_list_data进行授权
        """
        print("    Authorizing...")
        args_host_list = {
            "host_list": {},
            "user_name": permission_user
        }
        post_url = server_url + '/user/alloc-host-user'
        new_host_list = self.get_new_host_list()
        get_host_list = host_list_data['data']

        old_host_list = []
        for host in get_host_list:
            old_host_list.append(host["host_desc"])

        host_dict = {}
        for host in new_host_list:
            if host in old_host_list:
                for old_host in get_host_list:
                    if host == old_host["host_desc"]:
                        host_dict[str(old_host["host_id"])] = []
                        # old_host["host_id"]
                        for auth_info in old_host["auth_list"]:
                            if auth_info["user_name"] in user_list:
                                host_dict[str(old_host["host_id"])].append(auth_info["host_auth_id"])
        args_host_list["host_list"] = host_dict
        args_host_list_form = str(args_host_list).replace(' ', '').replace('\'', '\"')
        post_payload = {
            'args': args_host_list_form
        }
        if len(host_dict) == 0:
            print("    No host at this page...")
            return
        else:
            post_ret = requests.post(post_url, data=post_payload, headers=headers)
        try:
            if json.loads(post_ret.text)["code"] != 0:
                print("    Authorizing error！")
                print(post_ret.json()['message'])
                sys.exit()
            else:
                print('    {} hosts authorized.'.format(len(host_dict)))
                # return json.loads(post_ret.text)["data"]
        except json.JSONDecodeError:
            print(post_ret.text)

    def alloc_run(self):
        login = Login()
        getconf = GetConfig(CONF_PATH)

        ydata = getconf.get_yaml_conf_data()
        login_headers = login.get_login_headers(ydata)

        _sid = login.login(ydata['url'], ydata['secret'], ydata['login_user'], ydata['login_passwd'], login_headers)
        opt_headers = self.get_opt_headers(ydata)
        opt_headers['Cookie'] = '_sid=' + _sid

        server_url = ydata['url']
        host_group = ydata['host_group']
        user_list = ydata['user_list']
        permission_user = ydata['permission_user']
        page_count = math.ceil(self.host_list(opt_headers, '0', str(host_group), server_url)["total"] / 100)
        if page_count < 1:
            print('Config item "page_count" is {} less then 1, but must bigger then 1 or eval 1'.format(page_count))
            sys.exit()
        elif page_count == 1:
            print("****Get host list that user need permission at page {}...".format(page_count))
            host_list_data = self.host_list(opt_headers, '0', str(host_group), server_url)
            self.alloc_host_user(opt_headers, user_list, host_list_data, permission_user, server_url)
        else:
            for page_index in range(0, page_count):
                print("****Get host list that user need permission at page {}...".format(page_index + 1))
                host_list_data = self.host_list(opt_headers, str(page_index), str(host_group), server_url)
                self.alloc_host_user(opt_headers, user_list, host_list_data, permission_user, server_url)
