# Created by Jan Rummens at 18/01/2021
import json

import requests
from bs4 import BeautifulSoup
from jira import JIRA
from requests.auth import HTTPBasicAuth


def merge_json_xml(scenario_file, jira_flag=False):
    #read the scenario file into memory
    soup = None
    with open(scenario_file + ".xml") as fp:
        soup = BeautifulSoup(fp, "lxml")
        fp.close()

    # read the json zephyr file into memory
    data_json = None
    with open(scenario_file + ".json") as json_file:
        data_json = json.load(json_file)
        json_file.close()

    jira_id = 0
    #create an item in JIRA on the basis of the json configuration defintion
    if jira_flag:
        jira_connection = JIRA('https://jira.antwerpen.be', basic_auth=('user', 'pw'))
        jira_id = jira_connection.create_issue( project=data_json['plugin']['zephyr']['project'],
                                                summary=data_json['plugin']['zephyr']['summary'],
                                                description=data_json['plugin']['zephyr']['description'],
                                                issuetype={'name': 'Test'})


    #Merge json with xml
    root_tag = soup.graph
    new_tag_plugin = soup.new_tag("plugin")
    new_tag_zephyr = soup.new_tag("zephyr")
    new_tag_zephyr.attrs['project'] = data_json['plugin']['zephyr']['project']
    new_tag_zephyr.attrs['summary'] = data_json['plugin']['zephyr']['summary']
    new_tag_zephyr.attrs['description'] = data_json['plugin']['zephyr']['description']
    #id needed and is returned by the jira system
    new_tag_zephyr.attrs['id'] = jira_id
    new_tag_plugin.append(new_tag_zephyr)
    root_tag.append(new_tag_plugin)
    root_tag.prettify()
    with open( scenario_file + ".xml", 'w') as f:
        f.write(str(root_tag))
        f.close()


def set_jira_item_status(jira_number, jira_project, status=1):
    baseURL = 'https://jira.antwerpen.be'
    jira_connection = JIRA(baseURL, basic_auth=('User', 'pw'))
    issue = jira_connection.issue(jira_number)
    issue_id = issue.id
    jira_project = jira_connection.project( jira_project )
    jira_project_id = jira_project.id

    #get execution id
    headers = {'content-type': 'application/json', 'accept': 'application/json'}
    parameters = {'issueId': issue_id}
    get_execution_list = baseURL + ("/rest/zapi/latest/execution")
    response = requests.get(get_execution_list,
                     auth=HTTPBasicAuth('User', 'pw'),
                     params=parameters,
                     headers=headers)
    response_dict = response.json()
    executions_list = response_dict['executions']
    execution_id = executions_list[0]['id']

    put_execution_status = baseURL + ("/rest/zapi/latest/execution/%d/execute" % (execution_id))
    headers = {'content-type': 'application/json'}
    payload_status = { "status": str(status) }
    r = requests.put(put_execution_status,
                     auth=HTTPBasicAuth('User', 'pw'),
                     headers=headers,
                     params=parameters,
                     data=json.dumps(payload_status))