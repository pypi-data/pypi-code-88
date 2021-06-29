import requests
import json
import tabulate
import pandas as pd
from opinecli.config import ConfigUtils
from opinecli.projects import ProjectsUtils

class Data(object):
    def __init__(self):
        self.__config_utils = ConfigUtils()
    
    def count(self, project_id=''):
        """ 
        Count project data records. And empty project id defaults to the last project id saved in config.
        """
        config_data = self.__config_utils.get()
        
        if not project_id:
            project_id = ProjectsUtils().get_default_project()
        if not project_id:
            return ""
        params = {"id":project_id,"user_id":config_data["user"]["id"]}        
        headers = {"content-type": "application/json", "authorization": f'Token {config_data["user"]["access_token"]}'}        
        result = requests.post(f'{config_data["api_endpoint"]}/projects/stats', json=params, headers=headers)
        stats = result.json()['results']
        stats['data_values'] = stats['fields'] * stats['data_records']
        print(f"Records counts: {stats['data_records']}")
        print()
    
    def list(self, project_id='', output='table'):
        if not project_id:
            project_id = ProjectsUtils().get_default_project()
        if not project_id:
            return ""
        config_data = self.__config_utils.get()
        params = {"projectid":project_id,"filters":[],"coded":1,"sortby":"data._id","sortdir":"descending","page":1,"limit":"1000000"}
        headers = {"content-type": "application/json", "authorization": f'Token {config_data["user"]["access_token"]}'}        
        result = requests.post(f'{config_data["api_endpoint"]}/data/all', json=params, headers=headers)
        keys = ['rid','xstatus', 'username', 'xcreated','xfinish', 'xsource', 'xsourceversion']
        data = [{key: item[key] for key in keys} for item in result.json()['results']['records']] 
        print()
        if output == 'json':            
            print(json.dumps(data, indent=2))
        elif output == 'table':
            df = pd.DataFrame(data)
            df = df[keys]
            print(tabulate.tabulate(df, headers=keys, tablefmt="simple", colalign=("left",)))
        print()

    def describe(self, project_id='', record_id=''):
        if not project_id:
            project_id = ProjectsUtils().get_default_project()
        if not project_id:
            return
        if not record_id:
            print("record_id is required.")
            return
        config_data = self.__config_utils.get()
        params = {"project_id":project_id,"record":record_id}       
        headers = {"content-type": "application/json", "authorization": f'Token {config_data["user"]["access_token"]}'}        
        result = requests.post(f'{config_data["api_endpoint"]}/data/project', json=params, headers=headers)
        print()
        print(json.dumps(result.json()['results'], indent=2, sort_keys=True))
        print()