#!/usr/bin/python
# encoding: utf-8

import re
import json
import base64
import requests
import copy
import xml.etree.ElementTree as ET


class Client:

    def __init__(self, endpoint, job_auth_key):
        global false, true
        false, true = False, True
        self.endpoint = endpoint
        self.headers = {
            'X-Xsrftoken': 'zQtY4sw7sqYspVLrqV',
            "Sdk-Method": "zQtY4sw7sqYspVLrqV",
            'Cookie': f'auth_key={job_auth_key}'
        }

    def mission_start(self, flow_id, params, task_name='', user='', start_time=''):
        accept_url = self.endpoint + "/api/job/v1/flow/accept/create/"
        params = json.dumps(params).encode("utf-8")
        body = dict(
            flow_version_id=flow_id,  ### 模板ID 提前配置
            order_name=task_name,  ### 任务名称  加个索引标记 方便查询
            global_params=base64.b64encode(params).decode("utf-8"),  ### 参数必须为json类型，并且要base64编码
            creator=user,
            details=''  ### 备注数据
        )
        if start_time: body.update({'start_time': start_time})
        respond = requests.post(url=accept_url, data=json.dumps(body), headers=self.headers)
        print(respond.text)
        return respond

    def mission_log(self, mission_id):
        ### 查看日志
        params = {'list_id': mission_id}
        logs_url = self.endpoint + "/api/job/v1/job/logs/"
        response = requests.get(url=logs_url, params=params, headers=self.headers).json()
        return response.get('data')

    def mission_retry(self, mission_id):
        ### 重做任务
        body = {'flow_run_id': mission_id, 'do_type': 'redo'}
        redo_url = self.endpoint + "/api/job/v1/flow/current/list/"
        response = requests.put(url=redo_url, data=json.dumps(body), headers=self.headers).json()
        return response

    def mission_stop(self, mission_id):
        ### 终止任务
        body = {'flow_run_id': mission_id, 'do_type': 'stop'}
        redo_url = self.endpoint + "/api/job/v1/flow/current/list/"
        response = requests.patch(url=redo_url, data=json.dumps(body), headers=self.headers).json()
        return response

    def get_flow_id_by_name(self, temp_name):
        params = {'flow_name': temp_name}
        state_url = self.endpoint + "/api/job/v1/flow/design/version/new/"
        response = requests.get(url=state_url, params=params, headers=self.headers)
        try:
            flow_id = response.json().get('data', {}).get('id')
            return flow_id
        except Exception as err:
            raise Exception(f"从JOB流程系统获取任务流ID信息失败：{response.text}；{err}")

    def get_template_info(self, temp_name):
        params = {'flow_name': temp_name}
        state_url = self.endpoint + "/api/job/v1/flow/design/version/new/"
        response = requests.get(url=state_url, params=params, headers=self.headers)
        try:
            flow_xml = response.json().get('data', {}).get('flow_xml', '')
            return re.search('<definitions[\s\S]*</definitions>', flow_xml).group()
        except Exception as err:
            raise Exception(f"从JOB流程系统获取模板信息失败：{response.text}；{err}")

    def get_mission_xml(self, mission_id):
        params = {'flow_run_id': mission_id}
        state_url = self.endpoint + "/api/job/v1/flow/run/chart/"
        response = requests.get(url=state_url, params=params, headers=self.headers)
        return response.json().get('data', '')

    def current_mission_list(self):
        state_url = self.endpoint + "/api/job/v1/flow/current/list/"
        try:
            response = requests.get(url=state_url, headers=self.headers).json()
            return response.get('data', [])
        except Exception as err:
            print(err)
            return []

    def resolve_template(self, temp_name):
        bpmProcess = "{http://www.omg.org/spec/BPMN/20100524/MODEL}process"
        serviceTask = "{http://www.omg.org/spec/BPMN/20100524/MODEL}serviceTask"
        sequenceFlow = "{http://www.omg.org/spec/BPMN/20100524/MODEL}sequenceFlow"
        incoming = "{http://www.omg.org/spec/BPMN/20100524/MODEL}incoming"
        # outgoing = "{http://www.omg.org/spec/BPMN/20100524/MODEL}outgoing"
        data_as_string = self.get_template_info(temp_name)
        root = ET.fromstring(data_as_string)
        process_xml = root.find(bpmProcess)
        bpmn_sequence_dict = dict()
        [bpmn_sequence_dict.update({x.attrib.get('id'): x.attrib}) for x in process_xml.findall(sequenceFlow)]
        parent_dict = dict()
        name_map = dict()
        is_service = dict()
        for c in process_xml:
            for i in c:
                if i.tag == incoming:
                    sequence_id = i.text  ### 本节点的流入连线的ID
                    parent_id = bpmn_sequence_dict.get(sequence_id).get('sourceRef')
                    flow_bpm_id = c.attrib.get('id')
                    flow_bpm_name = c.attrib.get('name', flow_bpm_id)
                    parent_dict.update({flow_bpm_id: parent_id})
                    name_map.update({flow_bpm_id: flow_bpm_name})
                    is_service.update({flow_bpm_id: c.tag == serviceTask})
        steps = []
        while parent_dict:
            temp_dict = copy.deepcopy(parent_dict)
            for cid, pid in temp_dict.items():
                parent_name = name_map.get(pid, None)
                if not parent_name:
                    steps.insert(0, cid)
                    del parent_dict[cid]
                elif pid in steps:
                    steps.insert(steps.index(pid) + 1, cid)
                    del parent_dict[cid]
        service_steps = []
        [service_steps.append({'title': name_map[i], 'node_id': i}) for i in steps if is_service[i]]
        return service_steps
