# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
import logging
import os
import sys
import json
import re
from enum import Enum

import docker
import zipfile
import functools
import shutil
import uuid
import jwt
from os import name as os_name
from shlex import quote
from datetime import datetime
from pathlib import Path, PureWindowsPath
from uuid import UUID
from unittest import mock
from collections import namedtuple

from azureml.core import Workspace
from azureml.data.data_reference import DataReference
from azureml.data.abstract_dataset import AbstractDataset
from azureml.data._dataset import _Dataset
from azure.ml.component._restclients.designer.models import EntityStatus, DataInfo, \
    DataSetDefinition, RegisteredDataSetReference, SavedDataSetReference, \
    DataSetDefinitionValue, DataPath
from azureml.exceptions import WebserviceException


def _is_empty_dir(path):
    path = Path(path)
    return path.is_dir() and next(path.iterdir(), None) is None


def copytree(src, dst, symlinks=False, ignore=None, exist_ok=False):
    """Copy the folder to dst with the parameter exist_ok."""
    # If exist_ok is False, keep the behavior of shutil.copytree.
    if not exist_ok:
        shutil.copytree(src, dst, symlinks, ignore)
        return
    # Otherwise recursively copy the files in src to dst.
    os.makedirs(dst, exist_ok=True)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copytree(s, d, symlinks, ignore, exist_ok)
        else:
            _copy2(s, d)


def _extract_zip(zip_file, target_dir):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(target_dir)


def _normalize_identifier_name(name):
    import re
    normalized_name = name.lower()
    normalized_name = re.sub(r'[\W_]', ' ', normalized_name)  # No non-word characters
    normalized_name = re.sub(' +', ' ', normalized_name).strip()  # No double spaces, leading or trailing spaces
    if re.match(r'\d', normalized_name):
        normalized_name = 'n' + normalized_name  # No leading digits
    return normalized_name


def _sanitize_python_variable_name(name: str):
    return _normalize_identifier_name(name).replace(' ', '_')


def _sanitize_python_variable_name_with_value_check(name: str):
    sanitized_name = _sanitize_python_variable_name(name)
    if sanitized_name == '':
        raise ValueError('Given name {} could not be normalized into python variable name.'.format(name))
    return sanitized_name


basic_python_type = [str, int, float, bool, type(None)]


def _value_type_json_serializable(obj):
    """Check if an object is JSON serializable recursively."""
    # Inheriting from dict is the only way to make class JSON serializable
    # in circumstance of calling `dumps` with neither encoder nor jsonpickle.
    obj_id_set = set()

    def _is_valid_type(obj):
        # Extract value if obj is Enum
        if isinstance(obj, Enum):
            obj = obj.value
        if type(obj) in basic_python_type:
            return True
        valid_type = True
        obj_id = id(obj)
        if obj_id in obj_id_set:
            # Circular reference detected
            return False
        obj_id_set.add(obj_id)
        if type(obj) in [tuple, list]:
            for val in obj:
                valid_type &= _is_valid_type(val)
                if not valid_type:
                    break
        elif isinstance(obj, dict):
            for k, v in obj.items():
                valid_type &= _is_valid_type(k) & _is_valid_type(v)
                if not valid_type:
                    break
        else:
            valid_type = False
        obj_id_set.remove(obj_id)
        return valid_type

    return _is_valid_type(obj)


def _get_or_sanitize_python_name(name: str, name_map: dict):
    return name_map[name] if name in name_map.keys() \
        else _sanitize_python_variable_name(name)


def is_float_convertible(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def is_int_convertible(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


def is_bool_string(string):
    if not isinstance(string, str):
        return False
    return string == 'True' or string == 'False'


def _is_uuid(str):
    try:
        UUID(hex=str)
    except ValueError:
        return False
    return True


def int_str_to_pipeline_status(str):
    if str == '0':
        return EntityStatus.active.value
    elif str == '1':
        return EntityStatus.deprecated.value
    elif str == '2':
        return EntityStatus.disabled.value
    else:
        return 'Unknown'


def _unique(elements, key):
    return list({key(element): element for element in elements}.values())


def _is_prod_workspace(workspace):
    if workspace is None:
        return True

    return workspace.location != "eastus2euap" and workspace.location != "centraluseuap" and \
        workspace.subscription_id != "4faaaf21-663f-4391-96fd-47197c630979"


def _can_visualize():
    """Return true if the platform widget can be visualized in jupyter notebook, otherwise return false."""
    try:
        from IPython import get_ipython
        from traitlets import Unicode
        from ipywidgets import DOMWidget

        if Unicode and DOMWidget:
            pass

        # ContainerClient only exists for azure.storage.blob >= 12.0.0
        # we will fallback to BlockBlobService if ContainerClient not exist
        try:
            from azure.storage.blob import ContainerClient
            if ContainerClient:
                pass
        except:
            from azure.storage.blob import BlockBlobService
            if BlockBlobService:
                pass

        shell = get_ipython().__class__.__name__
        if shell == 'ZMQInteractiveShell':
            return True  # Jupyter notebook or qtconsole
        elif shell == 'TerminalInteractiveShell':
            return False  # Terminal running IPython
        else:
            return False  # Other type (?)
    except (NameError, ModuleNotFoundError, ImportError):
        return False  # Probably standard Python interpreter


def _is_json_string_convertible(string):
    try:
        json.loads(string)
    except ValueError:
        return False
    return True


def _dumps_raw_json(obj):
    try:
        json_string = json.dumps(obj)
    except TypeError:
        return False
    return json_string


def _is_json_string_in_type(val, types):
    try:
        obj = json.loads(val)
    except json.decoder.JSONDecodeError:
        return False
    for t in types:
        if isinstance(obj, t):
            return True
    return False


def _get_short_path_name(path, is_dir, create_dir=False):
    '''
        https://docs.microsoft.com/en-us/windows/win32/fileio/naming-a-file#short-vs-long-names
        Maximum length for a path may defined by 260 characters in Windows.
        So need to trans path to shorten path to avoid filename too long.
        Example short/long path in windows:
            dir path: C:\\pipeline-local_run\\67a8bfde-9014-45c0-acc7-1db02d422302\\A dummy pipeline
            dir short path: C:\\PIPELI~2\\67A8BF~1\\ADUMMY~1
            file path: C:\\pipeline-local_run\\67a8bfde-9014-45c0-acc7-1db02d422302\\A dummy pipeline\\long_name.txt
            file short path: 'C:\\PIPELI~1\\67A8BF~1\\ADUMMY~1\\LONG_N~1.TXT'
        :param path: need to be shorten path
        :type path: str
        :param is_dir: Path is dir or file
        :type is_dir: bool
        :param create_dir: If create_dir=True, when create dirs before get shorten name
        :type create_dir: bool
        :return: short path form. If path is a short path, will no change.
        :rtype: str
    '''
    if os.name == 'nt':
        try:
            # win32api is an additional module for windows in pywin32
            # https://docs.python.org/3/using/windows.html#additional-modules
            import win32api
            path_list = Path(path).absolute().parts
            short_path = win32api.GetShortPathName(os.path.join(path_list[0]))
            for item in path_list[1: None if is_dir else -1]:
                if create_dir:
                    Path(os.path.join(short_path, item)).mkdir(parents=True, exist_ok=True)
                short_path = win32api.GetShortPathName(os.path.join(short_path, item))
            if not is_dir:
                short_path = win32api.GetShortPathName(os.path.join(short_path, path_list[-1]))
            return short_path
        except Exception:
            # If path is not exist will raise error.
            return str(PureWindowsPath(Path(path).absolute()))
    else:
        short_path = Path(path)
        if not short_path.exists() and create_dir:
            if is_dir:
                short_path.mkdir(parents=True)
            elif not short_path.parent.exists():
                # On Linux, if exist_ok is true, FileExistError will be raised if the last path component is a file
                # So we check the existence first
                short_path.parent.mkdir(parents=True, exist_ok=True)
        return path


def _get_parameter_static_value(obj, pipeline_parameters=None):
    from azure.ml.component.component import Input
    from azure.ml.component._pipeline_parameters import PipelineParameter
    from azure.ml.component._parameter_assignment import _ParameterAssignment
    pipeline_parameters = {} if pipeline_parameters is None else pipeline_parameters
    if isinstance(obj, Input):
        obj = obj._get_internal_data_source()

    if isinstance(obj, PipelineParameter):
        return pipeline_parameters[obj.name] if obj.name in pipeline_parameters else obj.default_value
    elif isinstance(obj, _ParameterAssignment):
        return obj.value if len(pipeline_parameters) == 0 else \
            obj.get_value_with_pipeline_parameters(pipeline_parameters)
    return obj


def _get_valid_directory_path(directory_path):
    suffix = 1
    valid_path = directory_path
    while os.path.exists(valid_path):
        valid_path = '{}({})'.format(directory_path, suffix)
        suffix += 1
    return valid_path


def _scrubbed_exception(exception_type, msg: str, args):
    """
    Return the exception with scrubbed error message. Use this to add scrubbed message to exceptions
    that we don't want the record the full message in because it may contains sensitive information.

    :param exception_type: The exception type to create.
    :param msg: The message format.
    :param args: The original args for message formatting.
    :return: The created exception.
    """
    scrubbed_data = '[Scrubbed]'
    e = exception_type(msg.format(args))
    e.scrubbed_message = msg.replace("{}", scrubbed_data)
    return e


def _get_data_info_hash_id(data_info: DataInfo):
    if data_info.saved_dataset_id is not None:
        identifier = data_info.saved_dataset_id
    elif data_info.relative_path is not None:
        identifier = _sanitize_python_variable_name(data_info.relative_path)
    elif data_info.id is not None:
        identifier = data_info.id
    elif data_info.name is not None:
        identifier = data_info.name
    else:
        raise ValueError('Invalid data source {}'.format(data_info.as_dict()))

    return str(uuid.uuid3(uuid.NAMESPACE_DNS, identifier))


def pull_docker_image(docker_client, image_location, username, password, stop_event=None):
    """
    Pulls the docker image from the ACR
    :param docker_client:
    :type docker_client: docker.DockerClient
    :param image_location:
    :type image_location: str
    :param username:
    :type username: str
    :param password:
    :type password: str
    :return:
    :rtype: None
    """
    try:
        print('Pulling image from ACR (this may take a few minutes depending on image size)...\n')
        for message in docker_client.api.pull(image_location, stream=True, decode=True, auth_config={
            'username': username,
            'password': password
        }):
            if stop_event and stop_event.isSet():
                print('Cancel pull image.')
                break
            prefix = '{}: '.format(message['id']) if 'id' in message else ''
            status = message['status']
            progress = message.get('progressDetails', {}).get('progress', '')
            print(prefix + status + progress)
    except docker.errors.APIError as e:
        raise WebserviceException('Error: docker image pull has failed:\n{}'.format(e))
    except Exception as exc:
        raise WebserviceException('Error with docker pull {}'.format(exc))


def deprecated(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.warning('This method has been deprecated and will be removed in the future release.')
        return func(*args, **kwargs)

    return wrapper


def trans_to_valid_file_name(file_name):
    import re
    return re.sub('[/?<>\\\\:*|"]', '_', file_name)


def print_to_terminal(msg):
    from azure.ml.component._execution._component_run_logger import Logger
    if isinstance(sys.stdout, Logger):
        sys.stdout.print_to_terminal(msg)
    else:
        print(msg)


def get_dataset_def_from_dataset(workspace, dataset):
    # Resolve dataset def as value assignments if parameter is dataset
    dataset_def = None
    from .._dataset import _GlobalDataset
    if isinstance(dataset, _GlobalDataset) or isinstance(dataset, DataReference):
        dataset_def = _get_dataset_def_from_dataset(dataset)
    elif isinstance(dataset, _Dataset):
        _ensure_dataset_saved_in_workspace(dataset, workspace)
        dataset_def = _get_dataset_def_from_dataset(dataset)
    return dataset_def


def resolve_datasets_from_parameter(workspace, _param):
    _dataset_param = {}
    _other_param = {}
    # Resolve dataset def as value assignments if parameter is dataset
    for _k, _v in _param.items():
        dataset_def = get_dataset_def_from_dataset(workspace, _v)
        if dataset_def is not None:
            _dataset_param[_k] = dataset_def.value
        else:
            _other_param[_k] = _v
    return _other_param, _dataset_param


def _get_dataset_def_from_dataset(dataset):
    def _get_dataset_def_from_data_path(data_path, data_type):
        dataset_def_val = DataSetDefinitionValue(literal_value=data_path)
        dataset_def = DataSetDefinition(
            data_type_short_name=data_type,
            value=dataset_def_val
        )
        return dataset_def

    from .._dataset import _GlobalDataset
    if isinstance(dataset, _GlobalDataset):
        data_path = DataPath(data_store_name=dataset.data_store_name, relative_path=dataset.relative_path)
        return _get_dataset_def_from_data_path(data_path, 'DataFrameDirectory')

    if isinstance(dataset, DataReference):
        data_path = DataPath(data_store_name=dataset.datastore.name, relative_path=dataset.path_on_datastore)
        return _get_dataset_def_from_data_path(data_path, 'AnyDirectory')

    # Either data_set_reference or saved_data_set_reference shall be not None in dataset_def.
    saved_dataset_ref = None
    if dataset._registration and dataset._registration.registered_id:
        dataset_ref = RegisteredDataSetReference(
            id=dataset._registration.registered_id if dataset._registration else None,
            version=dataset._registration.version if dataset._registration else None,
            name=dataset._registration.name if dataset._registration else None
        )
    else:
        dataset_ref = None
        if dataset.id:
            saved_id = dataset.id
            saved_dataset_ref = SavedDataSetReference(id=saved_id)

    dataset_def_val = DataSetDefinitionValue(data_set_reference=dataset_ref,
                                             saved_data_set_reference=saved_dataset_ref)

    dataset_def = DataSetDefinition(
        data_type_short_name='AnyDirectory',
        value=dataset_def_val
    )
    return dataset_def


def _ensure_dataset_saved_in_workspace(dataset: AbstractDataset, ws: Workspace):
    """Ensure the dataset is saved in the target workspace.

    This is an alternative function for dataset._ensure_saved,
    since dataset._ensure_saved only check whether it is saved in 'some workspace' not the "target workspace".
    It will introduce unexpected behavior if we use this method twice for two different workspaces.
    This function make sure that it is always correct even it is called in multiple workspaces.
    """
    if dataset.name is not None:
        return  # The dataset with a name is a registered dataset, it doesn't need to take action
    if dataset._registration is not None and dataset._registration.workspace == ws:
        return  # If the dataset is registered in the target workspace, no need to take action.
    dataset._registration = None  # Set the registration as None to make sure it will be registered.
    dataset._ensure_saved(workspace=ws)


def _str_to_bool(s):
    """Returns True if literal 'true' is passed, otherwise returns False.

    Can be used as a type for argument in argparse, return argument's boolean value according to it's literal value.
    """
    if not isinstance(s, str):
        return False
    return s.lower() == 'true'


def _try_to_get_workspace():
    """Try to get workspace from config, returns None if not exist."""
    try:
        from azureml.core import Workspace
        return Workspace.from_config()
    except Exception:
        return None


def _copy2(src, dst):
    """Wraps shutil.copy2 and work around possible "Function not implemented" exception thrown by it.

    Background: shutil.copy2 will throw OSError when dealing with Azure File.
    See https://stackoverflow.com/questions/51616058 for more information.
    """
    if hasattr(os, 'listxattr'):
        # always shadow os.listxattr is exist to avoid error "Function not implemented" on Azure
        # since we don't need to copy them
        with mock.patch('os.listxattr', return_value=[]):
            shutil.copy2(src, dst)
    else:
        shutil.copy2(src, dst)


def _relative_to(path, basedir, raises_if_impossible=False):
    """Compute the relative path under basedir.

    This is a wrapper function of Path.relative_to, by default Path.relative_to raises if path is not under basedir,
    In this function, it returns None if raises_if_impossible=False, otherwise raises.

    """
    # The second resolve is to resolve possible win short path.
    path = Path(path).resolve().absolute().resolve()
    basedir = Path(basedir).resolve().absolute().resolve()
    try:
        return path.relative_to(basedir)
    except ValueError:
        if raises_if_impossible:
            raise
        return None


def _convert_to_shell_execution_command(command, conda_environment_name=None):
    """
    Convert command to shell execution command. If set conda_environment_name, it will add conda activate command
    before execute command. For linux, converted command will be str command. For windows, it depends on command type.
    For example, set list command as ['echo', 'space \'value'], str command as 'echo space \'value':
        In Windows, it only connect conda command and command:
            1) For list command, it will return ['conda', 'activate', conda_name, '&&', 'echo', 'space \'value'].
            2) For str command, it will return 'conda activate conda_name && echo space \'value'.
        In Linux, it will turn command to shell-escape version.
            1) For list command, it will return ". $(conda info --base)/etc/profile.d/conda.sh;conda activate conda
               conda_name;echo 'space \'value'".
            2) For str command, it will return ". $(conda info --base)/etc/profile.d/conda.sh;conda activate conda
               conda_name;'echo space \'value'".

    :return converted_command: Converted command
    :rtype converted_command: str or list[str]
    """
    converted_command = command
    conda_command = []
    if os_name == 'nt':
        if conda_environment_name:
            # Add conda activate command before command.
            conda_command = ['conda', 'activate', conda_environment_name, '&&']
        if isinstance(converted_command, str):
            # When command is string, to avoid translate original command,
            # need to connect conda command and command to string.
            converted_command = ' '.join(conda_command + [converted_command])
        else:
            # When command is list, subprocess will translate a sequence of arguments into a command line.
            # To avoid translate conda command as args, split conda command to list and add to command.
            converted_command[0:0] = conda_command
    else:
        if conda_environment_name:
            # In linux, conda may be not available in subshells, need to enable conda before use it.
            # https://github.com/conda/conda/issues/7980#issuecomment-441358406
            conda_command = [
                '. $(conda info --base)/etc/profile.d/conda.sh',
                'conda activate %s' % conda_environment_name]
        if isinstance(converted_command, list):
            # Convert args contains specail character to string that safely be used in shell.
            converted_command = ' '.join([quote(item) for item in converted_command])
        converted_command = ';'.join(conda_command + [converted_command])
    return converted_command


class TimerContext(object):
    """A context manager calculates duration when executing inner block."""

    def __init__(self):
        self.start_time = None

    def get_duration_seconds(self):
        """Get the duration from context manger start to this function call.
        Result will be format to two decimal places.

        """
        duration = datetime.utcnow() - self.start_time
        return round(duration.total_seconds(), 2)

    def __enter__(self):
        self.start_time = datetime.utcnow()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


def fetch_user_id_from_aad_token(token) -> (str, bool):
    """Fetch user object id from aad token and check if the user is service principle.

    :param token: aad token
    :return: user object id and if this user is service principle.
    """
    # We set verify=False, as we don't have keys to verify signature, and we also don't need to
    # verify signature, we just need the user object id.
    decode_json = jwt.decode(token, options={'verify_signature': False, 'verify_aud': False})
    # For an access tokens generated by service principal, 'name' does not exist in the token.
    is_service_principle = False if 'name' in decode_json.keys() else True
    return decode_json['oid'], is_service_principle


def _get_enum(value, enum_class, raise_unknown=False):
    """Return the enum according to the string value from backend."""
    if isinstance(value, enum_class):  # If an expected enum is passed, we simply return it.
        return value
    value = str(value)
    for i, s in enumerate(enum_class):
        if str(i) == value or s.value == value:
            return s
    # When the status is not in the enum, we raise exception if raise_unknown
    if raise_unknown:
        msg = "Got unknown value %s for enum %r," % (value, enum_class) + \
              " you may update the SDK/CLI to the latest version to resolve this issue."
        raise ValueError(msg)
    # otherwise we create a fake enum which has such value to avoid breaking.
    # We should try to make sure this branch is not reached.
    FakeStatus = namedtuple('FakeEnum', ['name', 'value'])
    return FakeStatus(name=value, value=value)


def _camel_to_snake_case(s):
    """Convert camel name to snake name.
    E.g. CamelToSnakeCase -> camel_to_snake_case.
    """
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()


def is_valid_experiment_name(name):
    """
    Validate experiment name.
    Experiment name must be 1-256 characters,
    start with a letter or a number, and can only contain letters, numbers, underscores, and dashes.

    :param name: Experiment name
    :type name: str
    :return: Boolean.
    """
    if name == '':
        return False
    pattern = re.compile('^[0-9a-zA-Z][0-9a-zA-Z_-]*$')
    return True if pattern.match(name) is not None else False


def transform_default_experiment_name(name):
    """
    transform default experiment_name to be valid: start with a letter or a number, and can only contain
    letters, numbers, underscores, and dashes

    :param name: default experiment name
    :type name: str
    :return: experiment_name.
    :rtype: str
    """
    experiment_name = re.sub("[^\\w-]", "_", name)
    experiment_name = experiment_name.lstrip('-_')
    return experiment_name
