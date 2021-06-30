import os
import sys
import subprocess

from energinetml.settings import PACKAGE_VERSION, DOCKERFILE_PATH_ML_MODEL


def build_prediction_api_docker_image(
        path, tag, trained_model_file_path, model_version):
    """
    TODO Add package version when installing energinet-ml-sdk

    :param str path:
    :param str tag: Docker tag
    :param str trained_model_file_path:
    :param str model_version: Model version (for logging)
    """
    trained_model_file_real_path = os.path.realpath(
        trained_model_file_path)
    trained_model_file_relative_path = os.path.relpath(
        trained_model_file_path, path)
    model_real_path = os.path.realpath(path)

    if not trained_model_file_real_path.startswith(model_real_path):
        raise ValueError((
            'Trained model file must be located within the model folder. '
            'You are trying to add file "%s" which is not located within '
            'the model folder (%s). This is not supported by Docker.'
        ) % (trained_model_file_path, path))

    build_docker_image(
        path=path,
        tag=tag,
        dockerfile_path=DOCKERFILE_PATH_ML_MODEL,
        build_args={
            'TRAINED_MODEL_PATH': trained_model_file_relative_path,
            'MODEL_VERSION': model_version,
        },
    )


def build_webapp_docker_image(project, tag):
    """
    TODO Add package version when installing energinet-ml-sdk

    :param energinetml.core.project.WebAppProject project:
    :param str tag: Docker tag
    """
    build_docker_image(
        path=project.path,
        tag=tag,
        dockerfile_path=project.dockerfile_path,
    )


def build_docker_image(path, tag, params=None, build_args=None, dockerfile_path=None):
    """
    Build a Docker image.

    :param str path: Source path
    :param str tag: Docker image tag (name:version format)
    :param typing.Dict[str, str] params: Docker build parameters
    :param typing.Dict[str, str] build_args: Docker build arguments
    :param typing.Optional[str] dockerfile_path: Explicit path to Dockerfile
    """
    if params is None:
        params = {}
    if build_args is None:
        build_args = {}

    if dockerfile_path:
        params['--file'] = dockerfile_path

    build_args['PACKAGE_VERSION'] = str(PACKAGE_VERSION)

    # Render 'docker build' command
    command = ['docker', 'build']
    command.extend(('--tag', tag))
    for k, v in params.items():
        command.extend((k, v))
    for k, v in build_args.items():
        command.extend(('--build-arg', '%s=%s' % (k, v)))
    command.append(path)

    # Run 'docker build' command in subprocess
    subprocess.check_call(
        command, stdout=sys.stdout, stderr=subprocess.STDOUT)
