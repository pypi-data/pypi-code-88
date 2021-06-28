import os
import kubernetes
import yaml
from kubernetes import client, config
from kubernetes.client.rest import ApiException
import string
import random
import joblib
import tempfile
import json

from easierSDK.classes.categories import Categories
from easierSDK.classes import constants
from easierSDK.classes.easier_model import EasierModel
from easierSDK.classes.training_metadata import TrainingMetadata
from easierSDK.training import easier_training_config_map
from easierSDK.training import easier_training_deployment
from easierSDK.training import easier_training_service 
from easierSDK.training import easier_training_ingress 

class DistributedTrainingAPI():
    """Class to control the Training API of EasierSDK.
    """

    _easier_user = None
    _easier_password = None

    def __init__(self, easier_user, easier_password, minio_client, my_public_repo, my_private_repo, easier_instance=None):
        """Constructor for the TrainingAPI.

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
        self._easier_instance = easier_instance
        
    def _id_generator(self, size=16, chars=string.ascii_lowercase + string.digits):
        """Generates random chars and returns a string.

        Args:
            size (int, optional): Size of generated string. Defaults to 16.
            chars (list, optional): types of chars to use for the generation. Defaults to string.ascii_lowercase+string.digits.

        Returns:
            str: string with randomly generated chars
        """
        return ''.join(random.choice(chars) for _ in range(size))

    def get_training_data(self, repo_path:str=None):
        """Loads training data from repository.

        Args:
            repo_path (str, optional): Path in repository to find training data. Defaults to None to read environment variable "model_path".

        Returns:
            tuple: tuple of size 4 with: x_train, y_train, x_test, y_test
        """
        
        # Pickle x and y from minio
        x = None
        y = None
        x_test = None
        y_test = None
        with tempfile.TemporaryDirectory() as path:
            if repo_path is None: repo_path = os.getenv("data_path", '/train/data')

            object_list = self.minio_client.list_objects(self.my_private_repo, prefix=repo_path, recursive=True)
            has_items = False
            # 3. Download
            for obj in object_list:
                if not obj.is_dir:
                    has_items = True
                    self.minio_client.fget_object(self.my_private_repo, obj.object_name, path+'/'+obj.object_name)
            if not has_items:
                print('[ERROR] Could not find file. Please check parameters and try again.')
                return False
            try:
                x = joblib.load(path+'/'+repo_path+'/x.joblib')
            except Exception as e:
                print("[ERROR] Loading training data (x): " + str(e))
            try:
                y = joblib.load(path+'/'+repo_path+'/y.joblib')
            except Exception as e:
                print("[ERROR] Loading training data (y): " + str(e))
            try:
                x_test = joblib.load(path+'/'+repo_path+'/x_test.joblib')
            except Exception as e:
                print("[ERROR] Loading validation data (x_test): " + str(e))
            try:
                y_test = joblib.load(path+'/'+repo_path+'/y_test.joblib')
            except Exception as e:
                print("[ERROR] Loading validation data (y_test): " + str(e))

        return x, y, x_test, y_test

    def clear_training_data(self, repo_path:str, repo_name:str):
        """Removes training data from repository.

        Args:
            repo_path (str): path in repository of the data
            repo_name (str): name of the repository
        """
        for obj in self.minio_client.list_objects(repo_name, repo_path, recursive=True):
            try:
                self.minio_client.remove_object(repo_name, obj.object_name)
            except Exception as e:
                print("[ERROR] When deleting object: ", str(e))

    def create_training(self, x, y, easier_model:EasierModel, training_metadata:TrainingMetadata=None, x_test=None, y_test=None, public=False, num_workers=3, worker_batch_size=64, resource_name=None):
        """Creates a training deployment on EASIER platform with the model given in easier_model according to its training parameters.

        Args:
            x (list): training data in a list-like object
            y (list): labels or prediction targets in a list-like object
            easier_model (EasierModel): Model to be trained encapsulated in an EasierModel variable.
            training_metadata (TrainingMetadata, optional): Metadata of the training process. Defaults to None to take the training_metadata parameter of the easier_model.
            x_test (list): validation data in a list-like object
            y_test (list): validation labels or targets in a list-like object
            public (bool, optional): whether this model is going to be public for other users or not. Defaults to False.
            num_workers ([int], optional): Number of workers to launch to distribute the training. Default is 3.
            worker_batch_size ([int], optional): Batch size of each worker to distribute the training. Default is 64.

        Returns:
            [str]: name of the kubernetes deployment identifier
        """
        base_hostname_url='.easier-ai.eu'

        # Test if model can be loaded
        if easier_model.get_model() is None:
            print("ERROR: There is no model to train")
            return None
        
        if resource_name is None: 
            random_name = self._id_generator(size=5)
        else:
            random_name = resource_name

        minio_path = 'train/' + random_name

        # Pickle x and y and upload to minio
        with tempfile.TemporaryDirectory() as path:
            filename_x = os.path.join(path, 'x.joblib')
            filename_y = os.path.join(path, 'y.joblib')
            joblib.dump(x, filename_x, compress=True)
            joblib.dump(y, filename_y, compress=True)

            filename_x_test = os.path.join(path, 'x_test.joblib')
            filename_y_test = os.path.join(path, 'y_test.joblib')
            joblib.dump(x_test, filename_x_test, compress=True)
            joblib.dump(y_test, filename_y_test, compress=True)

            if training_metadata: easier_model.set_training_metadata(training_metadata)
            
            # Upload model and set it to training state
            self._easier_instance.models.upload(easier_model, public=public, training=True)
            
            if public:
                bucket = self.my_public_repo
            else:    
                bucket = self.my_private_repo
            
            # Create bucket if doesn't exist
            if not self.minio_client.bucket_exists(bucket): self.minio_client.make_bucket(bucket, location='es')

            # Upload training data
            for f in os.listdir(path):
                try:    
                    file_path = (minio_path + "/" + f)
                    a, b =self.minio_client.fput_object(bucket, file_path, path + '/' + f)
                except Exception as ex:
                    print('[ERROR] Unknown error uploading file {}: {}'.format(f, ex))
                    return None

        namespace = self.namespace  
        
        # Enter a context with an instance of the API kubernetes.client
        with kubernetes.client.ApiClient() as api_client:
            # Create an instance of the API class
            api_instance = kubernetes.client.CoreV1Api(api_client)
            
            # api_instance.create_namespaced_persistent_volume_claim()

            # ------------- Configure TF_CONFIG with proper addresses -----------------
            # Get workers service names, all use same port
            worker_list = []
            for i in range(num_workers):
                random_worker_name = random_name + '-w-' + str(i)
                service_name = yaml.safe_load(easier_training_service.service_distributed)
                service_name = service_name['metadata']['name'] + '-' + self._easier_user.replace('.', '-') + '-' + random_worker_name
                worker_list.append(service_name + ":6010")
            
            # Get ps service names, all use same port
            # num_ps = 2
            # ps_list = []
            # for i in range(num_ps):
            #     random_ps_name = random_name + '-ps-' + str(i)
            #     service_name = yaml.safe_load(easier_training_service.service_distributed)
            #     service_name = service_name['metadata']['name'] + '-' + self._easier_user.replace('.', '-') + '-' + random_ps_name
            #     ps_list.append(service_name + ":6010")

            # Get chief service name
            # chief_list = []
            # random_chief_name = random_name + '-chief-' + str(0)
            # service_name = yaml.safe_load(easier_training_service.service_distributed)
            # service_name = service_name['metadata']['name'] + '-' + self._easier_user.replace('.', '-') + '-' + random_chief_name
            # chief_list.append(service_name + ":6010")

            # ---------- Sample TF_CONFIG ---------------
            # tf_config = json.dumps({
            #     "cluster": {
            #         "worker": ["host1:port", "host2:port", "host3:port"],
            #         "ps": ["host4:port", "host5:port"],
            #         "chief": ["host6:port"]
            #     },
            #     "task": {"type": "worker", "index": i}
            # })
            # -------------------------------------------

            tf_config = {}
            tf_config["cluster"] = {}
            tf_config["cluster"]["worker"] = worker_list
            # tf_config["cluster"]["ps"] = ps_list
            # tf_config["cluster"]["chief"] = chief_list

            # tf_config_evaluator = json.dumps({
            #     "cluster": {
            #         "evaluator": ["host7:port"]
            #     },
            #     "task": {"type": "evaluator", "index": 0}
            # })

            # ----------------------------------------------------------------------

            #------------------------ Workers deployment ----------------------------
            for i in range(num_workers):
                # Setup task type in TF_CONFIG
                tf_config["task"] = {"type": "worker", "index": i}

                api_instance = kubernetes.client.CoreV1Api(api_client)
                # config_map = None
                # with open(os.path.join(os.path.dirname(__file__), "easier-training-config_map.yaml")) as f:
                config_map = yaml.safe_load(easier_training_config_map.config_map_distributed)

                config_map['metadata']['name'] += '-' + random_name + '-w-' + str(i)
                config_map['data']['easier_user'] = self._easier_user
                config_map['data']['easier_password'] = self._easier_password
                config_map['data']['repo'] = bucket
                config_map['data']['category'] = easier_model.metadata.category.value
                config_map['data']['model_name'] = easier_model.metadata.name
                config_map['data']['experimentID'] = str(easier_model.metadata.version)
                config_map['data']['ignore_cert_warning'] = str(self._easier_instance.ignore_cert_warning)
                config_map['data']['minio_region'] = str(self._easier_instance.minio_region)
                config_map['data']['minio_secure'] = str(self._easier_instance.minio_secure)
                config_map['data']['easier_url'] = self._easier_instance.easier_url
                config_map['data']['data_path'] = minio_path
                config_map['data']['TF_CONFIG'] = json.dumps(tf_config)
                config_map['data']['PYTHONUNBUFFERED'] = '1'
                config_map['data']['WORKER_BATCH_SIZE'] = str(worker_batch_size)
                
                try:
                    api_response = api_instance.create_namespaced_config_map(namespace, config_map, pretty='true')
                    # print(api_response)
                except ApiException as e:
                    print("Exception when calling CoreV1Api->create_namespaced_config_map: %s\n" % e)

                # service = None
                # with open(os.path.join(os.path.dirname(__file__), "easier-serving-service.yaml")) as f:
                service = yaml.safe_load(easier_training_service.service_distributed)
            
                service['metadata']['name'] += '-' + random_name + '-w-' + str(i)
                service['metadata']['labels']['app'] += '-' + random_name + '-w-' + str(i)
                service['spec']['selector']['app'] += '-' + random_name + '-w-' + str(i)

                try:
                    api_response = api_instance.create_namespaced_service(namespace, service, pretty='true')
                    # print(api_response)
                except ApiException as e:
                    print("Exception when calling CoreV1Api->create_namespaced_service: %s\n" % e)

                api_instance = kubernetes.client.BatchV1Api(api_client)
                # deployment = None
                # with open(os.path.join(os.path.dirname(__file__), "easier-training-deployment.yaml")) as f:
                deployment = yaml.safe_load(easier_training_deployment.deployment_distributed)
            
                deployment['metadata']['name'] += '-' + random_name + '-w-' + str(i)
                deployment['metadata']['labels']['app'] += '-' + random_name + '-w-' + str(i)
                deployment['spec']['template']['metadata']['labels']['app'] += '-' + random_name + '-w-' + str(i)
                deployment['spec']['template']['spec']['containers'][0]['name'] += '-' + random_name + '-w-' + str(i)
                deployment['spec']['template']['spec']['containers'][0]['envFrom'][0]['configMapRef']['name'] += '-' + random_name + '-w-' + str(i)
        
                try:
                    api_response = api_instance.create_namespaced_job(namespace, deployment, pretty='true')
                    # print(api_response)
                except ApiException as e:
                    print("Exception when calling CoreV1Api->create_namespaced_pod: %s\n" % e)

                # # If chief worker and visualization enabled, run tensorboard with ingress
                # if i == 0 and training_viz:
                #     networking_v1_beta1_api = kubernetes.client.NetworkingV1beta1Api()
                    
                #     # ingress = None
                #     # with open(os.path.join(os.path.dirname(__file__), "easier-serving-ingress.yaml")) as f:
                #     ingress = yaml.safe_load(easier_training_ingress.ingress_dist)
                
                #     ingress['metadata']['name'] += '-' + self._easier_user.replace('.', '-') + '-' + random_name + '-w-' + str(i)
                #     ingress['metadata']['labels']['app'] += '-' + self._easier_user.replace('.', '-') + '-' + random_name + '-w-' + str(i)
                #     ingress['spec']['rules'][0]['host'] = easier_model.metadata.name + '-' + 'easier-training-viz' + '-' + random_name + base_hostname_url
                #     ingress['spec']['rules'][0]['http']['paths'][0]['backend']['serviceName'] += '-' + self._easier_user.replace('.', '-') + '-' + random_name + '-w-' + str(i)

                #     try:
                #         api_response = networking_v1_beta1_api.create_namespaced_ingress(namespace, ingress, pretty='true')
                #         # print(api_response)
                #     except ApiException as e:
                #         print("Exception when calling CoreV1Api->create_namespaced_ingress: %s\n" % e)
                    
                #     hostname = ingress['spec']['rules'][0]['host']
                #     print("Visualize the training of the model shortly in: " + str(hostname))
            # -----------------------------------------------------------------

            #------------------------ PS deployment ------------------------
            # for i in range(num_ps):
            #     # Setup task type in TF_CONFIG
            #     tf_config["task"] = {"type": "ps", "index": i}

            #     # config_map = None
            #     # with open(os.path.join(os.path.dirname(__file__), "easier-training-config_map.yaml")) as f:
            #     config_map = yaml.safe_load(easier_training_config_map.config_map_distributed)

            #     config_map['metadata']['name'] += '-' + self._easier_user.replace('.', '-') + '-' + random_name + '-ps-' + str(i)
            #     config_map['data']['easier_user'] = self._easier_user
            #     config_map['data']['easier_password'] = self._easier_password
            #     config_map['data']['repo'] = bucket
            #     config_map['data']['category'] = easier_model.metadata.category.value
            #     config_map['data']['model_name'] = easier_model.metadata.name
            #     config_map['data']['experimentID'] = str(easier_model.metadata.version)
            #     config_map['data']['data_path'] = minio_path
            #     config_map['data']['TF_CONFIG'] = json.dumps(tf_config)
                
            #     try:
            #         api_response = api_instance.create_namespaced_config_map(namespace, config_map, pretty='true')
            #         # print(api_response)
            #     except ApiException as e:
            #         print("Exception when calling CoreV1Api->create_namespaced_config_map: %s\n" % e)

            #     # service = None
            #     # with open(os.path.join(os.path.dirname(__file__), "easier-serving-service.yaml")) as f:
            #     service = yaml.safe_load(easier_training_service.service_distributed)
            
            #     service['metadata']['name'] += '-' + self._easier_user.replace('.', '-') + '-' + random_name + '-ps-' + str(i)
            #     service['metadata']['labels']['app'] += '-' + self._easier_user.replace('.', '-') + '-' + random_name + '-ps-' + str(i)
            #     service['spec']['selector']['app'] += '-' + self._easier_user.replace('.', '-') + '-' + random_name + '-ps-' + str(i)

            #     try:
            #         api_response = api_instance.create_namespaced_service(namespace, service, pretty='true')
            #         # print(api_response)
            #     except ApiException as e:
            #         print("Exception when calling CoreV1Api->create_namespaced_service: %s\n" % e)

            #     api_instance = kubernetes.client.BatchV1Api(api_client)
            #     # deployment = None
            #     # with open(os.path.join(os.path.dirname(__file__), "easier-training-deployment.yaml")) as f:
            #     deployment = yaml.safe_load(easier_training_deployment.deployment_distributed)
            
            #     deployment['metadata']['name'] += '-' + self._easier_user.replace('.', '-') + '-' + random_name + '-ps-' + str(i)
            #     deployment['metadata']['labels']['app'] += '-' + self._easier_user.replace('.', '-') + '-' + random_name + '-ps-' + str(i)
            #     deployment['spec']['template']['metadata']['labels']['app'] += '-' + self._easier_user.replace('.', '-') + '-' +  random_name + '-ps-' + str(i)
            #     deployment['spec']['template']['spec']['containers'][0]['name'] += '-' + self._easier_user.replace('.', '-') + '-' + random_name + '-ps-' + str(i)
            #     deployment['spec']['template']['spec']['containers'][0]['envFrom'][0]['configMapRef']['name'] += '-' + self._easier_user.replace('.', '-') + '-' + random_name + '-ps-' + str(i)
        
            #     try:
            #         api_response = api_instance.create_namespaced_job(namespace, deployment, pretty='true')
            #         # print(api_response)
            #     except ApiException as e:
            #         print("Exception when calling CoreV1Api->create_namespaced_pod: %s\n" % e)
            # -----------------------------------------------------------------
            
            #------------------------ Chief deployment ------------------------
            # Setup task type in TF_CONFIG
            # tf_config["task"] = {"type": "chief", "index": 0}

            # api_instance = kubernetes.client.CoreV1Api(api_client)
            # # config_map = None
            # # with open(os.path.join(os.path.dirname(__file__), "easier-training-config_map.yaml")) as f:
            # config_map = yaml.safe_load(easier_training_config_map.config_map_distributed)

            # config_map['metadata']['name'] += '-' + self._easier_user.replace('.', '-') + '-' + random_name + '-chief-' + str(0)
            # config_map['data']['easier_user'] = self._easier_user
            # config_map['data']['easier_password'] = self._easier_password
            # config_map['data']['repo'] = bucket
            # config_map['data']['category'] = easier_model.metadata.category.value
            # config_map['data']['model_name'] = easier_model.metadata.name
            # config_map['data']['experimentID'] = str(easier_model.metadata.version)
            # config_map['data']['data_path'] = minio_path
            # config_map['data']['TF_CONFIG'] = json.dumps(tf_config)
            # config_map['data']['PYTHONUNBUFFERED'] = '1'
            
            # try:
            #     api_response = api_instance.create_namespaced_config_map(namespace, config_map, pretty='true')
            #     # print(api_response)
            # except ApiException as e:
            #     print("Exception when calling CoreV1Api->create_namespaced_config_map: %s\n" % e)

            # # service = None
            # # with open(os.path.join(os.path.dirname(__file__), "easier-serving-service.yaml")) as f:
            # service = yaml.safe_load(easier_training_service.service_distributed)
        
            # service['metadata']['name'] += '-' + self._easier_user.replace('.', '-') + '-' + random_name + '-chief-' + str(0)
            # service['metadata']['labels']['app'] += '-' + self._easier_user.replace('.', '-') + '-' + random_name + '-chief-' + str(0)
            # service['spec']['selector']['app'] += '-' + self._easier_user.replace('.', '-') + '-' + random_name + '-chief-' + str(0)

            # try:
            #     api_response = api_instance.create_namespaced_service(namespace, service, pretty='true')
            #     # print(api_response)
            # except ApiException as e:
            #     print("Exception when calling CoreV1Api->create_namespaced_service: %s\n" % e)

            # api_instance = kubernetes.client.BatchV1Api(api_client)
            # # deployment = None
            # # with open(os.path.join(os.path.dirname(__file__), "easier-training-deployment.yaml")) as f:
            # deployment = yaml.safe_load(easier_training_deployment.deployment_distributed)
        
            # deployment['metadata']['name'] += '-' + self._easier_user.replace('.', '-') + '-' + random_name + '-chief-' + str(0)
            # deployment['metadata']['labels']['app'] += '-' + self._easier_user.replace('.', '-') + '-' + random_name + '-chief-' + str(0)
            # deployment['spec']['template']['metadata']['labels']['app'] += '-' + self._easier_user.replace('.', '-') + '-' +  random_name + '-chief-' + str(0)
            # deployment['spec']['template']['spec']['containers'][0]['name'] += '-' + self._easier_user.replace('.', '-') + '-' + random_name + '-chief-' + str(0)
            # deployment['spec']['template']['spec']['containers'][0]['envFrom'][0]['configMapRef']['name'] += '-' + self._easier_user.replace('.', '-') + '-' + random_name + '-chief-' + str(0)
    
            # try:
            #     api_response = api_instance.create_namespaced_job(namespace, deployment, pretty='true')
            #     # print(api_response)
            # except ApiException as e:
            #     print("Exception when calling CoreV1Api->create_namespaced_pod: %s\n" % e)
            # -----------------------------------------------------------------

        print("Resources identifier: " + random_name)
        return random_name

    def _get_resource_names(self, resource_list):
        resource_names = []
        for resource in resource_list:
            resource_names.append(resource.metadata.name)
        return resource_names

    def print_training_logs(self, deployment_identifier):

        # Enter a context with an instance of the API kubernetes.client
        with kubernetes.client.ApiClient() as api_client:
            deployment = yaml.safe_load(easier_training_deployment.deployment_distributed)        
            deployment['metadata']['name'] += '-' + deployment_identifier

            api_instance = kubernetes.client.CoreV1Api(api_client)
            name = deployment['metadata']['name'] # name of the Pod
            pretty = 'true' 
            
            try:
                api_response = api_instance.list_namespaced_pod(self.namespace, pretty='true')
                pods_list = self.get_resource_names(api_response.items)
            except ApiException as e:
                print("Exception when calling CoreV1Api->list_namespaced_pod: %s\n" % e)

            try: 
                pod_name = [string for string in pods_list if name in string]
                api_response = api_instance.read_namespaced_pod_log(pod_name[0], self.namespace, pretty=pretty)
                print(api_response)
            except ApiException as e:
                print("Exception when calling CoreV1Api->read_namespaced_pod_log: %s\n" % e)