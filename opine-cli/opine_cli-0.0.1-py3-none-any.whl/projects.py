import os
import requests
import json
import tabulate
import pandas as pd
from colorama import Fore, Style
from opinecli.config import ConfigUtils

class Projects(object):
    def __init__(self):
        self.__config_utils = ConfigUtils() 
    
    def list(self, org='o', output='table'):
        config_data = self.__config_utils.get()
        params = {"user_id":config_data["user"]["id"],"org_id":org,"private":"1"}
        headers = {"content-type": "application/json", "authorization": f'Token {config_data["user"]["access_token"]}'}        
        result = requests.post(f'{config_data["api_endpoint"]}/projects/user', json=params, headers=headers)
        keys = ['id','title','owner_id', 'created', 'modified']
        print()
        if output == 'json':
            data = [{key: item[key] for key in keys} for item in result.json()['results']] 
            print(json.dumps(data, indent=2))
        elif output == 'table':
            df = pd.DataFrame(result.json()['results'])
            df = df[keys]
            print(tabulate.tabulate(df, headers=keys, tablefmt="simple", colalign=("left",)))
        print()

    def describe(self, project_id=''):
        if not project_id:
            project_id = ProjectsUtils().get_default_project()
        if not project_id:
            return ""
        config_data = self.__config_utils.get()
        params = {"id":project_id,"user_id":config_data["user"]["id"]}        
        headers = {"content-type": "application/json", "authorization": f'Token {config_data["user"]["access_token"]}'}        
        result = requests.post(f'{config_data["api_endpoint"]}/projects', json=params, headers=headers)
        print()
        print(json.dumps(result.json()['results'], indent=2, sort_keys=True))
        print()

    def stats(self, project_id='', output='table'):
        """ 
        Get project statistics
        """
        if not project_id:
            project_id = ProjectsUtils().get_default_project()
        if not project_id:
            return ""
        config_data = self.__config_utils.get()
        params = {"id":project_id,"user_id":config_data["user"]["id"]}        
        headers = {"content-type": "application/json", "authorization": f'Token {config_data["user"]["access_token"]}'}        
        result = requests.post(f'{config_data["api_endpoint"]}/projects/stats', json=params, headers=headers)
        stats = result.json()['results']
        stats['data_values'] = stats['fields'] * stats['data_records']
        print()
        if output == 'json':
            print(json.dumps(stats, indent=2))
        elif output == 'table':
            print(tabulate.tabulate([(k, v) for k,v in stats.items()]))
        print()

class ProjectsUtils(object):

    def __init__(self):
        self.__config_utils = ConfigUtils() 

    def get_default_project(self):
        config_data = self.__config_utils.get()
        if 'project_id' not in config_data:
            print()
            print(Fore.RED + 'A project id is required. See --help' + Style.RESET_ALL)
            print()
            return
        else:
            project_id = config_data['project_id']
            print()
            print(Style.BRIGHT + Fore.CYAN + "project_id: " + project_id + Style.RESET_ALL)
            return project_id