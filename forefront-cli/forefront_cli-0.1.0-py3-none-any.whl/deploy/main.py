import click
import os
from ..api import API
from ..common import bcolors, get_user_token, get_project_id
from halo import Halo


def get_ext(path):
    return path.split('.')[-1]


@click.group()
def deploy():
    pass


@deploy.command()
@click.option("--name", "-n", type=str, help="Name of version to deploy", required=True)
@click.option("--description", "-d", type=str, help="Description of version")
@click.option("--model", "-m", type=str, help="Path to model file. Defaults to model.h5")
@click.option('--model-type', '-t', help="Type of deployment. Must be one of: [keras (.h5), SavedModel ( gzipped file .tar.gz ), or Onnx]. Refer to documentation for more details at https://docs.tryforefront.com", required=True)
@click.option('--custom', is_flag=True, type=bool, help="Specifies a custom deployment. Default is False")
@click.option('--handler', type=str, help="Required during custom deployment. Path to handler file")
@click.option('--requirements', type=str, help="Required during custom deployment. Path to requirements.txt file")
def deploy(name, description, model, model_type, custom, handler, requirements):
    """Deploy a model"""
    api = API()

    # check for api key
    if api.key is None or api.key == '':
        print(bcolors.FAIL +
              'You are not logged in. Run the `init` command to log in.' + bcolors.ENDC)
        return

    # check for project id
    if api.project_id is None or api.project_id == '':
        print(bcolors.FAIL +
              'You are not connected to a project. Please run the `init` command.')
        return

    # check for model
    if model is None:
        print(bcolors.OKBLUE +
              'Model path not specified. Using default relative path "./model.h5"' + bcolors.ENDC)
        model = './model.h5'
    found_file = os.path.exists(model)
    if found_file is False:
        print(bcolors.FAIL + 'Unable to find model. Please check that the model exists or specify model path. ' + bcolors.ENDC)
        return

    # check for model type
    model_types = ['keras', 'tensorflow', 'onnx']
    if model_type not in model_types:
        print(bcolors.FAIL +
              'File type mismatch. Model type must be one of: keras, tensorflow, onnx')
        return

    # check model file extension matches model type
    if model_type == 'keras' and get_ext(model) != 'h5':
        print(bcolors.FAIL + 'Keras model file should be a .h5 file' + bcolors.ENDC)
        return

    if model_type == 'tensorflow' and get_ext(model) != 'gz':
        print(bcolors.FAIL +
              'File type mismatch. Tensorflow model file should be a gzipped SavedModel file' + bcolors.ENDC)
        return

    if model_type == 'onnx' and get_ext(model) != 'onnx':
        print(bcolors.FAIL +
              'File type mismatch. Onnx model file should be a .onnx file' + bcolors.ENDC)
        return

    if custom is False:
        try:
            auth_spinner = Halo(text='Deploying model to Forefront...',
                                spinner='dots', text_color="blue")

            auth_spinner.start()
            url = api.deploy_string_path(
                name=name, model_path=model, description=description, model_type=model_type)
            auth_spinner.stop()
            print(bcolors.OKGREEN +
                  f"✅ Model deployed! View deployment in dashboard at: {url}" + bcolors.ENDC)
        except Exception as e:
            print(bcolors.FAIL + 'Error deploying model' + bcolors.ENDC)
    else:
        auth_spinner = Halo(text='Deploying custom model to Forefront...',
                            spinner='dots', text_color="blue")
        auth_spinner.start()
        url = api.deploy_version(name, model, description, model_type='custom',
                                 handler_path=handler, requirements_path=requirements)
        auth_spinner.stop()
        print(bcolors.OKGREEN +
              f"✅ Model deployed! View deployment in dashboard at: {url}" + bcolors.ENDC)
