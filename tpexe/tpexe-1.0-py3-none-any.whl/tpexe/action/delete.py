
import sys
import os
import requests
import json
import yaml
import pyotp
from tpexe.login.login import Login
from tpexe.conf.conf import GetConfig

CONF_PATH = './config.yaml'


class Delete(object):
    def search_host(self, url, headers, search_ip, conf_data, _sid):
        url = url + '/host/list'
        headers['Referer'] = conf_data['url'] + '/host'
        headers['Cookie'] = '_sid=' + _sid
        post_payload = {
            'args': '{"filter":{"host_group":0,"host_sys_type":0,"search":"' + search_ip + '"},"order":null,"limit":{"page_index":0,"per_page":10}}'
        }
        re = requests.post(url, data=post_payload, headers=headers)
        if re.json()['code'] == 0:
            try:
                return re.json()['data']['data'][0]['auth_list'][0]['host_id']
            except Exception as e:
                print(search_ip, e, re.json())
        else:
            print(re.json())
            sys.exit()

    def delete_host(self, url, headers, host_id, conf_data, _sid, host_ip):
        url = url + '/host/delete-host'
        headers['Referer'] = conf_data['url'] + '/host'
        headers['Cookie'] = '_sid=' + _sid
        post_payload = {
            'args': '{"host_list":[' + str(host_id) + ']}'
        }
        re = requests.post(url, data=post_payload, headers=headers)
        try:
            if re.json()['code'] == 0:
                print('Del host: %s' % host_ip)
        except Exception as e:
            print('Del err: no nush host %s' % host_ip)

    def delete_host_run(self):
        login = Login()
        getconfig = GetConfig(CONF_PATH)

        del_host_list = [host.replace('\n', '').replace(' ', '') for host in open('delete_hosts', 'r').readlines()]
        conf_data = getconfig.get_yaml_conf_data()
        _sid = login.login(conf_data['url'], conf_data['secret'], conf_data['login_user'], conf_data['login_passwd'],
                           login.get_login_headers(conf_data))

        for search_ip in del_host_list:
            host_id = self.search_host(conf_data['url'], login.get_login_headers(conf_data), search_ip, conf_data, _sid)
            self.delete_host(conf_data['url'], login.get_login_headers(conf_data), host_id, conf_data, _sid, search_ip)
