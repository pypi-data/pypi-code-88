import logging
from typing import Any, Tuple
import os
import shutil
import uuid
import json


from pydantic import parse_obj_as

from deeploy.services import DeeployService, GitService, ModelWrapper, ExplainerWrapper
from deeploy.models import ClientConfig, Deployment, CreateDeployment, DeployOptions, \
    V1Prediction, V2Prediction, ModelReferenceJson, PredictionLog, PredictionLogs
from deeploy.enums import ExplainerType
from deeploy.common.functions import delete_all_contents_in_directory, directory_exists, \
    directory_empty, file_exists


class Client(object):
    """
    A class for interacting with Deeploy
    """

    __config: ClientConfig

    def __init__(
            self, host: str, workspace_id: str, access_key: str = None, secret_key: str = None,
            deployment_token: str = None, branch_name: str = None) -> None:
        """Initialise the Deeploy client
        Parameters:
            host (str): The host at which Deeploy is located, i.e. deeploy.example.com
            workspace_id (str): The ID of the workspace in which your repository
                is located
            access_key (str): Personal Access Key generated from the Deeploy UI
            secret_key (str): Secret Access Key generated from the Deeploy UI
            token (str): Deployment token generated from the Deeploy UI
            branch_name (str, optional): The banchname on which to commit new models.
                Defaults to the current branchname.
        """
        self.__access_key = access_key
        self.__secret_key = secret_key

        self.__config = ClientConfig(**{
            'access_key': access_key,
            'secret_key': secret_key,
            'token': deployment_token,
            'host': host,
            'workspace_id': workspace_id,
            'branch_name': branch_name,
            'repository_id': '',
        })

        self.__deeploy_service = DeeployService(
            host,
            workspace_id,
            access_key,
            secret_key,
            deployment_token,
        )

        return

    def deploy(self, model: Any, options: DeployOptions, local_repository_path: str,
               explainer: Any = None, overwrite: bool = False,
               commit_message: str = None) -> Deployment:
        """Deploy a model on Deeploy
        Parameters:
            model (Any): The class instance of an ML model
            options (DeployOptions): An instance of the deploy options class
                containing the deployment options
            local_repository_path (str): Absolute path to the local git repository
                which is connected to Deeploy
            explainer (Any, optional): The class instance of an optional model explainer
            overwrite (bool, optional): Whether or not to overwrite files that are in the
                'model' and 'explainer' folders in the git folder. Defaults to False
            commit_message (str, optional): Commit message to use
        """
        if not (self.__access_key and self.__secret_key):
            raise Exception('Missing access credentials to create deployment.')

        git_service = GitService(local_repository_path)

        repository_in_workspace, repository_id = self.__is_git_repository_in_workspace(git_service)

        if not repository_in_workspace:
            raise Exception(
                'Repository was not found in the Deeploy workspace. \
                 Make sure you have connected it before')
        else:
            self.__config.repository_id = repository_id

        logging.info('Pulling from the remote repository...')
        git_service.pull()
        logging.info('Successfully pulled from the remote repository.')

        logging.info('Saving the model to disk...')
        model_wrapper = ModelWrapper(
            model,
            pytorch_model_file_path=options.pytorch_model_file_path,
            pytorch_torchserve_handler_name=options.pytorch_torchserve_handler_name)
        self.__prepare_model_directory(git_service, local_repository_path, overwrite)
        model_folder = os.path.join(
            local_repository_path, 'model')
        model_wrapper.save(model_folder)
        blob_storage_link = self.__upload_folder_to_blob(local_repository_path, model_folder)
        shutil.rmtree(model_folder)
        os.mkdir(model_folder)
        self.__create_reference_file(model_folder, blob_storage_link)
        git_service.add_folder_to_staging('model')
        commit_message = '[Deeploy Client] Add new model'

        metadata_path = './metadata.json'
        self.__prepare_metadata_file(git_service, metadata_path, options.feature_labels, overwrite)
        git_service.add_folder_to_staging(metadata_path)

        if explainer:
            logging.info('Saving the explainer to disk...')
            explainer_wrapper = ExplainerWrapper(explainer)
            self.__prepare_explainer_directory(git_service, local_repository_path, overwrite)
            explainer_folder = os.path.join(
                local_repository_path, 'explainer')
            explainer_wrapper.save(explainer_folder)
            blob_storage_link = self.__upload_folder_to_blob(
                local_repository_path, explainer_folder)
            shutil.rmtree(explainer_folder)
            os.mkdir(explainer_folder)
            self.__create_reference_file(explainer_folder, blob_storage_link)
            git_service.add_folder_to_staging('explainer')
            commit_message += ' and explainer'
            explainer_type = explainer_wrapper.get_explainer_type()
        else:
            explainer_type = ExplainerType.NO_EXPLAINER

        logging.info('Committing and pushing the result to the remote.')
        commit_sha = git_service.commit(commit_message)
        git_service.push()

        deployment_options = {
            'repository_id': self.__config.repository_id,
            'name': options.name,
            'description': options.description,
            # TODO: example input & output
            'example_input': options.example_input,
            'example_output': options.example_output,
            'model_type': model_wrapper.get_model_type().value,
            'model_serverless': options.model_serverless,
            'branch_name': git_service.get_current_branch_name(),
            'commit': commit_sha,
            'explainer_type': explainer_type.value,
            'explainer_serverless': options.explainer_serverless,
        }

        deployment = self.__deeploy_service.create_deployment(
            self.__config.workspace_id, CreateDeployment(**deployment_options))

        return deployment

    def predict(self, deployment_id: str, request_body: dict) -> V1Prediction or V2Prediction:
        """Make a predict call
        Parameters:
            deployment_id (str): ID of the Deeploy deployment
            request_body (dict): Request body with input data for the model
        """

        workspace_id = self.__config.workspace_id
        prediction = self.__deeploy_service.predict(workspace_id, deployment_id, request_body)
        return prediction

    def explain(self, deployment_id: str, request_body: dict, image: bool = False) -> object:
        """Make an explain call
        Parameters:
            deployment_id (str): ID of the Deeploy deployment
            request_body (dict): Request body with input data for the model
            image (bool): Return image or not
        """
        workspace_id = self.__config.workspace_id
        explanation = self.__deeploy_service.explain(
            workspace_id, deployment_id, request_body, image)
        return explanation

    def getLogs(self, deployment_id: str) -> PredictionLogs:
        """Retrieve logs
        Parameters:
            deployment_id (str): ID of the Deeploy deployment
        """
        workspace_id = self.__config.workspace_id
        logs = self.__deeploy_service.getLogs(workspace_id, deployment_id)
        return logs

    def getOneLog(self, deployment_id: str, log_id: str) -> PredictionLog:
        """Retrieve one log
        Parameters:
            deployment_id (str): ID of the Deeploy deployment
            log_id (str): ID of the log to be retrieved
        """
        workspace_id = self.__config.workspace_id
        log = self.__deeploy_service.getOneLog(workspace_id, deployment_id, log_id)
        return log

    def validate(self, deployment_id: str, log_id: str, validation_input: dict,
                 explanation: str = None) -> None:
        """Validate a log
        Parameters:
            deployment_id (str): ID of the Deeploy deployment
            log_id (int): ID of the log to be validated
            validation_input: Dict with result, value, and explanation
            explanation: Optional explanation of the validation
        """
        workspace_id = self.__config.workspace_id
        self.__deeploy_service.validate(workspace_id, deployment_id,
                                        log_id, validation_input, explanation)

    def __are_clientoptions_valid(self, config: ClientConfig) -> bool:
        """Check if the supplied options are valid
        """
        try:
            self.__deeploy_service.get_workspace(config.workspace_id)
        except Exception as e:
            raise e

        return True

    def __is_git_repository_in_workspace(self, git_service: GitService) -> Tuple[bool, str]:
        remote_url = git_service.get_remote_url()
        workspace_id = self.__config.workspace_id

        repositories = self.__deeploy_service.get_repositories(workspace_id)
        correct_repositories = list(
            filter(lambda x: x.git_ssh_pull_link == remote_url, repositories))

        if len(correct_repositories) != 0:
            repository_id = correct_repositories[0].id
            return True, repository_id

        return False, None

    def __prepare_model_directory(self, git_service: GitService, local_repository_path: str,
                                  overwrite=False) -> None:
        model_folder_path = os.path.join(
            local_repository_path, 'model')
        if not directory_exists(model_folder_path):
            try:
                os.mkdir(model_folder_path)
            except OSError:
                logging.error("Creation of the directory %s failed" %
                              model_folder_path)
        elif not directory_empty(model_folder_path):
            if not overwrite:
                raise Exception(
                    'The folder %s is not empty. Pass \'overwrite=True\' to overwrite contents.' %
                    model_folder_path)
            delete_all_contents_in_directory(model_folder_path)
            git_service.delete_folder_from_staging('model')
        else:  # folder exists and empty
            pass
        return

    def __prepare_explainer_directory(self, git_service: GitService, local_repository_path: str,
                                      overwrite=False) -> None:
        explainer_folder_path = os.path.join(
            local_repository_path, 'explainer')
        if not directory_exists(explainer_folder_path):
            try:
                os.mkdir(explainer_folder_path)
            except OSError:
                logging.error("Creation of the directory %s failed" %
                              explainer_folder_path)
        elif not directory_empty(explainer_folder_path):
            if not overwrite:
                raise Exception(
                    'The folder %s is not empty. Pass \'overwrite=True\' to overwrite contents.' %
                    explainer_folder_path)
            delete_all_contents_in_directory(explainer_folder_path)
            git_service.delete_folder_from_staging('explainer')
        else:  # folder exists and empty
            pass
        return

    def __prepare_metadata_file(self, git_service: GitService, path: str, featureLabels=None,
                                overwrite=False) -> None:
        data = {
            'featureLabels': []
        }

        if featureLabels:
            data['featureLabels'] = featureLabels

        if file_exists(path) and not overwrite:
            raise Exception(
                'The file %s already exists. Pass \'overwrite=True\' to overwrite contents.' % path)
        else:
            try:
                with open(path, 'w') as f:
                    json.dump(data, f)
            except OSError:
                logging.error("Creation of the file %s failed" % path)

    def __get_upload_size(self, local_folder_path: str) -> int:
        total_file_sizes = 0
        for root, _, files in os.walk(local_folder_path):
            for single_file in files:
                file_path = os.path.join(root, single_file)
                file_size = os.path.getsize(file_path)
                total_file_sizes += file_size
        return total_file_sizes

    def __upload_folder_to_blob(self, local_repository_path: str, local_folder_path: str) -> str:
        upload_locations = list()
        blob_folder_uuid = str(uuid.uuid4())
        relative_folder_path = os.path.relpath(local_folder_path, local_repository_path)
        for root, _, files in os.walk(local_folder_path):
            for single_file in files:
                relative_file_path = os.path.join(
                    relative_folder_path, os.path.relpath(root, local_folder_path))
                file_path = os.path.join(root, single_file)
                blob_file_location = self.__deeploy_service.upload_blob_file(
                    file_path,
                    relative_file_path,
                    self.__config.workspace_id,
                    self.__config.repository_id,
                    blob_folder_uuid)
                upload_locations.append(blob_file_location)

        partition = upload_locations[0].partition(relative_folder_path)
        blob_folder_path = partition[0] + partition[1]
        return blob_folder_path

    def __create_reference_file(self, local_folder_path: str, blob_storage_link: str = None,
                                docker_image: str = None, docker_image_port: int = None) -> None:
        file_path = os.path.join(local_folder_path, 'reference.json')

        reference_json = {
            'reference': {
                'docker': {
                    'image': docker_image,
                    'port': docker_image_port,
                },
                'blob': {
                    'url': blob_storage_link,
                },
            },
        }

        data = parse_obj_as(ModelReferenceJson, reference_json)

        with open(file_path, 'w') as outfile:
            json.dump(data.dict(), outfile)
        return
