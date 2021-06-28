import os
import kubernetes
import yaml
from kubernetes import client, config
from kubernetes.client.rest import ApiException
import string
import random

from easierSDK.classes.categories import Categories
from easierSDK.serving import easier_serving_config_map
from easierSDK.serving import easier_serving_deployment
from easierSDK.serving import easier_serving_service 
from easierSDK.serving import easier_serving_ingress 

class ServingAPI():
    """Class to control the Serving API of EasierSDK.
    """

    def __init__(self, easier_user, easier_password, minio_client, my_public_repo, my_private_repo, easier_instance=None):
        """Constructor for the ServingAPI.

        Args:
            minio_client (Minio): Minio client object with user session initialized.
            my_public_repo (str): Name of the public bucket of the user.
            my_private_repo (str): Name of the private bucket of the user.
        """
        self._easier_user = easier_user
        self._easier_password = easier_password
        self.minio_client = minio_client
        self.my_public_repo = my_public_repo
        self.my_private_repo = my_private_repo
        self.namespace = None
        self._easier_instance = easier_instance
        
    def id_generator(self, size=16, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def create_model_serving(self, repo_name:str, category:Categories, model_name:str, experimentID:int, base_hostname_url='.easier-ai.eu', resource_name=None, serving_name=None):
        """Creates a model serving deployment on the infrastructure.

        Args:
            repo_name (str): name of the repository where the model is
            category (Categories): category of the model
            model_name (str): name of the model
            experimentID (int): version of the model
            namespace ([type], optional): namespace where the deployment will be done. Defaults to None to take user's namespace.

        Returns:
            str: hostname of the deployed model
        """
        
        if isinstance(category, str):
           category = Categories[category.upper()]
        
        # Test if model can be loaded. 
        easier_model = self._easier_instance.models.get_model(repo_name=repo_name, category=category, model_name=model_name, experimentID=experimentID)    
        if easier_model.get_model() is None:
            print("ERROR: Could not load model " + str(model_name) +
                    " from repository " + repo_name + " and category " + category.value)
            return None

        if self.namespace is None:
            print("ERROR: No context (namespace) was provided. Please, initialize the platform connection before creating model servings.")
            return None
        namespace = self.namespace  
        
        # Enter a context with an instance of the API kubernetes.client
        with kubernetes.client.ApiClient() as api_client:
            # Create an instance of the API class
            api_instance = kubernetes.client.CoreV1Api(api_client)
            
            if resource_name is None: 
                random_name = self.id_generator(size=5)
            else:
                random_name = resource_name
            
            # config_map = None
            # with open(os.path.join(os.path.dirname(__file__), "easier-serving-config_map.yaml")) as f:
            config_map = yaml.safe_load(easier_serving_config_map.config_map)

            config_map['metadata']['name'] += '-' + random_name
            config_map['data']['easier_user'] = self._easier_user
            config_map['data']['easier_password'] = self._easier_password
            config_map['data']['repo'] = repo_name
            config_map['data']['category'] = category.value
            config_map['data']['model_name'] = model_name
            config_map['data']['experimentID'] = str(experimentID)
            config_map['data']['ignore_cert_warning'] = str(self._easier_instance.ignore_cert_warning)
            config_map['data']['minio_region'] = self._easier_instance.minio_region
            config_map['data']['minio_secure'] = str(self._easier_instance.minio_secure)
            config_map['data']['easier_url'] = self._easier_instance.easier_url
                                    
            try:
                api_response = api_instance.create_namespaced_config_map(namespace, config_map, pretty='true')
                # print(api_response)
            except ApiException as e:
                print("Exception when calling CoreV1Api->create_namespaced_config_map: %s\n" % e)

            # deployment = None
            # with open(os.path.join(os.path.dirname(__file__), "easier-serving-deployment.yaml")) as f:
            deployment = yaml.safe_load(easier_serving_deployment.deployment)
        
            deployment['metadata']['name'] += '-' + random_name
            deployment['metadata']['labels']['app'] += '-' +  random_name
            deployment['spec']['selector']['matchLabels']['app'] += '-' + random_name
            deployment['spec']['template']['metadata']['labels']['app'] += '-' + random_name
            deployment['spec']['containers'][0]['name'] += '-' + random_name
            deployment['spec']['containers'][0]['envFrom'][0]['configMapRef']['name'] += '-' + random_name
    
            try:
                api_response = api_instance.create_namespaced_pod(namespace, deployment, pretty='true')
                # print(api_response)
            except ApiException as e:
                print("Exception when calling CoreV1Api->create_namespaced_pod: %s\n" % e)

            # service = None
            # with open(os.path.join(os.path.dirname(__file__), "easier-serving-service.yaml")) as f:
            service = yaml.safe_load(easier_serving_service.service)
        
            service['metadata']['name'] += '-' + random_name
            service['metadata']['labels']['app'] += '-' + random_name
            service['spec']['selector']['app'] += '-' + random_name

            try:
                api_response = api_instance.create_namespaced_service(namespace, service, pretty='true')
                # print(api_response)
            except ApiException as e:
                print("Exception when calling CoreV1Api->create_namespaced_service: %s\n" % e)
        
            networking_v1_beta1_api = kubernetes.client.NetworkingV1beta1Api()
            hostname = None
            # ingress = None
            # with open(os.path.join(os.path.dirname(__file__), "easier-serving-ingress.yaml")) as f:
            ingress = yaml.safe_load(easier_serving_ingress.ingress)
        
            ingress['metadata']['name'] += '-' + random_name
            ingress['metadata']['labels']['app'] += '-' + random_name
            if serving_name:
                ingress['spec']['rules'][0]['host'] = serving_name + base_hostname_url
            else:
                ingress['spec']['rules'][0]['host'] = model_name + '-' + 'easier-serving' + '-' + random_name + base_hostname_url
            ingress['spec']['rules'][0]['http']['paths'][0]['backend']['serviceName'] += '-' + random_name

            try:
                api_response = networking_v1_beta1_api.create_namespaced_ingress(namespace, ingress, pretty='true')
                # print(api_response)
                hostname = ingress['spec']['rules'][0]['host']
            except ApiException as e:
                print("Exception when calling CoreV1Api->create_namespaced_ingress: %s\n" % e)
                        
            if hostname:
                print("Your model will be served shortly in: " + str(hostname))
                print("The identifier for the deployment is: " + random_name)
            else:
                print("There was a problem serving your model")

        return hostname

    def delete_serving(self, deployment_identifier:str):
        """Deletes the deployment resources of a serving.

        Args:
            hostname (str): hostname given as identifier when a serving was created
        """
        
        if self.namespace is None:
            print("ERROR: No context (namespace) was provided. Please, initialize the platform connection before creating model servings.")
            return None
        namespace = self.namespace  
        
        # Enter a context with an instance of the API kubernetes.client
        with kubernetes.client.ApiClient() as api_client:
            # Create an instance of the API class
            api_instance = kubernetes.client.CoreV1Api(api_client)

            try:
                config_map = yaml.safe_load(easier_serving_config_map.config_map)
            
                config_map['metadata']['name'] += '-' + deployment_identifier
                api_response = api_instance.delete_namespaced_config_map(config_map, namespace)
                # print(api_response)
            except ApiException as e:
                print("Exception when calling CoreV1Api->delete_namespaced_config_map: %s\n" % e)

            try:
                deployment = yaml.safe_load(easier_serving_deployment.deployment)
            
                deployment['metadata']['name'] += '-' + deployment_identifier
                api_response = api_instance.delete_namespaced_pod(deployment, namespace)
                # print(api_response)
            except ApiException as e:
                print("Exception when calling CoreV1Api->delete_namespaced_pod: %s\n" % e)
            
            try:
                service = yaml.safe_load(easier_serving_service.service)
            
                service['metadata']['name'] += '-' + deployment_identifier
                api_response = api_instance.delete_namespaced_service(service, namespace)
                # print(api_response)
            except ApiException as e:
                print("Exception when calling CoreV1Api->delete_namespaced_pod: %s\n" % e)

            try:
                ingress = yaml.safe_load(easier_serving_ingress.ingress)
            
                ingress['metadata']['name'] += '-' + deployment_identifier
                
                networking_v1_beta1_api = kubernetes.client.NetworkingV1beta1Api()
                api_response = networking_v1_beta1_api.delete_namespaced_ingress(ingress, namespace)
                # print(api_response)
            except ApiException as e:
                print("Exception when calling CoreV1Api->delete_namespaced_pod: %s\n" % e)
    