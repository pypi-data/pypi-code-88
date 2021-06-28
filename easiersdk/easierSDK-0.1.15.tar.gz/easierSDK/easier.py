#   Copyright  2020 Atos Spain SA. All rights reserved.
 
#   This file is part of EASIER AI.
 
#   EASIER AI is free software: you can redistribute it and/or modify it under the terms of Apache License, either version 2 of the License, or
#   (at your option) any later version.
 
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT ANY WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING 
#   BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT,
#   IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
#   WHETHER IN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE 
#   OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#   See  LICENSE file for full license information  in the project root.

import minio
from minio import Minio
import os
import json
import certifi
import urllib3
import kubernetes
from kubernetes.client.rest import ApiException
import yaml
from tqdm import tqdm

from easierSDK import modelsAPI, datasetsAPI
from easierSDK.classes.categories import Categories
from easierSDK.classes.repository_metadata import RepositoryMetadata
from easierSDK.classes.model_metadata import ModelMetadata
from easierSDK.classes.dataset_metadata import DatasetMetadata
from easierSDK.classes.category_metadata import CategoryMetadata

from easierSDK.serving import servingAPI
from easierSDK.training import trainingAPI, distributed_trainingAPI

import urllib3
urllib3.disable_warnings()

class EasierSDK():
    """Higher level class to interact with the EASIER platform.
    """

    _MODELS = 'models'
    _DATASETS = 'datasets'
    
    def __init__(self, easier_user:str, easier_password:str, easier_url:str="minio.easier-ai.eu", minio_secure=True, minio_region='es', ignore_cert_warning=False):
        """Initializer for the class.

        Args:
            easier_url (str): URL to an EASIER MINIO deployment.
            easier_user (str): Username.
            easier_password (str): Password.
        """
        self.my_easier_user = easier_user
        self.ignore_cert_warning = ignore_cert_warning
        self.minio_region = minio_region
        self.minio_secure = minio_secure
        self.easier_url = easier_url

        if ignore_cert_warning:
            cert = 'CERT_NONE'
        else: 
            cert = 'CERT_REQUIRED'

        # Load CA certificates from SSL_CERT_FILE file if set
        ca_certs = os.environ.get('SSL_CERT_FILE') or certifi.where()
        _http = urllib3.PoolManager(
            timeout=1,
            maxsize=minio.helpers.MAX_POOL_SIZE,
            cert_reqs=cert,
            ca_certs=ca_certs,
            retries=urllib3.Retry(
                total=3,
                backoff_factor=0.2,
                status_forcelist=[500, 502, 503, 504]
            )
        )

        self.minio_client = Minio(easier_url, access_key=easier_user, secret_key=easier_password, secure=minio_secure, region=minio_region, http_client=_http)
        
        # Test Connection
        try:
            self.minio_client.list_buckets()
        except Exception as e:
            raise Exception("ERROR when connecting to EASIER Repositories. Check input parameters.")

        # IF test is ok, then we reinit with default parameters of the http lib
        _http = urllib3.PoolManager(
            timeout=urllib3.Timeout.DEFAULT_TIMEOUT,
            maxsize=minio.helpers.MAX_POOL_SIZE,
            cert_reqs=cert,
            ca_certs=ca_certs,
            retries=urllib3.Retry(
                total=5,
                backoff_factor=0.2,
                status_forcelist=[500, 502, 503, 504]
            )
        )

        self.minio_client = Minio(easier_url, access_key=easier_user, secret_key=easier_password, secure=minio_secure, region=minio_region, http_client=_http)
        
        self.my_public_repo = str(easier_user).split('@')[0] + '-public'
        self.my_private_repo = str(easier_user).split('@')[0] + '-private' 

        self.models = modelsAPI.ModelsAPI(self.minio_client, self.my_public_repo, self.my_private_repo)
        self.datasets = datasetsAPI.DatasetsAPI(self.minio_client, self.my_public_repo, self.my_private_repo)

        self.serving = servingAPI.ServingAPI(easier_user, easier_password,  self.minio_client, 
                self.my_public_repo, self.my_private_repo, self)

        self.training = trainingAPI.TrainingAPI(easier_user, easier_password, self.minio_client, 
                self.my_public_repo, self.my_private_repo, self)

        self.distributed_training = distributed_trainingAPI.DistributedTrainingAPI(easier_user, easier_password, self.minio_client, 
                self.my_public_repo, self.my_private_repo, self)

    def initialize_connection(self, kube_config_path:str=None):
        """Initialices the connection to kubernetes infrastructure.

        Args:
            kube_config_path (str, optional): path to user's kubeconfig file. Defaults to None to get the file from ~/.kube/config
        """
        if kube_config_path:
            kubernetes.config.load_kube_config(kube_config_path)
            with open(os.path.join(os.path.dirname(__file__), kube_config_path)) as f:
                kubeconfig = yaml.safe_load(f)
                self.namespace = kubeconfig['contexts'][0]['context']['namespace']
        else:
            kubernetes.config.load_kube_config()
            with open(os.path.join(os.path.dirname(__file__), os.environ.get('KUBECONFIG', '~/.kube/config'))) as f:
                kubeconfig = yaml.safe_load(f)
                self.namespace = kubeconfig['contexts'][0]['context']['namespace']

        print("Current context on namespace: " + str(self.namespace))
        self.serving.namespace = self.namespace
        self.training.namespace = self.namespace
        self.distributed_training.namespace = self.namespace
    

    def _get_resource_names(self, resource_list):
        resource_names = []
        for resource in resource_list:
            resource_names.append(resource.metadata.name)
        return resource_names

    def get_deployed_resources(self):
        """Returns a dictionary with the deployed resources of the user. Fields of the dictionary are:
            pods: a python list of deployed pods names
            services: a python list of deployed services names
            ingress: a python list of deployed ingress names
            jobs: a python list of deployed jobs names

        Returns:
            dict: python dictionary with the deployed resources of the user
        """
        resources_dict = {}
        
        # Enter a context with an instance of the API kubernetes.client
        with kubernetes.client.ApiClient() as api_client:
            # Create an instance of the API class
            api_instance = kubernetes.client.CoreV1Api(api_client)

            try:
                api_response = api_instance.list_namespaced_pod(self.namespace, pretty='true')
                pods_list = self._get_resource_names(api_response.items)
                resources_dict['pods'] = pods_list
                # print(api_response)
            except ApiException as e:
                print("Exception when calling CoreV1Api->list_namespaced_pod: %s\n" % e)

            try:
                api_response = api_instance.list_namespaced_service(self.namespace, pretty='true')
                services_list = self._get_resource_names(api_response.items)
                resources_dict['services'] = services_list
                # print(api_response)
            except ApiException as e:
                print("Exception when calling CoreV1Api->list_namespaced_service: %s\n" % e)
            
            networking_v1_beta1_api = kubernetes.client.NetworkingV1beta1Api()

            try:
                api_response = networking_v1_beta1_api.list_namespaced_ingress(self.namespace, pretty='true')
                # print(api_response)
                ingress_list = self._get_resource_names(api_response.items)
                resources_dict['ingress'] = ingress_list
            except ApiException as e:
                print("Exception when calling NetworkingV1beta1Api->list_namespaced_ingress: %s\n" % e)

            api_instance = kubernetes.client.BatchV1Api(api_client)

            try:
                api_response = api_instance.list_namespaced_job(self.namespace, pretty='true')
                # print(api_response)
                jobs_list = self._get_resource_names(api_response.items)
                resources_dict['jobs'] = jobs_list
            except ApiException as e:
                print("Exception when calling BatchV1Api->list_namespaced_job: %s\n" % e)
            
            return resources_dict

    def get_repositories_metadata(self, category:Categories=None):
        """Reads repositories information regarding Datasets and Models and returns a dictionary with the information.

        Args:
            category (Categories, optional): Limit search to only one Category. Defaults to None.

        Returns:
            dict: dictionary with the repositories information
        """
        if isinstance(category, str):
           category = Categories[category.upper()]

        if category is None:
            categories = [cat for cat in Categories]
        else:
            categories = [category]
        
        repositories = {}
        repo_list = tqdm(self.minio_client.list_buckets(), colour="red", desc="Getting repositories information...")
        
        for repo in repo_list:
            cat_dict = {}
            repo_list.set_postfix({'repository': repo.name})
            for cat in categories: 
                num_models, models_list = self._count_repo_models(repo.name, cat)
                num_datasets, datasets_list = self._count_repo_datasets(repo.name, cat)
            
                cat_models = {}
                for model_path in models_list:
                    minio_path = model_path + '/' + 'metadata.json'
                    filename = minio_path.split('/')[1:]
                    filename = '/'.join(filename)
                    local_file = '/tmp/metadata.json'
                    try:
                        self.minio_client.fget_object(repo.name, filename, local_file)
                    except minio.error.NoSuchKey as ex:
                        continue
                    
                    with open(local_file, 'r') as f:
                        model_metadata = ModelMetadata(json.load(f))
                    if os.path.exists(local_file):
                        os.remove(local_file)
                    
                    _, model_metadata.experimentIDs = self.models._count_model_experiments(repo.name, cat.value, model_metadata.name)
                    cat_models[model_metadata.name] = model_metadata

                cat_datasets = {}
                for dataset_path in datasets_list:
                    minio_path = dataset_path + '/' + 'metadata.json'
                    filename = minio_path.split('/')[1:]
                    filename = '/'.join(filename)
                    local_file = '/tmp/metadata.json'
                    try:
                        self.minio_client.fget_object(repo.name, filename, local_file)
                    except minio.error.NoSuchKey as ex:
                        continue
                    
                    with open(local_file, 'r') as f:
                        dataset_metadata = DatasetMetadata(json.load(f))
                    if os.path.exists(local_file):
                        os.remove(local_file)

                    cat_datasets[dataset_metadata.name] = dataset_metadata

                cat_metadata = CategoryMetadata(cat.value, cat_models, num_models, cat_datasets, num_datasets)
                cat_dict[cat.value] = cat_metadata

            repo_metadata = RepositoryMetadata(repo.name, cat_dict)
            repositories[repo.name] = repo_metadata
        return repositories

    def _count_repo_models(self, repo_name:str, category_name:str=None):
        """Count number of models under a repository.

        Args:
            repo_name (str): Repository to count models from.
            category_name (str): Category to count models from.

        Returns:
            int: Number of models under the repository.
            list: List of models in the repository.
        """
        
        num_models = 0
        models_list = []
        
        if category_name:
            if isinstance(category_name, str):
                category_name = Categories[category_name.upper()]
            categories = [category_name]
        else:
            categories = [cat for cat in Categories]

        for category in categories:
            for obs in self.minio_client.list_objects(repo_name, prefix=self._MODELS + '/' + category.value, recursive=True):
                experiment_model = obs.object_name.split('/')[0:3]
                experiment_model = repo_name + '/' + '/'.join(experiment_model)
                if experiment_model not in models_list:
                    num_models += 1
                    models_list.append(experiment_model)
        return num_models, models_list

    def _count_repo_datasets(self, repo_name:str, category_name:str=None):
        """Count number of datasets under a repository.

        Args:
            repo_name (str): Repository to count datasets from.
            category_name (str): Category to count models from.

        Returns:
            int: Number of datasets under the repository.
            list: List of datasets in the repository.
        """
        num_datasets = 0
        datasets_list = []

        if category_name:
            if isinstance(category_name, str):
                category_name = Categories[category_name.upper()]
            categories = [category_name]
        else:
            categories = [cat for cat in Categories]

        for category in categories:
            for obs in self.minio_client.list_objects(repo_name, prefix=self._DATASETS + '/' + category.value, recursive=True):
                experiment_dataset = obs.object_name.split('/')[0:3]
                experiment_dataset = repo_name + '/' + '/'.join(experiment_dataset)
                if experiment_dataset not in datasets_list:
                    num_datasets += 1
                    datasets_list.append(experiment_dataset)
        return num_datasets, datasets_list
        
    def _count_category_models(self, category:Categories):
        """Count all available models under a specific category.

        Args:
            category (Categories): Category to which count the models from.

        Returns:
            int: number of models under the category
            list: list of models under the category
        """
        if isinstance(category, str):
           category = Categories[category.upper()]

        num_models = 0
        models_list = []
        repo_list = self.minio_client.list_buckets()
        for repo in repo_list:
            for obs in self.minio_client.list_objects(repo.name, prefix=self._MODELS + '/' + category.value, recursive=True):
                experiment_model = obs.object_name.split('/')[0:3]
                experiment_model = repo.name + '/' + '/'.join(experiment_model)            
                if experiment_model not in models_list:
                    num_models += 1
                    models_list.append(experiment_model)
        return num_models, models_list
    
    def _count_category_datasets(self, category:Categories):
        """Count all available datasets under a specific category.

        Args:
            category (Categories): Category to which count the datasets from.

        Returns:
            int: number of datasets under the category
            list: list of datasets under the category
        """
        if isinstance(category, str):
           category = Categories[category.upper()]
           
        num_datasets = 0
        datasets_list = []
        repo_list = self.minio_client.list_buckets()
        for repo in repo_list:
            for obs in self.minio_client.list_objects(repo.name, prefix=self._DATASETS + '/' + category.value, recursive=True):
                experiment_dataset = obs.object_name.split('/')[0:3]
                experiment_dataset = repo.name + '/' + '/'.join(experiment_dataset)
                if experiment_dataset not in datasets_list:
                    num_datasets += 1
                    datasets_list.append(experiment_dataset)
        return num_datasets, datasets_list
