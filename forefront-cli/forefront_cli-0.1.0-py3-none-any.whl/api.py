import pickle
from pathlib import Path
import os.path
import tarfile
from typing import Optional, Mapping, NoReturn, Any, List, Union
import requests
from requests.api import head
from .common import get_user_token, get_project_id


base_url = 'http://live-server.forefront.link/api'
base_dashboard_url = 'http://app.tryforefront.com'

endpoints_url = base_url + '/endpoints'
versions_url = base_url + '/versions'


def fetch_projects():
    headers = {"authorization": get_user_token()}
    projects = requests.get(endpoints_url, headers=headers)

    if projects.status_code == 450:
        print('Error with login. Please log in again.')
        return None

    return projects.text


def create_project(title, description):
    headers = {"authorization": get_user_token()}

    try:
        res = requests.post(endpoints_url,
                            json={"title": title, "description": description},
                            headers=headers
                            )
        return res.text
    except:
        print('Error creating project')


def make_tarfile(output_filename: str, source_dir: str):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))


class API:
    key: str
    endpoints: Mapping[str, str]
    methods: Mapping[str, str]
    base_endpoint: str
    organization_id: str
    project_id: str

    def __init__(self, key: str = get_user_token(), project_id: str = get_project_id(), base_url=base_url,  organization_id: Optional[str] = None):
        self.key = key
        self.project_id = project_id
        self.organization_id = organization_id
        self.base_endpoint = base_url
        self.endpoints = {
            'create_project': 'endpoints',
            'get_versions': 'versions',
            'delete_version': 'versions',
            'get_endpoints': 'endpoints',
            'delete_endpoint': 'endpoints',
            'deploy': 'versions',
            'upload': 'upload'
        }
        self.methods = {
            'create_project': 'POST',
            'get_versions': 'GET',
            'delete_version': 'DELETE',
            'get_endpoints': 'GET',
            'delete_endpoint': 'DELETE',
            'deploy': 'POST',
            'upload': 'POST'
        }

    def make_request(self, action: str, resource: Optional[str] = None, body=None) -> requests.Response:
        endpoint = self.make_endpoint(action, resource)
        method = self.methods[action]
        return requests.request(method=method, url=endpoint, json=body,
                                headers={'Authorization': self.key, 'Content-Type': 'application/json'})

    def make_endpoint(self, name: str, resource: Optional[str] = None) -> str:
        endpoint = f'{self.base_endpoint}/{self.endpoints[name]}'
        if resource:
            endpoint = endpoint + '/' + resource
            return endpoint
        else:
            return endpoint

    def create_project(self, name: str, description: Optional[str] = None) -> str:
        body: Any = {
            'title': name,
            'description': description,
            'orgId': self.organization_id,
        }
        try:
            action = 'create_project'
            response = self.make_request(action=action, body=body)
            return response.json()['endpointId']
        except Exception as e:
            raise e

    def get_versions(self) -> List[Any]:
        try:
            action = 'get_versions'
            response = self.make_request(action=action)
            if response is not None:
                return response.json()
            else:
                return []
        except Exception as e:
            raise e

    def get_projects(self) -> List[Any]:
        try:
            action = 'get_endpoints'
            response = self.make_request(action=action)
            if response is not None:
                return response.json()
            else:
                return []
        except Exception as e:
            raise e

    def delete_endpoint(self, endpoint):
        try:
            action = 'delete_endpoint'
            response = self.make_request(action=action, resource=endpoint)
            if response.status_code == 200:
                return 204
            else:
                return 500
        except Exception as e:
            raise e

    def delete_version(self, version):
        try:
            action = 'delete_version'
            response = self.make_request(action=action, resource=version)
            if response.status_code == 200:
                return 204
            else:
                return 500
        except Exception as e:
            raise e

    def upload_file(self, file_path: str) -> str:
        try:
            response = requests.post(self.make_endpoint(self.endpoints['upload']), headers={'Authorization': self.key},
                                     files={'file': open(file_path, 'rb')})
            url: str = response.json()['image']
            return url
        except Exception as e:
            raise e

    def deploy_tensorflow(self, model: Any, name: str, description: Optional[str] = None):
        try:
            path = '~/.forefront/model.h5'
            model.save(path)
        except:
            # either it's a TF2 model that can't be saved as a .h5, or an unknown error
            try:
                path = '~/.forefront/model'
                model.save(path)
                make_tarfile('~/.forefront/model.tar.gz', path)
                url: str = self.upload_file(path)
                body: Any = {
                    'title': name,
                    'description': description,
                    'file': url,
                    'orgId': self.organization_id,
                    'endpointId': self.project_id
                }
                response = self.make_request('deploy', body=body)
                print('Deployed successfully!')
                print(
                    f'Dashboard: {base_dashboard_url}/endpoints/{self.project_id}')
            except Exception as e:
                raise e

    def deploy_string_path(self,
                           model_path: str,
                           model_type: str,
                           name: str,
                           description: Optional[str],
                           handler_path: Optional[str] = None,
                           requirements_path: Optional[str] = None,
                           custom: Optional[bool] = False):
        try:
            model_exists = os.path.exists(model_path)
            if not model_exists:
                raise('Unable to find model file')

            if custom:
                handler_exists = os.path.exists(handler_path)
                requirements_exists = os.path.exists(requirements_path)
                if not handler_exists:
                    return 'Unable to find handler'
                if not requirements_exists:
                    return 'Unable to find requirementt'
                print('Perform custom deployment process')
                is_custom = True
                print('Uploading model file')
                model_url = self.upload_file(model_path)
                print('Uploading handler file')
                handler_url: str = self.upload_file(handler_path)
                print('Uploading requirements file')
                requirements_url: str = self.upload_file(requirements_path)
            else:
                print('Uploading model file')
                model_url = self.upload_file(model_path)

                is_custom = False
                handler_url = None
                requirements_url = None
            body: Any = {
                'title': name,
                'description': description,
                'file': model_url,
                'orgId': self.organization_id,
                'endpointId': self.project_id,
                'handler': handler_url,
                'requirements': requirements_url,
                'framework': model_type,
                'isCustom': is_custom
            }
            response = self.make_request('deploy', body=body)
            if response.status_code == 200:
                return f"{base_dashboard_url}/endpoints/{self.project_id}"
            else:
                return "Error deploying model. Please try again."
        except Exception as e:
            print(e)
            raise e

    def deploy_custom_model(self, model: Any, name: str, description: Optional[str] = None):
        path = '~/.forefront/model.pkl'
        print('Attempting to save as pickle')
        with open(path, 'wb') as f:
            pickle.dump(model, f)
        try:
            url: str = self.upload_file(path)
            body: Any = {
                'title': name,
                'description': description,
                'file': url,
                'orgId': self.organization_id,
                'endpointId': self.project_id
            }
            response = self.make_request('deploy', body=body)
            print('Deployed successfully!')
            print(
                f'Dashboard: {base_dashboard_url}/endpoints/{self.project_id}')
        except Exception as e:
            raise e

    def deploy_version(self,
                       name: str,
                       model: Union[str, Any],
                       description: Optional[str] = None,
                       model_type: Optional[str] = None,
                       handler_path: Optional[str] = None,
                       requirements_path: Optional[str] = None
                       ):
        # if model is a file path and model type is none
        if isinstance(model, str) and model_type is None:
            # passed a filepath to the model
            return self.deploy_string_path(
                model_path=model, name=name, description=description)

        # if model type is specified
        if isinstance(model_type, str):
            if model_type == 'tensorflow':
                self.deploy_tensorflow(model, name, description)
                return
            elif model_type == 'custom':
                return self.deploy_string_path(model, name, description, custom=True,
                                               handler_path=handler_path, requirements_path=requirements_path)
            else:
                raise Exception('Unknown model type!')
        # model type is not specified and model is not a file path
        # meaning we must infer the type of model
        model_type_str = str(type(model)).lower()
        if 'tensorflow' in model_type_str or 'tf' in model_type_str:
            self.deploy_tensorflow(model, name, description)
            return
        else:
            raise Exception(
                "Can't infer type of model! Try specifying your model type")
