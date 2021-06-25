import logging
from waveletai import constants
import threading
from waveletai.sessions import Session
from waveletai.backends.hosted_backend import HostedBackend
from waveletai.constants import ModelRegisterMode

import mlflow

logging.basicConfig(format='[%(process)d] [%(asctime)s] %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                    level=logging.INFO)

_logger = logging.getLogger(__name__)

__lock = threading.RLock()

""""Access as an anonymous user.
You can pass this value as api_token during init() call, either by an environment variable or passing it directly
"""
ANONYMOUS = constants.ANONYMOUS
"""Anonymous user API token.
You can pass this value as api_token during init() call, either by an environment variable or passing it directly
"""
ANONYMOUS_API_TOKEN = constants.ANONYMOUS_API_TOKEN
from waveletai._version import get_versions

__version__ = get_versions()['version']

_backend = None


def init(name=None, pwd=None, backend=None):
    with __lock:
        global _backend

        if backend is None:
            # backend_name = os.getenv(envs.BACKEND)
            # if backend_name == 'offline':
            #     backend = OfflineBackend()

            # elif backend_name is None:
            _backend = HostedBackend(name, pwd)

            # else:
            #     raise InvalidBackend(backend_name)
        return _backend
        # session = Session(backend=backend)
        # return session


def create_app(name, tags, desc):
    """
    创建应用
    :param name: 应用名称
    :param desc: 应用说明
    :return: App对象
    """
    global _backend
    return _backend.create_app(name, tags, desc)


def get_app(app_id):
    """
    获取应用
    :param app_id: 应用ID
    :return: App对象
    """
    global _backend
    return _backend.get_app(app_id)


def create_dataset(name, zone, path, data_type=constants.DataType.TYPE_FILE.value, desc=None):
    """
    创建数据集
    :param name: 数据集名称
    :param zone: 数据集区域
    :param path: 要上传的本地数据的路径
    :param data_type: 一个数据集中的数据类型是唯一的。备选值constants.DataType，固定提供图片、文件、视频、视频帧的数据类型
    :param desc: 数据集详情
    :return: Dataset对象
    """
    global _backend
    return _backend.create_dataset(name, zone, path, data_type, desc)


def get_dataset(dataset_id):
    """
    获取数据集对象
    :param dataset_id:数据集ID
    :return: Dataset对象
    """
    global _backend
    return _backend.get_dataset(dataset_id)


def download_dataset_artifact(dataset_id, path, destination):
    """
    获取模型对象
    :param dataset_id:数据集ID
    :param path:路径
    :param type:数据集类型
    :param destination:本地存储路径
    :return:
    """
    global _backend
    return _backend.download_dataset_artifact(dataset_id, path, destination)


def download_dataset_artifacts(dataset_id, destination):
    """
    获取模型对象
    :param dataset_id:数据集ID
    :param type:数据集类型
    :param destination:本地存储路径
    :return:
    """
    global _backend
    return _backend.download_dataset_artifacts(dataset_id, destination)


def upload_dataset_artifacts(dataset_id, path):
    """
    上传数据集资产文件
    :param dataset_id: 文件所属数据集
    :param path: 要上传的文件夹/文件路径
    :return:  上传文件 succ，共xxx个
    """
    global _backend
    return _backend.upload_dataset_artifacts(dataset_id, path)


def create_model(name, app_id, desc='', auth_id='', git_url='', http_url=''):
    """
    创建模型
    :param http_url: http地址 默认空
    :param git_url: git地址 默认空
    :param auth_id: auth_id 默认空
    :param name:模型名称
    :param desc:模型备注 默认空
    :param app_id:所属应用ID
    :return:
    """
    global _backend
    return _backend.create_model(name, app_id, desc, auth_id, git_url, http_url)


def get_model(model_id):
    """
    获取模型对象
    :param model_id:模型ID
    :return:
    """
    global _backend
    return _backend.get_model(model_id)


def register_model_version(model_id, desc, artifacts, mode=ModelRegisterMode.PYFUNC.value):
    """
    注册模型库版本
    :param model_id: 模型ID
    :param desc: 备注
    :param artifacts: 注册文件路径，可以是文件夹,当为docker模式时，此处为docker-image,可以用save命令导出  eg：deployment.tar
    :param mode: 注册模式,默认为自定义(ModelRegisterMode.PYFUNC.value)
    :return:
    """
    global _backend
    return _backend.register_model_version(model_id, desc, artifacts, mode)


def get_model_version_by_model(model_id, version):
    """
    过模型获取模型库指定信息
    :param model_id: 模型ID
    :param version:模型版本号
    :return:
    """
    global _backend
    return _backend.get_model_version(model_id, version)


def get_model_version_by_id(model_version_id):
    """
    通过模型库ID获取模型库指定信息
    :param model_version_id:模型库ID
    :return:
    """
    global _backend
    return _backend.get_repo_by_repo_id(model_version_id)


def list_models(app_id):
    """
    获取模型对象
    :param app_id:模型ID
    :return:
    """
    global _backend
    return _backend.list_models(app_id)


def update_dataset(dataset_id, name, zone, desc):
    """
    更新数据集id
    :param dataset_id:
    :param name:
    :param zone:
    :param desc:
    :return:
    """
    global _backend
    return _backend.update_dataset(dataset_id, name, zone, desc)


def delete_dataset(dataset_id):
    """
    删除数据集
    :param dataset_id:
    :return:
    """
    global _backend
    return _backend.delete_dataset(dataset_id)


def update_model(model_id, app_id, name, desc):
    """
    更新模型集
    :param model_id:
    :param app_id:
    :param name:
    :param desc:
    :return:
    """
    global _backend
    return _backend.update_model(model_id, app_id, name, desc)


def delete_model(model_id):
    """
    删除模型
    :param model_id:
    :return:
    """
    global _backend
    return _backend.delete_model(model_id)


def list_model_versions(model_id):
    """
    获取注册的各版本模型信息列表
    :param model_id:
    :return:
    """
    global _backend
    return _backend.list_model_versions(model_id)


def abandon_model_version(model_id, version):
    """
    根据模型id，删除指定version
    :param model_id:
    :param version:
    :return:
    """
    global _backend
    return _backend.abandon_model_version(model_id, version)


def update_model_version(model_id, version, desc):
    """
    根据模型id，修改指定模型版本
    :param desc:
    :param model_id:
    :param version:
    :return:
    """
    global _backend
    return _backend.update_model_version(model_id, version, desc)


def list_experiments(model_id):
    """
    根据模型id，获取实验数据
    :param model_id:
    :return:
    """
    global _backend
    return _backend.list_experiments(model_id)


def download_model_version_asset(repo_id, path, destination):
    """
    根据repo_id下载指定path(文件或文件夹)到本地的destination
    :param model_id:
    :param path:
    :param destination:
    :return:
    """
    global _backend
    return _backend.download_model_version_asset(repo_id, path, destination)


def download_model_version_artifacts(repo_id, destination):
    """
    根据repo_id下载全部文件到本地的destination
    :param repo_id:
    :param destination:
    :return:
    """
    global _backend
    return _backend.download_model_version_artifacts(repo_id, destination)


def list_model_releases(model_id, version):
    """
    根据模型id，版本，获取发布数据
    :param model_id:
    :param version: 默认为None
    :return:
    """
    global _backend
    return _backend.list_model_releases(model_id, version)


def list_model_releases_by_repo(repo_id):
    """
    查询当前模型版本的发布服务列表
    :param repo_id:
    :return:
    """
    global _backend
    return _backend.list_model_releases_by_repo(repo_id)


def create_experiment(name, model_id, params=None, desc=None, ):
    """
    创建实验
    :param name:模型名称
    :param desc:模型备注
    :param model_id:所属模型ID
    :param params: 参数字典{key:value, ...}
    :return:
    """
    global _backend
    return _backend.create_experiment(name=name, model_id=model_id, params=params, host_id=None,
                                      dataset_id=None, feature_id=None, is_train=True, desc=desc,
                                      mlexp_id=None, artifact_location=None, online_train=False,
                                      docker_args={})


def get_experiment(experiment_id):
    """
    获取实验对象
    :param experiment_id:实验ID
    :return:
    """
    global _backend
    return _backend.get_experiment(experiment_id)


# def get_mlflow_experiment(experiment_id):
#     """
#     获取mlflwo实验对象
#     :param experiment_id:
#     :return:
#     """
#     global _backend
#     return _backend.get_mlflow_experiment(experiment_id)


def create_mlflow_experiment(name, artifact_location):
    """
    创建mlflow实验
    :param name:
    :param artifact_location:
    :return:
    """
    global _backend
    return _backend.create_mlflow_experiment(name, artifact_location)


# def create_mlflow_run():
#     """
#     创建mlflow run
#     :return:
#     """
#     global _backend
#     return _backend.create_mlflow_run()`


def get_experiment_by_mlflow_experiment(experiment_id):
    """
    根据mlexperiment id 查询wai experiment
    :return:
    """
    global _backend
    return _backend.get_experiment_by_mlflow_experiment(experiment_id)


def get_experiment_by_mlflow_run(run_id):
    """
    根据mlrun id 查询wai experiment
    :param run_id:
    :return:
    """
    global _backend
    return _backend.get_experiment_by_mlflow_run(run_id)


def log_metric(key, value, step=None):
    mlflow.set_tracking_uri('waveletai-store://')
    mlflow.log_metric(key, value, step)


def log_param(key, value):
    mlflow.set_tracking_uri('waveletai-store://')
    mlflow.log_param(key, value)
